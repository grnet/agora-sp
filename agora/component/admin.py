from django.contrib import admin
from reversion.admin import VersionAdmin
from component.models import *
# Register your models here.


class ServiceComponentAdmin(VersionAdmin):
    pass


class ServiceComponentImplementationAdmin(VersionAdmin):
    pass


class ServiceComponentImplementationDetailAdmin(VersionAdmin):
    pass


class ServiceDetailsComponentAdmin(VersionAdmin):
    pass


admin.site.register(ServiceComponent, ServiceComponentAdmin)
admin.site.register(ServiceComponentImplementation, ServiceComponentImplementationAdmin)
admin.site.register(ServiceComponentImplementationDetail, ServiceComponentImplementationDetailAdmin)
admin.site.register(ServiceDetailsComponent, ServiceDetailsComponentAdmin)
