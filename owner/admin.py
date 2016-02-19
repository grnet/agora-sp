from django.contrib import admin
from owner.models import *

# Register your models here.


class InstitutionAdmin(admin.ModelAdmin):
    pass


class ServiceOwnerAdmin(admin.ModelAdmin):
    pass


class ContactInformationAdmin(admin.ModelAdmin):
    pass


class InternalAdmin(admin.ModelAdmin):
    pass

class ExternalAdmin(admin.ModelAdmin):
    pass


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(ServiceOwner, ServiceOwnerAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(Internal, InternalAdmin)
admin.site.register(External, ExternalAdmin)