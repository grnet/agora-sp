from django.db.models import Q

class ServiceAdminship(object):

    @staticmethod
    def has_serviceadminship(context):
        auth_user = context.extract('auth/user')
        return Q(admin=auth_user)
