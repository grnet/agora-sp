from django.test import TestCase, Client
from django.test.client import RequestFactory
from common import helper, strings
import json


# Create your tests here.
class OwnerTestCase(TestCase):

    fixtures = ["test.json"]

    def setUp(self):
        self.factory = RequestFactory()
        self.client_stub = Client()
        self.maxDiff = None

    def test_service_owner(self):
        response_name = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_owner')
        response_uuid = self.client_stub.get('/api/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_owner')

        data = {"first_name": "Claudio", "last_name": "Cacciari", "uuid": "a9976cd2-14e4-47b7-9353-7e9faba2f200", "email": "c.cacciari@cineca.it", "phone": "000", "institution": {"department": "Admin", "country": "ITALY", "address": "A", "uuid": "df3ab1f3-08d3-408a-bf00-532a41ccffa4", "name": "CINECA"}}
        expected_response = helper.get_response_info(strings.SERVICE_OWNER_INFORMATION, data)

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)

    def test_service_owner_institution(self):

        response_name = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_owner/Claudio_Cacciari/institution')
        response_uuid = self.client_stub.get('/api/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_owner/a9976cd2-14e4-47b7-9353-7e9faba2f200/institution')

        data = {
            "department": "Admin",
            "country": "ITALY",
            "address": "A",
            "uuid": "df3ab1f3-08d3-408a-bf00-532a41ccffa4",
            "name": "CINECA"
        }

        expected_response = helper.get_response_info(strings.SERVICE_OWNER_INSTITUTION, data)

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)

    def test_service_invalid_owner_institution(self):

        response_name = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_owner/Claudia_Cacciari/institution')
        response_uuid = self.client_stub.get('/api/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_owner/a9976cd2-14e4-47b7-9363-7e9faba2f200/institution')

        expected_response = helper.get_error_response(strings.OWNER_NOT_FOUND)

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)
