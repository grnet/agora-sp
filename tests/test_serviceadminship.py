from agora.testing import *


def test_serviceadminship_create_delete(serviceadmin, superadmin, client):

    service_url = RESOURCES_CRUD['services']['url']
    service_data = RESOURCES_CRUD['services']['create_data']
    sa_url = RESOURCES_CRUD['service_admins']['url']

    resp = superadmin.post(service_url, service_data)
    assert resp.status_code == 201
    service_id = resp.json()['id']

    """
    ServiceAdmin creates ServiceAdminship with status 'pending'.
    ServiceAdmin creates ServiceAdminship for himself only.
    ServiceAdmin can delete a ServiceAdminship he created in state pending.
    """
    resp = serviceadmin.post(sa_url, {'service': service_id})
    sa_id = resp.json()['id']
    assert resp.status_code == 201
    assert resp.json()['state'] == 'pending'
    assert resp.json()['admin_email'] == 'serviceadmin@test.org'

    resp = serviceadmin.delete(sa_url + sa_id + '/')
    assert resp.status_code == 204

    # Clean up
    superadmin.delete(service_url+service_id+'/')
