from access_tokens import scope, tokens
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from accounts.models import User
from component.models import *

def check_if_admin_or_owner():
    pass

def generate_token(request):

    response = {}


    service = Service.objects.get(name="B2SAFE")

    change_instance_token = tokens.generate(scope.access_obj(service, "service.change_B2SAFE"))

    response = {
        "token": change_instance_token.hex
    }

    return JsonResponse(response, status=int(response["status"][:3]))

def generate_access_tokens_for_all_users(request):
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)

    pass