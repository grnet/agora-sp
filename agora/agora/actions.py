# -*- coding: UTF-8 -*-
import requests
import logging
from datetime import datetime
from django.conf import settings
import json
from datetime import datetime
from django.utils import timezone
from apimas.errors import ValidationError
from agora.utils import create_eosc_api_json

EOSC_API_URL = getattr(settings, 'EOSC_API_URL', '')
EOSC_TOKEN = getattr(settings, 'EOSC_TOKEN', '')
logger = logging.getLogger(__name__)

def resource_publish_eosc(backend_input, instance, context):
    eosc_req = create_eosc_api_json(instance)
    url = EOSC_API_URL+'resource'
    id  = str(instance.id)
    username = context['auth/user'].username
    headers = {
        'Authorization': EOSC_TOKEN,
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
        raise ValidationError(response.json()['error'])
    instance.save()
    return instance