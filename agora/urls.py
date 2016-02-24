"""agora URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from service import views as service_views
from owner import views as owner_views

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'^services/$', service_views.show_service_list_view),
    url(r'^(portfolio|catalogue)/services', include('service.urls')),
    url(r'^owner', include('owner.urls')),
    url(r'^contact_info/(?P<uuid>[0-9a-zA-Z\-]+)', owner_views.get_contact_info),
    url(r'^service_details/(?P<uuid>[0-9a-zA-Z\-]+)', service_views.get_service_details)
]
