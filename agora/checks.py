from django.db.models import Q


def has_serviceownership(context):
    auth_user = context.extract('auth/user')
    return Q(owner=auth_user)
