from django.conf.urls import *
from options import views


urlpatterns = [

    url(r'^service_details_option/add/?$', views.insert_service_details_option),
    url(r'^service_option/add/?$', views.insert_service_option),
    url(r'^parameter/add/?$', views.insert_parameter),
    url(r'^SLA_paramters/add/?$', views.insert_SLA_parameter),
    url(r'^SLAs/add/?$', views.insert_SLA),
]