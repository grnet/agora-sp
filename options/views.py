from django.http import JsonResponse
from service import models as service_models
from options import models as options_models
from models import  ServiceDetailsOption, ServiceDetails, Service
from rest_framework.decorators import *
import re


# Returns the selected service details options information
@api_view(['GET'])
def get_service_sla(request, search_type, version, sla_uuid):
    """
    Retrieves the service sla

    """

    response = {}

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result = prog.match(search_type)
    result_comp = prog.match(sla_uuid)

    if result_comp is None:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "An invalid service sla UUID was supplied"
        }
        return JsonResponse(response)


    if result is None:
        parsed_name = search_type.replace("_", " ")
        parsed_name.strip()
    else:
        uuid = search_type


    try:
        if result is None:
            serv = service_models.Service.objects.get(name=parsed_name)
        else:
            serv = service_models.Service.objects.get(id=uuid)


        serv_details = service_models.ServiceDetails.objects.get(id_service=serv.pk, version=version)

        sla = options_models.SLA.objects.get(id=sla_uuid)
        serv_det_options = options_models.ServiceDetailsOption.objects.get(service_id=serv.pk,
                                                                           service_details_id=serv_details.pk,
                                                                           service_options_id=sla.service_option_id.pk)

        response["status"] = "200 OK"
        response["data"] = sla.as_json(serv.pk, version)
        response["info"] = "service SLA information"

    except service_models.Service.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service was not found"
        }

    except service_models.ServiceDetails.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The specified service details do not exist"
        }

    except options_models.SLA.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested SLA object was not found"
        }

    except options_models.ServiceDetailsOption.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "This SLA object does not belong to the specified service and service details"
        }

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }


    return JsonResponse(response)

# Returns the selected service details options information
@api_view(['GET'])
def get_service_sla_parameter(request, search_type, version, sla_uuid, sla_param_uuid):
    """
    Retrieves the service sla parameter

    """
    response = {}

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result = prog.match(search_type)
    result_comp = prog.match(sla_uuid)

    if result_comp is None:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "An invalid service sla UUID was supplied"
        }
        return JsonResponse(response)

    result_comp = prog.match(sla_param_uuid)
    if result_comp is None:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "An invalid service sla parameter UUID was supplied"
        }
        return JsonResponse(response)

    if result is None:
        parsed_name = search_type.replace("_", " ")
        parsed_name.strip()
    else:
        uuid = search_type


    try:
        if result is None:
            serv = service_models.Service.objects.get(name=parsed_name)
        else:
            serv = service_models.Service.objects.get(id=uuid)


        serv_details = service_models.ServiceDetails.objects.get(id_service=serv.pk, version=version)

        sla = options_models.SLA.objects.get(id=sla_uuid)

        serv_det_options = options_models.ServiceDetailsOption.objects.get(service_id=serv.pk,
                                                                           service_details_id=serv_details.pk,
                                                                           service_options_id=sla.service_option_id.pk)

        sla_param = options_models.SLAParameter.objects.get(sla_id=sla.pk, service_option_id=serv_det_options.service_options_id,
                                                            parameter_id=sla_param_uuid)

        parameter = options_models.Parameter.objects.get(id=sla_param_uuid)


        response["status"] = "200 OK"
        response["data"] = parameter.as_short()
        response["info"] = "service SLA paramter information"

    except service_models.Service.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service was not found"
        }

    except service_models.ServiceDetails.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The specified service details do not exist"
        }

    except options_models.SLA.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested SLA object was not found"
        }

    except options_models.SLAParameter.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested SLA parameter does not belong to the specified service"
        }

    except options_models.ServiceDetailsOption.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "This SLA object does not belong to the specified service and service details"
        }

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }


    return JsonResponse(response)

# Returns the selected service details options information
@api_view(['GET'])
def get_service_options(request, search_type, version):
    """
    Retrieves the service options

    """
    params = request.GET.copy()

    response = {}

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result = prog.match(search_type)

    if result is None:
        parsed_name = search_type.replace("_", " ")
        parsed_name.strip()
    else:
        uuid = search_type

    try:
        if result is None:
            service = service_models.Service.objects.get(name=parsed_name)
        else:
            service = service_models.Service.objects.get(id=uuid)

        detail = service.get_service_details_by_version(version=str(version))
        options = ServiceDetailsOption.objects.filter(service_details_id=detail.id, service_id=detail.id_service.pk)

    except ServiceDetails.DoesNotExist:
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

    except Service.DoesNotExist:
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
    response["data"] ={"count": len(options), "services": [ option.as_json() for option in options ] }
 
    response["info"] = "options for service detail information"
    return JsonResponse(response)
