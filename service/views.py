from django.core.serializers import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from service import models
from component.models import ServiceComponent, ServiceDetailsComponent, ServiceComponentImplementationDetail
from options.models import ServiceDetailsOption
from rest_framework.decorators import *
from agora_utils import *
import re
from django.contrib.sites.models import Site

@api_view(['GET'])
def list_services(request,  type):
    """
    Retrieves a JSON list of all services in the system

    """
    serv_models = models.Service.objects.all()
    params = request.GET.copy()
    detail_level = params.get('view')

    response = {}
    services = []
    if type == "portfolio":
        if detail_level is None or detail_level == "short":
            services = [s.as_portfolio() for s in serv_models]
        elif detail_level == "complete":
            services = [s.as_complete_portfolio() for s in serv_models]
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
    """
    Retrieves a list of objects of all services in the system

    """

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
    """
    Retrieves a specific service by name or uuid

    """
    type = request.get_full_path().split("/")[3]
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
                service = serv.as_complete_portfolio()
            else:
                response["status"] = "404 Not Found"
                response["errors"] = {
                    "detail": "The query parameter is invalid"
                }
        elif type == "catalogue":
            service = serv.as_catalogue()
        else:
            response["status"] = "404 Not Found"
            response["errors"] = {
            "detail": "No such detail level."
        }
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

    host = generete_full_url(request)

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

        detail = models.ServiceDetails.objects.get(id_service=service.pk, version=version)
        response["status"] = "200 OK"


        response["data"] = detail

        # response["data"]["links"]["related"]["href"] = host +  response["data"]["links"]["related"]["href"]

        response["info"] = "service detail information"

        if detail_level == 'short':
            response["data"] = detail.as_short()
        else:
            response["data"] = merge_service_components(detail)

    except models.Service.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "Service not found"
        }
    except models.ServiceDetails.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
                "detail": "Service details not found"
            }
    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }
        return JsonResponse(response)

    return JsonResponse(response)

# Returns the list of service details for the selected service
@api_view(['GET'])
def get_all_service_details(request, service_name_or_uuid):
    """
    Retrieves the service details of a service

    """
    params = request.GET.copy()
    detail_level = params.get('view')

    response = {}

    complete = False

    # host = generete_full_url(request)


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

    # for det in detail:
    #     det["links"]["related"]["href"] = host +  det["links"]["related"]["href"]

    response["data"] = detail
    response["info"] = "service detail information"
    return JsonResponse(response)

# Returns the service institution
@api_view(['GET'])
def get_service_institution(request, service_name_or_uuid):
    """
    Retrieves a the service institution

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

# Returns the selected services dependencies
@api_view(['GET'])
def get_service_dependencies(request,  service_name_or_uuid):
    """
    Retrieves the service dependencies

    """
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
    """
    Retrieves the external service dependencies

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
    """
    Retrieves the contact information for a specific service

    """
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
    """
    Retrieves the service options

    """
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

# Retrieve a service object by UUID or Name
def get_service_object():
    pass

# Creates a list of all service components belonging to a service
def merge_service_components(service_details):

        serv_components_imp_det = ServiceDetailsComponent.objects.filter(service_id=service_details.id_service.pk,
                                                                 service_details_id=service_details.pk)
        components = []

        for s in serv_components_imp_det:
            scid = ServiceComponentImplementationDetail.objects.get(id=s.service_component_implementation_detail_id.pk)
            components.append(scid.component_id.as_short(service_details.id_service.pk, service_details.version))

        data = service_details.as_complete()

        if (len(components)>0):
            data["components"] = {
                "count": len(components),
                "service_components_links":{
                    "related": {
                        "href":  current_site_url()+"/v1/portfolio/services/" + str(service_details.id_service.pk) + "/service_details/"
                                         + service_details.version + "/service_components",
                        "meta": {
                            "desc": "Link to the services components."
                        }
                    }},
                "data": components
            }
        else:
               data["components"] = {
                "components": "This service has no service components."
            }

        return data

def current_site_url():
        """Returns fully qualified URL (no trailing slash) for the current site."""

        current_site = Site.objects.get_current()
        url = 'http://%s' % (current_site.domain+"/api")

        return url
