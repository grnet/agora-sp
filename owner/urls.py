from django.conf.urls import url

from django.conf.urls import *
from owner import views


urlpatterns = [

    url(r'(?P<uuid>[0-9a-zA-Z\-]+)', views.get_owner),
]