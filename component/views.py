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

    :param search_type: service name or UUID
    :param version: service version
    :return: list of components
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
        service_details_comp = component_models.ServiceDetailsComponent.objects\
            .filter(service_id=service.pk, service_details_id=service_details.pk)
        service_components_implementation_detail = []
        for sdc in service_details_comp:
            service_components_implementation_detail.append(component_models.ServiceComponentImplementationDetail.
                                                            objects.get(id=sdc.
                                                                        service_component_implementation_detail_id.pk))

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


# Inserts the provided service component
@api_view(['POST'])
def insert_service_component(request):
    """

    Inserts the provided service component.

    :return: response message and service component URL
    """

    op_type = helper.get_last_url_part(request)
    comp = request.POST.copy()

    uuid = None

    if "name" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))
    if "description" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_DESCRIPTION_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    name = comp.get('name')
    description = comp.get('description')

    if name is None or len(name) == 0:
        return JsonResponse(helper.get_error_response(strings.
                                                      SERVICE_COMPONENT_NAME_EMPTY, status=strings.REJECTED_405))

    if "uuid" in comp:
        uuid = comp.get("uuid")

        prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_INVALID_UUID,
                                                          status=strings.REJECTED_405))

        try:
            component_models.ServiceComponent.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_UUID_EXISTS,
                                                              status=strings.CONFLICT_409))
        except component_models.ServiceComponent.DoesNotExist:
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404))
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    service_component = component_models.ServiceComponent()
    service_component.name = name
    service_component.description = description
    if uuid is not None:
        service_component.id = uuid
    service_component.save()

    data = service_component.as_json()
    msg = strings.SERVICE_COMPONENT_INSERTED if op_type == "add" else strings.SERVICE_COMPONENT_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)
    return JsonResponse(response)


# Returns the selected service component
@api_view(['GET'])
def get_service_component(request, search_type, version, comp_uuid):
    """

    Retrieves the specified component for the selected service.

    :param request:
    :param search_type:
    :param version:
    :param comp_uuid:
    :return:
    """

    response = {}

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result = prog.match(search_type)
    result_comp = prog.match(comp_uuid)
    parsed_name, uuid = None, None

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
            serv_det_comp = component_models.ServiceDetailsComponent.\
                objects.filter(service_id=serv.pk, service_details_id=serv_details.pk,
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


# Inserts the provided service component implementation
@api_view(['POST'])
def insert_service_component_implementation(request):
    """

    Inserts the provided service component implementation.

    :return: response message and service component implementation URL
    """

    op_type = helper.get_last_url_part(request)
    comp = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    uuid = None

    if "component_uuid" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    comp_uuid = comp.get("component_uuid")

    result = prog.match(comp_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_INVALID_UUID,
                                                      status=strings.REJECTED_405))

    if "name" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))
    if "description" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DESCRIPTION_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    name = comp.get('name')
    description = comp.get('description')

    if name is None or len(name) == 0:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_NAME_EMPTY,
                                                      status=strings.REJECTED_405))

    if "uuid" in comp:
        uuid = comp.get("uuid")

        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_INVALID_UUID,
                                                          status=strings.REJECTED_405))

        try:
            component_models.ServiceComponentImplementation.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_UUID_EXISTS,
                                                              status=strings.CONFLICT_409))
        except component_models.ServiceComponentImplementation.DoesNotExist:
            if op_type == "edit":
                return JsonResponse(helper.
                                    get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_NOT_FOUND,
                                                       status=strings.NOT_FOUND_404))
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    try:
        service_component = component_models.ServiceComponent.objects.get(id=comp_uuid)
    except component_models.ServiceComponent.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_NOT_FOUND))

    service_component_implementation = component_models.ServiceComponentImplementation()
    service_component_implementation.name = name
    service_component_implementation.description = description
    service_component_implementation.component_id = service_component
    if uuid is not None:
        service_component_implementation.id = uuid
    service_component_implementation.save()

    data = service_component_implementation.as_json()
    msg = strings.SERVICE_COMPONENT_IMPLEMENTATION_INSERTED if op_type == "add" else \
        strings.SERVICE_COMPONENT_IMPLEMENTATION_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)
    return JsonResponse(response)


# Returns the selected service component implementations
@api_view(['GET'])
def get_service_component_implementations(request, search_type, version, comp_uuid):
    """

    Retrieves the list of component implementations for the selected service component.

    :param search_type: service name or UUID
    :param version: service version
    :param comp_uuid: service component UUID
    :return: list of service component implementations
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
        service_comp_impl_det = component_models.ServiceComponentImplementationDetail.\
            objects.filter(component_id=comp_uuid)

        exists = False
        scids = []

        for s in service_comp_impl_det:
            serv_det_comp = component_models.ServiceDetailsComponent.objects.\
                filter(service_id=service.pk, service_details_id=service_details.pk,
                       service_component_implementation_detail_id=s.pk).count()

            if serv_det_comp > 0:
                exists = True
                scids.append(s)

        if not exists:
            raise component_models.ServiceDetailsComponent.DoesNotExist

        service_component_impl = [component_models.ServiceComponentImplementation.
                                      objects.get(id=s.component_implementation_id.pk) for s in scids]
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


# Inserts the provided service component implementation details
@api_view(['POST'])
def insert_service_component_implementation_details(request):
    """

    Inserts the provided service component implementation details.

    :return: response message and service component implementation details URL
    """

    op_type = helper.get_last_url_part(request)
    comp = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    uuid = None

    if "component_uuid" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    comp_uuid = comp.get("component_uuid")

    result = prog.match(comp_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_INVALID_UUID,
                                                      status=strings.REJECTED_405))

    if "component_implementation_uuid" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    imp_uuid = comp.get("component_implementation_uuid")

    result = prog.match(imp_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_INVALID_UUID,
                                                      status=strings.REJECTED_405))

    if "version" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_VERSION_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))
    if "configuration_parameters" not in comp:
        return JsonResponse(helper.get_error_response(
            strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_CONFIGURATION_PARAMETERS_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    version = comp.get('version')
    configuration_parameters = comp.get('configuration_parameters')

    if version is None or len(version) == 0:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_VERSION_EMPTY,
                                                      status=strings.REJECTED_405))

    if "uuid" in comp:
        uuid = comp.get("uuid")

        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_INVALID_UUID,
                                                          status=strings.REJECTED_405))

        try:
            component_models.ServiceComponentImplementationDetail.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_EXISTS,
                                                              status=strings.CONFLICT_409))
        except component_models.ServiceComponentImplementationDetail.DoesNotExist:
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404))
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    try:
        service_component = component_models.ServiceComponent.objects.get(id=comp_uuid)
        service_component_implementation = component_models.ServiceComponentImplementation.objects.get(id=imp_uuid)
    except component_models.ServiceComponent.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_NOT_FOUND))
    except component_models.ServiceComponentImplementation.DoesNotExist:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_NOT_FOUND))

    service_component_implementation_details = component_models.ServiceComponentImplementationDetail()
    service_component_implementation_details.version = version
    service_component_implementation_details.configuration_parameters = configuration_parameters
    service_component_implementation_details.component_id = service_component
    service_component_implementation_details.component_implementation_id = service_component_implementation
    if uuid is not None:
        service_component_implementation_details.id = uuid
    service_component_implementation_details.save()

    data = service_component_implementation_details.as_json()
    msg = strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_INSERTED if op_type == "add" else \
        strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)
    return JsonResponse(response)

# Returns the selected service component implementation details
@api_view(['GET'])
def get_service_component_implementation_detail(request, search_type, version, comp_uuid, imp_uuid):
    """

    Retrieves the list of component implementation details for the selected service component implementation.

    :param search_type: service name or UUID
    :param version: service version
    :param comp_uuid: service component UUID
    :param imp_uuid: service component implementation UUID
    :return: list of service component implementation details
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
            serv_det_comp = component_models.ServiceDetailsComponent.\
                objects.filter(service_id=service.pk, service_details_id=service_details.pk,
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

# Inserts the provided service component implementation details and service details relationship
@api_view(['POST'])
def insert_service_details_component_implementation_details(request):
    """

    Inserts the provided service component implementation details and service details relationship

    :return: response message
    """

    comp = request.POST.copy()
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    uuid, parsed_name = None, None

    if "component_implementation_details_uuid" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_NOT_PROVIDED,
                            status=strings.REJECTED_405))

    comp_imp_det_uuid = comp.get('component_implementation_details_uuid')
    result = prog.match(comp_imp_det_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_INVALID_UUID,
                            status=strings.REJECTED_405))

    if "service_id" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_NOT_PROVIDED, status=strings.REJECTED_405))

    if "service_version" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_VERSION_NOT_PROVIDED,
                                                      status=strings.REJECTED_405))

    search_type = comp.get('service_id')
    version = comp.get('service_version')

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

        service_details = service_models.ServiceDetails.objects.get(id_service=service.pk, version=version)

        get_service_component_implementation_detail = component_models.ServiceComponentImplementationDetail.objects\
                                                                        .get(id=comp_imp_det_uuid)


        obj, created = component_models.ServiceDetailsComponent.objects.get_or_create(service_id=service,
                            service_details_id=service_details,
                            service_component_implementation_detail_id=get_service_component_implementation_detail)

        if not created:
            response = helper.get_error_response(strings.SERVICE_DETAILS_COMPONENT_EXISTS, status=strings.REJECTED_405)
        else:
            data = obj.as_json()
            response = helper.get_response_info(strings.SERVICE_DETAILS_COMPONENT_INSERTED, data,
                                                status=strings.CREATED_201)

    except service_models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except service_models.ServiceDetails.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

    except component_models.ServiceComponentImplementationDetail.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_NOT_FOUND)

    return JsonResponse(response)