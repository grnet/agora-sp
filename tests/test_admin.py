import json
from agora.testing import *


def assertions_crud(resource, user, superadmin):
    """
    Flow:
    User can list empty resources set
    User can create resource
    User can list data set
    User can update resource (TBA)
    User cannot delete resource
    Superadmin deletes resource
    """
    url = RESOURCES_CRUD[resource]['url']
    data = RESOURCES_CRUD[resource]['create_data']
    edit_data = RESOURCES_CRUD[resource]['edit_data']
    assert user.get(url).json() == []
    resp = user.post(url, data)
    assert resp.status_code == 201
    for key, value in data.iteritems():
        assert resp.json()[key] == value
    assert len(user.get(url).json()) == 1
    id = resp.json()['id']
    if edit_data:
        resp = user.put(url+id+ '/', json.dumps(edit_data), content_type='application/json')
        assert resp.status_code == 200
        for key, value in edit_data.iteritems():
            assert resp.json()[key] == value
    resp = user.delete(url+id+'/')
    assert resp.status_code == 403
    resp = superadmin.delete(url+id+'/')
    assert resp.status_code == 204


# Tests for resources with no foreign keys

def test_user_roles(admin, client, superadmin):
    assertions_crud('user_roles', admin, superadmin)


def test_service_trls(admin, client, superadmin):
    assertions_crud('service_trls', admin, superadmin)


def test_service_status(admin, client, superadmin):
    assertions_crud('service_status', admin, superadmin)


def test_contact_information(admin, client, superadmin):
    assertions_crud('contact_information', admin, superadmin)


def test_institutions(admin, client, superadmin):
    assertions_crud('institutions', admin, superadmin)


def test_services(admin, client, superadmin):
    assertions_crud('services', admin, superadmin)
