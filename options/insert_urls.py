from django.conf.urls import *
from options import views


urlpatterns = [

    url(r'^service_details_option/edit/?$', views.edit_service_details_option),
    url(r'^service_details_option/add/?$', views.insert_service_details_option),
    url(r'^service_option/edit/?$', views.edit_service_option),
    url(r'^service_option/add/?$', views.insert_service_option),
    url(r'^parameter/edit/?$', views.edit_parameter),
    url(r'^parameter/add/?$', views.insert_parameter),
    url(r'^SLA_paramters/edit/?$', views.edit_SLA_parameter),
    url(r'^SLA_paramters/add/?$', views.insert_SLA_parameter),
    url(r'^SLAs/edit/?$', views.edit_SLA),
    url(r'^SLAs/add/?$', views.insert_SLA),
    url(r'^service_options/(?P<serv_opt_uuid>[0-9a-zA-Z\-]+)/?$', views.get_service_options_single),
]