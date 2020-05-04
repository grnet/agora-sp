import json
from django.test import Client
from agora.testing import superadmin, RESOURCES_CRUD


# def test_name_trim(superadmin):
    # """
    # Test that Service 'name' field is trimmed before the model is saved.
    # """
    # url = RESOURCES_CRUD['services']['url']
    # data = {
        # "internal": False,
        # "customer_facing": True,
    # }

    # data.update(name='ice hockey')
    # superadmin.post(url, data)
    # assert superadmin.get(url).json()[0]['name'] == 'ice hockey'

    # data.update(name='table tennis ')
    # superadmin.post(url, data)
    # assert superadmin.get(url).json()[1]['name'] == 'table tennis'

    # data.update({'name': ' ski'})
    # superadmin.post(url, data)
    # assert superadmin.get(url).json()[2]['name'] == 'ski'
