from agora.testing import *

def test_user_roles(admin, client):
    assert admin.get('/api/v2/user-roles/').json() == []
