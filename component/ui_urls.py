from django.conf.urls import *
from component import views


urlpatterns = [
    url(r'^$', views.service_component_write_ui),
    url(r'^all/?$', views.service_component_table),
    url(r'^implementation/?$', views.service_component_implementation_write_ui),
    url(r'^implementation_detail/?$', views.service_component_implementation_detail_write_ui),
    url(r'^(?P<comp_uuid>[0-9a-zA-Z\-]+)/?$', views.service_component_edit_ui),
    url(r'^implementation/(?P<comp_imp_uuid>[0-9a-zA-Z\-]+)/?$', views.service_component_implementation_edit_ui),
    url(r'^implementation_detail/(?P<comp_imp_det_uuid>[0-9a-zA-Z\-]+)/?$', views.service_component_implementation_detail_edit_ui),
]