from django.conf.urls import url

from django.conf.urls import *
from service import views


urlpatterns = [

    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_\ \.]+)/service_dependencies/edit/?$', views.edit_service_dependency),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_\ \.]+)/service_dependencies/add/?$', views.insert_service_dependency),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_\ \.]+)/service_details/edit/?$', views.edit_service_details),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_\ \.]+)/service_details/add/?$', views.insert_service_details),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_\ \.]+)/service_external_dependencies/edit/?$', views.edit_external_service_dependency),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_\ \.]+)/service_external_dependencies/add/?$', views.insert_external_service_dependency),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_\ \.]+)/user_customer/edit/?$', views.edit_user_customer),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_\ \.]+)/user_customer/add/?$', views.insert_user_customer),
    url(r'^edit/?$', views.edit_service),
    url(r'^add/?$', views.insert_service),
    url(r'^all/?$', views.get_services),
    url(r'^external/all/?$', views.get_external_services),
    url(r'^area/all/?$', views.get_service_areas),
    url(r'^area/add/?$', views.insert_service_area),
    url(r'^type/all/?$', views.get_service_types),
    url(r'^version/all/?$', views.get_service_versions),
    url(r'^external_service/edit/?$', views.edit_external_service),
    url(r'^external_service/add/?$', views.insert_external_service),
    url(r'^external_service/(?P<service_name_or_uuid>[0-9a-zA-Z\-\_\ \.]+)/?$', views.get_external_service),
    url(r'^external_dependency/(?P<external_dep_uuid>[0-9a-zA-Z\-\_]+)/?$', views.get_external_dependency),
    url(r'^internal_dependency/(?P<internal_dep_uuid>[0-9a-zA-Z\-\_]+)/?$', views.get_internal_dependency),
    url(r'^users_customers/(?P<user_customer_uuid>[0-9a-zA-Z\-\_]+)/?$', views.get_user_customer),

]