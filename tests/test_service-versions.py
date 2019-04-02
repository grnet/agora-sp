import json
from agora.testing import *
from service.models import ServiceStatus


def test_serviceversion_create_edit(serviceadmin, serviceadmin_id, superadmin):

    """
    S2 is owned by ServiceAdmin
    ServiceAdmin cannot create Service Version with not owned  service s1
    ServiceAdmin creates Service Version with  owned service s2 (sv2)
    Superadmin creates Service Version with  service s1 (sv1)
    ServiceAdmin cannot delete sv1
    ServiceAdmin cannot delete sv2
    Serviceadmin cannot edit is_in_catalogue and visible_to_marketplace
    fields.
    """

    sv_url = RESOURCES_CRUD['service_versions']['url']
    service_url = RESOURCES_CRUD['services']['url']
    status_url = RESOURCES_CRUD['service_status']['url']
    sa_url = RESOURCES_CRUD['service_admins']['url']

    # Prepare s1, s2 and status
    resp = superadmin.post(service_url, {
        'name': 'S1',
        'customer_facing': False,
        'internal': False
    })
    s1 = resp.json()['id']

    resp = superadmin.post(service_url, {
        'name': 'S2',
        'customer_facing': False,
        'internal': False
    })
    s2 = resp.json()['id']

    resp = superadmin.post(sa_url, {'service': s2, 'admin': serviceadmin_id})
    status, created = ServiceStatus.objects.get_or_create(value='st')

    SV_DATA_1 = {
        'version': '1.1',
        'id_service': s1,
        'status': status.id,
        'terms_of_use_has': True,
        'user_documentation_has': True,
        'privacy_policy_has': True,
        'operations_documentation_has': True,
        'monitoring_has': True,
        'accounting_has': True,
        'business_continuity_plan_has': True,
        'disaster_recovery_plan_has': True,
        'decommissioning_procedure_has': True,
        'is_in_catalogue': True,
        'visible_to_marketplace': True
    }

    SV_DATA_1_LIMITED = {
        'version': '1.1',
        'id_service': s1,
        'status': status.id,
        'terms_of_use_has': True,
        'user_documentation_has': True,
        'privacy_policy_has': True,
        'operations_documentation_has': True,
        'monitoring_has': True,
        'accounting_has': True,
        'business_continuity_plan_has': True,
        'disaster_recovery_plan_has': True,
        'decommissioning_procedure_has': True,
    }


    SV_DATA_2 = {
        'version': '1.2',
        'id_service': s2,
        'status': status.id,
        'terms_of_use_has': True,
        'user_documentation_has': True,
        'privacy_policy_has': True,
        'operations_documentation_has': True,
        'monitoring_has': True,
        'accounting_has': True,
        'business_continuity_plan_has': True,
        'disaster_recovery_plan_has': True,
        'decommissioning_procedure_has': True,
        'is_in_catalogue': True,
        'visible_to_marketplace': True
    }

    SV_DATA_2_LIMITED = {
        'version': '1.2',
        'id_service': s2,
        'status': status.id,
        'terms_of_use_has': True,
        'user_documentation_has': True,
        'privacy_policy_has': True,
        'operations_documentation_has': True,
        'monitoring_has': True,
        'accounting_has': True,
        'business_continuity_plan_has': True,
        'disaster_recovery_plan_has': True,
        'decommissioning_procedure_has': True,
    }



    # CREATE
    resp = serviceadmin.post(sv_url, SV_DATA_1)
    assert resp.status_code == 403

    resp = serviceadmin.post(sv_url, SV_DATA_1_LIMITED)
    assert resp.status_code == 400

    resp = superadmin.post(sv_url, SV_DATA_1)
    assert resp.status_code == 201
    sv1_id = resp.json()['id']

    resp = serviceadmin.post(sv_url, SV_DATA_2)
    assert resp.status_code == 403
     
    resp = serviceadmin.post(sv_url, SV_DATA_2_LIMITED)
    assert resp.status_code == 201
    sv2_id = resp.json()['id']


    # DELETE
    resp = serviceadmin.delete(sv_url + sv1_id + '/')
    assert resp.status_code == 403

    resp = serviceadmin.delete(sv_url + sv2_id + '/')
    assert resp.status_code == 403

    resp = superadmin.delete(sv_url + sv1_id + '/')
    assert resp.status_code == 204

    # Clean up
    superadmin.delete(service_url+s1+'/')
    superadmin.delete(service_url+s2+'/')
    superadmin.delete(sv_url+sv2_id+'/')
    superadmin.delete(status_url+str(status.id)+'/')
