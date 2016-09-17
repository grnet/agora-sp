from django.conf.urls import *
from owner import views


urlpatterns = [
    url(r'^institution/edit/?$', views.edit_institution),
    url(r'^institution/add/?$', views.insert_institution),
    url(r'^contact_information/add/?$', views.insert_contact_information),
    url(r'^contact_information/edit/?$', views.edit_contact_information),
    url(r'^add/?$', views.insert_service_owner),
    url(r'^edit/?$', views.edit_service_owner),
    url(r'^(?P<owner_uuid>[0-9a-zA-Z\@\-\_]+)$', views.get_service_owner_single),
    url(r'^contact_information/(?P<contact_uuid>[0-9a-zA-Z\@\-\_]+)$', views.get_contact_information),
    url(r'^institution/(?P<institution_uuid>[0-9a-zA-Z\@\-\_]+)$', views.get_institution)
]