from agora.testing import *


def assertions(user, url, data):
    """
    Flow:
    User can list empty resources set
    User can create resource
    User can list data set
    User can update resource (TBA)
    User can delete resource
    """
    assert user.get(url).json() == []
    resp = user.post(url, data)
    assert resp.status_code == 201
    for key, value in data.iteritems():
        assert resp.json()[key] == value
    assert len(user.get(url).json()) == 1
    id = resp.json()['id']
    # resp = user.put(url+id+ '/', data = {"name": "test-name-2"})
    # assert resp.json()['name'] == 'test-name=2'
    resp = user.delete(url+id+'/')
    assert user.get(url).json() == []


# Tests for resources with no foreign keys

def test_user_roles(superadmin, client):
    create_data = {"name": "test-name"}
    url = '/api/v2/user-roles/'
    assertions(superadmin, url, create_data)


def test_service_trls(superadmin, client):
    create_data = {"value": "test-value", "order": 1}
    url = '/api/v2/service-trls/'
    assertions(superadmin, url, create_data)


def test_service_status(superadmin, client):
    create_data = {"value": "test-value", "order": 1}
    url = '/api/v2/service-status/'
    assertions(superadmin, url, create_data)


def test_contact_information(superadmin, client):
    create_data = {
        "email": "contact@test.org",
        "first_name": "Hilary",
        "last_name": "Knight",
        "phone": "+30 2102103333",
        "url": "https://www.test.org"
    }
    url = '/api/v2/contact-information/'
    assertions(superadmin, url, create_data)


def test_institutions(superadmin, client):
    create_data = {
        "address": "Oneirwn 10, Parmythoupoli",
        "country": "Iceland",
        "department": "Test department",
        "name": "Test institution"
    }
    url = '/api/v2/institutions/'
    assertions(superadmin, url, create_data)
