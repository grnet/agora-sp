import logging
import json
import re
import urlparse
import os

from djoser import views as djoser_views
from rest_framework.views import exception_handler
from rest_framework.authtoken.models import Token
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import user_logged_in
from accounts.models import User
from agora.emails import send_email_shib_user_created
from agora.utils import load_resources, load_permissions, get_root_url
from agora.serializers import UserMeSerializer


logger = logging.getLogger(__name__)

TOKEN_LOGIN_URL = getattr(settings, 'TOKEN_LOGIN_URL', '/ui/auth/login')
AAI_ID_KEY = getattr(settings, 'AAI_ID_KEY', 'id')
API_ENDPOINT = getattr(settings, 'API_ENDPOINT', 'api/v2')
MEDIA_URL = getattr(settings, 'MEDIA_URL', 'media/')
BASE_DIR = getattr(settings, 'BASE_DIR')


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
        return HttpResponseRedirect(TOKEN_LOGIN_URL + "#error=foo" % e)

    try:
        user = User.objects.get(shibboleth_id=shibboleth_id)

    except User.DoesNotExist:
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
