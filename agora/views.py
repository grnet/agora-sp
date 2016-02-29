from django.http import JsonResponse


def error400(request):
    return JsonResponse({
        "status": "400 Page not found",
        "errors": {
            "detail": "The requested page was not found"
        }
    })


def error404(request):
    return JsonResponse({
        "status": "404 Page not found",
        "errors": {
            "detail": "The requested page was not found"
        }
    })


def error500(request):
    return JsonResponse({
        "status": "500 Server error",
        "errors": {
            "detail": "Something went wrong on our side"
        }
    })