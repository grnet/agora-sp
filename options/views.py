from django.http import JsonResponse
from service import models as service_models
from options import models as options_models
from models import  ServiceDetailsOption, ServiceDetails, Service
from rest_framework.decorators import *
from common import helper, strings
import re


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
        return JsonResponse(response)


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

    return JsonResponse(response)

# Returns the selected service details options information
@api_view(['GET'])
def get_service_sla_parameter(request, search_type, version, sla_uuid, sla_param_uuid):
    """
    Retrieves the service sla parameter

    """

    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(search_type)
    result_comp = prog.match(sla_uuid)

    if result_comp is None:
        response = helper.get_error_response(strings.SLA_INVALID_UUID)
        return JsonResponse(response)

    result_comp = prog.match(sla_param_uuid)
    if result_comp is None:
        response = helper.get_error_response(strings.SLA_PARAMETER_INVALID_UUID)
        return JsonResponse(response)

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

        sla_param = options_models.SLAParameter.objects.get(sla_id=sla.pk, service_option_id=service_det_options.service_options_id,
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


    return JsonResponse(response)

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

    return JsonResponse(response)
