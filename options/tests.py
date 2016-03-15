from django.test import TestCase, Client
from django.test.client import RequestFactory
import json

# Create your tests here.
class OptionsTestCase(TestCase):


    fixtures = ["test.json"]


    def setUp(self):
        self.factory = RequestFactory()
        self.client_stub = Client()
        self.maxDiff = None


    def test_get_service_options(self):
        response_name = self.client_stub.get('/v1/portfolio/services/B2SAFE/service_details/3.0/service_options')
        response_uuid = self.client_stub.get('/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0/service_options/')


        expected_response ={
            "status": "200 OK",
            "info": "options for service detail information",
            "data": {
                "service_option_description": "If we consider the DPM as part of the B2SAFE, then it would be "
                                              "more clear to define an explicit option which include it",
                "version": "3.0",
                "service_option_name": "With Data Policy Manager",
                "service_option_pricing": "Not specified yet",
                "service_name": "B2SAFE",
                "service_option_id": "0eb16991-f687-438e-9476-9ae45708d385",
                "service_id": "88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a",
                "service_details_id": "aa37cd70-c3e3-4334-a719-d467c22aed81"
            }}

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)


    def test_get_service_options_invalid_version(self):
        response_name = self.client_stub.get('/v1/portfolio/services/B2SAFE/service_details/5.0/service_options')
        response_uuid = self.client_stub.get('/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/12.0/service_options/')

        expected_response = {"status": "404 Not Found",
                             "errors":
                                 {"detail": "Service details with that version not found"}
                             }

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)