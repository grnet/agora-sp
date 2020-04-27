import pytest
from django.test import Client
from component.models import ServiceComponent, ServiceComponentImplementation
from accounts.models import User


class ApimasClient(Client):

    auth_token = None

    def set_token(self, token):
        self.auth_token = token

    def generic(self, *args, **kwargs):
        if self.auth_token:
            kwargs['HTTP_AUTHORIZATION'] = 'Token {}'.format(self.auth_token)
        print kwargs
        return super(ApimasClient, self).generic(*args, **kwargs)


def create_client(django_user_model, username, email, role,
                  is_superuser=False):
    user, _ = \
        django_user_model.objects.get_or_create(username=username,
                                                email=email,
                                                role=role,
                                                is_superuser=is_superuser)
    user.set_password('12345')
    user.save()

    credentials = {"username": username, "password": '12345'}
    client = ApimasClient()
    resp = client.post('/api/v2/auth/login/', credentials)
    token = resp.json().get('auth_token')
    client.set_token(token)
    return client


@pytest.fixture(name="create_client")
def create_client_fixture(django_user_model, username, email, role,
                          is_superuser=False):
    return create_client(django_user_model, username, email, role,
                         is_superuser)


@pytest.fixture('function')
def superadmin(django_user_model):
    return create_client(django_user_model,
                         'superadmin',
                         'superadmin@test.org',
                         'superadmin',
                         True)


@pytest.fixture('function')
def admin(django_user_model):
    return create_client(django_user_model,
                         'admin',
                         'admin@test.org',
                         'admin')


@pytest.fixture('function')
def serviceadmin(django_user_model):
    return create_client(django_user_model,
                         'serviceadmin',
                         'serviceadmin@test.org',
                         'serviceadmin')


@pytest.fixture('function')
def serviceadmin_id(serviceadmin):
    s, _ = User.objects.get_or_create(username='serviceadmin')
    return s.id


@pytest.fixture('function')
def serviceadmin2(django_user_model):
    return create_client(django_user_model,
                         'serviceadmin2',
                         'serviceadmin2@test.org',
                         'serviceadmin')


@pytest.fixture('function')
def observer(django_user_model):
    return create_client(django_user_model,
                         'observer',
                         'observer@test.org',
                         'observer')


@pytest.fixture('function')
def component():
    component, _ = ServiceComponent.objects.get_or_create(
        name='Servers',
        description='category description')
    return component


@pytest.fixture('function')
def component_id(component):
    return component.id


@pytest.fixture('function')
def component_implementation_id(component):
    component_implementation, _ = ServiceComponentImplementation.\
            objects.get_or_create(name='Apache',
                                  component_id=component,
                                  description='component description')
    return component_implementation.id


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
            'description': 'description',
        },
        'edit_data': {
            'value': 'test-value-edit',
            'description': 'description changed',
        }
    },
    'service_categories': {
        'url': '/api/v2/service-categories/',
        'create_data': {
            'name': 'Sports',
            'description': '<p>My awesome category</p>'
        },
        'edit_data': {
            'name': 'Games',
            'description': '<p>All the games I like</p>'
        }
    },
    'services': {
        'url': '/api/v2/services/',
        'create_data': {
            "name": "Test service",
            "internal": False,
            "customer_facing": True,
            "other_required_services": "Other service",
            "other_related_services": "Related service",
            "related_platform": "Platform",
        },
        'create_data_2': {
            "name": "Test service 2",
            "internal": False,
            "customer_facing": True,
        },
        'edit_data': {
            "name": "Test service 2",
            "internal": True,
            "customer_facing": False,
            "other_required_services": "Other service2",
            "other_related_services": "Related service2",
            "related_platform": "Platform2",
        }
    },
    'service_admins': {
        'url': '/api/v2/service-admins/'
    },
    'components': {
        'url': '/api/v2/components/',
        'create_data': {
            'name': 'Paros',
            'description': '<p>Description</p>',
        },
        'edit_data': {
            'name': 'Antiparos',
            'description': '<p>Description 2</p>',
        },
    },
    'component-implementation-details': {
        'url': '/api/v2/component-implementation-details/',
    },
    'ext-components': {
        'url': '/api/v2/ext-component',
    },
    'service_versions': {
        'url': '/api/v2/service-versions/'
    },
    'providers': {
        'url': '/api/v2/providers/',
        'create_data': {
            'name': 'CIA',
            'description': '<p>Description</p>',
            'pd_bai_3_legal_status': "NPP",
            'pd_bai_3_legal_entity': False,
        },
        'edit_data': {
            'name': 'FBI',
            'pd_bai_3_legal_entity': True,
            'pd_bai_3_legal_status': "NPP"
        },
    },
    'access_policies': {
        'url': '/api/v2/access-policies/',
        'create_data': {
            'name': 'Excellence-driven',
            'geo_availability': 'Europe',
        },
        'edit_data': {
            'name': 'Market-driven',
        },
    },
    'federation_members': {
        'url': '/api/v2/federation-members/',
        'create_data': {
            'name': 'Federation Member',
            'country': 'FR',
            'webpage': 'https://example.com',
        },
        'edit_data': {
            'name': 'Federation Member modified',
        },
    },
}
