from django.http import JsonResponse
from django.shortcuts import render
from service import models
from component.models import ServiceDetailsComponent, ServiceComponentImplementationDetail
from options.models import ServiceDetailsOption
from owner.models import ServiceOwner, ContactInformation
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

# Inserts service
@api_view(['POST'])
def insert_service(request, type):

    params = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    uuid, service_owner, service_contact_information = None, None, None

    if "name" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    if "service_owner_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OWNER_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    if "service_contact_information_uuid" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_CONTACT_INFORMATION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    name = params.get('name')
    if name is None or len(name) == 0:
        return JsonResponse(helper.get_error_response(strings.SERVICE_NAME_EMPTY, status=strings.REJECTED_405))

    description_external = params.get('description_external') if "description_external" in params else None
    description_internal = params.get('description_internal') if "description_internal" in params else None
    service_area = params.get('service_area') if "service_area" in params else None
    service_type = params.get('service_type') if "service_type" in params else None
    request_procedures = params.get('request_procedures') if "request_procedures" in params else None
    funders_for_service = params.get('funders_for_service') if "funders_for_service" in params else None
    value_to_customer = params.get('value_to_customer') if "value_to_customer" in params else None
    risks = params.get('risks') if "risks" in params else None
    competitors = params.get('competitors') if "competitors" in params else None
    service_owner_uuid = params.get('service_owner_uuid')
    service_contact_information_uuid = params.get('service_contact_information_uuid')

    result = prog.match(service_owner_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OWNER_INVALID_UUID,
                                                      status=strings.REJECTED_405))

    result = prog.match(service_contact_information_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_CONTACT_INFORMATION_INVALID_UUID,
                                                      status=strings.REJECTED_405))

    try:
        service_owner = ServiceOwner.objects.get(id=service_owner_uuid)
        service_contact_information = ContactInformation.objects.get(id=service_contact_information_uuid)
    except ServiceOwner.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OWNER_NOT_FOUND, status=strings.NOT_FOUND_404))
    except ContactInformation.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.CONTACT_INFORMATION_NOT_FOUND, status=strings.NOT_FOUND_404))

    if "uuid" in params:
        uuid = params.get("uuid")

        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_INVALID_UUID,
                                                          status=strings.REJECTED_405))

        try:
            models.Service.objects.get(id=uuid)
            return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_EXISTS,
                                                          status=strings.CONFLICT_409))
        except models.Service.DoesNotExist:
            pass

    service = models.Service()
    service.name = name
    service.description_external = description_external
    service.description_internal = description_internal
    service.service_area = service_area
    service.service_type = service_type
    service.request_procedures = request_procedures
    service.funders_for_service = funders_for_service
    service.value_to_customer = value_to_customer
    service.risks = risks
    service.competitors = competitors
    service.id_service_owner = service_owner
    service.id_contact_information = service_contact_information
    if uuid is not None:
        service.id = uuid
    service.save()

    data = {}
    response = helper.get_response_info(strings.SERVICE_INSERTED, data, status=strings.CREATED_201)
    return JsonResponse(response)

# Inserts external service
@api_view(['POST'])
def insert_external_service(request, type):

    params = request.POST.copy()

    uuid = None

    if "name" not in params:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    name = params.get('name')
    description = params.get('description') if "description" in params else None
    service = params.get('service') if "service" in params else None
    details = params.get('details') if "details" in params else None

    if name is None or len(name) == 0:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_NAME_EMPTY, status=strings.REJECTED_405))

    if "uuid" in params:
        uuid = params.get("uuid")

        prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_INVALID_UUID,
                                                          status=strings.REJECTED_405))

        try:
            models.ExternalService.objects.get(id=uuid)
            return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_UUID_EXISTS,
                                                          status=strings.CONFLICT_409))
        except models.ExternalService.DoesNotExist:
            pass


    external_service = models.ExternalService()
    external_service.name = name
    external_service.description = description
    external_service.service = service
    external_service.details = details
    if uuid is not None:
        external_service.id = uuid
    external_service.save()

    data = {}
    response = helper.get_response_info(strings.EXTERNAL_SERVICE_INSERTED, data, status=strings.CREATED_201)
    return JsonResponse(response)

# Inserts service dependency
@api_view(['POST'])
def insert_service_dependency(request, service_name_or_uuid):

    params = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    service, service_dependency, parsed_name, uuid = None, None, None, None

    if "service_dependency" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    dependency_uuid = params.get("service_dependency")
    result = prog.match(dependency_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_INVALID_UUID,
                                                      status=strings.REJECTED_405))

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
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND, status=strings.NOT_FOUND_404))

    try:
        service_dependency = models.Service.objects.get(id=dependency_uuid)
    except models.Service.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404))

    obj, created = models.Service_DependsOn_Service.objects.get_or_create(id_service_one=service,
                                                                          id_service_two=service_dependency)
    if not created:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_EXISTS, status=strings.REJECTED_405))

    data = {}
    response = helper.get_response_info(strings.SERVICE_DEPENDENCY_INSERTED, data, status=strings.CREATED_201)
    return JsonResponse(response)

# Inserts external service dependency
@api_view(['POST'])
def insert_external_service_dependency(request, service_name_or_uuid):

    params = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    service, external_service_dependency, parsed_name, uuid = None, None, None, None

    if "external_service_dependency" not in params:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    external_dependency_uuid = params.get("external_service_dependency")
    result = prog.match(external_dependency_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_INVALID_UUID,
                                                      status=strings.REJECTED_405))

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
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND, status=strings.NOT_FOUND_404))

    try:
        external_service_dependency = models.ExternalService.objects.get(id=external_dependency_uuid)
    except models.ExternalService.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404))

    obj, created = models.Service_ExternalService.objects.get_or_create(id_service=service,
                                                                          id_external_service=external_service_dependency)
    if not created:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_EXISTS, status=strings.REJECTED_405))

    data = {}
    response = helper.get_response_info(strings.EXTERNAL_SERVICE_DEPENDENCY_INSERTED, data, status=strings.CREATED_201)
    return JsonResponse(response)

# Inserts user customer
@api_view(['POST'])
def insert_user_customer(request, service_name_or_uuid):

    params = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    service, parsed_name, service_uuid, uuid = None, None, None, None

    if "name" not in params:
        return JsonResponse(helper.get_error_response(strings.USER_CUSTOMER_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))
    if "role" not in params:
        return JsonResponse(helper.get_error_response(strings.USER_CUSTOMER_ROLE_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))
    name = params.get('name')
    role = params.get('role')

    if role is None or len(role) == 0:
        return JsonResponse(helper.get_error_response(strings.USER_CUSTOMER_ROLE_EMPTY,
                                                      status=strings.REJECTED_405))

    if (name, name) not in models.UserCustomer.USER_TYPES:
        return JsonResponse(helper.get_error_response(strings.USER_CUSTOMER_NAME_INVALID,
                                                      status=strings.REJECTED_405))

    if "uuid" in params:
        uuid = params.get('uuid')

        prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.USER_CUSTOMER_INVALID_UUID,
                                                          status=strings.REJECTED_405))

        try:
            models.UserCustomer.objects.get(id=uuid)
            return JsonResponse(helper.get_error_response(strings.USER_CUSTOMER_EXISTS,
                                                          status=strings.CONFLICT_409))
        except models.UserCustomer.DoesNotExist:
            pass

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

        user_customer = models.UserCustomer()
        user_customer.name = name
        user_customer.role = role
        user_customer.service_id = service
        if uuid is not None:
            user_customer.id = uuid

        user_customer.save()

    except models.Service.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND, status=strings.NOT_FOUND_404))


    data = {}
    response = helper.get_response_info(strings.USER_CUSTOMER_INSERTED, data, status=strings.CREATED_201)
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
