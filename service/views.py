from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from service import models
from component.models import ServiceComponent, ServiceDetailsComponent

# Returns JSON response containing all services
def list_services(request, type):

    serv_models = models.Service.objects.all()
    params = request.GET.copy()
    detail_level = params.get('view')

    response = {}
    services = []

    if type == "portfolio":
        if detail_level is None or detail_level == "short":
            services = [s.as_portfolio() for s in serv_models]
        elif detail_level == "complete":
            services = [merge_service_components(s.as_complete_portfolio()) for s in serv_models]
        else:
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "The query parameter is invalid"
            }
    elif type == "catalogue":
        services = [s.as_catalogue() for s in serv_models]
    else:
        response["status"] = "404 Not Found"

    if len(services) > 0:
        response["status"] = "200 OK"
        response["data"] = {
            "count": len(services),
            "services": services
        }
        response["info"] = "list of services"

    return JsonResponse(response)

# Renders the list service view
def show_service_list_view(request):
    return render(request, 'service/service_list.html')

def show_service_details(request, uuid):
    return render(request, 'service/service_portfolio_view.html', { "uuid": uuid })

# Returns all objects
def list_service_objects(request):

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

def get_service(request, uuid):
    type = request.get_full_path().split("/")[1]
    params = request.GET.copy()
    detail_level = params.get('view')

    response = {}
    service = None

    try:
        serv = models.Service.objects.get(id=uuid)
    except models.Service.DoesNotExist:
        serv = None
    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response["status"] = "404 Not Found"
            response["errors"] = {
                "detail": "An invalid UUID was supplied"
            }
        return JsonResponse(response)

    if serv is not None:
        if type == "portfolio":
            if detail_level is None or detail_level == "short":
                service = serv.as_portfolio()
            elif detail_level == "complete":
                service = merge_service_components(serv.as_complete_portfolio())
            else:
                response["status"] = "404 Not Found"
                response["errors"] = {
                    "detail": "The query parameter is invalid"
                }
        elif type == "catalogue":
            service = serv.as_catalogue()
        else:
            response["status"] = "404 Not Found"
    else:
        response["status"] = "404 Not Found"
        response["errors"] = {
            "detail": "The requested service was not found"
        }

    if service is not None:
        response["status"] = "200 OK"
        response["data"] = service,
        response["info"] = "service information"

    return JsonResponse(response)

def get_service_details(request, uuid):

   params = request.GET.copy()
   detail_level = params.get('view')

   detail = models.ServiceDetails.objects.get(id=uuid)


   if detail_level == 'short':
        return JsonResponse({'detail' : detail.as_short()})
   else:
        return JsonResponse({'detail' : detail.as_complete()})


def merge_service_components(response):

        serv_components = ServiceDetailsComponent.objects.filter(service_id=response['uuid'])

        components = []

        for s in serv_components:
            components.append(ServiceComponent.objects.get(id=s.service_component_id.pk).as_json())

        response["components"] = components

        return response


