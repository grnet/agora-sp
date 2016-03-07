from django.conf.urls import *
from component import views


urlpatterns = [

    url(r'(?P<comp_uuid>[0-9a-zA-Z\-]+)/service_component_implementations/?$', views.get_service_component_implementations),
    url(r'(?P<comp_uuid>[0-9a-zA-Z\-]+)/service_component_implementations/(?P<imp_uuid>[0-9a-zA-Z\-]+)'
        r'/service_component_implementation_detail/?$', views.get_service_component_implementation_detail),
    url(r'(?P<comp_uuid>[0-9a-zA-Z\-]+)/?$', views.get_service_component),
    url(r'', views.get_service_components),

]