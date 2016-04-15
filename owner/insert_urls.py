from django.conf.urls import *
from owner import views


urlpatterns = [
    url(r'^institution/edit/?$', views.insert_institution),
    url(r'^institution/add/?$', views.insert_institution),
    url(r'^contact_information/add/?$', views.insert_contact_information),
    url(r'^contact_information/edit/?$', views.insert_contact_information),
    url(r'^add/?$', views.insert_service_owner),
    url(r'^edit/?$', views.insert_service_owner),
]