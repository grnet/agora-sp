import json
from agora.testing import *
from accounts.models import User


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
        resp = user.patch(
            url + id + '/',
            json.dumps(edit_data),
            content_type='application/json')
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


def test_services(superadmin, client):
    assertions_crud('services', superadmin)


def test_components(superadmin, client):
    assertions_crud('components', superadmin)


def test_organisations(superadmin, client):
    assertions_crud('organisations', superadmin)


def test_access_policies(superadmin, client):
    assertions_crud('access_policies', superadmin)


def test_service_providers(superadmin, client):
    assertions_crud('service_providers', superadmin)


# Tests for ServiceAdminship

def test_serviceadminship_create(superadmin, client):

    service_url = RESOURCES_CRUD['services']['url']
    service_data = RESOURCES_CRUD['services']['create_data']
    resp = superadmin.post(service_url, service_data)

    service_id = resp.json()['id']
    test_user, created = User.objects.get_or_create(
        username='test_user',
        email='test_user@test.org',
        role='serviceadmin')
    test_user.set_password('12345')
    test_user.save()
    sa_url = RESOURCES_CRUD['service_admins']['url']

    """
    Superadmin creates ServiceAdminship with status 'approved'.
    Superadmin can delete a serviceAdminship
    """
    resp = superadmin.post(sa_url,
                           {'admin': test_user.id, 'service': service_id})
    sa_id = resp.json()['id']
    assert resp.status_code == 201
    assert resp.json()['state'] == 'approved'

    resp = superadmin.delete(sa_url+sa_id+'/')
    assert resp.status_code == 204

    resp = superadmin.delete(service_url+service_id+'/')
    assert resp.status_code == 204

    resp = superadmin.post(service_url, service_data)
    service_id = resp.json()['id']
    test_user, created = User.objects.get_or_create(
        username='test_user',
        email='test_user@test.org')
    """
    Superadmin cannot create ServiceAdminship for user with roles 'observer',
    'superadmin' or 'admin'.
    """
    for role in ['observer', 'superadmin', 'admin']:
        test_user.role = role
        test_user.save()

        resp = superadmin.post(sa_url,
                               {'admin': test_user.id, 'service': service_id})
        assert resp.status_code == 400

    superadmin.delete(service_url+service_id+'/')


def test_serviceadminship_update(superadmin, client):
    """
    Allowed state transitions are:
    ('pending', 'approved'),
    ('pending', 'rejected'),
    ('rejected', 'pending'),
    ('approved', 'pending'),
    """

    service_url = RESOURCES_CRUD['services']['url']
    service_data = RESOURCES_CRUD['services']['create_data']
    resp = superadmin.post(service_url, service_data)

    service_id = resp.json()['id']
    test_user, created = User.objects.get_or_create(
        username='test_user',
        email='test_user@test.org',
        role='serviceadmin')
    test_user.set_password('12345')
    test_user.save()
    sa_url = RESOURCES_CRUD['service_admins']['url']

    resp = superadmin.post(sa_url,
                           {'admin': test_user.id, 'service': service_id})
    sa_id = resp.json()['id']

    resp = superadmin.patch(
        sa_url + sa_id + '/',
        json.dumps({'state': 'rejected'}),
        content_type='application/json')
    assert resp.status_code == 400

    resp = superadmin.patch(
        sa_url + sa_id + '/',
        json.dumps({'state': 'approved'}),
        content_type='application/json')
    assert resp.status_code == 400

    resp = superadmin.patch(
        sa_url + sa_id + '/',
        json.dumps({'state': 'pending'}),
        content_type='application/json')
    assert resp.status_code == 200


# Tests for resources with related data

def test_component_implementations(superadmin, component_id):
    url = '/api/v2/component-implementations/'
    data = {
        'name': 'component category',
        'component_id': component_id
    }
    resp = superadmin.post(url, data)
    assert resp.status_code == 201


def test_component_implementations_details(superadmin, component_id,
                                           component_implementation_id):
    url = '/api/v2/component-implementation-details/'
    data = {
        'version': '1.0.0',
        'component_id': component_id,
        'component_implementation_id': component_implementation_id
    }
    resp = superadmin.post(url, data)
    assert resp.status_code == 201
