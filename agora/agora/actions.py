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
logger = logging.getLogger(__name__)

def get_access_token(oidc_url, refresh_token, client_id ):
    obj={
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token,
        'client_id': client_id,
        'scope': 'openid email profile'
    }
    try:
        response = requests.post(oidc_url, data=obj)
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
        response = requests.post(url, headers=headers,json=eosc_req)
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
        response = requests.put(url, headers=headers,json=eosc_req)
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
    eosc_req = create_eosc_api_json_provider(instance)
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
        response = requests.post(url, headers=headers,json=eosc_req)
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

def provider_update_eosc(backend_input, instance, context):
    eosc_req = create_eosc_api_json_provider(instance)
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
        response = requests.put(url, headers=headers,json=eosc_req)
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