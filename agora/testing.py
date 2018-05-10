from django.test import Client
import pytest

class ApimasClient(Client):

    auth_token = None

    def set_token(self, token):
        self.auth_token = token

    def generic(self, *args, **kwargs):
        if self.auth_token:
            kwargs['HTTP_AUTHORIZATION'] = 'Token {}'.format(self.auth_token)
        print kwargs
        return super(ApimasClient, self).generic(*args, **kwargs)


@pytest.fixture('function')
def superadmin(django_user_model):
    user, created = \
        django_user_model.objects.get_or_create(username='superadmin',
                                                role='superadmin',
                                                email='superadmin@test.org',
                                                is_superuser=True)
    user.set_password('12345')
    user.save()

    credentials = {"username": 'superadmin', "password": '12345'}
    client = ApimasClient()
    resp = client.post('/api/v2/auth/login/', credentials)
    token = resp.json().get('auth_token')
    client.set_token(token)
    return client


@pytest.fixture('function')
def admin(django_user_model):
    user, created = \
        django_user_model.objects.get_or_create(username='admin',
                                                email='admin@test.org',
                                                role='admin')
    user.set_password('12345')
    user.save()

    credentials = {"username": 'admin', "password": '12345'}
    client = ApimasClient()
    resp = client.post('/api/v2/auth/login/', credentials)
    token = resp.json().get('auth_token')
    client.set_token(token)
    return client


@pytest.fixture('function')
def serviceadmin(django_user_model):
    user, created = \
        django_user_model.objects.get_or_create(username='serviceadmin',
                                                email='serviceadmin@test.org',
                                                role='serviceadmin')
    user.set_password('12345')
    user.save()

    credentials = {"username": 'serviceadmin', "password": '12345'}
    client = ApimasClient()
    resp = client.post('/api/v2/auth/login/', credentials)
    token = resp.json().get('auth_token')
    client.set_token(token)
    return client


@pytest.fixture('function')
def serviceadmin2(django_user_model):
    user, created = \
        django_user_model.objects.get_or_create(username='serviceadmin2',
                                                email='serviceadmin2@test.org',
                                                role='serviceadmin')
    user.set_password('12345')
    user.save()

    credentials = {"username": 'serviceadmin2', "password": '12345'}
    client = ApimasClient()
    resp = client.post('/api/v2/auth/login/', credentials)
    token = resp.json().get('auth_token')
    client.set_token(token)
    return client



@pytest.fixture('function')
def observer(django_user_model):
    user, created = \
        django_user_model.objects.get_or_create(username='observer',
                                                email='observer@test.org',
                                                role='observer')
    user.set_password('12345')
    user.save()

    credentials = {"username": 'observer', "password": '12345'}
    client = ApimasClient()
    resp = client.post('/api/v2/auth/login/', credentials)
    token = resp.json().get('auth_token')
    client.set_token(token)
    return client

RESOURCES_CRUD = {
    'user_roles': {
        'url': '/api/v2/user-roles/',
        'create_data': {
            'name': 'test-name'
        },
        'edit_data': {
            'name': 'test-name-edit'
        }
    },
    'service_trls': {
        'url': '/api/v2/service-trls/',
        'create_data': {
            'value': 'test-value',
            'order': 1
        },
        'edit_data': {
            'value': 'test-value-edit',
            'order': 2
        }
    },
    'service_status': {
        'url': '/api/v2/service-status/',
        'create_data': {
            'value': 'test-value',
            'order': 1
        },
        'edit_data': {
            'value': 'test-value-edit',
            'order': 2
        }
    },
    'contact_information': {
        'url': '/api/v2/contact-information/',
        'create_data':  {
            'email': 'contact@test.org',
            'first_name': 'Hilary',
            'last_name': 'Knight',
            'phone': '+30 2102103333',
            'url': 'https://www.test.org'
        },
        'edit_data': {
            'email': 'contact2@test.org',
            'first_name': 'Hilary2',
            'last_name': 'Knight2',
            'phone': '+30 21021033332',
            'url': 'https://www.test2.org'
        }
    },
    'institutions': {
        'url': '/api/v2/institutions/',
        'create_data': {
            'address': 'Dreams 3',
            'country': 'Iceland',
            'department': 'magic',
            'name': 'test institution',
        },
        'edit_data': {
            'address': 'Dreams 3 edit',
            'country': 'Iceland-edit',
            'department': 'magic-edit',
            'name': 'test institution edit',
        },
    },
    'services': {
        'url': '/api/v2/services/',
        'create_data': {
            "name": "Test service",
        },
        'edit_data': {
            "name": "Test service 2",
        }
    },
    'service_admins': {
        'url': '/api/v2/service-admins/'
    }
}
