from agora.testing import *


def assertions(user, url, data, superadmin):
    """
    Flow:
    Superadmin creates a resource
    User can list resources set
    User can retrieve resource
    User cannot delete resource
    User cannot create resource (TBA)
    User cannot update resource (TBA)
    Superadmin deletes resource
    """
    superadmin.post(url, data)
    assert len(user.get(url).json()) == 1
    resp = user.get(url)
    id = resp.json()[0]['id']
    resp = user.get(url+id+'/')
    for key, value in data.iteritems():
        assert resp.json()[key] == value
    resp = user.delete(url+id+'/')
    assert resp.status_code == 403
    superadmin.delete(url+id+'/')
    #resp = user.post(url, data)
    #assert resp.status_code == 403


# Tests for resources with no foreign keys or special handling

def test_user_roles(observer, client, superadmin):
    create_data = {"name": "test-name"}
    url = '/api/v2/user-roles/'
    assertions(observer, url, create_data, superadmin)


def test_service_trls(observer, client, superadmin):
    create_data = {"value": "test-value", "order": 1}
    url = '/api/v2/service-trls/'
    assertions(observer, url, create_data, superadmin)


def test_service_status(observer, client, superadmin):
    create_data = {"value": "test-value", "order": 1}
    url = '/api/v2/service-status/'
    assertions(observer, url, create_data, superadmin)


def test_contact_information(observer, client, superadmin):
    create_data = {
        "email": "contact@test.org",
        "first_name": "Hilary",
        "last_name": "Knight",
        "phone": "+30 2102103333",
        "url": "https://www.test.org"
    }
    url = '/api/v2/contact-information/'
    assertions(observer, url, create_data, superadmin)


def test_institutions(observer, client, superadmin):
    create_data = {
        "address": "Oneirwn 10, Parmythoupoli",
        "country": "Iceland",
        "department": "Test department",
        "name": "Test institution"
    }
    url = '/api/v2/institutions/'
    assertions(observer, url, create_data, superadmin)
