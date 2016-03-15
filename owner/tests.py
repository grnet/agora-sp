from django.test import TestCase, Client
from django.test.client import RequestFactory

import json

# Create your tests here.
class OwnerTestCase(TestCase):


    fixtures = ["test.json"]


    def setUp(self):
        self.factory = RequestFactory()
        self.client_stub = Client()
        self.maxDiff = None


    def test_service_owner(self):
        response_name = self.client_stub.get('/v1/portfolio/services/B2SAFE/service_owner')
        response_uuid = self.client_stub.get('/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_owner')


        expected_response = {
            "status": "200 OK",
            "info": "service owner information",
            "data": {
                "phone": "000",
                "first_name": "Claudio",
                "last_name": "Cacciari",
                "uuid": "a9976cd2-14e4-47b7-9353-7e9faba2f200",
                "email": "c.cacciari@cineca.it"
            }}

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)


    def test_service_owner_institution(self):

        response_name = self.client_stub.get('/v1/portfolio/services/B2SAFE/service_owner/Claudio_Cacciari/institution')
        response_uuid = self.client_stub.get('/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_owner/a9976cd2-14e4-47b7-9353-7e9faba2f200/institution')


        expected_response = {
            "status": "200 OK",
            "info": "service owner institution information",
            "data": {
                "department": "Admin",
                "country": "ITALY",
                "address": "A",
                "uuid": "df3ab1f3-08d3-408a-bf00-532a41ccffa4",
                "name": "CINECA"}}

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)


    def test_service_invlaid_owner_institution(self):

        response_name = self.client_stub.get('/v1/portfolio/services/B2SAFE/service_owner/Claudia_Cacciari/institution')
        response_uuid = self.client_stub.get('/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_owner/a9976cd2-14e4-47b7-9363-7e9faba2f200/institution')


        expected_response = {
            "status": "404 Not Found",
            "errors": {"detail": "The requested service owner was not found"}
        }

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)