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
def admin(django_user_model):
    user, created = \
        django_user_model.objects.get_or_create(username='admin',
                                                is_superuser=True)
    user.set_password('admin')
    user.save()

    credentials = {"username": 'admin', "password": 'admin'}
    client = ApimasClient()
    resp = client.post('/api/v2/auth/login/', credentials)
    token = resp.json().get('auth_token')
    client.set_token(token)
    return client
