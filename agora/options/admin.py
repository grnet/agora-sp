from django.contrib import admin
from reversion.admin import VersionAdmin
from options.models import *
# Register your models here.


class ServiceOptionAdmin(VersionAdmin):
    pass


class SLAAdmin(VersionAdmin):
    pass


class ParameterAdmin(VersionAdmin):
    pass


class SLAParameterAdmin(VersionAdmin):
    pass


class ServiceDetailsOptionAdmin(VersionAdmin):
    pass


admin.site.register(ServiceOption, ServiceOptionAdmin)
admin.site.register(SLA, SLAAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(SLAParameter, SLAParameterAdmin)
admin.site.register(ServiceDetailsOption, ServiceDetailsOptionAdmin)
