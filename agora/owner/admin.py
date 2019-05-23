from django.contrib import admin
from reversion.admin import VersionAdmin
from owner.models import *

# Register your models here.


class InstitutionAdmin(VersionAdmin):
    pass


class ServiceOwnerAdmin(VersionAdmin):
    pass


class ContactInformationAdmin(VersionAdmin):
    pass


class InternalAdmin(VersionAdmin):
    pass


class ExternalAdmin(VersionAdmin):
    pass


admin.site.register(Institution, InstitutionAdmin)
admin.site.register(ServiceOwner, ServiceOwnerAdmin)
admin.site.register(ContactInformation, ContactInformationAdmin)
admin.site.register(Internal, InternalAdmin)
admin.site.register(External, ExternalAdmin)
