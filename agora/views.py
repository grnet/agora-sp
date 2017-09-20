import logging

from django.http import JsonResponse
from rest_framework.views import exception_handler

from agora import utils


logger = logging.getLogger(__name__)


def config(request):
    permissions = utils.get_permissions()

    json_data = {
        'permissions': permissions,
    }

    return JsonResponse(json_data)


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
