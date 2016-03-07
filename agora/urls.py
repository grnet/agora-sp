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

urlpatterns = [
    url(r'^admin/?', admin.site.urls),
    url(r'^docs/?', include('rest_framework_swagger.urls')),
    url(r'^api-docs/?', include('rest_framework_swagger.urls')),
    #url(r'^services/$', service_views.show_service_list_view),

    url(r'^v[0-9]+/(portfolio|catalogue)/services/(?P<search_type>[0-9a-zA-Z\-\_]+)/service_details/(?P<version>[0-9a-zA-Z\.]+)/service_components/?', include('component.urls')),
    url(r'^v[0-9]+/(portfolio|catalogue)/services/(?P<search_type>[0-9a-zA-Z\-\_]+)/service_details/(?P<version>[0-9.]+)/service_options/sla/(?P<sla_search_type>[0-9a-fA-F\-]+)/?$', include('component.urls')),
    url(r'^v[0-9]+/(portfolio|catalogue)/services/', include('service.urls')),
]

handler404 = "agora.views.error404"
handler400 = "agora.views.error400"
handler500 = "agora.views.error500"