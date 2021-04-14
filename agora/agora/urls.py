import os
import json
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.static import serve

from agora import views as agora_views
from djoser import views as djoser_views

from apimas_django import provider
from agora.spec import APP_CONFIG

app_spec = provider.configure_apimas_app(APP_CONFIG)

config_file = os.path.join(settings.SETTINGS_DIR, 'deployment.conf')
if os.path.isfile(config_file):
    with open(config_file) as f:
        deploy_config = json.load(f)
    deployment_spec = provider.configure_spec(app_spec, deploy_config)
else:
    deployment_spec = app_spec

api_urls = provider.construct_views(deployment_spec)

urlpatterns = [
    url(r'^api/admin/?', admin.site.urls),
    url(r'^api/shibboleth$', agora_views.shibboleth_login,
        name='shibboleth_login'),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^api/v2/auth/me/$', agora_views.CustomMe.as_view(),
        name='custom_me'),
    url(r'^api/v2/auth/', include('djoser.urls')),
    url(r'^api/v2/auth/login/$',
        djoser_views.LoginView.as_view(), name='login'),
    url(r'^api/v2/auth/', include('djoser.urls.authtoken')),
    url(r'^api/v2/config.json$', agora_views.config, name='config'),
    url(r'^api/v2/accounting/?', agora_views.accounting, name='accounting'),
    url(r'^api/v2/monthly_stats', agora_views.monthly_stats, name='monthly_stats'),
]

urlpatterns.extend(api_urls)

urls_static = static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urls_static_files = static(settings.STATIC_URL,
                           document_root=settings.STATIC_ROOT)
urlpatterns.extend(urls_static)
urlpatterns.extend(urls_static_files)


if getattr(settings, 'SERVE_UI', True):
    # make django app serve ember dist files

    ui_prefix = getattr(settings, 'UI_PREFIX', 'ui/')
    if ui_prefix and ui_prefix != '/':
        urlpatterns += [url('^$', RedirectView.as_view(url=ui_prefix))]

    root = os.path.dirname(__file__)
    ui_root = os.path.abspath(os.path.join(root, '..', '..', 'ui/dist'))

    # admin may optionaly use a custom dist dir via settings
    ui_root = getattr(settings, 'DISTPATH_UI', ui_root)
    assets = os.path.join(ui_root, 'assets')
    if ui_prefix == '/':
        ui_prefix = ''

    urlpatterns += static('%sassets/' % ui_prefix, document_root=assets)

    # serve index.html for all paths
    urlpatterns += [
        url('^%s.*' % ui_prefix, serve, {
            'path': 'index.html',
            'document_root': ui_root
            }),
    ]


handler404 = "agora.views.error404"
handler400 = "agora.views.error400"
handler500 = "agora.views.error500"
