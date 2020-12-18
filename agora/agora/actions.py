import requests
import logging
from datetime import datetime

from django.conf import settings

EOSC_API_URL = getattr(settings, 'EOSC_API_URL', '')
EOSC_TOKEN = getattr(settings, 'EOSC_TOKEN', '')

logger = logging.getLogger(__name__)


def resource_post_eosc(backend_input, instance, context):
    username = context['auth/user'].username
    url = EOSC_API_URL+'resource'
    id  = str(instance.id)
    headers = {
        'Authorization': EOSC_TOKEN,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    # TODO: Perform call to EOSC PORTAL API
    logger.info('EOSC PORTAL API call to POST resource \
        with id %s to %s has been made by %s at %s \
        ' %(id, url, username, datetime.now()))


