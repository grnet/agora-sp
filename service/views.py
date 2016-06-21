from django.http import JsonResponse
from django.shortcuts import render
from service import models
from component.models import ServiceDetailsComponent, ServiceComponentImplementationDetail
from options.models import ServiceDetailsOption
from owner.models import ServiceOwner, ContactInformation
from rest_framework.decorators import *
from common import helper, strings
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from common.decorators import check_service_ownership_or_superuser
from django.db import IntegrityError
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
        for s in serv_models:
            s = s.as_catalogue()
            if s["service_details_list"]["count"] == 0:
                continue
            services.append(s)
        # services = [s.as_catalogue() for s in serv_models]

    if len(services) > 0:
        data = {
            "count": len(services),
            "services": services
        }
        response = helper.get_response_info(strings.SERVICE_LIST, data)

    return JsonResponse(response, status=int(response["status"][:3]))

# Renders the list service view
@api_view(['GET'])
def show_service_list_view(request):
    return render(request, 'service/service_list.html')

# Renders the details view for the selected service
# @check_service_ownership_or_superuser
@api_view(['GET'])
def show_service_details(request, uuid):
    return render(request, 'service/service_portfolio_view.html', { "uuid": uuid })

# Returns the service logo
def get_service_logo(request, service_name_or_uuid):
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(service_name_or_uuid)
    parsed_name, uuid = None, None

    response = {}

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
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND), status=404)

    response["status"] = "200 OK"
    response["data"] = {
            "logo": service.get_service_logo()
        }

    return JsonResponse(response, status=int(response["status"][:3]))

def get_catalogue_main_page(request):

    service_areas = models.Service.objects.values('service_area').distinct()

    services = {}
    name_help = {}

    for area in service_areas:
        services_buffer  = models.Service.objects.filter(service_area=area['service_area']).values_list('name', flat=True)
        for service in services_buffer:
            name_help[service] = service.replace(" ","_").strip()



    for area in service_areas:
        services_buffer  = models.Service.objects.filter(service_area=area['service_area']).values_list('name', flat=True)
        services[area['service_area']] = services_buffer


    return render(request, 'catalogue.html', {"areas": service_areas, "services": services, "names": name_help})

def get_service_catalogue_view(request, service):
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(service)
    parsed_name, uuid = None, None

    if result is None:
        parsed_name = service.replace("_", " ").strip()
    else:
        uuid = service

    try:
        if result is None:
            service = models.Service.objects.get(name=parsed_name)
        else:
            service = models.Service.objects.get(id=uuid)

    except models.Service.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND), status=404)

    try:
        service_details = models.ServiceDetails.objects.get(id_service=service, status="Active")
    except models.ServiceDetails.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND), status=404)
    # except:
    #     return JsonResponse({"error": "Multiple active service versions"})


    users = models.UserCustomer.objects.filter(service_id=service)
    service.users = users

    features = service_details.features_current
    if service.name == "B2DROP":
        features = features.strip('"B2DROP offers an intuitive user-interface via the web; ').strip().lstrip('Features :').strip().split("\n")
    else:
        features = features.strip('"').lstrip('"Features:').strip().split("\n")
    features = [f.strip().lstrip("-").strip().capitalize() for f in features]
    service_details.features_current = features

    service_options = ServiceDetailsOption.objects.filter(service_id=service, service_details_id=service_details)
    service.options = [so.service_options_id for so in service_options]

    return render(request, 'service.html', {"service": service, "service_details": service_details})

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

    return JsonResponse(response, status=int(response["status"][:3]))

# Returns the required information about the service chosen by uuid
# @check_service_ownership_or_superuser
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
        return JsonResponse(response, status=int(response["status"][:3]))

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

    return JsonResponse(response, status=int(response["status"][:3]))

# Returns the service details about the service chosen by uuid
# @check_service_ownership_or_superuser
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

    return JsonResponse(response, status=int(response["status"][:3]))

# Returns the list of service details for the selected service
# @check_service_ownership_or_superuser
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

    return JsonResponse(response, status=int(response["status"][:3]))

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
        return JsonResponse(response, status=int(response["status"][:3]))

    if serv is not None:
            response["status"] = "200 OK"
            response["data"] = serv.get_service_institution()
            response["info"] = "service institution information"

    return JsonResponse(response, status=int(response["status"][:3]))

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

    return JsonResponse(response, status=int(response["status"][:3]))

@api_view(['GET'])
def get_service_dependencies_with_graphics(request,  service_name_or_uuid):
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

        dependencies = service.get_service_dependencies_with_graphics()
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

    return JsonResponse(response, status=int(response["status"][:3]))


# Updates service
# @csrf_exempt
# @check_service_ownership_or_superuser
@api_view(['POST'])
def edit_service(request):
    """

    :param request:
    :return:
    """

    return insert_service(request)

# Inserts service
@api_view(['POST'])
def insert_service(request):
    """
    Inserts a service object

    """
    import json
    op_type = helper.get_last_url_part(request)
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")
    uuid, service, service_owner, service_contact_information, name = None, None, None, None, None

    if "name" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.SERVICE_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "name" in params:
        name = params.get('name')
        if (name is None or len(name) == 0) and "name" in params:
            return JsonResponse(helper.get_error_response(strings.SERVICE_NAME_EMPTY, status=strings.REJECTED_406),
                                status=406)
    elif op_type == "edit":
        name = None

    # if "service_owner_uuid" not in params:
    #     return JsonResponse(helper.get_error_response(strings.SERVICE_OWNER_UUID_NOT_PROVIDED,
    #                                                   status=strings.REJECTED_406), status=406)
    #
    # if "service_contact_information_uuid" not in params:
    #     return JsonResponse(helper.get_error_response(strings.SERVICE_CONTACT_INFORMATION_UUID_NOT_PROVIDED,
    #                                                   status=strings.REJECTED_406), status=406)


    if "service_owner_uuid" in params:
        service_owner_uuid = params.get('service_owner_uuid')
        result = prog.match(service_owner_uuid)
        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_OWNER_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service_owner = ServiceOwner.objects.get(id=service_owner_uuid)
        except ServiceOwner.DoesNotExist:
            return JsonResponse(helper.get_error_response(strings.SERVICE_OWNER_NOT_FOUND, status=strings.NOT_FOUND_404),
                                status=404)

    if "service_contact_information_uuid" in params:
        service_contact_information_uuid = params.get('service_contact_information_uuid')
        result = prog.match(service_contact_information_uuid)
        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_CONTACT_INFORMATION_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service_contact_information = ContactInformation.objects.get(id=service_contact_information_uuid)
        except ContactInformation.DoesNotExist:
            return JsonResponse(helper.get_error_response(strings.CONTACT_INFORMATION_NOT_FOUND, status=strings.NOT_FOUND_404),
                                status=404)

    if "uuid" in params:
        uuid = params.get("uuid")

        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service = models.Service.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_EXISTS,
                                                              status=strings.CONFLICT_409), status=409)
        except models.Service.DoesNotExist:
            service = models.Service()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404), status=404)
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_NOT_PROVIDED, status=strings.REJECTED_406),
                            status=406)
    elif op_type == "add":
        service = models.Service()

    if name is not None:
        service.name = name

    if "description_external" in params:
        service.description_external = params.get('description_external')

    if "description_internal" in params:
        service.description_internal = params.get('description_internal')

    if "service_area" in params:
        service.service_area = params.get('service_area')

    if "service_type" in params:
        service.service_type = params.get('service_type')

    if "request_procedures" in params:
        service.request_procedures = params.get('request_procedures')

    if "funders_for_service" in params:
        service.funders_for_service = params.get('funders_for_service')

    if "value_to_customer" in params:
        service.value_to_customer = params.get('value_to_customer')

    if "risks" in params:
        service.risks = params.get('risks')

    if "competitors" in params:
        service.competitors = params.get('competitors')

    service.id_service_owner = service_owner
    service.id_contact_information = service_contact_information

    if uuid is not None:
        service.id = uuid

    try:
        service.save()
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.SERVICE_NAME_EXISTS, status=strings.REJECTED_406),
                            status=406)

    data = service.as_portfolio()
    msg = strings.SERVICE_INSERTED if op_type == "add" else strings.SERVICE_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)
    return JsonResponse(response, status=int(response["status"][:3]))

# Updates external service
@api_view(['POST'])
def edit_external_service(request):
    """

    :param request:
    :return:
    """

    return insert_external_service(request)

# Inserts external service
@api_view(['POST'])
def insert_external_service(request):
    """
    Inserts an external service object

    """

    op_type = helper.get_last_url_part(request)
    params = helper.get_request_data(request)
    uuid, name, external_service = None, None, None

    if "name" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "name" in params:
        name = params.get('name')
        if name is None or len(name) == 0:
            return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_NAME_EMPTY,
                                                          status=strings.REJECTED_406), status=406)
    elif op_type == "edit":
        name = None

    if "uuid" in params:
        uuid = params.get("uuid")

        prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            external_service = models.ExternalService.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_UUID_EXISTS,
                                                              status=strings.CONFLICT_409), status=409)
        except models.ExternalService.DoesNotExist:
            external_service = models.ExternalService()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404), status=404)
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif op_type == "add":
        external_service = models.ExternalService()

    if name is not None:
        external_service.name = name

    if "description" in params:
        external_service.description = params.get('description')

    if "service" in params:
        external_service.service = params.get('service')

    if "details" in params:
        external_service.details = params.get('details')

    if uuid is not None:
        external_service.id = uuid


    try:
        external_service.save()
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_NAME_EXISTS, status=strings.REJECTED_406),
                            status=406)

    data = external_service.as_json()
    msg = strings.EXTERNAL_SERVICE_INSERTED if op_type == "add" else strings.EXTERNAL_SERVICE_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)
    return JsonResponse(response, status=int(response["status"][:3]))

# Inserts service dependency
@api_view(['POST'])
def insert_service_dependency(request, service_name_or_uuid):
    """
    Inserts a service dependency object

    """
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")
    service, service_dependency, parsed_name, uuid = None, None, None, None

    if "service_dependency" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    dependency_uuid = params.get("service_dependency")
    result = prog.match(dependency_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

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
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND, status=strings.NOT_FOUND_404),
                            status=404)

    try:
        service_dependency = models.Service.objects.get(id=dependency_uuid)
    except models.Service.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)

    obj, created = models.Service_DependsOn_Service.objects.get_or_create(id_service_one=service,
                                                                          id_service_two=service_dependency)
    if not created:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_EXISTS, status=strings.CONFLICT_409),
                            status=409)

    data = obj.as_json()
    response = helper.get_response_info(strings.SERVICE_DEPENDENCY_INSERTED, data, status=strings.CREATED_201)
    return JsonResponse(response, status=int(response["status"][:3]))

# Inserts service dependency
@api_view(['POST'])
def edit_service_dependency(request, service_name_or_uuid):
    """
    Inserts a service dependency object

    """
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")
    service, service_dependency, parsed_name, uuid = None, None, None, None

    if "service_dependency" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "new_service_dependency" not in params:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_DEPENDENCY_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    dependency_uuid = params.get("service_dependency")
    new_dependency_uuid = params.get("new_service_dependency")

    result = prog.match(dependency_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(new_dependency_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_DEPENDENCY_INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

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
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND, status=strings.NOT_FOUND_404),
                            status=404)

    try:
        service_dependency = models.Service.objects.get(id=dependency_uuid)
        new_service_dependency = models.Service.objects.get(id=new_dependency_uuid)

        obj = models.Service_DependsOn_Service.objects.get(id_service_one=service,
                                                                          id_service_two=service_dependency)

        obj.id_service_two = new_service_dependency
        obj.save()
    except models.Service.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)
    except models.Service_DependsOn_Service.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_NOT_FOUND,
                            status=strings.NOT_FOUND_404), status=404)
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_EXISTS,
                                                      status=strings.REJECTED_406), status=406)

    data = obj.as_json()
    response = helper.get_response_info(strings.SERVICE_DEPENDENCY_UPDATED, data, status=strings.UPDATED_202)
    return JsonResponse(response, status=int(response["status"][:3]))


# Updates service details for a specific service
@api_view(['POST'])
def edit_service_details(request, service_name_or_uuid):
    """

    :param request:
    :param service_name_or_uuid:
    :return:
    """

    return insert_service_details(request, service_name_or_uuid)

# Inserts service details for a specific service
@api_view(['POST'])
def insert_service_details(request, service_name_or_uuid):
    """
    Inserts a service details object

    """

    op_type = helper.get_last_url_part(request)
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")

    service, uuid, parsed_name, manual_uuid, version, service_details = None, None, None, None, None, None

    # if "service_uuid_name" not in params:
    #     return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_NOT_PROVIDED,
    #                                                   status=strings.REJECTED_406))


    if "version" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_VERSION_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "version" in params:
        version = params.get('version')
        if version is None or len(version) == 0:
            return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_VERSION_EMPTY,
                                                          status=strings.REJECTED_406), status=406)
    elif op_type == "edit":
        version = None

    # service_uuid_name = params.get("service_uuid_name")
    service_uuid_name = service_name_or_uuid

    result = prog.match(service_uuid_name)

    try:
        if result is None:
            parsed_name = service_uuid_name.replace("_", " ").strip()
            service = models.Service.objects.get(name=parsed_name)

        else:
            uuid = service_uuid_name

            secondary_check = prog.match(uuid)

            if secondary_check is None:
                return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                              status=strings.REJECTED_406), status=406)

            service = models.Service.objects.get(id=uuid)

    except models.Service.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND, status=strings.NOT_FOUND_404),
                            status=404)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID, status=strings.REJECTED_406),
                                status=406)


    if "uuid" in params:

        manual_uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service_details = models.ServiceDetails.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_EXISTS,
                                                              status=strings.CONFLICT_409), status=409)
        except models.ServiceDetails.DoesNotExist:
            service_details = models.ServiceDetails()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND,
                                                              status=strings.REJECTED_406), status=406)
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_UUID_NOT_PROVIDED,
                                                      status=strings.NOT_FOUND_404), status=404)
    elif op_type == "add":
        service_details = models.ServiceDetails()

    service_details.id_service = service

    if version is not None:
        service_details.version = version

    if "status" in params:
        service_details.status = params.get('status')

    if "features_current" in params:
        service_details.features_current = params.get('features_current')

    if "features_future" in params:
        service_details.features_future = params.get('features_future')

    if "usage_policy_has" in params:
        service_details.usage_policy_has = params.get('usage_policy_has')

    if "usage_policy_url" in params:
        service_details.usage_policy_url = params.get('usage_policy_url')

    if "user_documentation_has" in params:
        service_details.user_documentation_has = params.get('user_documentation_has')

    if "user_documentation_url" in params:
        service_details.user_documentation_url = params.get('user_documentation_url')

    if "operations_documentation_has" in params:
        service_details.operations_documentation_has = params.get('operations_documentation_has')

    if "operations_documentation_url" in params:
        service_details.operations_documentation_url = params.get('operations_documentation_url')

    if "monitoring_has" in params:
        service_details.monitoring_has = params.get('monitoring_has')

    if "monitoring_url" in params:
        service_details.monitoring_url = params.get('monitoring_url')

    if "accounting_has" in params:
        service_details.accounting_has = params.get('accounting_has')

    if "accounting_url" in params:
        service_details.accounting_url = params.get('accounting_url')

    if "business_continuity_plan_has" in params:
        service_details.business_continuity_plan_has = params.get('business_continuity_plan_has')

    if "business_continuity_plan_url" in params:
        service_details.business_continuity_plan_url = params.get('business_continuity_plan_url')

    if "disaster_recovery_plan_has" in params:
        service_details.disaster_recovery_plan_has = params.get('disaster_recovery_plan_has')

    if "disaster_recovery_plan_url" in params:
        service_details.disaster_recovery_plan_url = params.get('disaster_recovery_plan_url')

    if "decommissioning_procedure_has" in params:
        service_details.decommissioning_procedure_has = params.get('decommissioning_procedure_has')

    if "decommissioning_procedure_url" in params:
        service_details.decommissioning_procedure_url = params.get('decommissioning_procedure_url')

    if "cost_to_run" in params:
        service_details.cost_to_run = params.get('cost_to_run')

    if "cost_to_build" in params:
        service_details.cost_to_build = params.get('cost_to_build')

    if "use_cases" in params:
        service_details.use_cases = params.get('use_cases')

    if "is_in_catalogue" in params:
        is_in_catalogue = params.get('is_in_catalogue')
        if type(is_in_catalogue) is not bool:
            return JsonResponse(helper.get_error_response(strings.VARIABLE_MUST_BE_BOOLEAN, status=strings.REJECTED_406,
                                                          additional_status_msg="is_in_catalogue"), status=406)
        service_details.is_in_catalogue = is_in_catalogue

    if manual_uuid is not None:
        service_details.id = manual_uuid


    try:
        service_details.save()
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_VERSION_EXISTS, status=strings.REJECTED_406),
                            status=406)

    data = service_details.as_json()
    msg = strings.SERVICE_DETAILS_INSERTED if op_type == "add" else strings.SERVICE_DETAILS_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)
    return JsonResponse(response, status=int(response["status"][:3]))


# Inserts external service dependency
@api_view(['POST'])
def insert_external_service_dependency(request, service_name_or_uuid):
    """
    Inserts a external service details object

    """
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")
    service, external_service_dependency, parsed_name, uuid = None, None, None, None

    if "external_service_dependency" not in params:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    external_dependency_uuid = params.get("external_service_dependency")
    result = prog.match(external_dependency_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

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
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND, status=strings.NOT_FOUND_404),
                            status=404)

    try:
        external_service_dependency = models.ExternalService.objects.get(id=external_dependency_uuid)
    except models.ExternalService.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)

    obj, created = models.Service_ExternalService.objects.get_or_create(id_service=service,
                                                                          id_external_service=external_service_dependency)
    if not created:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_EXISTS, status=strings.CONFLICT_409),
                            status=409)

    data = obj.as_json()
    response = helper.get_response_info(strings.EXTERNAL_SERVICE_DEPENDENCY_INSERTED, data, status=strings.CREATED_201)
    return JsonResponse(response, status=int(response["status"][:3]))

# Inserts external service dependency
@api_view(['POST'])
def edit_external_service_dependency(request, service_name_or_uuid):
    """
    Inserts a external service details object

    """
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")
    service, external_service_dependency, parsed_name, uuid = None, None, None, None

    if "external_service_dependency" not in params:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "new_external_service_dependency" not in params:
        return JsonResponse(helper.get_error_response(strings.NEW_EXTERNAL_SERVICE_DEPENDENCY_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    external_dependency_uuid = params.get("external_service_dependency")
    new_external_dependency_uuid = params.get("new_external_service_dependency")

    result = prog.match(external_dependency_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(new_external_dependency_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.NEW_EXTERNAL_SERVICE_DEPENDENCY_INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

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
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND, status=strings.NOT_FOUND_404), status=404)

    try:
        external_service_dependency = models.ExternalService.objects.get(id=external_dependency_uuid)
        new_external_service_dependency = models.ExternalService.objects.get(id=new_external_dependency_uuid)

        obj = models.Service_ExternalService.objects.get(id_service=service,
                                                                          id_external_service=external_service_dependency)

        obj.id_external_service = new_external_service_dependency
        obj.save()

    except models.ExternalService.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)
    except models.Service_ExternalService.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_EXISTS,
                                                      status=strings.REJECTED_406), status=404)

    data = obj.as_json()
    response = helper.get_response_info(strings.EXTERNAL_SERVICE_DEPENDENCY_INSERTED, data, status=strings.CREATED_201)
    return JsonResponse(response, status=int(response["status"][:3]))


# Updates user customer
@api_view(['POST'])
def edit_user_customer(request, service_name_or_uuid):
    """

    :param request:
    :param service_name_or_uuid:
    :return:
    """

    return insert_user_customer(request, service_name_or_uuid)

# Inserts user customer
@api_view(['POST'])
def insert_user_customer(request, service_name_or_uuid):
    """
    Inserts an user customer object

    """

    op_type = helper.get_last_url_part(request)
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")
    service, parsed_name, service_uuid, uuid, user_customer, name, role = None, None, None, None, None, None, None

    if "name" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.USER_CUSTOMER_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "name" in params:
        name = params.get('name')
        if (name, name) not in models.UserCustomer.USER_TYPES:
            return JsonResponse(helper.get_error_response(strings.USER_CUSTOMER_NAME_INVALID,
                                                          status=strings.REJECTED_406), status=406)
    elif op_type == "edit":
        name = None

    if "role" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.USER_CUSTOMER_ROLE_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "role" in params:
        role = params.get('role')
        if role is None or len(role) == 0:
            return JsonResponse(helper.get_error_response(strings.USER_CUSTOMER_ROLE_EMPTY,
                                                          status=strings.REJECTED_406), status=406)
    elif op_type == "edit":
        role = None

    if "uuid" in params:
        uuid = params.get('uuid')

        prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.USER_CUSTOMER_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            user_customer = models.UserCustomer.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.USER_CUSTOMER_EXISTS,
                                                              status=strings.CONFLICT_409), status=409)
        except models.UserCustomer.DoesNotExist:
            user_customer = models.UserCustomer()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.USER_CUSTOMER_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404), status=404)
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.USER_CUSTOMER_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif op_type == "add":
        user_customer = models.UserCustomer()

    result = prog.match(service_name_or_uuid)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ").strip()
    else:
        service_uuid = service_name_or_uuid

    try:
        if result is None:
            service = models.Service.objects.get(name=parsed_name)
        else:
            service = models.Service.objects.get(id=service_uuid)

    except models.Service.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND, status=strings.NOT_FOUND_404),
                            status=404)

    if name is not None:
        user_customer.name = name

    if role is not None:
        user_customer.role = role

    user_customer.service_id = service

    if uuid is not None:
        user_customer.id = uuid

    user_customer.save()

    data = user_customer.as_json()
    msg = strings.USER_CUSTOMER_INSERTED if op_type == "add" else strings.USER_CUSTOMER_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)
    return JsonResponse(response, status=int(response["status"][:3]))

# Returns the selected services external dependencies
# @check_service_ownership_or_superuser
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

    return JsonResponse(response, status=int(response["status"][:3]))

# Return the selected service contact information
# @api_view(['GET'])
# @check_service_ownership_or_superuser
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
        return JsonResponse(response, status=int(response["status"][:3]))


    response["status"] = "200 OK"
    response["data"] = serv.get_service_contact_information()
    response["info"] = "service contact information"

    return JsonResponse(response, status=int(response["status"][:3]))

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
                "links":{
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
            "links": {
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
