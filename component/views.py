from django.http import JsonResponse
import re
from service import models as service_models
from component import models as component_models
from rest_framework.decorators import *
from common import helper, strings

# Create your views here.


# Returns the selected service components
@api_view(['GET'])
def get_service_components(request, search_type, version):
    """
    Retrieves the list of components for the selected service.

    """

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(search_type)

    service, parsed_name, uuid = None, None, None

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
        service_details_comp = component_models.ServiceDetailsComponent.objects.filter(service_id=service.pk,
                                                                                service_details_id=service_details.pk)
        service_components_implementation_detail = []
        for sdc in service_details_comp:
            service_components_implementation_detail.append(component_models.ServiceComponentImplementationDetail.objects.get(id=sdc.service_component_implementation_detail_id.pk))

        service_components = []
        seen = set()

        for sc in service_components_implementation_detail:
            if sc.component_id.pk in seen:
                continue
            service_components.append(sc.component_id.as_short(service.pk, version))
            seen.add(sc.component_id.pk)

        data = helper.build_list_object("service_components", service_components)
        response = helper.get_response_info(strings.SERVICE_COMPONENTS_INFORMATION, data)

    except service_models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    except service_models.ServiceDetails.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

    return JsonResponse(response)


# Returns the selected service component
@api_view(['GET'])
def get_service_component(request, search_type, version, comp_uuid):
    """
    Retrieves the specified component for the selected service.

    """

    response = {}

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result = prog.match(search_type)
    result_comp = prog.match(comp_uuid)

    if result_comp is None:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "An invalid service component UUID was supplied"
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
        serv_comp_impl_det = component_models.ServiceComponentImplementationDetail.objects.filter(component_id=comp_uuid)

        exists = False

        for s in serv_comp_impl_det:
            serv_det_comp = component_models.ServiceDetailsComponent.objects.filter(service_id=serv.pk,
                                                        service_details_id=serv_details.pk,
                                                            service_component_implementation_detail_id=s.pk).count()

            if serv_det_comp > 0:
                exists = True
                break

        if not exists:
            raise component_models.ServiceDetailsComponent.DoesNotExist

        # if len(serv_det_comp) <= 0:
        #     raise component_models.ServiceDetailsComponent.DoesNotExist

        service_component = component_models.ServiceComponent.objects.get(id=comp_uuid)

        response["status"] = "200 OK"
        response["data"] = service_component.as_json()
        response["info"] = "service component information"

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

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }

    except component_models.ServiceComponent.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service component was not found"
        }

    except component_models.ServiceDetailsComponent.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "A service component matching the specified service version does not exists"
        }

    # except:
    #     response["status"] = "404 Not Found"
    #     response["errors"] = {
    #         "detail": "The requested service was not found"
    #     }


    return JsonResponse(response)

# Returns the selected service component implementations
@api_view(['GET'])
def get_service_component_implementations(request, search_type, version, comp_uuid):
    """
    Retrieves the list of component implementations for the selected service component.

    """

    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(search_type)
    result_comp = prog.match(comp_uuid)

    if result_comp is None:
        response = helper.get_error_response(strings.SERVICE_COMPONENT_INVALID_UUID)
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
        service_comp_impl_det = component_models.ServiceComponentImplementationDetail.objects.filter(component_id=comp_uuid)

        exists = False
        scids = []

        for s in service_comp_impl_det:
            serv_det_comp = component_models.ServiceDetailsComponent.objects.filter(service_id=service.pk,
                                                        service_details_id=service_details.pk,
                                                            service_component_implementation_detail_id=s.pk).count()

            if serv_det_comp > 0:
                exists = True
                scids.append(s)

        if not exists:
            raise component_models.ServiceDetailsComponent.DoesNotExist


        service_component_impl = [component_models.ServiceComponentImplementation.objects.get(id=s.component_implementation_id.pk) for s in scids]
        service_comp_impl_list = [sci.as_short(service.pk, version) for sci in service_component_impl]
        data = helper.build_list_object("service_component_implementations", service_comp_impl_list)
        response = helper.get_response_info(strings.SERVICE_COMPONENT_IMPLEMENTATIONS_INFORMATION, data)

    except service_models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except service_models.ServiceDetails.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

    except component_models.ServiceComponentImplementation.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_COMPONENT_NO_IMPLEMENTATIONS)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    except component_models.ServiceComponentImplementationDetail.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_NOT_FOUND)

    except component_models.ServiceComponent.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_COMPONENT_NOT_FOUND)

    except component_models.ServiceDetailsComponent.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_COMPONENTS_IMPLEMENTATION_NONMATCHING_UUID)

    return JsonResponse(response)

# Returns the selected service component implementation details
@api_view(['GET'])
def get_service_component_implementation_detail(request, search_type, version, comp_uuid, imp_uuid):
    """
    Retrieves the list of component implementation details for the selected service component implementation.

    """

    service, parsed_name, uuid = None, None, None

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(search_type)
    result_comp = prog.match(comp_uuid)

    if result_comp is None:
        response = helper.get_error_response(strings.SERVICE_COMPONENT_INVALID_UUID)
        return JsonResponse(response)

    result_comp = prog.match(imp_uuid)
    if result_comp is None:
        response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_INVALID_UUID)
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
        service_component_impl_detail = component_models.ServiceComponentImplementationDetail\
            .objects.filter(component_id=comp_uuid, component_implementation_id=imp_uuid)

        exists = False
        scids = []

        for s in service_component_impl_detail:
            serv_det_comp = component_models.ServiceDetailsComponent.objects.filter(service_id=service.pk,
                                                        service_details_id=service_details.pk,
                                                            service_component_implementation_detail_id=s.pk).count()

            if serv_det_comp > 0:
                exists = True
                scids.append(s)

        if not exists:
            raise component_models.ServiceDetailsComponent.DoesNotExist

        service_component_impl_detail_list = [scid.as_json() for scid in scids]
        data = helper.build_list_object("service_component_implementation_details", service_component_impl_detail_list)
        response = helper.get_response_info(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS, data)

    except service_models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except service_models.ServiceDetails.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

    except component_models.ServiceComponentImplementation.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_COMPONENT_NO_IMPLEMENTATIONS)

    except component_models.ServiceComponentImplementationDetail.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    except component_models.ServiceComponent.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_COMPONENT_NOT_FOUND)

    except component_models.ServiceDetailsComponent.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_COMPONENTS_IMPLEMENTATION_NONMATCHING_UUID)

    return JsonResponse(response)
