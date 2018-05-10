import json
from agora.testing import *


def assertions_crud(resource, user, superadmin):
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
    url = RESOURCES_CRUD[resource]['url']
    data = RESOURCES_CRUD[resource]['create_data']
    edit_data = RESOURCES_CRUD[resource]['edit_data']
    superadmin.post(url, data)
    assert len(user.get(url).json()) == 1
    resp = user.get(url)
    id = resp.json()[0]['id']
    resp = user.get(url+id+'/')
    for key, value in data.iteritems():
        assert resp.json()[key] == value
    resp = user.delete(url+id+'/')
    assert resp.status_code == 403
    resp = superadmin.delete(url+id+'/')
    assert resp.status_code == 204
    #resp = user.post(url, data)
    #assert resp.status_code == 403


# Tests for resources with no foreign keys or special handling

def test_user_roles(observer, client, superadmin):
    assertions_crud('user_roles', observer, superadmin)


def test_service_trls(observer, client, superadmin):
    assertions_crud('service_trls', observer, superadmin)


def test_service_status(observer, client, superadmin):
    assertions_crud('service_status', observer, superadmin)


def test_contact_information(observer, client, superadmin):
    assertions_crud('contact_information', observer, superadmin)


def test_institutions(observer, client, superadmin):
    assertions_crud('institutions', observer, superadmin)

def test_services(observer, client, superadmin):
    assertions_crud('services', observer, superadmin)


# Tests for ServiceAdminship

def test_serviceadminship(observer, superadmin, client):
    """
    Observer cannot list  ServiceAdminships
    Observer cannot create  ServiceAdminships
    """
    service_url = RESOURCES_CRUD['services']['url']
    service_data = RESOURCES_CRUD['services']['create_data']
    resp = superadmin.post(service_url, service_data)

    service_id = resp.json()['id']
    sa_url = RESOURCES_CRUD['service_admins']['url']

    resp = observer.get(sa_url)
    assert resp.status_code == 403

    resp = observer.post(sa_url, {'admin': 1, 'service': 1})
    assert resp.status_code == 403
