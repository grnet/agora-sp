from django.http import JsonResponse
from django.shortcuts import render
from service import models
from component.models import ServiceDetailsComponent, ServiceComponentImplementationDetail
from options.models import ServiceDetailsOption
from rest_framework.decorators import *
from django.contrib.sites.models import Site
from common import helper, strings
import re


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
            response = helper.get_error_response(strings.INVALID_QUERY_PARAMETER)

    elif type == "catalogue":
        services = [s.as_catalogue() for s in serv_models]

    if len(services) > 0:
        data = {
            "count": len(services),
            "services": services
        }
        response = helper.get_response_info(strings.SERVICE_LIST, data)

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

    if detail_level is not None and detail_level != "short" and detail_level != "complete":
        response = helper.get_error_response(strings.INVALID_QUERY_PARAMETER)
        return JsonResponse(response)

    response = {}
    service, parsed_name, uuid = None, None, None

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(service_name_or_uuid)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ").strip()
    else:
        uuid = service_name_or_uuid

    try:
        if result is None:
            service = models.Service.objects.get(name=parsed_name)
        else:
            service = models.Service.objects.get(id=uuid)

    except models.Service.DoesNotExist:
        service = None
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    if service is not None:
        if type == "portfolio":
            if detail_level is None or detail_level == "short":
                service = service.as_portfolio()
            elif detail_level == "complete":
                service = service.as_complete_portfolio()

        elif type == "catalogue":
            service = service.as_catalogue()

        response = helper.get_response_info(strings.SERVICE_INFORMATION, service)

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
    parsed_name, uuid = None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(service_name_or_uuid)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ").strip()
    else:
        uuid = service_name_or_uuid

    try:
        if result is None:
            service = models.Service.objects.get(name=parsed_name)
        else:
            service = models.Service.objects.get(id=uuid)

        detail = models.ServiceDetails.objects.get(id_service=service.pk, version=version)

        if detail_level == 'short':
            data = detail.as_short()
        else:
            data = merge_service_components(detail)

        response = helper.get_response_info(strings.SERVICE_DETAIL_INFORMATION, data)

    except models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except models.ServiceDetails.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

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
    parsed_name, uuid = None, None

    if detail_level == "complete":
        complete = True

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(service_name_or_uuid)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ").strip()
    else:
        uuid = service_name_or_uuid

    try:
        if result is None:
            service = models.Service.objects.get(name=parsed_name)
        else:
            service = models.Service.objects.get(id=uuid)

        detail = service.get_service_details(complete)
        data = {
            "count": len(detail),
            "service_details": detail
        }
        response = helper.get_response_info(strings.SERVICE_DETAIL_INFORMATION, data)

    except models.ServiceDetails.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

    except models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

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
    parsed_name, uuid = None, None

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ").strip()
    else:
        uuid = service_name_or_uuid

    try:
        if result is None:
            service = models.Service.objects.get(name=parsed_name)
        else:
            service = models.Service.objects.get(id=uuid)

        dependencies = service.get_service_dependencies()
        data = {
            "count": len(dependencies),
            "dependencies": dependencies
        }
        response = helper.get_response_info(strings.SERVICE_DEPENDENCIES_INFORMATION, data)

    except models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    return JsonResponse(response)

# Returns the selected services external dependencies
@api_view(['GET'])
def get_service_external_dependencies(request,  service_name_or_uuid):
    """
    Retrieves the external service dependencies

    """

    response = {}
    service, parsed_name, uuid = None, None, None

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(service_name_or_uuid)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ").strip()
    else:
        uuid = service_name_or_uuid

    try:
        if result is None:
            service = models.Service.objects.get(name=parsed_name)
        else:
            service = models.Service.objects.get(id=uuid)

        dependencies = service.get_service_external_dependencies()
        data = {
            "count": len(dependencies),
            "dependencies": dependencies
        }
        response = helper.get_response_info(strings.SERVICE_EXTERNAL_DEPENDENCIES_INFORMATION, data)

    except models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

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


# Retrieve a service object by UUID or Name
def get_service_object():
    pass

# Creates a list of all service components belonging to a service
def merge_service_components(service_details):

        serv_components_imp_det = ServiceDetailsComponent.objects.filter(service_id=service_details.id_service.pk,
                                                                 service_details_id=service_details.pk)
        components = []
        seen = set()

        for s in serv_components_imp_det:
            scid = ServiceComponentImplementationDetail.objects.get(id=s.service_component_implementation_detail_id.pk)
            if scid.component_id.pk in seen:
                continue

            seen.add(scid.component_id.pk)
            components.append(scid.component_id.as_short(service_details.id_service.pk, service_details.version))

        data = service_details.as_complete()

        if len(components) > 0:
            data["service_components_list"] = {
                "count": len(components),
                "service_components_link":{
                    "related": {
                        "href":  helper.current_site_url()+"/v1/portfolio/services/" + str(service_details.id_service.name) + "/service_details/"
                                         + service_details.version + "/service_components",
                        "meta": {
                            "desc": "Link to the services components."
                        }
                    }},
                "service_components": components
            }
        else:
               data["components"] = {
                "components": "This service has no service components."
            }


        serv_options = ServiceDetailsOption.objects.filter(service_id=service_details.id_service.pk,
                                                           service_details_id=service_details.pk)

        options = [so.as_json() for so in serv_options]
        data["service_options_list"] = {
            "count": len(options),
            "service_options_link": {
                "related": {
                    "href": helper.current_site_url() + "/v1/portfolio/services/" + service_details.id_service.name.replace(" ", "_")
                            + "/service_details/" + service_details.version + "/service_options",
                    "meta": {
                        "desc": "Link to the service options"
                    }
                }
            },
            "service_options": options
        }


        return data
