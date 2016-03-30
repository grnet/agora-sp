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


# Inserts an Institution object
@api_view(['POST'])
def insert_institution(request):

    params = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    if "name" not in params:
        return JsonResponse(helper.get_error_response(strings.INSTITUTION_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    uuid = None

    name = params.get('name')

    if name is None or len(name) == 0:
        return JsonResponse(helper.get_error_response(strings.INSTITUTION_NAME_EMPTY, status=strings.REJECTED_405))

    address = params.get('address') if "address" in params else None
    country = params.get('country') if "country" in params else None
    department = params.get('department') if 'department' in params else None


    if "uuid" in params:

        uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_405))

        try:
            models.Institution.objects.get(id=uuid)
            return JsonResponse(helper.get_error_response(strings.INSTITUTION_UUID_EXISTS,
                                                          status=strings.CONFLICT_409))
        except models.Institution.DoesNotExist:
            pass


    institution = models.Institution()
    institution.name = name
    institution.address = address
    institution.country = country
    institution.department = department
    institution.save()

    if uuid is not None:
        institution.id = uuid

    institution.save()

    data = {}

    response = helper.get_response_info(strings.INSTITUTION_INSERTED, data, status=strings.CREATED_201)

    return JsonResponse(response)
