from django.conf.urls import *
from options import views


urlpatterns = [

    url(r'sla/(?P<sla_uuid>[0-9a-zA-Z\-]+)/sla_parameter/(?P<sla_param_uuid>[0-9a-zA-Z\-]+)/parameter/?$', views.get_service_sla_parameter),
    url(r'sla/(?P<sla_uuid>[0-9a-zA-Z\-]+)/?$', views.get_service_sla),
]