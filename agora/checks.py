from django.db.models import Q


def has_serviceadminship(context):
    auth_user = context.extract('auth/user')
    return Q(admin=auth_user)
