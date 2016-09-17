from django.conf.urls import *
from options import views


urlpatterns = [

    url(r'^sla/?$', views.options_sla_write_ui),
    url(r'^parameter/?$', views.options_parameter_write_ui),
    url(r'^service_options/?$', views.service_options_write_ui),
    url(r'^service_options/(?P<serv_opt_uuid>[0-9a-zA-Z\-]+)/?$', views.service_options_edit_ui),
    url(r'^sla/(?P<sla_uuid>[0-9a-zA-Z\-]+)/?$', views.options_sla_edit_ui),
]