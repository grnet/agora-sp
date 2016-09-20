from django.conf.urls import url

from django.conf.urls import *
from service import views


urlpatterns = [

    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_details/(?P<version>[0-9.]+)/view/?$', views.get_service_details_for_view),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_details/(?P<version>[0-9.]+)/?$', views.get_service_details),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_details/?$', views.get_all_service_details),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_logo/?$', views.get_service_logo),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_options/?$', views.get_service_options),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/institution/?$', views.get_service_institution),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/contact_information/?$', views.get_service_contact_information),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_dependencies/?$', views.get_service_dependencies),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_dependencies_with_graphics/?$', views.get_service_dependencies_with_graphics),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_external_dependencies/?$', views.get_service_external_dependencies),
    url(r'^(?P<service>[0-9a-zA-Z\-\_]+)/view?$', views.get_service_catalogue_view),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/?$', views.get_service),
    url(r'^$', views.list_services),

]