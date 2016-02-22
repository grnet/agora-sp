from django.conf.urls import url

from django.conf.urls import *
from service import views


urlpatterns = [



    url(r'(?P<uuid>[0-9a-zA-Z\-]+)/service_details', views.get_service_details),
    url(r'(?P<uuid>[0-9a-zA-Z\-]+)', views.get_service),
    url(r'$', views.list_services),


]