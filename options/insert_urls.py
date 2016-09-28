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
    url(r'^service_options/all/?$', views.get_service_options_all),
    url(r'^parameter/all/?$', views.get_parameter_all),
    url(r'^sla/all/?$', views.get_sla_all),
    url(r'^service_options/(?P<serv_opt_uuid>[0-9a-zA-Z\-]+)/?$', views.get_service_options_single),
    url(r'^sla/(?P<sla_uuid>[0-9a-zA-Z\-]+)/?$', views.get_sla),
    url(r'^parameter/(?P<param_uuid>[0-9a-zA-Z\-]+)/?$', views.get_parameter),
    url(r'^sla_parameter/(?P<sla_param_uuid>[0-9a-zA-Z\-]+)/?$', views.get_sla_parameter),
]