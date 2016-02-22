from django.http import JsonResponse
# Create your views here.



def list_services(request, type):


    if type is "portfolio":
      return JsonResponse({"Portfolio":str(request)})
    else:
      return JsonResponse({str(type):str(request)})


def get_service(request, uuid):

    if request is not None:
      return JsonResponse({str(request):str(uuid)})
    else:
      return JsonResponse({str(request):str(request)})



def get_service_details(request, uuid):

    if request is not None:
      return JsonResponse({str("Service Details"):str(uuid)})
    else:
      return JsonResponse({str(request):str(request)})