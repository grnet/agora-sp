from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from owner import models

def get_owner(request, uuid):


   own = models.ServiceOwner.objects.get(id=uuid)

   return JsonResponse({'owner' : own.as_json()})
