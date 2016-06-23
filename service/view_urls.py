from django.conf.urls import url

from django.conf.urls import *
from service import views


urlpatterns = [
    url(r'^catalogue/services/(?P<service>[0-9a-zA-Z\-\_]+)/?$', views.service_view_catalogue),
    url(r'^portfolio/services/(?P<service>[0-9a-zA-Z\-\_]+)/?$', views.service_view_portfolio)

]