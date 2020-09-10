import json
from agora.testing import *
from accounts.models import User, Organisation


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

    resp = user.delete(url + id + '/')
    assert resp.status_code == 204
    assert user.get(url).json() == []


# Tests for resources with no foreign keys

def test_target_users(superadmin):
    assertions_crud('target_users', superadmin)

def test_providers(superadmin):
    assertions_crud('providers', superadmin)

def test_resources(superadmin):
    assertions_crud('resources', superadmin)

def test_access_modes(superadmin):
    assertions_crud('access_modes',superadmin)

def test_domains(superadmin):
    assertions_crud('domains',superadmin)

# Tests for ResourceAdminship

def test_resourceadminship_create(superadmin):

    # Prepare tests: Create a Provider, a resource belonging to
    # this Provider and a serviceadmin that also belongs to
    # this Provider.
    provider_url = RESOURCES_CRUD['providers']['url']
    provider_data = RESOURCES_CRUD['providers']['create_data']
    resp = superadmin.post(provider_url, provider_data)

    provider_id = resp.json()['id']
    provider = Organisation.objects.get(pk=provider_id)

    resource_url = RESOURCES_CRUD['resources']['url']
    resource_data = RESOURCES_CRUD['resources']['create_data']
    resource_data['erp_bai_2_service_organisation'] = provider_id
    resp = superadmin.post(resource_url, resource_data)

    resource_id = resp.json()['id']
    test_user, _ = User.objects.get_or_create(
        username='test_user',
        email='test_user@test.org',
        organisation=provider,
        role='serviceadmin')
    test_user.set_password('12345')
    test_user.save()
    ra_url = RESOURCES_CRUD['resource_admins']['url']

    """
    Superadmin creates ResourceAdminship with status 'approved'.
    Superadmin can delete a ResrouceAdminship.
    """
    resp = superadmin.post(ra_url,
                           {'admin': test_user.id, 'resource': resource_id})
    assert resp.status_code == 201
    assert resp.json()['state'] == 'approved'
    ra_id = resp.json()['id']

    resp = superadmin.delete(ra_url + ra_id + '/')
    assert resp.status_code == 204

    resp = superadmin.delete(resource_url + resource_id + '/')
    assert resp.status_code == 204

    resp = superadmin.post(resource_url, resource_data)
    resource_id = resp.json()['id']
    test_user, _ = User.objects.get_or_create(
        username='test_user',
        email='test_user@test.org')
    """
    Superadmin cannot create ResourceAdminship for user with roles 'observer',
    'superadmin' or 'admin'.
    """
    for role in ['observer', 'superadmin', 'admin']:
        test_user.role = role
        test_user.save()

        resp = superadmin.post(ra_url,
                               {'admin': test_user.id, 'resource': resource_id})
        assert resp.status_code == 400

    superadmin.delete(resource_url + resource_id + '/')
    superadmin.delete(provider_url + provider_id + '/')


def test_resourceadminship_update(superadmin):
    """
    Allowed state transitions are:
    ('pending', 'approved'),
    ('pending', 'rejected'),
    ('rejected', 'pending'),
    ('approved', 'pending'),
    """

    # Prepare tests: Create a Provider, a resource belonging to
    # this Provider and a serviceadmin that also belongs to
    # this Provider.
    provider_url = RESOURCES_CRUD['providers']['url']
    provider_data = RESOURCES_CRUD['providers']['create_data']
    resp = superadmin.post(provider_url, provider_data)
    provider_id = resp.json()['id']
    provider = Organisation.objects.get(pk=provider_id)

    resource_url = RESOURCES_CRUD['resources']['url']
    resource_data = RESOURCES_CRUD['resources']['create_data']
    resource_data['erp_bai_2_service_organisation'] = provider_id
    resp = superadmin.post(resource_url, resource_data)

    resource_id = resp.json()['id']
    test_user, _ = User.objects.get_or_create(
        username='test_user',
        email='test_user@test.org',
        organisation=provider,
        role='serviceadmin')
    test_user.set_password('12345')
    test_user.save()
    ra_url = RESOURCES_CRUD['resource_admins']['url']

    resp = superadmin.post(ra_url,
                           {'admin': test_user.id, 'resource': resource_id})
    ra_id = resp.json()['id']

    resp = superadmin.patch(
        ra_url + ra_id + '/',
        json.dumps({'state': 'rejected'}),
        content_type='application/json')
    assert resp.status_code == 400

    resp = superadmin.patch(
        ra_url + ra_id + '/',
        json.dumps({'state': 'approved'}),
        content_type='application/json')
    assert resp.status_code == 400

    resp = superadmin.patch(
        ra_url + ra_id + '/',
        json.dumps({'state': 'pending'}),
        content_type='application/json')
    assert resp.status_code == 200
