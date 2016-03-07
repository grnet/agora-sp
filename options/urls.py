from django.conf.urls import *
from options import views


urlpatterns = [

    url(r'', views.get_service_sla),

]