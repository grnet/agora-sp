from django.conf.urls import *
from owner import views


urlpatterns = [
    url(r'^institution/add/?$', views.insert_institution),
    url(r'^contact_information/add/?$', views.insert_contact_information),
    url(r'^add/?$', views.insert_service_owner),
]