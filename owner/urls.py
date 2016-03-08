from django.conf.urls import url

from django.conf.urls import *
from owner import views


urlpatterns = [

    url(r'^$', views.get_service_owner),
    url(r'(?P<service_owner>[0-9a-zA-Z\-\_]+)/institution/?$', views.get_service_owner_institution),
]