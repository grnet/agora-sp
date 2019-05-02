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


# Tests for resources with no foreign keys or special handling

def test_user_roles(serviceadmin, client, superadmin):
    assertions_crud('user_roles', serviceadmin, superadmin)


def test_service_trls(serviceadmin, client, superadmin):
    assertions_crud('service_trls', serviceadmin, superadmin)


def test_service_status(serviceadmin, client, superadmin):
    assertions_crud('service_status', serviceadmin, superadmin)


def test_contact_information(serviceadmin, client, superadmin):
    assertions_crud('contact_information', serviceadmin, superadmin)


def test_providers(serviceadmin, client, superadmin):
    assertions_crud('providers', serviceadmin, superadmin)


def test_access_policies(serviceadmin, client, superadmin):
    assertions_crud('access_policies', serviceadmin, superadmin)


def test_federation_members(serviceadmin, client, superadmin):
    assertions_crud('federation_members', serviceadmin, superadmin)


def test_components(serviceadmin, client, superadmin):
    """
    Flow:
    Serviceadmin creates components
    Serviceadmin can retrieve service
    Serviceadmin cannot update component
    Serviceadmin cannot delete component
    """
    url = RESOURCES_CRUD['components']['url']
    data = RESOURCES_CRUD['components']['create_data']
    edit_data = RESOURCES_CRUD['components']['edit_data']

    serviceadmin.post(url, data)
    assert len(serviceadmin.get(url).json()) == 1
    resp = serviceadmin.get(url)
    id = resp.json()[0]['id']
    resp = serviceadmin.get(url+id+'/')
    for key, value in data.iteritems():
        assert resp.json()[key] == value
    resp = serviceadmin.put(url + id + '/',
                            json.dumps(edit_data),
                            content_type='application/json')
    assert resp.status_code == 403
    resp = serviceadmin.delete(url + id + '/')
    assert resp.status_code == 403
    resp = superadmin.delete(url+id+'/')
    assert resp.status_code == 204


def test_services(serviceadmin, serviceadmin2, client, superadmin):
    """
    Flow:
    Serviceadmin creates service
    Serviceadmin can retrieve service
    Serviceadmin can update service
    Serviceadmin cannot delete service
    Superadmin deletes service
    Serviceadmin2 creates service2
    Serviceadmin can retrieve service2
    Serviceadmin cannot update service2
    Superadmin deletes service2
    """
    url = RESOURCES_CRUD['services']['url']
    data = RESOURCES_CRUD['services']['create_data']
    edit_data = RESOURCES_CRUD['services']['edit_data']

    serviceadmin.post(url, data)
    assert len(serviceadmin.get(url).json()) == 1
    resp = serviceadmin.get(url)
    id = resp.json()[0]['id']
    resp = serviceadmin.get(url+id+'/')
    for key, value in data.iteritems():
        assert resp.json()[key] == value
    if edit_data:
        resp = serviceadmin.patch(url + id + '/',
                                json.dumps(edit_data),
                                content_type='application/json')
        assert resp.status_code == 200
        for key, value in edit_data.iteritems():
            assert resp.json()[key] == value
    resp = serviceadmin.delete(url + id + '/')
    assert resp.status_code == 403
    resp = superadmin.delete(url+id+'/')
    assert resp.status_code == 204

    serviceadmin2.post(url, data)
    assert len(serviceadmin.get(url).json()) == 1
    resp = serviceadmin.get(url)
    id = resp.json()[0]['id']
    resp = serviceadmin.get(url + id + '/')
    for key, value in data.iteritems():
        assert resp.json()[key] == value
    if edit_data:
        resp = serviceadmin.patch(url + id + '/',
                                json.dumps(edit_data),
                                content_type='application/json')
        assert resp.status_code == 400
    resp = superadmin.delete(url+id+'/')
    assert resp.status_code == 204


# Tests for resources with related data

def test_component_implementations(serviceadmin, superadmin, component_id):
    url = '/api/v2/component-implementations/'
    data = {
        'name': 'component category',
        'component_id': component_id
    }
    resp = serviceadmin.post(url, data)
    assert resp.status_code == 201


def test_component_implementations_details(serviceadmin, superadmin, component_id,
                                           component_implementation_id):
    url = '/api/v2/component-implementation-details/'
    data = {
        'version': '1.0.0',
        'component_id': component_id,
        'component_implementation_id': component_implementation_id
    }
    resp = serviceadmin.post(url, data)
    assert resp.status_code == 201
