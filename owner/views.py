from django.http import JsonResponse
from owner import models
from service import models as service_models
from rest_framework.decorators import *
from common import helper, strings
from django.contrib.auth.decorators import login_required
import re
from django.db import IntegrityError


# Returns a list of the service owners
@api_view(['GET'])
def get_service_owner(request, service_name_or_uuid):
    """
    Retrieves a the service owner

    """

    response = {}
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(service_name_or_uuid)
    service, parsed_name, uuid = None, None, None

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ").strip()
    else:
        uuid = service_name_or_uuid

    try:
        if result is None:
            service = service_models.Service.objects.get(name=parsed_name)
        else:
            service = service_models.Service.objects.get(id=uuid)

    except service_models.Service.DoesNotExist:
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    if service is not None:
        response = helper.get_response_info(strings.SERVICE_OWNER_INFORMATION, service.get_service_owners())

    return JsonResponse(response, status=int(response["status"][:3]))


# Returns the institution of the service owner by both name and uuid
@api_view(['GET'])
def get_service_owner_institution(request, service_name_or_uuid, service_owner):
    """
    Retrieves the institution of the owner

    """

    response = {}
    service, owner, parsed_name, uuid, owner_name, owner_uuid, owner_email = None, None, None, None, None, None, None

    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}")
    result = prog.match(service_name_or_uuid)
    owner_match = prog.match(service_owner)

    if result is None:
        parsed_name = service_name_or_uuid.replace("_", " ").strip()
    else:
        uuid = service_name_or_uuid

    if owner_match is None:
        if '@' not in service_owner:
            owner_name = service_owner.split("_")
        else:
            owner_email = service_owner

    else:
        owner_uuid = service_owner

    try:
        if result is None:
            service = service_models.Service.objects.get(name=parsed_name)
        else:
            service = service_models.Service.objects.get(id=uuid)

        if owner_match is None:
            if '@' not in service_owner:
                owner = service_models.ServiceOwner.objects.get(first_name=owner_name[0], last_name=owner_name[1])
            else:
                owner = service_models.ServiceOwner.objects.get(email=owner_email)

        else:
            owner = service_models.ServiceOwner.objects.get(id=owner_uuid)

    except models.ServiceOwner.DoesNotExist:
        owner = None
        response = helper.get_error_response(strings.OWNER_NOT_FOUND)

    except service_models.Service.DoesNotExist:
        service = None
        response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

    except ValueError as v:
        if str(v) == "badly formed hexadecimal UUID string":
            response = helper.get_error_response(strings.INVALID_UUID)

    if service is not None and owner is not None:
        response = helper.get_response_info(strings.SERVICE_OWNER_INSTITUTION, owner.get_institution())

    return JsonResponse(response, status=int(response["status"][:3]))


# Updates an Institution object
@api_view(['POST'])
def edit_institution(request):
    """

    :param request:
    :return:
    """

    return insert_institution(request)

# Inserts an Institution object
# @login_required
@api_view(['POST'])
def insert_institution(request):
    """
    Inserts an institution object

    :param request:
    :return:
    """

    op_type = helper.get_last_url_part(request)
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")
    uuid, name, institution = None, None, None

    if "name" not in params and op_type == "add":
        return JsonResponse(helper.get_error_response(strings.INSTITUTION_NAME_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif "name" in params:
        name = params.get('name')
        if name is None or len(name) == 0:
            return JsonResponse(helper.get_error_response(strings.INSTITUTION_NAME_EMPTY, status=strings.REJECTED_406),
                                status=406)
    elif op_type == "edit":
        name = None

    if "uuid" in params:

        uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            institution = models.Institution.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.INSTITUTION_UUID_EXISTS,
                                                              status=strings.CONFLICT_409), status=409)
        except models.Institution.DoesNotExist:
            institution = models.Institution()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.INSTITUTION_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404), status=404)
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.INSTITUTION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif op_type == "add":
        institution = models.Institution()

    if name is not None:
        institution.name = name
    if "address" in params:
        institution.address = params.get('address')
    if "country" in params:
        institution.country = params.get('country')
    if "department" in params:
        institution.department = params.get('department')

    if uuid is not None:
        institution.id = uuid

    try:
        institution.save()
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.INSTITUTION_NAME_EXISTS, status=strings.REJECTED_406),
                            status=406)

    data = institution.as_json()

    msg = strings.INSTITUTION_INSERTED if op_type == "add" else strings.INSTITUTION_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response, status=int(response["status"][:3]))


# Updates an Contact Information object
@api_view(['POST'])
def edit_contact_information(request):
    """

    :param request:
    :return:
    """

    return insert_contact_information(request)

# Inserts an Contact Information object
# @login_required
@api_view(['POST'])
def insert_contact_information(request):
    """
    Inserts a contact information object

    """

    op_type = helper.get_last_url_part(request)
    uuid, contact_information = None, None
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")

    condition = False

    if "uuid" in params:

        uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            contact_information = models.ContactInformation.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.CONTACT_INFORMATION_UUID_EXISTS,
                                                              status=strings.CONFLICT_409), status=409)
        except models.ContactInformation.DoesNotExist:
            contact_information = models.ContactInformation()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.CONTACT_INFORMATION_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404), status=404)
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SERVICE_CONTACT_INFORMATION_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif op_type == "add":
        contact_information = models.ContactInformation()


    if ("email" not in params) and ("url" not in params):
        return JsonResponse(helper.get_error_response(strings.OWNER_URL_OR_EMAIL_NOT_PROVIDED, status=strings.REJECTED_406))


    if "first_name" in params:
        first_name = params.get('first_name')
        # if first_name is None or len(first_name) == 0:
        #     return JsonResponse(helper.get_error_response(strings.OWNER_FIRST_NAME_EMPTY, status=strings.REJECTED_406))
        contact_information.first_name = first_name

    if "last_name" in params:
        last_name = params.get('last_name')
        # if last_name is None or len(last_name) == 0:
        #     return JsonResponse(helper.get_error_response(strings.OWNER_LAST_NAME_EMPTY, status=strings.REJECTED_406))
        contact_information.last_name = last_name

    if "email" in params:
        email = params.get('email')
        if email is None or len(email) == 0:
            return JsonResponse(helper.get_error_response(strings.OWNER_EMAIL_EMPTY, status=strings.REJECTED_406),
                                status=406)
        contact_information.email = email

    if "phone" in params:
        phone = params.get('phone')
        # if phone is None or len(phone) == 0:
        #     return JsonResponse(helper.get_error_response(strings.OWNER_PHONE_EMPTY, status=strings.REJECTED_406))
        contact_information.phone = phone

    if "url" in params:
        url = params.get('url')
        if url is None or len(url) == 0:
            return JsonResponse(helper.get_error_response(strings.OWNER_URL_EMPTY, status=strings.REJECTED_406),
                                status=406)
        contact_information.url = url

    if uuid is not None:
        contact_information.id = uuid

    try:
        contact_information.save()
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.CONTACT_INFORMATION_EXISTS, status=strings.REJECTED_406),
                            status=406)

    data = contact_information.as_json()

    msg = strings.CONTACT_INFORMATION_INSERTED if op_type == "add" else strings.CONTACT_INFORMATION_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)

    return JsonResponse(response, status=int(response["status"][:3]))


# Updates a Service Owner object
@api_view(['POST'])
def edit_service_owner(request):
    """

    :param request:
    :return:
    """

    return insert_service_owner(request)

# Inserts an Service Owner object
# @login_required
@api_view(['POST'])
def insert_service_owner(request):
    """
    Inserts a service owner object

    """

    op_type = helper.get_last_url_part(request)
    params = helper.get_request_data(request)
    prog = re.compile("[a-fA-F0-9]{8}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{4}-[a-fA-F0-9]{12}$")


    if "email" not in params:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OWNER_EMAIL_NOT_PROVIDED,
                                                      status=strings.REJECTED_406))

    institution, institution_uuid, service_owner, uuid = None, None, None, None


    # if "institution_uuid" not in params:
    #     return JsonResponse(helper.get_error_response(strings.INSTITUTION_UUID_NOT_PROVIDED,
    #                                                   status=strings.REJECTED_406), status=406)

    if "institution_uuid" in params:
        institution_uuid = params.get('institution_uuid')

        result = prog.match(institution_uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            institution = models.Institution.objects.get(id=institution_uuid)

        except models.Institution.DoesNotExist:
            return JsonResponse(helper.get_error_response(strings.INSTITUTION_NOT_FOUND, status=strings.NOT_FOUND_404),
                                status=404)

    if "uuid" in params:

        uuid = params.get("uuid")
        result = prog.match(uuid)

        if result is None:
            return JsonResponse(helper.get_error_response(strings.INVALID_UUID,
                                                          status=strings.REJECTED_406), status=406)

        try:
            service_owner = models.ServiceOwner.objects.get(id=uuid)
            if op_type == "add":
                return JsonResponse(helper.get_error_response(strings.SERVICE_OWNER_UUID_EXISTS,
                                                              status=strings.CONFLICT_409), status=409)
        except models.ServiceOwner.DoesNotExist:
            service_owner = models.ServiceOwner()
            if op_type == "edit":
                return JsonResponse(helper.get_error_response(strings.SERVICE_OWNER_NOT_FOUND,
                                                              status=strings.NOT_FOUND_404), status=404)
    elif op_type == "edit":
        return JsonResponse(helper.get_error_response(strings.SERVICE_OWNER_UUID_NOT_PROVIDED,
                                                      status=strings.REJECTED_406), status=406)
    elif op_type == "add":
        service_owner = models.ServiceOwner()

    if "first_name" in params:
        first_name = params.get('first_name')
        # if first_name is None or len(first_name) == 0:
        #     return JsonResponse(helper.get_error_response(strings.OWNER_FIRST_NAME_EMPTY, status=strings.REJECTED_406))
        service_owner.first_name = first_name

    if "last_name" in params:
        last_name = params.get('last_name')
        # if last_name is None or len(last_name) == 0:
        #     return JsonResponse(helper.get_error_response(strings.OWNER_LAST_NAME_EMPTY, status=strings.REJECTED_406))
        service_owner.last_name = last_name

    if "email" in params:
        email = params.get('email')
        if email is None or len(email) == 0:
            return JsonResponse(helper.get_error_response(strings.OWNER_EMAIL_EMPTY, status=strings.REJECTED_406),
                                status=406)
        service_owner.email = email

    if "phone" in params:
        phone = params.get('phone')
        # if phone is None or len(phone) == 0:
        #     return JsonResponse(helper.get_error_response(strings.OWNER_PHONE_EMPTY, status=strings.REJECTED_406))
        service_owner.phone = phone

    service_owner.id_service_owner = institution

    if uuid is not None:
        service_owner.id = uuid
    try:
        service_owner.save()
    except IntegrityError:
        return JsonResponse(helper.get_error_response(strings.SERVICE_OWNER_EMAIL_EXISTS, status=strings.REJECTED_406),
                            status=406)

    data = service_owner.as_json()
    msg = strings.SERVICE_OWNER_INSERTED if op_type == "add" else strings.SERVICE_OWNER_UPDATED
    status = strings.CREATED_201 if op_type == "add" else strings.UPDATED_202
    response = helper.get_response_info(msg, data, status=status)
    return JsonResponse(response, status=int(response["status"][:3]))