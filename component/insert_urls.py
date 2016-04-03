from django.conf.urls import *
from component import views


urlpatterns = [
    url(r'^insert_service_component_implementation/?$', views.insert_service_component_implementation),
    url(r'^insert_service_component_implementation_detail/?$', views.insert_service_component_implementation_details),
    url(r'^insert_component/?$', views.insert_service_component),
    url(r'^insert_service_details_component_implementation_details/?$', views.insert_service_details_component_implementation_details),
]