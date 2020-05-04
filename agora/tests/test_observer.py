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
    resp = user.get(url + id + '/')
    for key, value in data.iteritems():
        assert resp.json()[key] == value
    resp = user.delete(url + id + '/')
    assert resp.status_code == 403
    resp = superadmin.delete(url + id + '/')
    assert resp.status_code == 204


# Tests for resources with no foreign keys or special handling

def test_target_users(observer, superadmin):
    assertions_crud('target_users', observer, superadmin)


# Tests for ServiceAdminship

# def test_serviceadminship(observer, superadmin):
    # """
    # Observer cannot list  ServiceAdminships
    # Observer cannot create  ServiceAdminships
    # """
    # service_url = RESOURCES_CRUD['services']['url']
    # service_data = RESOURCES_CRUD['services']['create_data']
    # resp = superadmin.post(service_url, service_data)

    # sa_url = RESOURCES_CRUD['service_admins']['url']

    # resp = observer.get(sa_url)
    # assert resp.status_code == 403

    # resp = observer.post(sa_url, {'admin': 1, 'service': 1})
    # assert resp.status_code == 403


# Tests for resources with related data
