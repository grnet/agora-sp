import logging
import json
import re

from agora.utils import load_permissions

from django.http import JsonResponse
from rest_framework.views import exception_handler
from django.http import HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse
from accounts.models import User
from rest_framework.authtoken.models import Token
from django.http import HttpResponseRedirect
from django.contrib.auth import user_logged_in


logger = logging.getLogger(__name__)

TOKEN_LOGIN_URL = getattr(settings, 'TOKEN_LOGIN_URL', '/auth/login')
AAI_ID_KEY = getattr(settings, 'AAI_ID_KEY', 'id')


def config(request):

    permissions = load_permissions()
    shibboleth_endpoint = reverse('shibboleth_login')

    config_data = {
        'permissions': permissions,
        'shibboleth_login_url': shibboleth_endpoint
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
    'mail'
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
    """
    result = {}
    for user_key, shib_key in SHIBBOLETH_USER_MAP.iteritems():
        if shib_key in shib_data.keys():
            result[user_key] = shib_data[shib_key]
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

    token, _ = Token.objects.get_or_create(user=user)
    user_logged_in.send(sender=user.__class__, request=request, user=user)

    token_fragment = '#token=' + token.key
    redirect_url = redirect_url + token_fragment

    return HttpResponseRedirect(redirect_url)
