# -*- coding: UTF-8 -*-
import requests
import logging
from datetime import datetime
from django.conf import settings
import json
from datetime import datetime
from django.utils import timezone
from apimas.errors import ValidationError
from agora.utils import create_eosc_api_json_resource, create_eosc_api_json_provider

EOSC_API_URL = getattr(settings, 'EOSC_API_URL', '')
OIDC_REFRESH_TOKEN = getattr(settings, 'OIDC_REFRESH_TOKEN', '')
OIDC_CLIENT_ID =  getattr(settings, 'OIDC_CLIENT_ID', '')
OIDC_URL = getattr(settings, 'OIDC_URL', '')
CA_BUNDLE = getattr(settings, 'CA_BUNDLE', '/etc/ssl/certs/ca-bundle.crt')
logger = logging.getLogger(__name__)

def get_access_token(oidc_url, refresh_token, client_id ):
    obj={
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'scope': 'openid email profile'
    }
    try:
        response = requests.post(oidc_url, data=obj, verify=CA_BUNDLE)
        response.raise_for_status()
    except requests.exceptions.RequestException as err:
        logger.info('Response status code: %s, %s, %s' % (oidc_url, err, response.json()))
        raise ValidationError("AAI: "+response.json()['error'])
    return response.json()['access_token']

def resource_publish_eosc(backend_input, instance, context):
    eosc_req = create_eosc_api_json_resource(instance)
    if 'resourceOrganisation' not in eosc_req or eosc_req['resourceOrganisation'] == None or len(eosc_req['resourceOrganisation'].strip()) == 0:
        raise ValidationError('Resource provider has not an eosc_id')
    url = EOSC_API_URL+'resource'
    id  = str(instance.id)
    username = context['auth/user'].username
    eosc_token = get_access_token(OIDC_URL, OIDC_REFRESH_TOKEN, OIDC_CLIENT_ID)
    headers = {
        'Authorization': eosc_token,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    logger.info('EOSC PORTAL API call to POST resource \
        with id %s to %s has been made by %s at %s \
        ' %(id, url, username, datetime.now()))
    try:
        response = requests.post(url, headers=headers,json=eosc_req, verify=CA_BUNDLE)
        response.raise_for_status()
        logger.info('Response status code: %s' %(response.status_code))
        logger.info('Response json: %s' %(response.json()))
        instance.eosc_state = "Published"
        instance.eosc_id = response.json()['id']
        instance.eosc_published_at = datetime.now(timezone.utc)
    except requests.exceptions.RequestException as err:
        logger.info('Response status code: %s, %s, %s' % (url, err, response.json()))
        instance.eosc_state = "Error"
        raise ValidationError("EOSC API: " +response.json()['error'])
    instance.save()
    return instance


def resource_update_eosc(backend_input, instance, context):
    eosc_req = create_eosc_api_json_resource(instance)
    if 'resourceOrganisation' not in eosc_req or eosc_req['resourceOrganisation'] == None or len(eosc_req['resourceOrganisation'].strip()) == 0:
        raise ValidationError('Resource provider has not an eosc_id')
    url = EOSC_API_URL+'resource'
    id  = str(instance.id)
    username = context['auth/user'].username
    eosc_token = get_access_token(OIDC_URL, OIDC_REFRESH_TOKEN, OIDC_CLIENT_ID)
    headers = {
        'Authorization': eosc_token,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    logger.info('EOSC PORTAL API call to PUT resource \
        with id %s to %s has been made by %s at %s \
        ' %(id, url, username, datetime.now()))
    try:
        response = requests.put(url, headers=headers,json=eosc_req, verify=CA_BUNDLE)
        response.raise_for_status()
        logger.info('Response status code: %s' %(response.status_code))
        logger.info('Response json: %s' %(response.json()))
        instance.eosc_state = "Updated"
        instance.eosc_updated_at = datetime.now(timezone.utc)
    except requests.exceptions.RequestException as err:
        logger.info('Response status code: %s, %s, %s' % (url, err, response.json()))
        instance.eosc_state = "Error"
        raise ValidationError("EOSC API: " + response.json()['error'])
    instance.save()
    return instance

def provider_publish_eosc(backend_input, instance, context):
    provider_email = context['auth/user'].email
    eosc_req = create_eosc_api_json_provider(instance, provider_email)
    url = EOSC_API_URL+'provider'
    id  = str(instance.id)
    username = context['auth/user'].username
    eosc_token = get_access_token(OIDC_URL, OIDC_REFRESH_TOKEN, OIDC_CLIENT_ID)
    headers = {
        'Authorization': eosc_token,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    logger.info('EOSC PORTAL API call to POST provider \
        with id %s to %s has been made by %s at %s \
        ' %(id, url, username, datetime.now()))
    try:
        response = requests.post(url, headers=headers,json=eosc_req, verify=CA_BUNDLE)
        response.raise_for_status()
        logger.info('Response status code: %s' %(response.status_code))
        logger.info('Response json: %s' %(response.json()))
        instance.eosc_state = "pending initial approval"
        instance.eosc_id = response.json()['id']
        instance.eosc_published_at = datetime.now(timezone.utc)
    except requests.exceptions.RequestException as err:
        logger.info('Response status code: %s, %s, %s' % (url, err, response.json()))
        instance.eosc_state = "Error"
        raise ValidationError("EOSC API: " +response.json()['error'])
    instance.save()
    return instance

def provider_update_eosc(backend_input, instance, context):
    provider_email = context['auth/user'].email
    eosc_req = create_eosc_api_json_provider(instance, provider_email)
    url = EOSC_API_URL+'provider'
    id  = str(instance.id)
    username = context['auth/user'].username
    eosc_token = get_access_token(OIDC_URL, OIDC_REFRESH_TOKEN, OIDC_CLIENT_ID)
    headers = {
        'Authorization': eosc_token,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    logger.info('EOSC PORTAL API call to PUT provider \
        with id %s to %s has been made by %s at %s \
        ' %(id, url, username, datetime.now()))
    try:
        response = requests.put(url, headers=headers,json=eosc_req, verify=CA_BUNDLE)
        response.raise_for_status()
        logger.info('Response status code: %s' %(response.status_code))
        logger.info('Response json: %s' %(response.json()))
        instance.eosc_updated_at = datetime.now(timezone.utc)
    except requests.exceptions.RequestException as err:
        logger.info('Response status code: %s, %s, %s' % (url, err, response.json()))
        raise ValidationError("EOSC API: " + response.json()['error'])
    instance.save()
    return instance


def resource_activate_eosc(backend_input, instance, context):
    url = EOSC_API_URL+'service/publish/' + instance.eosc_id
    id  = str(instance.id)
    username = context['auth/user'].username
    eosc_token = get_access_token(OIDC_URL, OIDC_REFRESH_TOKEN, OIDC_CLIENT_ID)
    headers = {
        'Authorization': 'Bearer ' +eosc_token
    }
    params = '''active=true'''
    logger.info('EOSC PORTAL API call to PATCH resource activate \
        with id %s to %s has been made by %s at %s \
        ' %(id, url, username, datetime.now()))
    try:
        response = requests.patch(url + '/?' + params, headers=headers, verify=CA_BUNDLE)
        response.raise_for_status()
        logger.info('Response status code: %s' %(response.status_code))
        logger.info('Response json: %s' %(response.json()))
        instance.eosc_state = response.json()['status']
        instance.eosc_id = response.json()['id']
        instance.eosc_published_at = datetime.now(timezone.utc)
    except requests.exceptions.RequestException as err:
        logger.info('Response status code: %s, %s, %s' % (url, err, response.json()))
        instance.eosc_state = "error"
        raise ValidationError("EOSC API: " + response.json()['error'])
    instance.save()
    return instance

def resource_deactivate_eosc(backend_input, instance, context):
    url = EOSC_API_URL+'service/publish/' + instance.eosc_id
    id  = str(instance.id)
    username = context['auth/user'].username
    eosc_token = get_access_token(OIDC_URL, OIDC_REFRESH_TOKEN, OIDC_CLIENT_ID)
    headers = {
        'Authorization': 'Bearer ' +eosc_token
    }
    params = '''active=false'''
    logger.info('EOSC PORTAL API call to PATCH resource deactivate \
        with id %s to %s has been made by %s at %s \
        ' %(id, url, username, datetime.now()))
    try:
        response = requests.patch(url + '/?' + params, headers=headers, verify=CA_BUNDLE)
        response.raise_for_status()
        logger.info('Response status code: %s' %(response.status_code))
        logger.info('Response json: %s' %(response.json()))
        instance.eosc_state = response.json()['status']
        instance.eosc_id = response.json()['id']
        instance.eosc_published_at = datetime.now(timezone.utc)
    except requests.exceptions.RequestException as err:
        logger.info('Response status code: %s, %s, %s' % (url, err, response.json()))
        instance.eosc_state = "error"
        raise ValidationError("EOSC API: " + response.json()['error'])
    instance.save()
    return instance

def provider_approve_temp_eosc(backend_input, instance, context):
    url = EOSC_API_URL+'provider/verifyProvider/' + instance.eosc_id
    id  = str(instance.id)
    username = context['auth/user'].username
    eosc_token = get_access_token(OIDC_URL, OIDC_REFRESH_TOKEN, OIDC_CLIENT_ID)
    headers = {
        'Authorization': 'Bearer ' +eosc_token
    }
    params = '''active=false&status=pending%20template%20submission'''
    logger.info('EOSC PORTAL API call to PATCH provider temp approval \
        with id %s to %s has been made by %s at %s \
        ' %(id, url, username, datetime.now()))
    try:
        response = requests.patch(url + '/?' + params, headers=headers, verify=CA_BUNDLE)
        response.raise_for_status()
        logger.info('Response status code: %s' %(response.status_code))
        logger.info('Response json: %s' %(response.json()))
        instance.eosc_state = response.json()['status']
        instance.eosc_id = response.json()['id']
        instance.eosc_published_at = datetime.now(timezone.utc)
    except requests.exceptions.RequestException as err:
        try:
            logger.info('Response status code: %s, %s, %s' % (url, err, response.json()))
            raise ValidationError("EOSC API: " + response.json()['error'])
        except:
            raise ValidationError("EOSC API: " + response.text)
    instance.save()
    return instance

def provider_approve_eosc(backend_input, instance, context):
    url = EOSC_API_URL+'provider/verifyProvider/' + instance.eosc_id
    id  = str(instance.id)
    username = context['auth/user'].username
    eosc_token = get_access_token(OIDC_URL, OIDC_REFRESH_TOKEN, OIDC_CLIENT_ID)
    headers = {
        'Authorization': 'Bearer ' +eosc_token
    }
    params = '''active=true&status=approved'''
    logger.info('EOSC PORTAL API call to PATCH provider approval \
        with id %s to %s has been made by %s at %s \
        ' %(id, url, username, datetime.now()))
    try:
        response = requests.patch(url + '/?' + params, headers=headers, verify=CA_BUNDLE)
        response.raise_for_status()
        logger.info('Response status code: %s' %(response.status_code))
        logger.info('Response json: %s' %(response.json()))
        instance.eosc_state = response.json()['status']
        instance.eosc_id = response.json()['id']
        instance.eosc_published_at = datetime.now(timezone.utc)
    except requests.exceptions.RequestException as err:
        try:
            logger.info('Response status code: %s, %s, %s' % (url, err, response.json()))
            raise ValidationError("EOSC API: " + response.json()['error'])
        except:
            raise ValidationError("EOSC API: Provider should publish at least one resource to be fully approved")
    instance.save()
    return instance

def provider_reject_eosc(backend_input, instance, context):
    url = EOSC_API_URL+'provider/verifyProvider/' + instance.eosc_id
    id  = str(instance.id)
    username = context['auth/user'].username
    eosc_token = get_access_token(OIDC_URL, OIDC_REFRESH_TOKEN, OIDC_CLIENT_ID)
    headers = {
        'Authorization': 'Bearer ' +eosc_token
    }
    params = '''active=false&status=rejected'''
    logger.info('EOSC PORTAL API call to PATCH provider rejection \
        with id %s to %s has been made by %s at %s \
        ' %(id, url, username, datetime.now()))
    try:
        response = requests.patch(url + '/?' + params, headers=headers, verify=CA_BUNDLE)
        response.raise_for_status()
        logger.info('Response status code: %s' %(response.status_code))
        logger.info('Response json: %s' %(response.json()))
        instance.eosc_state = response.json()['status']
        instance.eosc_id = response.json()['id']
        instance.eosc_published_at = datetime.now(timezone.utc)
    except requests.exceptions.RequestException as err:
        logger.info('Response status code: %s, %s, %s' % (url, err, response.json()))
        instance.eosc_state = "error"
        raise ValidationError("EOSC API: " + response.json()['error'])
    instance.save()
    return instance
