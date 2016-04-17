from django.contrib import admin
from reversion.admin import VersionAdmin
from accounts.models import User

class UserAdmin(VersionAdmin):
    pass


admin.site.register(User, UserAdmin)