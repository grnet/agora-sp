from django.http import JsonResponse, HttpResponse
from owner import models
from service import models as service_models
from rest_framework.decorators import *
import re


# Returns a list of the service owners
@api_view(['GET'])
def get_service_owner(request, service_name_or_uuid):
    """
    Retrieves a the service owner

    """

    type = request.get_full_path().split("/")[1]
    params = request.GET.copy()
    detail_level = params.get('view')

    response = {}
    service = None

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result = prog.match(service_name_or_uuid)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ")
        parsed_name.strip()
    else:
        uuid = service_name_or_uuid

    try:
        if result is None:

            serv = service_models.Service.objects.get(name=parsed_name)
        else:
            serv = service_models.Service.objects.get(id=uuid)

    except service_models.Service.DoesNotExist:
        serv = None
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service was not found"
        }
    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }
        return JsonResponse(response)

    if serv is not None:
            response["status"] = "200 OK"
            response["data"] = serv.get_service_owners()
            response["info"] = "service owner information"

    return JsonResponse(response)


# Returns the institution of the service owner by both name and uuid
@api_view(['GET'])
def get_service_owner_institution(request, service_name_or_uuid, service_owner):
    """
    Retrieves the institution of the owner

    """

    type = request.get_full_path().split("/")[1]
    params = request.GET.copy()
    detail_level = params.get('view')

    response = {}
    service = None

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result = prog.match(service_name_or_uuid)

    owner_match = prog.match(service_owner)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ")
        parsed_name.strip()
    else:
        uuid = service_name_or_uuid

    if owner_match is None:
        owner_name = service_owner.split("_")
    else:
        owner_uuid = service_owner

    try:
        if result is None:
            serv = service_models.Service.objects.get(name=parsed_name)
        else:
            serv = service_models.Service.objects.get(id=uuid)

        if owner_match is None:
            owner = service_models.ServiceOwner.objects.get(first_name=owner_name[0], last_name=owner_name[1])
        else:
            owner = service_models.ServiceOwner.objects.get(id=owner_uuid)

    except models.ServiceOwner.DoesNotExist:
        owner = None
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service owner was not found"
        }
        return JsonResponse(response)

    except service_models.Service.DoesNotExist:
        serv = None
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service was not found"
        }
        return JsonResponse(response)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }
        return JsonResponse(response)

    if serv is not None:
            response["status"] = "200 OK"
            response["data"] = owner.get_institution()
            response["info"] = "service owner institution information"

    return JsonResponse(response)

