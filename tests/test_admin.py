import json
from agora.testing import *
from accounts.models import User


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
        resp = user.put(
            url + id + '/',
            json.dumps(edit_data),
            content_type='application/json')
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


# Tests for ServiceAdminship

def test_serviceadminship_create(admin, superadmin, client):

    service_url = RESOURCES_CRUD['services']['url']
    service_data = RESOURCES_CRUD['services']['create_data']
    sa_url = RESOURCES_CRUD['service_admins']['url']

    resp = admin.post(service_url, service_data)
    service_id = resp.json()['id']
    test_user, created = User.objects.get_or_create(
        username='test_user1',
        email='test_user1@test.org',
        role='serviceadmin')
    test_user.set_password('12345')
    test_user.save()

    """
    Admin creates ServiceAdminship with status 'approved'.
    Admin cannot delete a ServiceAdminship
    """
    resp = admin.post(sa_url, {'admin': test_user.id, 'service': service_id})
    sa_id = resp.json()['id']
    assert resp.status_code == 201
    assert resp.json()['state'] == 'approved'

    resp = admin.delete(sa_url+sa_id+'/')
    assert resp.status_code == 403

    resp = admin.delete(service_url+service_id+'/')
    assert resp.status_code == 403

    # Clean up
    superadmin.delete(sa_url+sa_id+'/')
    superadmin.delete(service_url+service_id+'/')

    resp = admin.post(service_url, service_data)
    service_id = resp.json()['id']
    test_user, created = User.objects.get_or_create(
        username='test_user1',
        email='test_user1@test.org')
    """
    Admin cannot create ServiceAdminship for user with roles 'observer',
    'superadmin' or 'admin'.
    """
    for role in ['observer', 'superadmin', 'admin']:
        test_user.role = role
        test_user.save()

        resp = admin.post(sa_url, {'admin': test_user.id, 'service': service_id})
        assert resp.status_code == 400

    # Clean up
    superadmin.delete(service_url+service_id+'/')
