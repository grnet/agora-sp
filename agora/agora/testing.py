import pytest
from django.test import Client
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
def provideradmin(django_user_model):
    return create_client(django_user_model,
                         'provideradmin',
                         'provideradmin@test.org',
                         'provideradmin')


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



RESOURCES_CRUD = {
    'target_users': {
        'url': '/api/v2/target-users/',
        'create_data': {
            'user': 'Manager',
            'description': 'Cool manager'
        },
        'edit_data': {
            'user': 'Boss',
            'description': 'Even better boss'
        }
    },
    'resource_admins': {
      'url': '/api/v2/resource-admins/',
    },
    'resources': {
        'url': '/api/v2/resources/',
        'create_data': {
            'erp_bai_0_id': 'aw',
            'erp_bai_1_name': 'Athens Warriors1',
            'erp_bai_4_webpage': 'www.test.com',
            'erp_gla_1_geographical_availability': 'Europe'
        },
        'edit_data': {
            'erp_gla_1_geographical_availability': 'Africa'
        },
    },
    'providers': {
        'url': '/api/v2/providers/',
        'create_data': {
            'epp_bai_id': 'id',
            'epp_bai_name': 'epp_name',
            'epp_bai_abbreviation': 'epp_abb',
            'epp_bai_website': 'epp_website',
            'epp_bai_legal_entity': False,
            'epp_loi_1_street_name_and_number': 'Kings Cross 7',
            'epp_loi_2_postal_code': '938393',
            'epp_loi_3_city': 'London',
            'epp_loi_4_region': 'Greater London',
            'epp_loi_5_country_or_territory': 'United Kingdom',
            'epp_mri_1_description': '<p>short provider description</p>',
            'epp_mri_2_logo': 'https://example.com/provider.png',
            'epp_mri_3_multimedia': 'https://vimeo.com/1001010938',
            'epp_mti_1_life_cycle_status': 'Operational',
            'epp_mti_2_certifications': 'ISO-27001'
        },
        'edit_data': {
            'epp_bai_id': 'id',
            'epp_bai_name': 'epp_name',
            'epp_bai_abbreviation': 'epp_abb',
            'epp_bai_website': 'epp_website',
            'epp_bai_legal_entity': False,
            'epp_loi_1_street_name_and_number': 'Kings Cross 17',
            'epp_loi_2_postal_code': '538393',
            'epp_loi_3_city': 'London',
            'epp_loi_4_region': 'Major London',
            'epp_loi_5_country_or_territory': 'Great Britain',
            'epp_mri_1_description': '<p>short provider description</p>',
            'epp_mri_2_logo': 'https://example.com/provider.png',
            'epp_mri_3_multimedia': 'https://vimeo.com/1001010938',
            'epp_mti_1_life_cycle_status': 'Operational',
            'epp_mti_2_certifications': 'ISO-27001'
        },
    },
    'access_modes': {
        'url': '/api/v2/access-modes/',
        'create_data': {
          'name': 'Name',
          'description': 'Description',
        },
        'edit_data': {
          'name': 'Name2',
          'description': 'Description2',
        }
    },
    'domains': {
        'url': '/api/v2/domains/',
        'create_data': {
          'name': 'Name',
        },
        'edit_data': {
          'name': 'Name2',
        }
    },
}
