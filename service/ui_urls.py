from django.conf.urls import url

from django.conf.urls import *
from service import views


urlpatterns = [

    url(r'^$', views.service_write_ui),
    url(r'^external/?$', views.external_service_write_ui),
    url(r'^area/?$', views.service_area_write_ui),
    url(r'^version/?$', views.service_details_write_ui),

]