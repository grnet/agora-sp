from collections import defaultdict

import sys
from django.http import JsonResponse, HttpResponse
import re
from service import models as service_models
from component import models as component_models
from rest_framework.decorators import *
from common import helper, strings
from django.db import IntegrityError
from django.shortcuts import render
from common.decorators import check_service_ownership_or_superuser
# Create your views here.


# Returns the selected service components
# @check_service_ownership_or_superuser
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

    return JsonResponse(response, status=int(response["status"][:3]))

# Get all service components with the details
@api_view(['GET'])
def get_service_components_complete(request, search_type ):
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

        service_details_list = service_models.ServiceDetails.objects.filter(id_service=service.pk)
        service_components_dict = defaultdict(list)

        for service_details in service_details_list:

            service_details_comp = component_models.ServiceDetailsComponent.objects\
                .filter(service_id=service.pk, service_details_id=service_details.pk)

            service_components_dict[service_details.version].append(service_details_comp)

        service_components_implementation_detail = defaultdict(list)

        for version in service_components_dict:
            # print >>sys.stderr, service_components_dict[version]


            for component_list in service_components_dict[version]:
                for service_details_component in component_list:
                    # print >>sys.stderr, service_details_component

                    service_components_implementation_detail[version].append(component_models.ServiceComponentImplementationDetail.
                                                                objects.get(id=service_details_component.
                                                                            service_component_implementation_detail_id.pk))

        # print >>sys.stderr, service_components_implementation_detail

        service_components = []

        seen = set()

        for version in service_components_implementation_detail:

            print >>sys.stderr, service_components_implementation_detail[version]

            for concrete_implementation in service_components_implementation_detail[version]:

                # if concrete_implementation.component_id.pk in seen:
                #     continue

                service_components.append(concrete_implementation.component_id.as_view_compatible(version))

                # seen.add(concrete_implementation.component_id.pk)

        data = helper.build_list_object("service_components", service_components)
        response = helper.get_response_info(strings.SERVICE_COMPONENTS_INFORMATION, data)


    except service_models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    except service_models.ServiceDetails.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

    # print >>sys.stderr,  service_components_dict

    return JsonResponse(response, status=int(response["status"][:3]))





# Updates the provided service component
@api_view(['POST'])
def edit_service_component(request):
    """

    Updates an existing service component with the provided data.

    :param uuid: service component UUID
    :param name: service component name
    :param description: service component description
    :return: the updated service component
    """

    return insert_service_component(request)

# Inserts the provided service component
@api_view(['POST'])
def insert_service_component(request):
    """

    Inserts the provided service component.

    :param uuid: service component UUID
    :param name: service component name
    :param description: service component description
    :return: the inserted service component
    """

    op_type = helper.get_last_url_part(request)
    params = helper.get_request_data(request)
    uuid, name, service_component = None, None, None

    if "name" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "name" in params:
        name = params.get('name')
        if name is None or len(name) == 0:
            return JsonResponse(helper.get_error_response(strings.
                                                          SERVICE_COMPONENT_NAME_EMPTY, status=strings.REJECTED_406),
                                status=406)
    elif op_type == "edit":
        name = None

    # if "description" not in comp:
    #     return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_DESCRIPTION_NOT_PROVIDED,
    #                                                   status=strings.REJECTED_406))


    if "uuid" in params:
        uuid = params.get("uuid")

        prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service_component = component_models.ServiceComponent.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_UUID_EXISTS,
                                                              status=strings.CONFLICT_409), status=409)
        except component_models.ServiceComponent.DoesNotExist:
            service_component = component_models.ServiceComponent()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404), status=404)
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif op_type == "add":
        service_component = component_models.ServiceComponent()

    if name is not None:
        service_component.name = name
    if "description" in params:
        service_component.description = params.get('description')
    if uuid is not None:
        service_component.id = uuid

    try:
        service_component.save()
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_NAME_EXISTS,
                                                      status=strings.REJECTED_406), status=406)

    data = service_component.as_json()
    msg = strings.SERVICE_COMPONENT_INSERTED if op_type == "add" else strings.SERVICE_COMPONENT_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)
    return JsonResponse(response, status=int(response["status"][:3]))


def get_service_component_single(request, comp_uuid):
    response = {}

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result_comp = prog.match(comp_uuid)

    if result_comp is None:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "An invalid service component UUID was supplied"
        }
        return JsonResponse(response, status=int(response["status"][:3]))

    try:
        service_component = component_models.ServiceComponent.objects.get(id=comp_uuid)

        response["status"] = "200 OK"
        response["data"] = service_component.as_json()
        response["info"] = "service component information"

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

    return JsonResponse(response, status=int(response["status"][:3]))

def get_service_component_implementation(request, comp_imp_uuid):
    response = {}

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result_comp = prog.match(comp_imp_uuid)

    if result_comp is None:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "An invalid service component implementation UUID was supplied"
        }
        return JsonResponse(response, status=int(response["status"][:3]))

    try:
        service_component_imp = component_models.ServiceComponentImplementation.objects.get(id=comp_imp_uuid)

        response["status"] = "200 OK"
        response["data"] = service_component_imp.as_json_up()
        response["info"] = "service component implementation information"

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }

    except component_models.ServiceComponent.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service component implementation was not found"
        }

    return JsonResponse(response, status=int(response["status"][:3]))

def get_service_component_implementation_all(request):
    response = {}

    service_component_imp = component_models.ServiceComponentImplementation.objects.all()
    response["status"] = "200 OK"
    response["data"] = [s.as_json_up() for s in service_component_imp]
    response["info"] = "service component implementation information"

    return JsonResponse(response, status=int(response["status"][:3]))

def get_service_component_implementation_details(request, comp_imp_det_uuid):
    response = {}

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

    result_comp = prog.match(comp_imp_det_uuid)

    if result_comp is None:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "An invalid service component implementation details UUID was supplied"
        }
        return JsonResponse(response, status=int(response["status"][:3]))

    try:
        service_component_imp_det = component_models.ServiceComponentImplementationDetail.objects.get(id=comp_imp_det_uuid)

        response["status"] = "200 OK"
        response["data"] = service_component_imp_det.as_json()
        response["info"] = "service component implementation details information"

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }

    except component_models.ServiceComponent.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service component implementation details was not found"
        }

    return JsonResponse(response, status=int(response["status"][:3]))

# Returns the selected service component
# @check_service_ownership_or_superuser
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
        return JsonResponse(response, status=int(response["status"][:3]))

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

    return JsonResponse(response, status=int(response["status"][:3]))


def service_component_write_ui(request):
    return render(request, 'service/write.html', {"type": "service_component"})

def service_component_edit_ui(request, comp_uuid):
    source = helper.current_site_url() + "/v1/component/" + comp_uuid
    return render(request, 'service/write.html', {"type": "service_component", "source": source})

def service_component_table(request):
    source = helper.current_site_url() + "/v1/component/all"
    return render(request, 'service/write.html', {"type": "service_component_table", "source": source})

def service_component_implementation_write_ui(request):
    return render(request, 'service/write.html', {"type": "service_component_implementation"})

def service_component_implementation_edit_ui(request, comp_imp_uuid):
    source = helper.current_site_url() + "/v1/component/implementation/" + comp_imp_uuid
    return render(request, 'service/write.html', {"type": "service_component_implementation", "source": source})


def service_component_implementation_detail_write_ui(request):
    return render(request, 'service/write.html', {"type": "service_component_implementation_detail"})

def service_component_implementation_detail_edit_ui(request, comp_imp_det_uuid):
    source = helper.current_site_url() + "/v1/component/implementation_detail/" + comp_imp_det_uuid
    return render(request, 'service/write.html', {"type": "service_component_implementation_detail", "source": source})


# Updates the provided service component implementation
@api_view(['POST'])
def edit_service_component_implementation(request):
    """

    :param component_uuid: UUID of the related service component
    :param uuid: service component implementation UUID
    :param name: service component implementation name
    :param description: service component implementation description
    :return: the updated service component implementation
    """

    return insert_service_component_implementation(request)

# Inserts the provided service component implementation
@api_view(['POST'])
def insert_service_component_implementation(request):
    """

    Inserts the provided service component implementation.

    :param component_uuid: UUID of the related service component
    :param uuid: service component implementation UUID
    :param name: service component implementation name
    :param description: service component implementation description
    :return: the inserted service component implementation
    """

    op_type = helper.get_last_url_part(request)
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")
    uuid, name, service_component_implementation, service_component = None, None, None, None

    if "component_uuid" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "component_uuid" in params:

        comp_uuid = params.get("component_uuid")

        result = prog.match(comp_uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service_component = component_models.ServiceComponent.objects.get(id=comp_uuid)
        except component_models.ServiceComponent.DoesNotExist:
            return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_NOT_FOUND), status=404)

    elif op_type == "edit":
        service_component = None


    if "name" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "name" in params:
        name = params.get('name')
        if name is None or len(name) == 0:
            return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_NAME_EMPTY,
                                                          status=strings.REJECTED_406), status=406)
    elif op_type == "edit":
        name = None

    # if "description" not in params:
    #     return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DESCRIPTION_NOT_PROVIDED,
    #                                                   status=strings.REJECTED_406))

    if "uuid" in params:
        uuid = params.get("uuid")

        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service_component_implementation = component_models.ServiceComponentImplementation.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_UUID_EXISTS,
                                                              status=strings.CONFLICT_409), status=409)
        except component_models.ServiceComponentImplementation.DoesNotExist:
            service_component_implementation = component_models.ServiceComponentImplementation()
            if op_type == "edit":
                return JsonResponse(helper.
                                    get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_NOT_FOUND,
                                                       status=strings.NOT_FOUND_404), status=404)
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif op_type == "add":
        service_component_implementation = component_models.ServiceComponentImplementation()



    if name is not None:
        service_component_implementation.name = name
    if "description" in params:
        service_component_implementation.description = params.get('description')
    if service_component is not None:
        service_component_implementation.component_id = service_component
    if uuid is not None:
        service_component_implementation.id = uuid

    try:
        service_component_implementation.save()
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_NAME_EXISTS,
                                                      status=strings.REJECTED_406), status=406)

    data = service_component_implementation.as_json()
    msg = strings.SERVICE_COMPONENT_IMPLEMENTATION_INSERTED if op_type == "add" else \
        strings.SERVICE_COMPONENT_IMPLEMENTATION_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)
    return JsonResponse(response, status=int(response["status"][:3]))


# Returns the selected service component implementations
@api_view(['GET'])
# @check_service_ownership_or_superuser
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

    return JsonResponse(response, status=int(response["status"][:3]))

# Updates the provided service component implementation details
@api_view(['POST'])
def edit_service_component_implementation_details(request):
    """

    Updates the provided service component implementation details

    :param uuid: service component implementation details UUID
    :param component_uuid: the related service component UUID
    :param component_implementation_uuid: the related service component implementation UUID
    :param version: service component implementation details version
    :param configuration_parameters: service component implementation details configuration parameters
    :return: the updated service component implementation details
    """

    return insert_service_component_implementation_details(request)

# Inserts the provided service component implementation details
@api_view(['POST'])
def insert_service_component_implementation_details(request):
    """

    Inserts the provided service component implementation details.

    :param uuid: service component implementation details UUID
    :param component_uuid: the related service component UUID
    :param component_implementation_uuid: the related service component implementation UUID
    :param version: service component implementation details version
    :param configuration_parameters: service component implementation details configuration parameters
    :return: the inserted service component implementation details
    """

    op_type = helper.get_last_url_part(request)
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")
    uuid, version, service_component_implementation_details, service_component, service_component_implementation = \
        None, None, None, None, None

    if "component_uuid" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "component_uuid" in params:

        comp_uuid = params.get("component_uuid")

        result = prog.match(comp_uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service_component = component_models.ServiceComponent.objects.get(id=comp_uuid)
        except component_models.ServiceComponent.DoesNotExist:
            return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_NOT_FOUND), status=404)

    elif op_type == "edit":
        service_component = None


    if "component_implementation_uuid" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "component_implementation_uuid" in params:


        imp_uuid = params.get("component_implementation_uuid")

        result = prog.match(imp_uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service_component_implementation = component_models.ServiceComponentImplementation.objects.get(id=imp_uuid)
        except component_models.ServiceComponentImplementation.DoesNotExist:
            return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_NOT_FOUND), status=404)

    elif op_type == "edit":
        service_component_implementation = None


    if "version" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_VERSION_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "version" in params:
        version = params.get('version')
        if version is None or len(version) == 0:
            return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_VERSION_EMPTY,
                                                          status=strings.REJECTED_406), status=406)
    elif op_type == "edit":
        version = None

    # if "configuration_parameters" not in comp:
    #     return JsonResponse(helper.get_error_response(
    #         strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_CONFIGURATION_PARAMETERS_NOT_PROVIDED,
    #                                                   status=strings.REJECTED_406))

    if "uuid" in params:
        uuid = params.get("uuid")

        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service_component_implementation_details = component_models.ServiceComponentImplementationDetail.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_EXISTS,
                                                              status=strings.CONFLICT_409), status=409)
        except component_models.ServiceComponentImplementationDetail.DoesNotExist:
            service_component_implementation_details = component_models.ServiceComponentImplementationDetail()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404), status=404)
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif op_type == "add":
        service_component_implementation_details = component_models.ServiceComponentImplementationDetail()



    if version is not None:
        service_component_implementation_details.version = version

    if "configuration_parameters" in params:
        service_component_implementation_details.configuration_parameters = params.get('configuration_parameters')

    if service_component is not None:
        service_component_implementation_details.component_id = service_component
    if service_component_implementation is not None:
        service_component_implementation_details.component_implementation_id = service_component_implementation

    if uuid is not None:
        service_component_implementation_details.id = uuid

    try:
        service_component_implementation_details.save()
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_NAME_EXISTS,
                                                      status=strings.REJECTED_406), status=406)

    data = service_component_implementation_details.as_json()
    msg = strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_INSERTED if op_type == "add" else \
        strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)
    return JsonResponse(response, status=int(response["status"][:3]))

# Returns the selected service component implementation details
# @check_service_ownership_or_superuser
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
        return JsonResponse(response, status=int(response["status"][:3]))

    result_comp = prog.match(imp_uuid)
    if result_comp is None:
        response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_INVALID_UUID)
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

    return JsonResponse(response, status=int(response["status"][:3]))

# Updates the provided service component implementation details and service details relationship
@api_view(['POST'])
def edit_service_details_component_implementation_details(request):
    """

    Updates the provided service component implementation details and service details relationship

    :param service_id: the service UUID
    :param new_service_id: the new service UUID
    :param service_version: the service details version
    :param new_service_version: the new service details version
    :param component_implementation_details_uuid: the service component implementation details UUID
    :param new_component_implementation_details_uuid: the new service component implementation details UUID
    :return: the updated service details component
    """

    comp = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")
    uuid, parsed_name, new_uuid, new_parsed_name = None, None, None, None

    if "component_implementation_details_uuid" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    comp_imp_det_uuid = comp.get('component_implementation_details_uuid')
    result = prog.match(comp_imp_det_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    if "new_component_implementation_details_uuid" not in comp:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    new_comp_imp_det_uuid = comp.get('new_component_implementation_details_uuid')
    result = prog.match(new_comp_imp_det_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    if "service_id" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_NOT_PROVIDED, status=strings.REJECTED_406),
                            status=406)

    if "service_version" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_VERSION_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    if "new_service_id" not in comp:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_UUID_NOT_PROVIDED, status=strings.REJECTED_406),
                            status=406)

    if "new_service_version" not in comp:
        return JsonResponse(helper.get_error_response(strings.NEW_SERVICE_DETAILS_VERSION_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    search_type = comp.get('service_id')
    version = comp.get('service_version')
    new_search_type = comp.get('new_service_id')
    new_version = comp.get('new_service_version')

    result = prog.match(search_type)

    if result is None:
        parsed_name = search_type.replace("_", " ").strip()
    else:
        uuid = search_type

    new_result = prog.match(new_search_type)

    if new_result is None:
        new_parsed_name = new_search_type.replace("_", " ").strip()
    else:
        new_uuid = new_search_type

    try:
        if result is None:
            service = service_models.Service.objects.get(name=parsed_name)
        else:
            service = service_models.Service.objects.get(id=uuid)

        if new_result is None:
            new_service = service_models.Service.objects.get(name=new_parsed_name)
        else:
            new_service = service_models.Service.objects.get(id=new_uuid)

        service_details = service_models.ServiceDetails.objects.get(id_service=service.pk, version=version)

        get_service_component_implementation_detail = component_models.ServiceComponentImplementationDetail.objects\
                                                                        .get(id=comp_imp_det_uuid)

        new_service_details = service_models.ServiceDetails.objects.get(id_service=new_service.pk, version=new_version)

        new_get_service_component_implementation_detail = component_models.ServiceComponentImplementationDetail.objects\
                                                                        .get(id=new_comp_imp_det_uuid)


        obj = component_models.ServiceDetailsComponent.objects.get(service_id=service,
                            service_details_id=service_details,
                            service_component_implementation_detail_id=get_service_component_implementation_detail)


        obj.service_id = new_service
        obj.service_details_id = new_service_details
        obj.service_component_implementation_detail_id = new_get_service_component_implementation_detail
        obj.save()
        data = obj.as_json()
        response = helper.get_response_info(strings.SERVICE_DETAILS_COMPONENT_UPDATED, data,
                                            status=strings.UPDATED_202)

    except service_models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except service_models.ServiceDetails.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

    except component_models.ServiceComponentImplementationDetail.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_NOT_FOUND)
    except component_models.ServiceDetailsComponent.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_DETAILS_COMPONENT_NOT_FOUND)
    except IntegrityError:
        response = helper.get_error_response(strings.SERVICE_DETAILS_COMPONENT_EXISTS, status=strings.REJECTED_406)

    return JsonResponse(response, status=int(response["status"][:3]))

# Inserts the provided service component implementation details and service details relationship
@api_view(['POST'])
def insert_service_details_component_implementation_details(request):
    """

    Inserts the provided service component implementation details and service details relationship

    :param service_id: the service UUID
    :param service_version: the service details version
    :param component_implementation_details_uuid: the service component implementation details UUID
    :return: the inserted service details component
    """

    comp = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")
    uuid, parsed_name = None, None

    if "component_implementation_details_uuid" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

    comp_imp_det_uuid = comp.get('component_implementation_details_uuid')
    result = prog.match(comp_imp_det_uuid)

    if result is None:
        return JsonResponse(helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_INVALID_UUID,
                                                      status=strings.REJECTED_406), status=406)

    if "service_id" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_UUID_NOT_PROVIDED, status=strings.REJECTED_406),
                            status=406)

    if "service_version" not in comp:
        return JsonResponse(helper.get_error_response(strings.SERVICE_DETAILS_VERSION_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)

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
            response = helper.get_error_response(strings.SERVICE_DETAILS_COMPONENT_EXISTS, status=strings.REJECTED_406)
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

    return JsonResponse(response, status=int(response["status"][:3]))