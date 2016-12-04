from rest_framework.authtoken.models import Token
from agora.settings import LOGIN_REDIRECT_URL
from django.shortcuts import redirect
from django.http import JsonResponse
from service.models import Service
from common import helper, strings
from accounts.models import User
import re

def check_service_ownership_or_superuser(func):

    def check_and_call(request, *args, **kwargs):

        user = request.user

        print user.id

        params = request.POST.copy()

        if user.is_superuser:
            return func(request, *args, **kwargs)

        if "uuid" in params:
            service_name_or_uuid = params.get('uuid')

        prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")

        result = prog.match(service_name_or_uuid)

        if result is None:
            parsed_name = service_name_or_uuid.replace("_", " ").strip()
        else:
            uuid = service_name_or_uuid

        try:
            if result is None:
                service = Service.objects.get(name=parsed_name)
            else:
                service = Service.objects.get(id=uuid)

        except Service.DoesNotExist:
            response = helper.get_error_response(strings.SERVICE_NOT_FOUND)
            return JsonResponse(response)

        owner = service.get_service_owners()

        if  owner['account_id'] == user.id:
            return func(request, *args, **kwargs)
        else:
            response = helper.get_error_response(strings.OPERATION_NOT_PERMITTED, strings.FORBIDDEN_403)

            return redirect(LOGIN_REDIRECT_URL+"?next="+request.path)

    return check_and_call


def check_service_staff(func):

    def check_and_call(request, *args, **kwargs):

        user = request.user

        if user.is_superuser:
            return func(request, *args, **kwargs)

        if user.is_staff:
            return func(request, *args, **kwargs)

        response = helper.get_error_response(strings.OPERATION_NOT_PERMITTED, strings.FORBIDDEN_403)

        return redirect(LOGIN_REDIRECT_URL+"?next="+request.path)

    return check_and_call


def check_auth_and_type(func):

    def check_and_call(request, *args, **kwargs):

        user = request.user

        if ('catalogue' in args):
            return func(request, *args, **kwargs)


        if (user.is_superuser) | (user.is_staff):
            token = Token.objects.get(user_id=user.id)
            request.session['api-info'] = str(token) + "~" + str(user.email)
            return func(request, *args, **kwargs)

        if (request.method == "GET") & (user.is_authenticated()):
            token = Token.objects.get(user_id=user.id)
            request.session['api-info'] = str(token) + "~" + str(user.email)
            return func(request, *args, **kwargs)


        regex = re.compile('^HTTP_')
        headers = dict((regex.sub('', header), value) for (header, value)
               in request.META.items() if header.startswith('HTTP'))

#	json.dumps(request)

        if 'AUTHTOKEN' in headers.keys() and 'EMAIL' in headers.keys():
            try:
                user_search = User.objects.get(email=headers['EMAIL'])
                token = Token.objects.get(user_id=user_search.id)
            except:
                response = helper.get_error_response(strings.OPERATION_NOT_PERMITTED, strings.FORBIDDEN_403)
                return JsonResponse({"resp": response, "user": user.is_authenticated(), "type": args, "token": headers['AUTHTOKEN'], "email": headers['EMAIL']})


            if (str(token) == str(headers['AUTHTOKEN'])) & (str(user_search.email) == headers['EMAIL']):
                request.session['api-info'] = str(token) + "~" + str(headers['EMAIL'])
                return func(request, *args, **kwargs)
            else:
                response = helper.get_error_response(strings.OPERATION_NOT_PERMITTED, strings.FORBIDDEN_403)
                return JsonResponse({"resp": response, "user": user.is_authenticated(), "type": args, "token": headers['AUTHTOKEN'], "email": user_search.email, "token": str(token)})
        else:


            response = helper.get_error_response(strings.OPERATION_NOT_PERMITTED, strings.FORBIDDEN_403)

            return redirect(LOGIN_REDIRECT_URL+"?next="+request.path)

            # return JsonResponse({"resp": response, "user": user.is_authenticated(), "type": args})

    return check_and_call

