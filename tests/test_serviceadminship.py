import json
from agora.testing import *
from django.core import mail


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


def test_serviceadminship_emails(serviceadmin, serviceadmin2,
                                 superadmin, client):

    service_url = RESOURCES_CRUD['services']['url']
    service_data = RESOURCES_CRUD['services']['create_data']
    sa_url = RESOURCES_CRUD['service_admins']['url']

    resp = serviceadmin.post(service_url, service_data)
    service_id = resp.json()['id']

    """
    When a serviceadmin applies for adminship for a service, an email is sent
    to all other approved admins of the service.

    """
    resp = serviceadmin2.post(sa_url, {'service': service_id})
    sa_id = resp.json()['id']
    admin2_id = resp.json()['admin_id']
    assert len(mail.outbox) == 1
    assert mail.outbox[0].recipients() == ['serviceadmin@test.org']
    assert mail.outbox[0].subject == 'Agora: Application created'

    # Clean up mail outbox
    mail.outbox = []

    """
    When an adminship is approved an email is sent to the applicant and emails
    are sent to all other approved admins of the service.

    """

    resp = serviceadmin.patch(sa_url + sa_id + '/',
                              json.dumps({'state': 'approved'}),
                              content_type='application/json')

    assert len(mail.outbox) == 2
    assert mail.outbox[0].recipients() == ['serviceadmin2@test.org']
    assert mail.outbox[0].subject == 'Agora: Application approved'
    assert mail.outbox[1].recipients() == ['serviceadmin@test.org']
    assert mail.outbox[1].subject == 'Agora: Application approved'

    # Clean up mail outbox
    mail.outbox = []

    """
    When an adminship is rejected an email is sent to the applicant and emails
    are sent to all other approved admins of the service.

    """

    resp = serviceadmin.patch(sa_url + sa_id + '/',
                              json.dumps({'state': 'pending'}),
                              content_type='application/json')
    resp = serviceadmin.patch(sa_url + sa_id + '/',
                              json.dumps({'state': 'rejected'}),
                              content_type='application/json')

    assert len(mail.outbox) == 2
    assert mail.outbox[0].recipients() == ['serviceadmin2@test.org']
    assert mail.outbox[0].subject == 'Agora: Application rejected'
    assert mail.outbox[1].recipients() == ['serviceadmin@test.org']
    assert mail.outbox[1].subject == 'Agora: Application rejected'

    # Clean up mail outbox
    mail.outbox = []

    """
    When a superadmin assigns a serviceadmin as admin of a service, an email
    is sent to the newly created admin and to all other approved admins of
    the service.

    """

    resp = serviceadmin.patch(sa_url + sa_id + '/',
                              json.dumps({'state': 'pending'}),
                              content_type='application/json')
    resp = serviceadmin2.delete(sa_url + sa_id + '/')
    resp = superadmin.post(sa_url, {'service': service_id, 'admin': admin2_id})

    assert len(mail.outbox) == 2
    assert mail.outbox[0].recipients() == ['serviceadmin2@test.org']
    assert mail.outbox[0].subject == 'Agora: Service administrator assigned'
    assert mail.outbox[1].recipients() == ['serviceadmin@test.org']
    assert mail.outbox[1].subject == 'Agora: Service administrator assigned'

    # Clean up mail outbox
    mail.outbox = []

    # Clean up
    superadmin.delete(service_url+service_id+'/')
