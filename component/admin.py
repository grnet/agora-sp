from django.contrib import admin
from component.models import *
# Register your models here.


class ServiceComponentAdmin(admin.ModelAdmin):
    pass


class ServiceComponentImplementationAdmin(admin.ModelAdmin):
    pass


class ServiceComponentImplementationDetailAdmin(admin.ModelAdmin):
    pass


class ServiceDetailsComponentAdmin(admin.ModelAdmin):
    pass


admin.site.register(ServiceComponent, ServiceComponentAdmin)
admin.site.register(ServiceComponentImplementation, ServiceComponentImplementationAdmin)
admin.site.register(ServiceComponentImplementationDetail, ServiceComponentImplementationDetailAdmin)
admin.site.register(ServiceDetailsComponent, ServiceDetailsComponentAdmin)
