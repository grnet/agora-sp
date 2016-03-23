from django.http import JsonResponse
from owner import models
from service import models as service_models
from rest_framework.decorators import *
from common import helper, strings
import re


# Returns a list of the service owners
@api_view(['GET'])

def get_service_owner(request, service_name_or_uuid):
    """
    Retrieves a the service owner

    """

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(service_name_or_uuid)
    service, parsed_name, uuid = None, None, None

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ").strip()
    else:
        uuid = service_name_or_uuid

    try:
        if result is None:
            service = service_models.Service.objects.get(name=parsed_name)
        else:
            service = service_models.Service.objects.get(id=uuid)

    except service_models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    if service is not None:
        response = helper.get_response_info(strings.SERVICE_OWNER_INFORMATION, service.get_service_owners())

    return JsonResponse(response)


# Returns the institution of the service owner by both name and uuid
@api_view(['GET'])
def get_service_owner_institution(request, service_name_or_uuid, service_owner):
    """
    Retrieves the institution of the owner

    """

    response = {}
    service, owner, parsed_name, uuid, owner_name, owner_uuid = None, None, None, None, None, None

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(service_name_or_uuid)
    owner_match = prog.match(service_owner)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ").strip()
    else:
        uuid = service_name_or_uuid

    if owner_match is None:
        owner_name = service_owner.split("_")
    else:
        owner_uuid = service_owner

    try:
        if result is None:
            service = service_models.Service.objects.get(name=parsed_name)
        else:
            service = service_models.Service.objects.get(id=uuid)

        if owner_match is None:
            owner = service_models.ServiceOwner.objects.get(first_name=owner_name[0], last_name=owner_name[1])
        else:
            owner = service_models.ServiceOwner.objects.get(id=owner_uuid)

    except models.ServiceOwner.DoesNotExist:
        owner = None
        response = helper.get_error_response(strings.OWNER_NOT_FOUND)

    except service_models.Service.DoesNotExist:
        service = None
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    if service is not None and owner is not None:
        response = helper.get_response_info(strings.SERVICE_OWNER_INSTITUTION, owner.get_institution())

    return JsonResponse(response)
