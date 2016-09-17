from django.conf.urls import *
from options import views


urlpatterns = [

    url(r'^sla/?$', views.options_sla_write_ui),
    url(r'^parameter/?$', views.options_parameter_write_ui),
    url(r'^service_options/?$', views.service_options_write_ui),
]