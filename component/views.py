from django.http import JsonResponse
import re
from service import models as service_models
from component import models as component_models
from rest_framework.decorators import *
# Create your views here.

# Returns the selected service components
@api_view(['GET'])
def get_service_components(request, search_type, version):
    """
    Retrieves the list of components for the selected service.

    """

    # type = request.get_full_path().split("/")[2]
    # params = request.GET.copy()
    # detail_level = params.get('view')
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
            serv = service_models.Service.objects.get(name=parsed_name)
        else:
            serv = service_models.Service.objects.get(id=uuid)

        serv_details = service_models.ServiceDetails.objects.get(id_service=serv.pk, version=version)
        serv_det_comp = component_models.ServiceDetailsComponent.objects.filter(service_id=serv.pk, service_details_id=serv_details.pk)
        service_components_implementation_detail = []
        for sdc in serv_det_comp:
            service_components_implementation_detail.extend(component_models.ServiceComponentImplementationDetail.objects.filter(id=sdc.service_component_implementation_detail_id.pk))

        response["status"] = "200 OK"
        response["data"] = [sc.component_id.as_json() for sc in service_components_implementation_detail]
        response["info"] = "service components information"

    except service_models.Service.DoesNotExist:
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

    except service_models.ServiceDetails.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service details were not found"
        }


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

        

        service_component_impl = component_models.ServiceComponentImplementation.objects.filter(component_id=comp_uuid)

        response["status"] = "200 OK"
        response["data"] = [sci.as_json() for sci in service_component_impl]
        response["info"] = "service component implementation information"

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

    except component_models.ServiceComponentImplementation.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "There are no implementations for the specified service component"
        }

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }

    except component_models.ServiceComponentImplementationDetail.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "There requested service component for this service was not found"
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

    return JsonResponse(response)

# Returns the selected service component implementation details
@api_view(['GET'])
def get_service_component_implementation_detail(request, search_type, version, comp_uuid, imp_uuid):
    """
    Retrieves the list of component implementation details for the selected service component implementation.

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

    result_comp = prog.match(imp_uuid)
    if result_comp is None:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "An invalid service component implementation UUID was supplied"
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
        # serv_comp_impl_det = component_models.ServiceComponentImplementationDetail.objects.get(component_id=comp_uuid,
        #                                                                                        component_implementation_id=imp_uuid)
        # serv_det_comp = component_models.ServiceDetailsComponent.objects.get(service_id=serv.pk,
        #                                                                      service_details_id=serv_details.pk,
        #                                                                      service_component_id=serv_comp_impl_det.pk)
        #
        # service_component = component_models.ServiceComponent.objects.get(id=comp_uuid)


        # service_component_impl = component_models.ServiceComponentImplementation.objects.filter(component_id=comp_uuid)
        service_component_impl_detail = component_models.ServiceComponentImplementationDetail\
            .objects.filter(component_id=comp_uuid, component_implementation_id=imp_uuid)

        response["status"] = "200 OK"
        response["data"] = [scid.as_json() for scid in service_component_impl_detail]
        response["info"] = "service component implementation detail"

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

    except component_models.ServiceComponentImplementation.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "There are no implementations of the specified service component"
        }

    except component_models.ServiceComponentImplementationDetail.DoesNotExist:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service component implementation details do not exist"
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
