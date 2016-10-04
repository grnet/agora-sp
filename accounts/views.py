import hashlib
import os
import urllib2
from django.core.files.base import ContentFile
import agora.settings
from access_tokens import scope, tokens
from django.http import JsonResponse
from rest_framework.authtoken.models import Token
from accounts.models import User
from component.models import *
from django.shortcuts import render
from social.backends.google import GoogleOAuth2
# from social.apps.django_app.default.models import UserSocialAuth


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

def login_screen(request):

    state = hashlib.sha256(os.urandom(1024)).hexdigest()

    request.session['state'] = state

    if request.user.is_authenticated():

        return render(request, "accounts/login.html",
          {   "CLIENT_ID" : agora.settings.CLIENT_ID,
              "STATE" : state,
              "APPLICATION_NAME" : agora.settings.APPLICATION_NAME,
              "AUTHENTICATION" : request.user.is_authenticated(),
              "USER": request.user
              })

    else:
        return render(request, "accounts/login.html",
                  {   "CLIENT_ID" : agora.settings.CLIENT_ID,
                      "STATE" : state,
                      "APPLICATION_NAME" : agora.settings.APPLICATION_NAME,
                      "AUTHENTICATION" : request.user.is_authenticated()})

def save_avatar(backend, user, response, *args, **kwargs):
    if isinstance(backend, GoogleOAuth2):
        if response.get('image') and response['image'].get('url'):
            url = response['image'].get('url')

            if user.avatar == "":
                ext = url.split('.')[-1][-5]
                user.avatar.save(
                   '{0}_{1}.jpg'.format('avatar',str(user.id)),
                   ContentFile(urllib2.urlopen(url).read()),
                   save=False
                )
                user.save()

def retrieve_social_auth_users(request):


    user = UserSocialAuth.objects.all()[0]

    # response = {}
    #
    # for user in users:
    #     response[str(user.uid)] = str(user.extra_data)

    return JsonResponse({"access_token": user.extra_data['access_token']})
