import logging
import json

from agora.utils import load_permissions

from django.http import JsonResponse
from rest_framework.views import exception_handler
from django.http import HttpResponse


logger = logging.getLogger(__name__)


def _strip_api_version(permissions):
    perms = {}

    for (key, value) in permissions.items():
        perms[key.replace('api/v2/', '')] = value

    return perms


def config(request):

    permissions = load_permissions()

    config_data = {
        'permissions': _strip_api_version(permissions),
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
        response.data['errors']['detail'] = response.data['detail']
        del response.data['detail']

    return response
