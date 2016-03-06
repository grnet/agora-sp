from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from service import models
from component.models import ServiceComponent, ServiceDetailsComponent
from options.models import ServiceDetailsOption
from rest_framework.decorators import *
import re

@api_view(['GET'])
def list_services(request,  type):
    serv_models = models.Service.objects.all()
    params = request.GET.copy()
    detail_level = params.get('view')

    response = {}
    services = []

    if type == "portfolio":
        if detail_level is None or detail_level == "short":
            services = [s.as_portfolio() for s in serv_models]
        elif detail_level == "complete":
            services = [merge_service_components(s.as_complete_portfolio()) for s in serv_models]
        else:
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "The query parameter is invalid"
            }
    elif type == "catalogue":
        services = [s.as_catalogue() for s in serv_models]
    else:
        response["status"] = "404 Not Found"

    if len(services) > 0:
        response["status"] = "200 OK"
        response["data"] = {
            "count": len(services),
            "services": services
        }
        response["info"] = "list of services"

    return JsonResponse(response)

# Renders the list service view
@api_view(['GET'])
def show_service_list_view(request):
    return render(request, 'service/service_list.html')

# Renders the details view for the selected service
@api_view(['GET'])
def show_service_details(request, uuid):
    return render(request, 'service/service_portfolio_view.html', { "uuid": uuid })

# Returns all service object
@api_view(['GET'])
def list_service_objects(request, api_version):
    '''
    Lorem ipsum `dolor` sit amet, consectetur adipiscing elit. Etiam sodales lacus at _nulla_ fringilla fringilla.

    ### Consectetur adipiscing:

       * __dummy_var__: Nunc ut erat justo. Duis turpis augue, posuere a ornare sed,
       * another: Vestibulum suscipit congue neque sed faucibus.
       * `code`: Cras sit amet ullamcorper ipsum.
    '''

    serv_models =  models.Service.objects.all()
    services = [s.as_portfolio() for s in serv_models]

    response = {}
    services = []


    if len(serv_models) > 0:
        response["status"] = "200 OK"
        response["data"] = {
            "count": len(services),
            "services": services
        }
        response["info"] = "list of services"
    else:
        response["errors"] = {
                "services": "No services in database"
            }

    return JsonResponse(response)

# Returns the required information about the service chosen by uuid
@api_view(['GET'])
def get_service(request,  service_name_or_uuid):
    type = request.get_full_path().split("/")[2]
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
            serv = models.Service.objects.get(name=parsed_name)
        else:
            serv = models.Service.objects.get(id=uuid)


    except models.Service.DoesNotExist:

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

    except Exception as e:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service was not found"
        }

    if serv is not None:
        if type == "portfolio":
            if detail_level is None or detail_level == "short":
                service = serv.as_portfolio()
            elif detail_level == "complete":
                service = merge_service_components(serv.as_complete_portfolio())
            else:
                response["status"] = "404 Not Found"
                response["errors"] = {
                    "detail": "The query parameter is invalid"
                }
        elif type == "catalogue":
            service = serv.as_catalogue()
        else:
            response["status"] = "404 Not Found"
    else:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service was not found"
        }

    if service is not None:
        response["status"] = "200 OK"
        response["data"] = service
        response["info"] = "service information"

    return JsonResponse(response)

# Returns the service details about the service chosen by uuid
@api_view(['GET'])
def get_service_details(request, service_name_or_uuid, version):
    """
    Retrieves the service details of a specific service version

    ---

    type:
        service_name_or_uuid:
            required: true
            type: string
        version:
            required: true
            type: string

    responseMessages:
    - code: 404
    message: An invalid UUID was supplied
    consumes:
    - application/json
    produces:
    - application/json
    """
    params = request.GET.copy()

    detail_level = params.get('view')

    response = {}

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result = prog.match(service_name_or_uuid)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ")
        parsed_name.strip()
    else:
        uuid = service_name_or_uuid

    try:
        if result is None:
            uuid = models.Service.objects.get(name=parsed_name).pk

        detail = models.ServiceDetails.objects.get(id_service=uuid, version=version)

    except models.ServiceDetails.DoesNotExist:
        detail = None
    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }
        return JsonResponse(response)

    if detail is not None:
        response["status"] = "200 OK"
        response["data"] = detail
        response["info"] = "service detail information"

        if detail_level == 'short':
            response["data"] = detail.as_short()
        else:
            response["data"] = detail.as_complete()
    else:
        response["status"] = "404 Not Found"
        response["errors"] = {
                "detail": "Service details not found"
            }

    return JsonResponse(response)

# Creates a list of all service components belonging to a service
def merge_service_components(response):

        serv_components = ServiceDetailsComponent.objects.filter(service_id=response['uuid'])

        components = []

        for s in serv_components:
            components.append(ServiceComponent.objects.get(id=s.service_component_id.pk).as_json())

        response["components"] = components

        return response

# Returns a list of the service owners
@api_view(['GET'])
def get_service_owners(request, service_name_or_uuid):

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

            serv = models.Service.objects.get(name=parsed_name)
        else:
            serv = models.Service.objects.get(id=uuid)

    except models.Service.DoesNotExist:
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

# Returns the list of service details for the selected service
@api_view(['GET'])
def get_all_service_details(request, service_name_or_uuid):

    params = request.GET.copy()
    detail_level = params.get('view')

    response = {}

    complete = False

    if detail_level == "complete":
        complete = True

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result = prog.match(service_name_or_uuid)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ")
        parsed_name.strip()
    else:
        uuid = service_name_or_uuid

    try:
        if result is None:
            service = models.Service.objects.get(name=parsed_name)
        else:
            service = models.Service.objects.get(id=uuid)

        detail = service.get_service_details(complete)

    except models.ServiceDetails.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
                "detail": "Service details not found"
            }

        return JsonResponse(response)

    except models.Service.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
                "detail": "Service does not exist"
            }
        return JsonResponse(response)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }
        return JsonResponse(response)

    response["status"] = "200 OK"
    response["data"] = detail
    response["info"] = "service detail information"
    return JsonResponse(response)

# Returns the service institution
@api_view(['GET'])
def get_service_institution(request, service_name_or_uuid):

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
            serv = models.Service.objects.get(name=parsed_name)
        else:
            serv = models.Service.objects.get(id=uuid)

    except models.Service.DoesNotExist:
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
            response["data"] = serv.get_service_institution()
            response["info"] = "service institution information"

    return JsonResponse(response)

# Returns the institution of the service owner by both name and uuid
@api_view(['GET'])
def get_service_owner_institution(request, service_name_or_uuid, service_owner):


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
            serv = models.Service.objects.get(name=parsed_name)
        else:
            serv = models.Service.objects.get(id=uuid)

        if owner_match is None:
            owner = models.ServiceOwner.objects.get(first_name=owner_name[0], last_name=owner_name[1])
        else:
            owner = models.ServiceOwner.objects.get(id=owner_uuid)

    except models.ServiceOwner.DoesNotExist:
        owner = None
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service owner was not found"
        }
        return JsonResponse(response)

    except models.Service.DoesNotExist:
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

# Returns the selected services dependencies
@api_view(['GET'])
def get_service_dependencies(request,  service_name_or_uuid):

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(service_name_or_uuid)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ")
        parsed_name.strip()
    else:
        uuid = service_name_or_uuid

    try:
        if result is None:
            serv = models.Service.objects.get(name=parsed_name)
        else:
            serv = models.Service.objects.get(id=uuid)

    except models.Service.DoesNotExist:
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

            dependencies = serv.get_service_dependencies()
            response["status"] = "200 OK"
            response["data"] ={
                "count": len(dependencies),
                "dependencies": dependencies
            }
            response["info"] = "service dependencies information"

    return JsonResponse(response)

# Returns the selected services external dependencies
@api_view(['GET'])
def get_service_external_dependencies(request,  service_name_or_uuid):

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
            serv = models.Service.objects.get(name=parsed_name)
        else:
            serv = models.Service.objects.get(id=uuid)

    except models.Service.DoesNotExist:
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

            dependencies = serv.get_service_external_dependencies()

            response["status"] = "200 OK"
            response["data"] ={
                "count": len(dependencies),
                "dependencies": dependencies
            }

            response["info"] = "service external dependencies information"

    return JsonResponse(response)

# Return the selected service contact information
@api_view(['GET'])
def get_service_contact_information(request, service_name_or_uuid):

    params = request.GET.copy()

    response = {}

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result = prog.match(service_name_or_uuid)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ")
        parsed_name.strip()
    else:
        uuid = service_name_or_uuid

    try:
        if result is None:
            serv = models.Service.objects.get(name=parsed_name)
        else:
            serv = models.Service.objects.get(id=uuid)

    except models.Service.DoesNotExist:
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


    response["status"] = "200 OK"
    response["data"] = serv.get_service_contact_information()
    response["info"] = "service contact information"

    return JsonResponse(response)

# Returns the selected service details options information
@api_view(['GET'])
def get_service_options(request, service_name_or_uuid, version):

    params = request.GET.copy()

    response = {}

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result = prog.match(service_name_or_uuid)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ")
        parsed_name.strip()
    else:
        uuid = service_name_or_uuid

    try:
        if result is None:
            service = models.Service.objects.get(name=parsed_name)
        else:
            service = models.Service.objects.get(id=uuid)

        detail = service.get_service_details_by_version(version=version)
        options = ServiceDetailsOption.objects.get(service_details_id=detail.id, service_id=detail.id_service.pk).as_json()

    except models.ServiceDetails.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
                "detail": "Service details with that version not found"
            }

        return JsonResponse(response)

    except ServiceDetailsOption.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
                "detail": "This service has no service options for the current version"
            }

        return JsonResponse(response)

    except models.Service.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
                "detail": "Service does not exist"
            }
        return JsonResponse(response)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }
        return JsonResponse(response)


    response["status"] = "200 OK"
    response["data"] = options
    response["info"] = "options for service detail information"
    return JsonResponse(response)

