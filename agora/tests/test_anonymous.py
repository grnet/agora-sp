import json
from django.test import Client
from agora.testing import *

client = Client()


def assertions_crud(resource, user, superadmin):
    """
    Flow:
    Superadmin creates a resource
    Anonymous user cannot list resources
    Anonymous user cannot create resource
    Anonymous user cannot retrieve resource
    Anonymous user cannot update resource
    Anonymous user cannot delete resource
    Superadmin deletes resource
    """
    url = RESOURCES_CRUD[resource]['url']
    data = RESOURCES_CRUD[resource]['create_data']
    edit_data = RESOURCES_CRUD[resource]['edit_data']
    resp = user.get(url)
    assert resp.status_code == 403
    resp = user.post(url, data)
    assert resp.status_code == 403
    superadmin.post(url, data)
    id = superadmin.get(url).json()[0]['id']
    resp = user.get(url + id + '/')
    assert resp.status_code == 403
    if edit_data:
        resp = user.patch(
            url + id + '/',
            json.dumps(edit_data),
            content_type='application/json')
        assert resp.status_code == 403
    resp = user.delete(url + id + '/')
    assert resp.status_code == 403
    resp = superadmin.delete(url + id + '/')
    assert resp.status_code == 204


# Tests for resources with no foreign keys or special handling

def test_target_users(superadmin):
    assertions_crud('target_users', client, superadmin)
