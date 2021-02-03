import requests
import logging
from datetime import datetime

from django.conf import settings

EOSC_API_URL = getattr(settings, 'EOSC_API_URL', '')
EOSC_TOKEN = getattr(settings, 'EOSC_TOKEN', '')

logger = logging.getLogger(__name__)


def resource_post_eosc(backend_input, instance, context):
    session = requests.Session()
    url = EOSC_API_URL+'resource'
    id  = str(instance.id)
    username = context['auth/user'].username
    headers = {
        'Authorization': EOSC_TOKEN,
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    req = requests.Request('POST',url ,headers=headers,json={"name": "Foo", "resourceOrganisation": "grnet"})
    prepared = req.prepare()
    logger.info('EOSC PORTAL API call to POST resource \
        with id %s to %s has been made by %s at %s \
        ' %(id, url, username, datetime.now()))
    res = session.send(prepared)

    logger.info('Response status code: %s' %(res.status_code))
    logger.info('Response json: %s' %(res.json()))

def pretty_print_POST(req):
    print('{}\n{}\r\n{}\r\n\r\n{}'.format(
        '-----------START-----------',
        req.method + ' ' + req.url,
        '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
        req.body,
    ))
