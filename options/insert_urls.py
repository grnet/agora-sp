from django.conf.urls import *
from options import views


urlpatterns = [

    url(r'^insert_service_option/?$', views.insert_service_option),
    url(r'^insert_parameter/?$', views.insert_parameter),
    url(r'^insert_SLA_parameter/?$', views.insert_SLA_parameter),
    url(r'^insert_SLA/?$', views.insert_SLA),
]