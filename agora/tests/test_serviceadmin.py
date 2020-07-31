import json
from agora.testing import *
from accounts.models import Organisation, User


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

def test_target_users(serviceadmin, superadmin):
    assertions_crud('target_users', serviceadmin, superadmin)

def test_providers(serviceadmin, superadmin):
    assertions_crud('providers', serviceadmin, superadmin)

def test_access_modes(serviceadmin, superadmin):
    assertions_crud('access_modes', serviceadmin, superadmin)

def test_domains(serviceadmin, superadmin):
    assertions_crud('domains', serviceadmin, superadmin)

# def test_resources(serviceadmin, serviceadmin2, superadmin):

    # # Prepare tests: Create a Provider, a resource belonging to
    # # this Provider and a serviceadmin that also belongs to
    # # this Provider.
    # provider_url = RESOURCES_CRUD['providers']['url']
    # provider_data = RESOURCES_CRUD['providers']['create_data']
    # resp = superadmin.post(provider_url, provider_data)
    # provider_id = resp.json()['id']
    # provider = Organisation.objects.get(pk=provider_id)
    # serviceadmin_id = str(User.objects.get(username='serviceadmin').id)
    # serviceadmin2_id = str(User.objects.get(username='serviceadmin2').id)


    # """
    # Flow:
    # Serviceadmin creates resource
    # Serviceadmin can retrieve resource
    # Serviceadmin can update resource
    # Serviceadmin cannot delete resource
    # Superadmin deletes resource
    # Serviceadmin2 creates resource2
    # Serviceadmin can retrieve resource2
    # Serviceadmin cannot update resource2
    # Superadmin deletes resource2
    # """
    # url = RESOURCES_CRUD['resources']['url']
    # data = RESOURCES_CRUD['resources']['create_data']
    # extended_data = data.copy()
    # extended_data['erp_bai_2_service_organisation_id'] = provider_id
    # edit_data = RESOURCES_CRUD['resources']['edit_data']
    # resp = superadmin.patch('/api/v2/custom-users/' + serviceadmin_id + '/',
        # json.dumps({'organisation': provider_id}),
                              # content_type='application/json')

    # resp = superadmin.patch('/api/v2/custom-users/' + serviceadmin2_id + '/',
        # json.dumps({'organisation': provider_id}),
                              # content_type='application/json')

    # resp = serviceadmin.post(url, extended_data)


    # assert len(serviceadmin.get(url).json()) == 1
    # resp = serviceadmin.get(url)
    # id = resp.json()[0]['id']
    # resp = serviceadmin.get(url + id + '/')
    # for key, value in data.iteritems():
        # assert resp.json()[key] == value
    # if edit_data:
        # resp = serviceadmin.patch(url + id + '/',
                                  # json.dumps(edit_data),
                                  # content_type='application/json')
        # assert resp.status_code == 200
        # for key, value in edit_data.iteritems():
            # assert resp.json()[key] == value
    # resp = serviceadmin.delete(url + id + '/')
    # assert resp.status_code == 403
    # resp = superadmin.delete(url + id + '/')
    # assert resp.status_code == 204

    # serviceadmin2.post(url, extended_data)
    # assert len(serviceadmin.get(url).json()) == 1
    # resp = serviceadmin.get(url)
    # id = resp.json()[0]['id']
    # resp = serviceadmin.get(url + id + '/')
    # for key, value in data.iteritems():
        # assert resp.json()[key] == value
    # if edit_data:
        # resp = serviceadmin.patch(url + id + '/',
                                  # json.dumps(edit_data),
                                  # content_type='application/json')
        # assert resp.status_code == 400
    # resp = superadmin.delete(url + id + '/')
    # assert resp.status_code == 204

    # superadmin.delete(provider_url + provider_id + '/')
