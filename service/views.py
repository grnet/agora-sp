from django.http import JsonResponse
from django.shortcuts import render
from service import models
from component.models import ServiceDetailsComponent, ServiceComponentImplementationDetail
from options.models import ServiceDetailsOption, ServiceOption
from owner.models import ServiceOwner, ContactInformation
from rest_framework.decorators import *
from common import helper, strings
from common.decorators import check_auth_and_type
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from collections import defaultdict
import re
from django.views.decorators.clickjacking import xframe_options_exempt

def list_catalogue_services(request):
    return list_services(request, "catalogue")

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

    if len(services) > 0:
        data = {
            "count": len(services),
            "services": services
        }
        response = helper.get_response_info(strings.SERVICE_LIST, data)

    return JsonResponse(response, status=int(response["status"][:3]))

def get_services_by_area(request, type):
    '''
    Retrieves a JSON list of all services for the service landing page.
    :return:
    '''
    serv_models = [s for s in models.Service.objects.all()]
    services = []

    for s in serv_models:
        if type == "catalogue":
            s1 = s.as_catalogue()
            if s1["service_details_list"]["count"] == 0:
                continue
            services.append(s)
        elif type == "portfolio":
            services.append(s)

    areas = models.Service.objects.values_list('service_area', flat=True).distinct()

    response = defaultdict(list)
    data = defaultdict(list)

    for area in areas:
        for service in services:

          if area == service.service_area:
            response[area].append(service.as_service_picker_compliant())

        if response[area] != []:
            icon = None
            try:
                icon = models.ServiceArea.objects.get(name=area).icon.name.split("/")[-1]
            except:
                pass
            data["areas"].append((response[area], icon))


    response = helper.get_response_info(strings.SERVICE_LIST, data)
    return JsonResponse(response, status=int(response["status"][:3]))

@xframe_options_exempt
def service_catalogue_picker(request):
    return service_picker(request, "catalogue")

@xframe_options_exempt
@check_auth_and_type
def service_picker(request, view_type):
    response =  render(request, "service/picker.html", {"view_type": view_type})

    if view_type is 'portfolio':
        response.set_cookie(key="api-credentials", value=request.session['api-info'])

    return response

def service_view_catalogue(request, service):

    return render(request, "service/catalogue.html", {"service_name": service})

@check_auth_and_type
def service_view_portfolio(request, service):
    response = render(request, "service/portfolio.html", {"service_name": service})
    response.set_cookie(key="api-credentials", value=request.session['api-info'])
    return response

# Renders the list service view
@api_view(['GET'])
def show_service_list_view(request):
    return render(request, 'service/service_list.html')

# Renders the details view for the selected service
# @check_service_ownership_or_superuser
@api_view(['GET'])
def show_service_details(request, uuid):
    return render(request, 'service/service_portfolio_view.html', { "uuid": uuid })


def get_service_options(request, service_name_or_uuid):
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

        details = models.ServiceDetails.objects.filter(id_service=service.pk)

        options = []
        op_set = set()

        for d in details:
            op = ServiceDetailsOption.objects.filter(service_details_id=d.pk)
            for o in op:
                if o.pk in op_set:
                    continue
                op_set.add(o.pk)
                options.append(o)


    except models.Service.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND), status=404)

    response["status"] = "200 OK"
    response["data"] = {
            "options": [o.as_json() for o in options]
        }

    return JsonResponse(response, status=int(response["status"][:3]))

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

def home_write_ui(request):
    return render(request, 'service/write.html', {"type": "home"})

# @login_required()
def service_write_ui(request):
    return render(request, 'service/write.html', {"type": "service"})

# @login_required()
def service_edit_ui(request, service_name_or_uuid):
    source = helper.current_site_url() + "/v1/portfolio/services/" + service_name_or_uuid + "/complete"
    return render(request, 'service/write.html', {"type": "service", "source": source})

@login_required()
def external_service_write_ui(request):
    return render(request, 'service/write.html', {"type": "external_service"})

@login_required()
def external_service_edit_ui(request, service_name_or_uuid):
    source = helper.current_site_url() + "/v1/services/external_service/" + service_name_or_uuid
    return render(request, 'service/write.html', {"type": "external_service", "source": source})

@login_required()
def service_area_write_ui(request):
    return render(request, 'service/write.html', {"type": "service_area"})

# @login_required()
def service_details_write_ui(request):
    return render(request, 'service/write.html', {"type": "service_details"})

@login_required()
def internal_dependency_write_ui(request):
    return render(request, 'service/write.html', {"type": "internal_service_dependencies"})

@login_required()
def internal_dependency_edit_ui(request, internal_dep_uuid):
    source = helper.current_site_url() + "/v1/services/internal_dependency/" + internal_dep_uuid
    return render(request, 'service/write.html', {"type": "internal_service_dependencies", "source": source})

# @login_required()
def external_dependency_write_ui(request):
    return render(request, 'service/write.html', {"type": "external_service_dependencies"})

# @login_required()
def external_dependency_edit_ui(request, external_dep_uuid):
    source = helper.current_site_url() + "/v1/services/external_dependency/" + external_dep_uuid
    return render(request, 'service/write.html', {"type": "external_service_dependencies", "source": source})

# @login_required()
def users_customers_write_ui(request):
    return render(request, 'service/write.html', {"type": "users_customers"})

# @login_required()
def users_customers_edit_ui(request, user_customer_uuid):
    source = helper.current_site_url() + "/v1/services/users_customers/" + user_customer_uuid
    return render(request, 'service/write.html', {"type": "users_customers", "source": source})

# @login_required()
def service_details_edit_ui(request, service_name_or_uuid, version):
    source = helper.current_site_url() + "/v1/portfolio/services/" + service_name_or_uuid + "/service_details/" + version + "/view"
    return render(request, 'service/write.html', {"type": "service_details", "source": source})

@login_required()
def service_write(request, type):
    return render(request, 'write/service.html')

def services_table(request):
    source = helper.current_site_url() + "/v1/portfolio/services"
    return render(request, 'service/write.html', {"type": "services_table", "source": source})


def get_external_service(request, service_name_or_uuid):

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
            service = models.ExternalService.objects.get(name=parsed_name)
        else:
            service = models.ExternalService.objects.get(id=uuid)

    except models.ExternalService.DoesNotExist:
        service = None
        response = helper.get_error_response(strings.EXTERNAL_SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)


    response = helper.get_response_info(strings.SERVICE_INFORMATION, service.as_json())

    return JsonResponse(response, status=int(response["status"][:3]))


def get_external_dependency(request, external_dep_uuid):

    response = {}
    service, parsed_name, uuid = None, None, None

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(external_dep_uuid)



    try:
        if result is None:
            response = helper.get_error_response(strings.INVALID_UUID)
            return JsonResponse(response, status=int(response["status"][:3]))
        else:
            ext_de = models.Service_ExternalService.objects.get(id=external_dep_uuid)

    except models.Service_ExternalService.DoesNotExist:
        response = helper.get_error_response(strings.EXTERNAL_SERVICE_NOT_FOUND)
        return JsonResponse(response, status=int(response["status"][:3]))

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)
            return JsonResponse(response, status=int(response["status"][:3]))

    response = helper.get_response_info(strings.SERVICE_INFORMATION, ext_de.as_full())

    return JsonResponse(response, status=int(response["status"][:3]))

def get_internal_dependency(request, internal_dep_uuid):

    response = {}
    service, parsed_name, uuid = None, None, None

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(internal_dep_uuid)

    try:
        if result is None:
            response = helper.get_error_response(strings.INVALID_UUID)
            return JsonResponse(response, status=int(response["status"][:3]))
        else:
            int_de = models.Service_DependsOn_Service.objects.get(id=internal_dep_uuid)

    except models.Service_DependsOn_Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DEPENDENCY_NOT_FOUND)
        return JsonResponse(response, status=int(response["status"][:3]))

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)
            return JsonResponse(response, status=int(response["status"][:3]))

    response = helper.get_response_info(strings.SERVICE_INFORMATION, int_de.as_full())

    return JsonResponse(response, status=int(response["status"][:3]))

def get_user_customer(request, user_customer_uuid):

    response = {}
    service, parsed_name, uuid = None, None, None

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(user_customer_uuid)

    try:
        user_customer = models.UserCustomer.objects.get(id=user_customer_uuid)

    except models.UserCustomer.DoesNotExist:
        service = None
        response = helper.get_error_response(strings.EXTERNAL_SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)


    response = helper.get_response_info(strings.SERVICE_INFORMATION, user_customer.as_full())

    return JsonResponse(response, status=int(response["status"][:3]))

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

def get_service_contact_complete(request,  service_name_or_uuid):
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
                service = service.as_complete_contact_portfolio()
            elif detail_level == "complete":
                service = service.as_complete_contact_portfolio()

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


def get_service_details_for_view(request, service_name_or_uuid, version):
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

        data = detail.as_portfolio_view()


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
# @login_required()
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
    uuid, service, service_owner, service_contact_information, service_internal_contact_information, name = None, None, None, None, None, None

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

        if service_owner_uuid is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_OWNER_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

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

        if service_contact_information_uuid is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_CONTACT_INFORMATION_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        result = prog.match(service_contact_information_uuid)
        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_CONTACT_INFORMATION_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service_contact_information = ContactInformation.objects.get(id=service_contact_information_uuid)
        except ContactInformation.DoesNotExist:
            return JsonResponse(helper.get_error_response(strings.CONTACT_INFORMATION_NOT_FOUND, status=strings.NOT_FOUND_404),
                                status=404)

    if "service_internal_contact_information_uuid" in params:
        service_internal_contact_information_uuid = params.get('service_internal_contact_information_uuid')

        if service_internal_contact_information_uuid is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_CONTACT_INFORMATION_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        result = prog.match(service_internal_contact_information_uuid)
        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_CONTACT_INFORMATION_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service_internal_contact_information = ContactInformation.objects.get(id=service_internal_contact_information_uuid)
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
    service.id_contact_information_internal = service_internal_contact_information

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

    if "service_dependency" not in params or params["service_dependency"] is None:
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


def get_services(request):

    query = request.GET.get('search')
    if query is not None:
        query = query.lower()

    services = [s.as_catalogue() for s in models.Service.objects.all()
              if (query == None or query == "") or query in s.name.lower()]
    response = helper.get_response_info(strings.SERVICE_OWNER_INFORMATION, services)

    return JsonResponse(response, status=int(response["status"][:3]))

def get_external_services(request):

    query = request.GET.get('search')
    if query is not None:
        query = query.lower()

    services = [s.as_json() for s in models.ExternalService.objects.all()
              if (query == None or query == "") or query in s.name.lower()]
    response = helper.get_response_info(strings.SERVICE_OWNER_INFORMATION, services)

    return JsonResponse(response, status=int(response["status"][:3]))

def get_service_versions(request):

    query = request.GET.get('search')
    if query is not None:
        query = query.lower()


    service = request.GET.get('service')
    if service is not None:
        service = service.lower()

    service_details = [s.as_portfolio_view() for s in models.ServiceDetails.objects.all()
              if (query == None or query == "") or ((service is None or service == "" or service == s.id_service.name.lower())
                                                    and query in (s.id_service.name.lower() + " " + s.version.lower()))]
    response = helper.get_response_info(strings.SERVICE_OWNER_INFORMATION, service_details)

    return JsonResponse(response, status=int(response["status"][:3]))

def get_service_areas(request):

    query = request.GET.get('search')
    if query is not None:
        query = query.lower()

    areas_set = set([s.service_area for s in models.Service.objects.all() if (query == None or query == "") or
                     (s.service_area is not None and query in s.service_area.lower())])

    areas_set = [{"area": a} for a in areas_set]

    response = helper.get_response_info(strings.SERVICE_OWNER_INFORMATION, areas_set)
    return JsonResponse(response, status=int(response["status"][:3]))


def get_service_types(request):

    query = request.GET.get('search')
    if query is not None:
        query = query.lower()

    types_set = set([s.service_type for s in models.Service.objects.all() if (query == None or query == "") or
                     (s.service_type is not None and query in s.service_type.lower())])

    types_set = [{"type": t} for t in types_set]

    response = helper.get_response_info(strings.SERVICE_OWNER_INFORMATION, types_set)
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

    if "service_dependency" not in params or params["service_dependency"] is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "new_service_dependency" not in params or params["new_service_dependency"] is None:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_DEPENDENCY_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "service_id" not in params or params["service_id"] is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    dependency_uuid = params.get("service_dependency")
    new_dependency_uuid = params.get("new_service_dependency")
    old_service_uuid = params.get("service_id")

    result = prog.match(dependency_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DEPENDENCY_INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(new_dependency_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_DEPENDENCY_INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(old_service_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_INVALID_UUID,
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
        old_service = models.Service.objects.get(id=old_service_uuid)

        obj = models.Service_DependsOn_Service.objects.get(id_service_one=old_service,
                                                                          id_service_two=service_dependency)

        obj.id_service_one = service
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
        uph = params.get('usage_policy_has')
        if uph == "false":
            service_details.usage_policy_has = False
        elif uph == "true":
            service_details.usage_policy_has = True
        else:
            service_details.usage_policy_has = uph

    if "usage_policy_url" in params:
        service_details.usage_policy_url = params.get('usage_policy_url')

    if "privacy_policy_has" in params:
        pph = params.get('privacy_policy_has')
        if pph == "false":
            service_details.privacy_policy_has = False
        elif pph == "true":
            service_details.privacy_policy_has = True
        else:
            service_details.privacy_policy_has = pph

    if "privacy_policy_url" in params:
        service_details.privacy_policy_url = params.get('privacy_policy_url')

    if "user_documentation_has" in params:
        udh = params.get('user_documentation_has')
        if udh == "false":
            service_details.user_documentation_has = False
        elif udh == "true":
            service_details.user_documentation_has = True
        else:
           service_details.user_documentation_has = udh

    if "user_documentation_url" in params:
        service_details.user_documentation_url = params.get('user_documentation_url')

    if "operations_documentation_has" in params:
        odh = params.get('operations_documentation_has')
        if odh == "false":
            service_details.operations_documentation_has = False
        elif odh == "true":
            service_details.operations_documentation_has = True
        else:
            service_details.operations_documentation_has = odh

    if "operations_documentation_url" in params:
        service_details.operations_documentation_url = params.get('operations_documentation_url')

    if "monitoring_has" in params:
        mh = params.get('monitoring_has')
        if mh == "false":
            service_details.monitoring_has = False
        elif mh == "true":
            service_details.monitoring_has = True
        else:
            service_details.monitoring_has = mh

    if "monitoring_url" in params:
        service_details.monitoring_url = params.get('monitoring_url')

    if "accounting_has" in params:
        ah = params.get('accounting_has')
        if ah == "false":
            service_details.accounting_has = False
        elif ah == "true":
            service_details.accounting_has = True
        else:
            service_details.accounting_has = ah

    if "accounting_url" in params:
        service_details.accounting_url = params.get('accounting_url')

    if "business_continuity_plan_has" in params:
        bcph = params.get('business_continuity_plan_has')
        if bcph == "false":
            service_details.business_continuity_plan_has = False
        elif bcph == "true":
            service_details.business_continuity_plan_has = True
        else:
            service_details.business_continuity_plan_has = bcph

    if "business_continuity_plan_url" in params:
        service_details.business_continuity_plan_url = params.get('business_continuity_plan_url')

    if "disaster_recovery_plan_has" in params:
        drph = params.get('disaster_recovery_plan_has')
        if drph == "false":
            service_details.disaster_recovery_plan_has = False
        elif drph == "true":
            service_details.disaster_recovery_plan_has = True
        else:
            service_details.disaster_recovery_plan_has = drph

    if "disaster_recovery_plan_url" in params:
        service_details.disaster_recovery_plan_url = params.get('disaster_recovery_plan_url')

    if "decommissioning_procedure_has" in params:
        dph = params.get('decommissioning_procedure_has')
        if dph == "false":
            service_details.decommissioning_procedure_has = False
        elif dph == "true":
            service_details.decommissioning_procedure_has = True
        else:
            service_details.decommissioning_procedure_has = dph

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

    if "external_service_dependency" not in params or params["external_service_dependency"] is None:
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

    if "external_service_dependency" not in params or params["external_service_dependency"] is None:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "new_external_service_dependency" not in params or params["new_external_service_dependency"] is None:
        return JsonResponse(helper.get_error_response(strings.NEW_EXTERNAL_SERVICE_DEPENDENCY_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "service_id" not in params or params["service_id"] is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    external_dependency_uuid = params.get("external_service_dependency")
    new_external_dependency_uuid = params.get("new_external_service_dependency")
    old_service_uuid = params.get("service_id")

    result = prog.match(external_dependency_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(new_external_dependency_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.NEW_EXTERNAL_SERVICE_DEPENDENCY_INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(old_service_uuid)
    if result is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_INVALID_UUID,
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
        old_service = models.Service.objects.get(id=old_service_uuid)

        obj = models.Service_ExternalService.objects.get(id_service=old_service,
                                                                          id_external_service=external_service_dependency)

        obj.id_service = service
        obj.id_external_service = new_external_service_dependency
        obj.save()

    except models.Service.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)

    except models.ExternalService.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.EXTERNAL_SERVICE_NOT_FOUND,
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
        return JsonResponse(response, status=int(response["status"][:3]))

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }
        return JsonResponse(response, status=int(response["status"][:3]))

    response["status"] = "200 OK"
    response["data"] = {}
    response["data"].update(serv.get_service_contact_information_internal())
    response["data"].update(serv.get_service_contact_information())
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
