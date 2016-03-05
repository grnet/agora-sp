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

urlpatterns = [
    url(r'^admin/?', admin.site.urls),
    url(r'^docs/?', include('rest_framework_swagger.urls')),
    url(r'^v[0-9]+/(portfolio|catalogue)/services/', include('service.urls')),
]

handler404 = "agora.views.error404"
handler400 = "agora.views.error400"
handler500 = "agora.views.error500"