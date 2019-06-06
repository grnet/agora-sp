import json
from django.test import Client
from service.models import Service
from agora.testing import superadmin, RESOURCES_CRUD
from agora.permissions import SERVICE_SENSITIVE_DATA


def test_name_trim(superadmin):
    """
    Test that Service 'name' field is trimmed before the model is saved.
    """
    url = RESOURCES_CRUD['services']['url']
    data = {
        "internal": False,
        "customer_facing": True,
    }

    data.update(name='ice hockey')
    superadmin.post(url, data)
    assert superadmin.get(url).json()[0]['name'] == 'ice hockey'

    data.update(name='table tennis ')
    superadmin.post(url, data)
    assert superadmin.get(url).json()[1]['name'] == 'table tennis'

    data.update({'name': ' ski'})
    superadmin.post(url, data)
    assert superadmin.get(url).json()[2]['name'] == 'ski'


def test_required_related_services(superadmin):
    """
    Test that required_services and related_services m2m fields work.

    We will first create a hockey service, then create a tennis service
    with hockey as a requirement and then create a ski service with both
    required_services and related_services filled. Finally, we will add ski
    as a requirement to itself to test that this can be done too.
    """
    url = RESOURCES_CRUD['services']['url']
    data = {
        'internal': False,
        'customer_facing': True,
        'name': 'hockey',
    }
    superadmin.post(url, data)
    assert superadmin.get(url).json()[0]['name'] == 'hockey'
    hockey_service = superadmin.get(url).json()[0]
    hockey_service_obj = Service.objects.get(name=hockey_service['name'])

    data.update(name='tennis', required_services=[hockey_service['id']])
    superadmin.post(url, json.dumps(data), content_type='application/json')
    assert superadmin.get(url).json()[1]['name'] == 'tennis'
    tennis_service = superadmin.get(url).json()[1]
    tennis_service_obj = Service.objects.get(name=tennis_service['name'])
    assert len(tennis_service['required_services']) == 1
    assert tennis_service_obj.required_services.first() == hockey_service_obj

    # Also test that required_services is not symmetrical
    hockey_service_obj = Service.objects.get(name=hockey_service['name'])
    assert len(hockey_service_obj.required_services.values()) == 0

    data.update({
        'name': 'ski',
        'related_services': [hockey_service['id'], tennis_service['id']],
        'required_services': [hockey_service['id']],
        })
    superadmin.post(url, json.dumps(data), content_type='application/json')
    assert superadmin.get(url).json()[2]['name'] == 'ski'
    ski_service = superadmin.get(url).json()[2]
    ski_service_obj = Service.objects.get(name=ski_service['name'])
    assert len(ski_service['related_services']) == 2
    assert len(ski_service['required_services']) == 1
    assert ski_service_obj.related_services.get(name='tennis') \
                           == tennis_service_obj

    data.clear()
    data.update(required_services=[hockey_service['id'], ski_service['id']])
    resp = superadmin.patch(url + ski_service['id'] + '/', json.dumps(data),
                            content_type='application/json')
    assert resp.status_code == 200
    ski_service = superadmin.get(url).json()[2]
    ski_service_obj = Service.objects.get(name=ski_service['name'])
    assert len(ski_service['required_services']) == 2
    assert ski_service_obj.required_services.get(name='ski') \
                           == ski_service_obj


def test_service_sensitive_data(superadmin):
    """
    Check that sensitive data are not exposed publicly.

    Check that public api /api/v2/ext-services does not expose sensitive data.
    Check that anonymous user does not view sensitive data
    in public /api/v2/services call.
    Check that authenticated user can view sensitive data in
    /api/v2/services call.
    """

    sensitive_len = len(SERVICE_SENSITIVE_DATA)
    client = Client()

    # Create a Service
    service_url = RESOURCES_CRUD['services']['url']
    service_data = RESOURCES_CRUD['services']['create_data']
    resp = superadmin.post(service_url, service_data)

    # Anonymous user /api/v2/ext-services
    resp = client.get('/api/v2/ext-services/')
    service = resp.json()[0]
    keys = service.keys()
    assert not list(set(keys) & set(SERVICE_SENSITIVE_DATA))

    # Anonymous user /api/v2/services
    resp = client.get(service_url)
    service = resp.json()[0]
    keys = service.keys()
    assert not list(set(keys) & set(SERVICE_SENSITIVE_DATA))

    # Authenticated user /api/v2/services
    resp = superadmin.get(service_url)
    service = resp.json()[0]
    keys = service.keys()
    assert len(list(set(keys) & set(SERVICE_SENSITIVE_DATA))) == sensitive_len
