from django.contrib import admin
from options.models import *
# Register your models here.


class ServiceOptionAdmin(admin.ModelAdmin):
    pass


class SLAAdmin(admin.ModelAdmin):
    pass


class ParameterAdmin(admin.ModelAdmin):
    pass


class SLAParameterAdmin(admin.ModelAdmin):
    pass


class ServiceDetailsOptionAdmin(admin.ModelAdmin):
    pass


admin.site.register(ServiceOption, ServiceOptionAdmin)
admin.site.register(SLA, SLAAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(SLAParameter, SLAParameterAdmin)
admin.site.register(ServiceDetailsOption, ServiceDetailsOptionAdmin)