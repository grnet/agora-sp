from django.conf.urls import *
from options import views


urlpatterns = [

    url(r'^insert_service_option/?$', views.insert_service_option),
    url(r'^insert_SLA/?$', views.insert_SLA),
]