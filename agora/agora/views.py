import logging
import json
import re
import urlparse
import os
import datetime

from djoser import views as djoser_views
from rest_framework.views import exception_handler
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import user_logged_in
from accounts.models import User, Organisation, ProviderAudit
from service.models import Resource, ResourceAudit
from agora.emails import send_email_shib_user_created
from agora.utils import load_resources, load_permissions, get_root_url
from agora.serializers import UserMeSerializer
from django.db import connection
from django.db.models.functions import ( ExtractMonth, ExtractYear )
from django.db.models import Count


PAST = datetime.date(2000, 1, 1)
FUTURE = datetime.date(2100, 1, 1)
VERSION = getattr(settings, 'VERSION', '')

def valid_date(date_text, default, add_day=False):
    try:
        date = datetime.datetime.strptime(date_text, '%d-%m-%Y')
        if add_day:
          date = date + datetime.timedelta(days=1)
        return date
    except ValueError:
        return default


logger = logging.getLogger(__name__)

TOKEN_LOGIN_URL = getattr(settings, 'TOKEN_LOGIN_URL', '/ui/auth/login')
AAI_ID_KEY = getattr(settings, 'AAI_ID_KEY', 'id')
API_ENDPOINT = getattr(settings, 'API_ENDPOINT', 'api/v2')
MEDIA_URL = getattr(settings, 'MEDIA_URL', 'media/')
BASE_DIR = getattr(settings, 'BASE_DIR')
ACCOUNTING_BASE_YEAR = getattr(settings, 'ACCOUNTING_BASE_YEAR', 2021)

def config(request):

    permissions = load_permissions()
    shibboleth_endpoint = reverse('shibboleth_login')
    backend_host = urlparse.urljoin(get_root_url(), API_ENDPOINT)
    backend_media_root = urlparse.urljoin(get_root_url(), MEDIA_URL)
    version_file = os.path.join(BASE_DIR, '../version')

    with open(version_file) as f:
        version = f.read().replace('\n', '')

    config_data = {
        'permissions': permissions,
        'shibboleth_login_url': shibboleth_endpoint,
        'backend_host': backend_host,
        'backend_media_root': backend_media_root,
        'resources': load_resources(),
        'version': version
    }
    return HttpResponse(json.dumps(config_data),
                        content_type='application/json')


def error400(request):
    return JsonResponse({
        "status": "400 Page not found",
        "errors": {
            "detail": "The requested page was not found"
        }
    }, status=400)


def error404(request):
    return JsonResponse({
        "status": "404 Page not found",
        "errors": {
            "detail": "The requested page was not found"
        }
    }, status=404)


def error500(request):
    return JsonResponse({
        "status": "500 Server error",
        "errors": {
            "detail": "Something went wrong on our side"
        }
    }, status=500)


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        response.data['status'] = str(response.status_code)
        if response.status_code == 405:
            response.data['status'] += " Method not allowed"
        response.data['errors'] = {}
        if response.data['errors'] and response.data['errors'].detail:
            response.data['errors']['detail'] = response.data['detail']
            del response.data['detail']

    return response


SHIBBOLETH_USER_MAP = {
    'email': 'mail',
    'username': 'mail',
    'shibboleth_id': AAI_ID_KEY
}

INCLUDED_HEADERS = [
    AAI_ID_KEY,
    'mail',
    'displayname',
    'sn',
    'givenname'
]


def shibboleth_headers(headers):
    """
    Keep useful shibboleth headers
    """

    for key, val in headers.iteritems():

        if key.startswith('HTTP_'):
            key = re.sub('^HTTP_', '', key)
            key = key.lower()

            if key in INCLUDED_HEADERS:
                yield key, val


def get_user_data(shib_data):
    """
    Extract user model fields from shibboleth data.
    First name and last name are extracted either from givenName and sn, either
    from displayName
    """
    result = {}
    for user_key, shib_key in SHIBBOLETH_USER_MAP.iteritems():
        if shib_key in shib_data.keys():
            result[user_key] = shib_data[shib_key]
    dn = shib_data.get('displayname')
    sn = shib_data.get('sn')
    gn = shib_data.get('givenname')
    if gn and sn:
        result['first_name'] = gn
        result['last_name'] = sn
    if dn and len(dn.split(' ')) > 0:
        tmp_list = dn.split(' ')
        result['first_name'] = tmp_list.pop(0)
        result['last_name'] = ' '.join(tmp_list)
    return result


def shibboleth_login(request):
    headers = request.META
    # clean up headers data
    shibboleth_data = dict(zip(*zip(*shibboleth_headers(headers))))
    # resolve data used for class User
    user_data = get_user_data(shibboleth_data)

    # initialize
    user = None
    token = None

    redirect_url = TOKEN_LOGIN_URL

    shibboleth_id = user_data.get('shibboleth_id')
    if not shibboleth_id:
        e = 'No shibboleth id'
        return HttpResponseRedirect(TOKEN_LOGIN_URL + "#error=%s" % e)


    try:
        user = User.objects.get(shibboleth_id=shibboleth_id)

    except User.DoesNotExist:
        try:
            user = User.objects.get(email=user_data.get('email'))
            e = 'shibboleth_duplicate_email'
            return HttpResponseRedirect(TOKEN_LOGIN_URL + "#error=%s" % e)
        except  User.DoesNotExist:
            user = User.objects.create(**user_data)
            send_email_shib_user_created(user, headers['HTTP_HOST'])

    token, _ = Token.objects.get_or_create(user=user)
    user_logged_in.send(sender=user.__class__, request=request, user=user)

    token_fragment = '#token=' + token.key
    redirect_url = redirect_url + token_fragment

    return HttpResponseRedirect(redirect_url)


class CustomMe(djoser_views.UserView):

    def get_serializer_class(self):
        return UserMeSerializer

def accounting(request):
    date_from = valid_date(request.GET.get('from', ''), PAST)
    date_to = valid_date(request.GET.get('to', ''), FUTURE, True)

    new_users = User.objects.filter(date_joined__range=(date_from, date_to)).count()
    new_resources = Resource.objects.filter(created_at__range=(date_from, date_to)).count()
    new_providers = Organisation.objects.filter(created_at__range=(date_from, date_to)).count()

    updated_resources = ResourceAudit.objects.filter(updated_at__range=(date_from, date_to)).order_by('resource').values('resource').distinct().count()
    updated_providers = ProviderAudit.objects.filter(updated_at__range=(date_from, date_to)).order_by('provider').values('provider').distinct().count()

    updated_resources_total = ResourceAudit.objects.filter(updated_at__range=(date_from, date_to)).count()
    updated_providers_total = ProviderAudit.objects.filter(updated_at__range=(date_from, date_to)).count()

    data = {
        'date_from': date_from,
        'date_to': date_to,
        'resources': {
            'new_resources': new_resources,
            'updated_resources': updated_resources,
            'total_updated_resources': updated_resources_total
        },
        'providers': {
            'new_providers': new_providers,
            'updated_providers': updated_providers,
            'total_updated_providers': updated_providers_total
        },
        'users': {
            'new_users': new_users,
        }
    }

    return JsonResponse(data)


def get_field_date(year,month,data,label):
    for entry in data:
        if entry['year'] == year and entry['month'] == month:
            return entry[label]
    return 0

def create_response(new_users, new_resources, new_providers, updated_resources, updated_providers, updated_resources_total, updated_provider_total, year_base):
    now = datetime.datetime.now()
    curr_year = now.year
    curr_month = now.month
    data = []
    for year in range(year_base, curr_year+1):
        if year-curr_year==0:
            end_month = curr_month
        else:
            end_month=13
        for month in range(1,end_month):
            new_users_count = get_field_date(year,month,new_users,'new_users')
            new_resources_count = get_field_date(year,month,new_resources,'new_resources')
            new_providers_count = get_field_date(year,month,new_providers,'new_providers')
            updated_resources_count = get_field_date(year,month,updated_resources,'updated_resources')
            updated_providers_count = get_field_date(year,month,updated_providers,'updated_providers')
            updated_resources_total_count = get_field_date(year,month,updated_resources_total,'updated_resources_total')
            updated_providers_total_count = get_field_date(year,month,updated_provider_total,'updated_providers_total')
            data.append({
                'year':year,
                'month': month,
                'new_users': new_users_count,
                'new_resources': new_resources_count,
                'new_providers': new_providers_count,
                'updated_resources': updated_resources_count,
                'updated_providers': updated_providers_count,
                'updated_resources_total': updated_resources_total_count,
                'updated_providers_total': updated_providers_total_count
            })
    return JsonResponse(data, safe=False)
    

def monthly_stats(request):
    base_year = ACCOUNTING_BASE_YEAR
    new_users = User.objects.filter(date_joined__gte=datetime.datetime(base_year,1,1)).annotate(month=ExtractMonth('date_joined'),
                                year=ExtractYear('date_joined'),).order_by().values('month', 'year').annotate(new_users=Count('*')).values('month', 'year', 'new_users')
    new_resources = Resource.objects.filter(created_at__gte=datetime.datetime(base_year,1,1)).annotate(month=ExtractMonth('created_at'),
                                year=ExtractYear('created_at'),).order_by().values('month', 'year').annotate(new_resources=Count('*')).values('month', 'year', 'new_resources')
    new_providers = Organisation.objects.filter(created_at__gte=datetime.datetime(base_year,1,1)).annotate(month=ExtractMonth('created_at'),
                                year=ExtractYear('created_at'),).order_by().values('month', 'year').annotate(new_providers=Count('*')).values('month', 'year', 'new_providers')

    updated_resources = ResourceAudit.objects.filter(updated_at__gte=datetime.datetime(base_year,1,1)).annotate(month=ExtractMonth('updated_at'),
                                year=ExtractYear('updated_at'),).values('month','year').annotate(updated_resources=Count('resource',distinct=True))
    updated_providers = ProviderAudit.objects.filter(updated_at__gte=datetime.datetime(base_year,1,1)).annotate(month=ExtractMonth('updated_at'),
                                year=ExtractYear('updated_at'),).values('month','year').annotate(updated_providers=Count('provider',distinct=True))

    updated_resources_total = ResourceAudit.objects.filter(updated_at__gte=datetime.datetime(base_year,1,1)).annotate(month=ExtractMonth('updated_at'),
                                year=ExtractYear('updated_at'),).order_by().values('month', 'year').annotate(updated_resources_total=Count('*')).values('month', 'year', 'updated_resources_total')
    updated_providers_total = ProviderAudit.objects.filter(updated_at__gte=datetime.datetime(base_year,1,1)).annotate(month=ExtractMonth('updated_at'),
                                year=ExtractYear('updated_at'),).order_by().values('month', 'year').annotate(updated_providers_total=Count('*')).values('month', 'year', 'updated_providers_total')

    new_users=[v for v in new_users]
    new_resources=[v for v in new_resources]
    new_providers=[v for v in new_providers]
    updated_resources=[v for v in updated_resources]
    updated_providers=[v for v in updated_providers]
    updated_resources_total=[v for v in updated_resources_total]
    updated_providers_total=[v for v in updated_providers_total]
    print(updated_resources_total)
    return create_response(new_users, new_resources, new_providers, updated_resources, updated_providers, updated_resources_total, updated_providers_total, base_year)

def get_version(request):
    data = {
        'version': VERSION
    }
    return HttpResponse(json.dumps(data),
                    content_type='application/json')
