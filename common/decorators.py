import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from service.models import Service
from common import helper, strings
import re

def check_service_ownership_or_superuser(func):

    def check_and_call(request, *args, **kwargs):

        user = request.user

        print user.id

        params = request.POST.copy()

        if user.is_superuser:
            return func(request, *args, **kwargs)

        if "uuid" in params:
            service_name_or_uuid = params.get('uuid')

        prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

        result = prog.match(service_name_or_uuid)

        if result is None:
            parsed_name = service_name_or_uuid.replace("_", " ").strip()
        else:
            uuid = service_name_or_uuid

        try:
            if result is None:
                service = Service.objects.get(name=parsed_name)
            else:
                service = Service.objects.get(id=uuid)

        except Service.DoesNotExist:
            response = helper.get_error_response(strings.SERVICE_NOT_FOUND)
            return JsonResponse(response)

        owner = service.get_service_owners()

        if  owner['account_id'] == user.id:
            return func(request, *args, **kwargs)
        else:
            response = helper.get_error_response(strings.OPERATION_NOT_PERMITTED, strings.FORBIDDEN_403)

            return JsonResponse({"resp": response, "user": user.is_authenticated()})

    return check_and_call


def check_service_staff(func):

    def check_and_call(request, *args, **kwargs):

        user = request.user

        if user.is_superuser:
            return func(request, *args, **kwargs)

        if user.is_staff:
            return func(request, *args, **kwargs)

        response = helper.get_error_response(strings.OPERATION_NOT_PERMITTED, strings.FORBIDDEN_403)

        return JsonResponse({"resp": response, "user": user.is_authenticated()})

    return check_and_call