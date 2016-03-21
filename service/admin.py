from django.contrib import admin
from service.models import *
# Register your models here.


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]


class ServiceDetailsAdmin(admin.ModelAdmin):
    list_display = ['id', 'id_service', 'version']


class ExternalServiceAdmin(admin.ModelAdmin):
    pass


class Service_DependsOn_ServiceAdmin(admin.ModelAdmin):
    pass


class Service_ExternalServiceAdmin(admin.ModelAdmin):
    pass


class UserCustomerAdmin(admin.ModelAdmin):
    pass

admin.site.register(Service, ServiceAdmin)
admin.site.register(ServiceDetails, ServiceDetailsAdmin)
admin.site.register(ExternalService, ExternalServiceAdmin)
admin.site.register(Service_DependsOn_Service, Service_DependsOn_ServiceAdmin)
admin.site.register(Service_ExternalService, Service_ExternalServiceAdmin)
admin.site.register(UserCustomer, UserCustomerAdmin)
