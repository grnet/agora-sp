from django.conf.urls import *
from owner import views


urlpatterns = [
    url(r'^insert_institution/?$', views.insert_institution),
    url(r'^insert_contact_information/?$', views.insert_contact_information),
    url(r'^insert_service_owner/?$', views.insert_service_owner),
]