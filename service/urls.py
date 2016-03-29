from django.conf.urls import url

from django.conf.urls import *
from service import views


urlpatterns = [

    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_details/(?P<version>[0-9.]+)/?$', views.get_service_details),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_details/?$', views.get_all_service_details),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/institution/?$', views.get_service_institution),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/contact_information/?$', views.get_service_contact_information),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_dependencies/?$', views.get_service_dependencies),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/service_external_dependencies/?$', views.get_service_external_dependencies),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/insert_service_dependency/?$', views.insert_service_dependency),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/insert_external_service_dependency/?$', views.insert_external_service_dependency),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/insert_user_customer/?$', views.insert_user_customer),
    url(r'^insert_service/?$', views.insert_service),
    url(r'^insert_external_service/?$', views.insert_external_service),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/?$', views.get_service),
    url(r'^$', views.list_services),

]