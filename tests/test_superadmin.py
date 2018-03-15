import json
from agora.testing import *


def assertions_crud(resource, user):
    """
    Flow:
    User can list empty resources set
    User can create resource
    User can list data set
    User can update resource
    User can delete resource
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
    assert resp.status_code == 204
    assert user.get(url).json() == []


# Tests for resources with no foreign keys

def test_user_roles(superadmin, client):
    assertions_crud('user_roles', superadmin)


def test_service_trls(superadmin, client):
    assertions_crud('service_trls', superadmin)


def test_service_status(superadmin, client):
    assertions_crud('service_status', superadmin)


def test_contact_information(superadmin, client):
    assertions_crud('contact_information', superadmin)


def test_institutions(superadmin, client):
    assertions_crud('institutions', superadmin)
