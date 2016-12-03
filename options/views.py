from django.http import JsonResponse
from service import models as service_models
from options import models as options_models
from models import  ServiceDetailsOption, ServiceDetails, Service
from rest_framework.decorators import *
from common import helper, strings
from django.db import IntegrityError
import re
from django.shortcuts import render


# Returns the selected service details options information
@api_view(['GET'])
def get_service_sla(request, search_type, version, sla_uuid):
    """
    Retrieves the service sla

    """

    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(search_type)
    result_comp = prog.match(sla_uuid)

    if result_comp is None:
        response = helper.get_error_response(strings.SLA_INVALID_UUID)
        return JsonResponse(response, status=int(response["status"][:3]))


    if result is None:
        parsed_name = search_type.replace("_", " ").strip()
    else:
        uuid = search_type


    try:
        if result is None:
            service = service_models.Service.objects.get(name=parsed_name)
        else:
            service = service_models.Service.objects.get(id=uuid)


        service_details = service_models.ServiceDetails.objects.get(id_service=service.pk, version=version)

        sla = options_models.SLA.objects.get(id=sla_uuid)
        service_det_options = options_models.ServiceDetailsOption.objects.get(service_id=service.pk,
                                                                           service_details_id=service_details.pk,
                                                                           service_options_id=sla.service_option_id.pk)

        data = sla.as_json(service.name, version)
        response = helper.get_response_info(strings.SLA_INFORMATION, data)

    except service_models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except service_models.ServiceDetails.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

    except options_models.SLA.DoesNotExist:
        response = helper.get_error_response(strings.SLA_NOT_FOUND)

    except options_models.ServiceDetailsOption.DoesNotExist:
        response = helper.get_error_response(strings.SLA_SERVICE_DETAILS_MISMATCH)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    return JsonResponse(response, status=int(response["status"][:3]))


# Returns the selected service details options information
@api_view(['GET'])
def get_service_sla_parameter(request, search_type, version, sla_uuid, sla_param_uuid):
    """
    Retrieves the service sla parameter

    """
    """
    Inserts a service option object

    """
    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(search_type)
    result_comp = prog.match(sla_uuid)

    if result_comp is None:
        response = helper.get_error_response(strings.SLA_INVALID_UUID)
        return JsonResponse(response, status=int(response["status"][:3]))

    result_comp = prog.match(sla_param_uuid)
    if result_comp is None:
        response = helper.get_error_response(strings.SLA_PARAMETER_INVALID_UUID)
        return JsonResponse(response, status=int(response["status"][:3]))

    if result is None:
        parsed_name = search_type.replace("_", " ").strip()
    else:
        uuid = search_type

    try:
        if result is None:
            service = service_models.Service.objects.get(name=parsed_name)
        else:
            service = service_models.Service.objects.get(id=uuid)


        service_details = service_models.ServiceDetails.objects.get(id_service=service.pk, version=version)

        sla = options_models.SLA.objects.get(id=sla_uuid)

        service_det_options = options_models.ServiceDetailsOption.objects.get(service_id=service.pk,
                                                                           service_details_id=service_details.pk,
                                                                           service_options_id=sla.service_option_id.pk)

        sla_param = options_models.SLAParameter.objects.get(sla_id=sla.pk,
                                                            service_option_id=service_det_options.service_options_id,
                                                            parameter_id=sla_param_uuid)
        parameter = options_models.Parameter.objects.get(id=sla_param_uuid)

        data = parameter.as_json(service.name, version, sla_uuid)
        response = helper.get_response_info(strings.SLA_PARAMETER_INFORMATION, data)

    except service_models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except service_models.ServiceDetails.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

    except options_models.SLA.DoesNotExist:
        response = helper.get_error_response(strings.SLA_NOT_FOUND)

    except options_models.SLAParameter.DoesNotExist:
        response = helper.get_error_response(strings.SLA_PARAMETER_NOT_FOUND)

    except options_models.ServiceDetailsOption.DoesNotExist:
        response = helper.get_error_response(strings.SLA_SERVICE_DETAILS_MISMATCH)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)


    return JsonResponse(response, status=int(response["status"][:3]))


def get_options_for_service_details(request, version):
    response = {}

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result = prog.match(version)
    options = []

    if result is None:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "An invalid service component UUID was supplied"
        }
        return JsonResponse(response, status=int(response["status"][:3]))

    try:

        service_details = service_models.ServiceDetails.objects.get(id=version)

        serv_det_opt = options_models.ServiceDetailsOption.objects.filter(service_details_id=service_details)

        for o in serv_det_opt:
            o = options_models.ServiceOption.objects.get(id=o.service_options_id.pk)
            options.append(o.as_short())


        # if len(serv_det_comp) <= 0:
        #     raise component_models.ServiceDetailsComponent.DoesNotExist


        response["status"] = "200 OK"
        response["data"] = options
        response["info"] = "service component information"

    except service_models.ServiceDetails.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The specified service details do not exist"
        }

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }

    except options_models.ServiceOption.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service options were not found"
        }

    except options_models.ServiceDetailsOption.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "A service option matching the specified service version does not exists"
        }

    return JsonResponse(response, status=int(response["status"][:3]))

def get_parameters_for_sla(request, sla):
    response = {}

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result = prog.match(sla)
    params = []

    if result is None:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "An invalid service component UUID was supplied"
        }
        return JsonResponse(response, status=int(response["status"][:3]))

    try:

        sla = options_models.SLA.objects.get(id=sla)

        sla_params = options_models.SLAParameter.objects.filter(sla_id=sla, service_option_id=sla.service_option_id)

        for s in sla_params:
            s = options_models.Parameter.objects.get(id=s.parameter_id.pk)
            params.append(s.as_short())


        # if len(serv_det_comp) <= 0:
        #     raise component_models.ServiceDetailsComponent.DoesNotExist


        response["status"] = "200 OK"
        response["data"] = params
        response["info"] = "service component information"

    except options_models.SLA.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The specified SLA does not exist"
        }

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }

    except options_models.SLAParameter.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested SLA parameters were not found"
        }

    except options_models.Parameter.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "A parameter matching the specified SLA does not exists"
        }

    return JsonResponse(response, status=int(response["status"][:3]))


def get_service_options_all(request):
    response = {}

    query = request.GET.get('search')
    if query is not None:
        query = query.lower()

    service_options = options_models.ServiceOption.objects.all()
    response["status"] = "200 OK"
    response["data"] = [s.as_short() for s in service_options if (query == None or query == "") or query in s.name.lower()]
    response["info"] = "service options information"

    return JsonResponse(response, status=int(response["status"][:3]))

def get_parameter_all(request):
    response = {}

    query = request.GET.get('search')
    if query is not None:
        query = query.lower()

    parameters = options_models.Parameter.objects.all()
    response["status"] = "200 OK"
    response["data"] = [p.as_short() for p in parameters if (query == None or query == "") or query in p.name.lower()]
    response["info"] = "service options information"

    return JsonResponse(response, status=int(response["status"][:3]))

def get_sla_all(request):
    response = {}

    query = request.GET.get('search')
    if query is not None:
        query = query.lower()

    slas = options_models.SLA.objects.all()
    response["status"] = "200 OK"
    response["data"] = [s.as_short() for s in slas if (query == None or query == "") or query in s.name.lower()]
    response["info"] = "service options information"

    return JsonResponse(response, status=int(response["status"][:3]))

# Returns the selected service details options information
@api_view(['GET'])
def get_service_options(request, search_type, version):
    """
    Retrieves the service options

    """

    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(search_type)

    if result is None:
        parsed_name = search_type.replace("_", " ").strip()
    else:
        uuid = search_type

    try:
        if result is None:
            service = service_models.Service.objects.get(name=parsed_name)
        else:
            service = service_models.Service.objects.get(id=uuid)

        detail = service.get_service_details_by_version(version=str(version))
        options = ServiceDetailsOption.objects.filter(service_details_id=detail.id, service_id=detail.id_service.pk)

        data = helper.build_list_object("service_options", [ option.as_json() for option in options ])
        response = helper.get_response_info(strings.SERVICE_OPTIONS, data)

    except ServiceDetails.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

    except ServiceDetailsOption.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_OPTIONS_NOT_FOUND)

    except Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    return JsonResponse(response, status=int(response["status"][:3]))


def get_service_options_single(request, serv_opt_uuid):
    """
    Retrieves the service options

    """

    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(serv_opt_uuid)

    try:
        options = options_models.ServiceOption.objects.get(id=serv_opt_uuid)
        response = helper.get_response_info(strings.SERVICE_OPTIONS, options.as_short())

    except options_models.ServiceOption.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    return JsonResponse(response, status=int(response["status"][:3]))

def get_service_options_with_sla(request, serv_opt_uuid):
    """
    Retrieves the service options

    """

    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(serv_opt_uuid)

    try:
        options = options_models.ServiceOption.objects.get(id=serv_opt_uuid)
        response = helper.get_response_info(strings.SERVICE_OPTIONS, options.as_full_sla())

    except options_models.ServiceOption.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    return JsonResponse(response, status=int(response["status"][:3]))

def get_sla(request, sla_uuid):
    """
    Retrieves the service options

    """

    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(sla_uuid)

    try:
        sla = options_models.SLA.objects.get(id=sla_uuid)
        response = helper.get_response_info(strings.SERVICE_OPTIONS, sla.as_full())

    except options_models.SLA.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    return JsonResponse(response, status=int(response["status"][:3]))

def get_parameter(request, param_uuid):
    """
    Retrieves the service options

    """

    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(param_uuid)

    try:
        parameter = options_models.Parameter.objects.get(id=param_uuid)
        response = helper.get_response_info(strings.SERVICE_OPTIONS, parameter.as_short())

    except options_models.ServiceOption.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    return JsonResponse(response, status=int(response["status"][:3]))

def get_sla_parameter(request, sla_param_uuid):
    """
    Retrieves the service options

    """

    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(sla_param_uuid)

    try:
        sla_parameter = options_models.SLAParameter.objects.get(id=sla_param_uuid)
        response = helper.get_response_info(strings.SERVICE_OPTIONS, sla_parameter.as_full())

    except options_models.ServiceOption.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    return JsonResponse(response, status=int(response["status"][:3]))


def get_service_details_options(request, serv_det_option_uuid):
    """
    Retrieves the service options

    """

    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(serv_det_option_uuid)

    try:
        service_details_options = options_models.ServiceDetailsOption.objects.get(id=serv_det_option_uuid)
        response = helper.get_response_info(strings.SERVICE_OPTIONS, service_details_options.as_full())

    except options_models.ServiceDetailsOption.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_OPTIONS_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    return JsonResponse(response, status=int(response["status"][:3]))


def options_sla_write_ui(request):
    return render(request, 'service/write.html', {"type": "options_sla"})

def options_sla_edit_ui(request, sla_uuid):
    source = helper.current_site_url() + "/v1/options/sla/" + sla_uuid
    return render(request, 'service/write.html', {"type": "options_sla", "source": source})

def options_parameter_write_ui(request):
    return render(request, 'service/write.html', {"type": "options_parameter"})

def options_parameter_edit_ui(request, param_uuid):
    source = helper.current_site_url() + "/v1/options/parameter/" + param_uuid
    return render(request, 'service/write.html', {"type": "options_parameter", "source": source})

def options_sla_parameter_write_ui(request):
    return render(request, 'service/write.html', {"type": "options_sla_parameter"})

def options_sla_parameter_edit_ui(request, sla_param_uuid):
    source = helper.current_site_url() + "/v1/options/sla_parameter/" + sla_param_uuid
    return render(request, 'service/write.html', {"type": "options_sla_parameter", "source": source})

def service_options_write_ui(request):
    return render(request, 'service/write.html', {"type": "service_option"})

def service_options_edit_ui(request, serv_opt_uuid):
    source = helper.current_site_url() + "/v1/options/service_options_sla/" + serv_opt_uuid
    return render(request, 'service/write.html', {"type": "service_option", "source": source})

def service_details_options_write_ui(request):
    return render(request, 'service/write.html', {"type": "service_details_options"})

def service_details_options_edit_ui(request, serv_det_opt_uuid):
    source = helper.current_site_url() + "/v1/options/service_details_options/" + serv_det_opt_uuid
    return render(request, 'service/write.html', {"type": "service_details_options", "source": source}, )

# Updates a Service Option object
@api_view(['POST'])
def edit_service_option(request):
    """

    :param request:
    :return:
    """

    return insert_service_option(request)

# Inserts a Service Option object
@api_view(['POST'])
def insert_service_option(request):
    """
    Inserts a service option object

    """

    op_type = helper.get_last_url_part(request)
    uuid, name, service_option = None, None, None
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")

    if "name" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "name" in params:
        name = params.get('name')
        if name is None or len(name) == 0:
            return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NAME_EMPTY,
                                                          status=strings.REJECTED_406), status=406)
    elif op_type == "edit":
        name = None

    if "uuid" in params:

        uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service_option = options_models.ServiceOption.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_EXISTS,
                                                              status=strings.CONFLICT_409), status=409)
        except options_models.ServiceOption.DoesNotExist:
            service_option = options_models.ServiceOption()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404), status=404)
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif op_type == "add":
        service_option = options_models.ServiceOption()

    if name is not None:
        service_option.name = name
    if "description" in params:
        service_option.description = params.get('description')
    if "pricing" in params:
        service_option.pricing = params.get('pricing')

    if uuid is not None:
        service_option.id = uuid

    try:
        service_option.save()
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NAME_EXISTS, status=strings.REJECTED_406),
                            status=406)

    data = service_option.as_short()
    msg = strings.SERVICE_OPTION_INSERTED if op_type == "add" else strings.SERVICE_OPTION_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response, status=int(response["status"][:3]))


# Updates a SLA object
@api_view(['POST'])
def edit_SLA(request):
    """

    :param request:
    :return:
    """

    return insert_SLA(request)

# Inserts an SLA object
@api_view(['POST'])
def insert_SLA(request):
    """
    Inserts a SLA object

    """

    op_type = helper.get_last_url_part(request)
    uuid, name, SLA, service_option = None, None, None, None
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")

    if "name" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.SLA_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "name" in params:
        name = params.get('name')
        if name is None or len(name) == 0:
            return JsonResponse(helper.get_error_response(strings.SLA_NAME_EMPTY, status=strings.REJECTED_406),
                                status=406)
    elif op_type == "edit":
        name = None

    # if "service_option_uuid" not in params:
    #     return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_NOT_PROVIDED,
    #                                                   status=strings.REJECTED_406), status=406)


    if "service_option_uuid" in params:
        service_option_uuid = params.get('service_option_uuid')

        if service_option_uuid is None or len(service_option_uuid) == 0:
            return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_EMPTY, status=strings.REJECTED_406),
                                status=406)


        result = prog.match(service_option_uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service_option = options_models.ServiceOption.objects.get(id=service_option_uuid)
        except options_models.ServiceOption.DoesNotExist:
            return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND,
                                                          status=strings.NOT_FOUND_404), status=404)

    if "uuid" in params:

        uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            SLA = options_models.SLA.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.SLA_UUID_EXISTS,
                                                              status=strings.CONFLICT_409), status=409)
        except options_models.SLA.DoesNotExist:
            SLA = options_models.SLA()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.SLA_NOT_FOUND, status=strings.NOT_FOUND_404),
                                    status=404)
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SLA_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif op_type == "add":
        SLA = options_models.SLA()

    if name is not None:
        SLA.name = name
    SLA.service_option_id = service_option

    if uuid is not None:
        SLA.id = uuid

    try:
        SLA.save()
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.SLA_NAME_EXISTS, status=strings.REJECTED_406),
                            status=406)

    data = SLA.as_short()
    msg = strings.SLA_INSERTED if op_type == "add" else strings.SLA_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response, status=int(response["status"][:3]))


# Updates a Parameter object
@api_view(['POST'])
def edit_parameter(request):
    """

    :param request:
    :return:
    """

    return insert_parameter(request)

# Inserts a Parameter object
@api_view(['POST'])
def insert_parameter(request):
    """
    Inserts a paramater object

    """

    op_type = helper.get_last_url_part(request)
    uuid, name, type, parameter = None, None, None, None
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")

    if "name" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.PARAMETER_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "name" in params:
        name = params.get('name')
        if name is None or len(name) == 0:
            return JsonResponse(helper.get_error_response(strings.PARAMETER_NAME_EMPTY, status=strings.REJECTED_406),
                                status=406)
    elif op_type == "edit":
        name = None

    # if "type" not in params and op_type == "add":
    #     return JsonResponse(helper.get_error_response(strings.PARAMETER_TYPE_NOT_PROVIDED,
    #                                                   status=strings.REJECTED_406), status=406)
    # elif "type" in params:
    #     type = params.get('type')
    #     if type is None or len(type) == 0:
    #         return JsonResponse(helper.get_error_response(strings.PARAMETER_TYPE_EMPTY, status=strings.REJECTED_406),
    #                             status=406)
    # elif op_type == "edit":
    #     type = None

    if "uuid" in params:

        uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            parameter = options_models.Parameter.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.PARAMETER_UUID_EXISTS,
                                                              status=strings.CONFLICT_409), status=409)
        except options_models.Parameter.DoesNotExist:
            parameter = options_models.Parameter()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.PARAMETER_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404), status=404)
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.PARAMETER_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif op_type == "add":
        parameter = options_models.Parameter()

    if name is not None:
        parameter.name = name
    if "type" in params:
        parameter.type = params.get('type')
    if "expression" in params:
        parameter.expression = params.get('expression')

    if uuid is not None:
        parameter.id = uuid


    try:
        parameter.save()

    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.PARAMETER_NAME_EXISTS, status=strings.REJECTED_406),
                            status=406)

    data = parameter.as_short()
    msg = strings.PARAMETER_INSERTED if op_type == "add" else strings.PARAMETER_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response, status=int(response["status"][:3]))


# Updates a SLA parameter object
@api_view(['POST'])
def edit_SLA_parameter(request):
    """

    :param request:
    :return:
    """

    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")

    if "parameter_uuid" not in params or params["parameter_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.PARAMETER_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "sla_uuid" not in params or params["sla_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.SLA_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "service_options_uuid" not in params or params["service_options_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "new_parameter_uuid" not in params or params["new_parameter_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.PARAMETER_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "new_sla_uuid" not in params or params["new_sla_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.SLA_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "new_service_options_uuid" not in params or params["new_service_options_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_OPTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    parameter_id = params.get('parameter_uuid')
    sla_id = params.get('sla_uuid')
    service_options_id = params.get('service_options_uuid')

    new_parameter_id = params.get('new_parameter_uuid')
    new_sla_id = params.get('new_sla_uuid')
    new_service_options_id = params.get('new_service_options_uuid')


    result = prog.match(parameter_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(sla_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(service_options_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(new_parameter_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(new_sla_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(new_service_options_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    try:
        parameter = options_models.Parameter.objects.get(id=parameter_id)
        sla = options_models.SLA.objects.get(id=sla_id)
        service_option = options_models.ServiceOption.objects.get(id=service_options_id)

        new_parameter = options_models.Parameter.objects.get(id=new_parameter_id)
        new_sla = options_models.SLA.objects.get(id=new_sla_id)
        new_service_option = options_models.ServiceOption.objects.get(id=new_service_options_id)

    except options_models.ServiceOption.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)
    except options_models.Parameter.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.PARAMETER_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)
    except options_models.SLA.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SLA_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)

    try:
        sla_parameter = options_models.SLAParameter.objects.get(parameter_id=parameter, sla_id=sla, service_option_id=service_option)

        sla_parameter.parameter_id = new_parameter
        sla_parameter.sla_id = new_sla
        sla_parameter.service_option_id = new_service_option
        sla_parameter.save()
    except options_models.SLAParameter.DoesNotExist:
            return JsonResponse(helper.get_error_response(strings.SLA_PARAMETER_NOT_FOUND,
                                                          status=strings.NOT_FOUND_404), status=404)
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.SLA_PARAMETER_EXISTS,
                                                      status=strings.REJECTED_406), status=406)

    data = sla_parameter.as_json()
    msg = strings.SLA_PARAMETER_UPDATED
    status = strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response, status=int(response["status"][:3]))



# Inserts an SLA parameter object
@api_view(['POST'])
def insert_SLA_parameter(request):
    """
    Inserts a SLA parameter object

    """

    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")


    uuid, sla_parameter = None, None


    if "parameter_uuid" not in params or params["parameter_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.PARAMETER_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "sla_uuid" not in params or params["sla_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.SLA_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "service_options_uuid" not in params or params["service_options_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)


    parameter_uuid = params.get('parameter_uuid')
    sla_uuid = params.get('sla_uuid')
    service_option_uuid = params.get('service_options_uuid')

    if parameter_uuid is None or len(parameter_uuid) == 0:
        return JsonResponse(helper.get_error_response(strings.PARAMETER_UUID_EMPTY, status=strings.REJECTED_406),
                            status=406)


    if service_option_uuid is None or len(service_option_uuid) == 0:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_EMPTY, status=strings.REJECTED_406),
                            status=406)


    if sla_uuid is None or len(parameter_uuid) == 0:
        return JsonResponse(helper.get_error_response(strings.SLA_UUID_EMPTY, status=strings.REJECTED_406), status=406)



    result = prog.match(parameter_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(service_option_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(sla_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)


    try:
        service_option = options_models.ServiceOption.objects.get(id=service_option_uuid)
        sla = options_models.SLA.objects.get(id=sla_uuid)
        parameter = options_models.Parameter.objects.get(id=parameter_uuid)
    except options_models.ServiceOption.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)
    except options_models.SLA.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SLA_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)
    except options_models.Parameter.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.PARAMETER_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)

    obj, created = options_models.SLAParameter.objects.get_or_create(parameter_id=parameter,
                                                                          sla_id=sla,
                                                                     service_option_id=service_option)

    if not created:
        return JsonResponse(helper.get_error_response(strings.SLA_PARAMETER_EXISTS, status=strings.CONFLICT_409),
                            status=409)

    data = obj.as_json()
    msg = strings.SLA_PARAMETER_INSERTED
    status = strings.CREATED_201
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response, status=int(response["status"][:3]))

def edit_service_details_option(request):
    """

    :param request:
    :return:
    """

    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")

    if "service_uuid" not in params or params["service_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "service_details_uuid" not in params or params["service_details_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "service_options_uuid" not in params or params["service_options_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "new_service_uuid" not in params or params["new_service_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "new_service_details_uuid" not in params or params["new_service_details_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_DETAILS_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "new_service_options_uuid" not in params or params["new_service_options_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_OPTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    service_id = params.get('service_uuid')
    service_details_id = params.get('service_details_uuid')
    service_options_id = params.get('service_options_uuid')

    new_service_id = params.get('new_service_uuid')
    new_service_details_id = params.get('new_service_details_uuid')
    new_service_options_id = params.get('new_service_options_uuid')


    result = prog.match(service_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(service_details_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(service_options_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(new_service_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(new_service_details_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(new_service_options_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    try:
        service = service_models.Service.objects.get(id=service_id)
        service_details = service_models.ServiceDetails.objects.get(id=service_details_id)
        service_option = options_models.ServiceOption.objects.get(id=service_options_id)

        new_service = service_models.Service.objects.get(id=new_service_id)
        new_service_details = service_models.ServiceDetails.objects.get(id=new_service_details_id)
        new_service_option = options_models.ServiceOption.objects.get(id=new_service_options_id)

    except options_models.ServiceOption.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)
    except service_models.Service.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)
    except service_models.ServiceDetails.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)

    try:
        service_details_option = options_models.ServiceDetailsOption.objects.get(service_id=service,
                                                                                 service_details_id=service_details,
                                                                                 service_options_id=service_option)

        service_details_option.service_id = new_service
        service_details_option.service_details_id = new_service_details
        service_details_option.service_options_id = new_service_option
        service_details_option.save()
    except options_models.ServiceDetailsOption.DoesNotExist:
            return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_OPTIONS_NOT_FOUND,
                                                          status=strings.NOT_FOUND_404), status=404)
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_OPTIONS_EXISTS,
                                                      status=strings.REJECTED_406), status=406)

    data = service_details_option.as_json()
    msg = strings.SERVICE_DETAILS_OPTION_UPDATED
    status = strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response, status=int(response["status"][:3]))

# Inserts an service details option object
@api_view(['POST'])
def insert_service_details_option(request):
    """
    Inserts a service details object

    """

    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")


    uuid, service_details_option = None, None


    if "service_uuid" not in params or params["service_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "service_details_uuid" not in params or params["service_details_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "service_options_uuid" not in params or params["service_options_uuid"] is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    service_id = params.get('service_uuid')
    service_details_id = params.get('service_details_uuid')
    service_options_id = params.get('service_options_uuid')

    if service_id is None or len(service_id) == 0:
        return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_EMPTY, status=strings.REJECTED_406),
                            status=406)


    if service_details_id is None or len(service_details_id) == 0:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_UUID_EMPTY, status=strings.REJECTED_406),
                            status=406)


    if service_options_id is None or len(service_options_id) == 0:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_UUID_EMPTY, status=strings.REJECTED_406),
                            status=406)


    result = prog.match(service_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(service_details_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    result = prog.match(service_options_id)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    try:
        service = service_models.Service.objects.get(id=service_id)
        service_details = service_models.ServiceDetails.objects.get(id=service_details_id)
        service_option = options_models.ServiceOption.objects.get(id=service_options_id)

    except options_models.ServiceOption.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)
    except service_models.Service.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)
    except service_models.ServiceDetails.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND,
                                                      status=strings.NOT_FOUND_404), status=404)

    service_details_option, created = options_models.ServiceDetailsOption.objects.get_or_create(service_id=service,
                                                                          service_details_id=service_details,
                                                                     service_options_id=service_option)
    if not created:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OPTION_EXISTS, status=strings.CONFLICT_409),
                            status=409)

    data = service_details_option.as_json()
    msg = strings.SERVICE_DETAILS_OPTION_INSERTED
    status = strings.CREATED_201
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response, status=int(response["status"][:3]))

