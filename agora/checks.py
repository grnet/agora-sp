from django.db.models import Q
from apimas.errors import ValidationError


class ServiceAdminship(object):

    @staticmethod
    def has_serviceadminship(context):
        auth_user = context.extract('auth/user')
        return Q(admin=auth_user)


class Service(object):

    @staticmethod
    def owned(backend_input, instance, context):
        auth_user = context.extract('auth/user')
        auth_user_id = str(auth_user.id)
        service_admins_ids = instance.service_admins_ids.split(",")
        if auth_user_id in service_admins_ids:
            return
        else:
            raise ValidationError("Unauthorized action")
