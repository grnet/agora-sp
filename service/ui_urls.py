from django.conf.urls import url

from django.conf.urls import *
from service import views


urlpatterns = [

    url(r'^$', views.service_write_ui),
    url(r'^all/?$', views.services_table),
    url(r'^external/?$', views.external_service_write_ui),
    url(r'^internal_dependency/?$', views.internal_dependency_write_ui),
    url(r'^external_dependency/?$', views.external_dependency_write_ui),
    url(r'^external_dependency/(?P<external_dep_uuid>[0-9a-zA-Z\@\-\_]+)?$', views.external_dependency_edit_ui),
    url(r'^internal_dependency/(?P<internal_dep_uuid>[0-9a-zA-Z\@\-\_]+)?$', views.internal_dependency_edit_ui),
    url(r'^users_customers/?$', views.users_customers_write_ui),
    url(r'^users_customers/(?P<user_customer_uuid>[0-9a-zA-Z\@\-\_]+)/?$', views.users_customers_edit_ui),
    url(r'^area/?$', views.service_area_write_ui),
    url(r'^version/?$', views.service_details_write_ui),
    url(r'^external/(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/?$', views.external_service_edit_ui),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/?$', views.service_edit_ui),
    url(r'^(?P<service_name_or_uuid>[0-9a-zA-Z\-\_]+)/version/(?P<version>[0-9\.]+)/?$', views.service_details_edit_ui),

]