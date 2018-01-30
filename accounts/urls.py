from django.conf.urls import *
from accounts import views


urlpatterns = [
    #url(r'^generate_tokens/?$', views.generate_access_tokens_for_all_users),
    #url(r'^retrieve_tokens/?', views.retrieve_social_auth_users),
    url(r'^login/?', views.login_screen),
]
