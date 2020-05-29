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
    print resp
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



# Tests for ServiceAdminship

# def test_serviceadminship_create(superadmin):

    # service_url = RESOURCES_CRUD['services']['url']
    # service_data = RESOURCES_CRUD['services']['create_data']
    # resp = superadmin.post(service_url, service_data)

    # service_id = resp.json()['id']
    # test_user, created = User.objects.get_or_create(
        # username='test_user',
        # email='test_user@test.org',
        # role='serviceadmin')
    # test_user.set_password('12345')
    # test_user.save()
    # sa_url = RESOURCES_CRUD['service_admins']['url']

    # """
    # Superadmin creates ServiceAdminship with status 'approved'.
    # Superadmin can delete a serviceAdminship
    # """
    # resp = superadmin.post(sa_url,
                           # {'admin': test_user.id, 'service': service_id})
    # sa_id = resp.json()['id']
    # assert resp.status_code == 201
    # assert resp.json()['state'] == 'approved'

    # resp = superadmin.delete(sa_url + sa_id + '/')
    # assert resp.status_code == 204

    # resp = superadmin.delete(service_url + service_id + '/')
    # assert resp.status_code == 204

    # resp = superadmin.post(service_url, service_data)
    # service_id = resp.json()['id']
    # test_user, created = User.objects.get_or_create(
        # username='test_user',
        # email='test_user@test.org')
    # """
    # Superadmin cannot create ServiceAdminship for user with roles 'observer',
    # 'superadmin' or 'admin'.
    # """
    # for role in ['observer', 'superadmin', 'admin']:
        # test_user.role = role
        # test_user.save()

        # resp = superadmin.post(sa_url,
                               # {'admin': test_user.id, 'service': service_id})
        # assert resp.status_code == 400

    # superadmin.delete(service_url + service_id + '/')


# def test_serviceadminship_update(superadmin):
    # """
    # Allowed state transitions are:
    # ('pending', 'approved'),
    # ('pending', 'rejected'),
    # ('rejected', 'pending'),
    # ('approved', 'pending'),
    # """

    # service_url = RESOURCES_CRUD['services']['url']
    # service_data = RESOURCES_CRUD['services']['create_data']
    # resp = superadmin.post(service_url, service_data)

    # service_id = resp.json()['id']
    # test_user, created = User.objects.get_or_create(
        # username='test_user',
        # email='test_user@test.org',
        # role='serviceadmin')
    # test_user.set_password('12345')
    # test_user.save()
    # sa_url = RESOURCES_CRUD['service_admins']['url']

    # resp = superadmin.post(sa_url,
                           # {'admin': test_user.id, 'service': service_id})
    # sa_id = resp.json()['id']

    # resp = superadmin.patch(
        # sa_url + sa_id + '/',
        # json.dumps({'state': 'rejected'}),
        # content_type='application/json')
    # assert resp.status_code == 400

    # resp = superadmin.patch(
        # sa_url + sa_id + '/',
        # json.dumps({'state': 'approved'}),
        # content_type='application/json')
    # assert resp.status_code == 400

    # resp = superadmin.patch(
        # sa_url + sa_id + '/',
        # json.dumps({'state': 'pending'}),
        # content_type='application/json')
    # assert resp.status_code == 200


# Tests for resources with related data
