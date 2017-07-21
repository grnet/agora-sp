from django.contrib import admin
from reversion.admin import VersionAdmin
from service.models import *
# Register your models here.

class ServiceTrlAdmin(VersionAdmin):
    pass

class UserRoleAdmin(VersionAdmin):
    pass

class ServiceAdmin(VersionAdmin):
    list_display = ['id', 'name', ]

class ServiceStatusAdmin(VersionAdmin):
    pass

class ServiceDetailsAdmin(VersionAdmin):
    list_display = ['id', 'id_service', 'version']

class ExternalServiceAdmin(VersionAdmin):
    pass


class Service_DependsOn_ServiceAdmin(VersionAdmin):
    pass


class Service_ExternalServiceAdmin(VersionAdmin):
    pass


class UserCustomerAdmin(VersionAdmin):
    pass

class ServiceAreaAdmin(VersionAdmin):
    pass

admin.site.register(ServiceTrl, ServiceTrlAdmin)
admin.site.register(UserRole, UserRoleAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceStatus, ServiceStatusAdmin)
admin.site.register(ServiceDetails, ServiceDetailsAdmin)
admin.site.register(ExternalService, ExternalServiceAdmin)
admin.site.register(Service_DependsOn_Service, Service_DependsOn_ServiceAdmin)
admin.site.register(Service_ExternalService, Service_ExternalServiceAdmin)
admin.site.register(UserCustomer, UserCustomerAdmin)
admin.site.register(ServiceArea, ServiceAreaAdmin)
