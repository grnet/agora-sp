from django.conf.urls import *
from accounts import views


urlpatterns = [

    url(r'^generate_tokens/?$', views.generate_access_tokens_for_all_users),
]