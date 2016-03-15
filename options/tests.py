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


    def test_get_service_options_invalid_url(self):
        response_name = self.client_stub.get('/v1/portfolio/services/B2SAFE/service_details/5.0/service_optionsasdfasd/')
        response_uuid = self.client_stub.get('/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/12.0/service_optionsasdfsdfs/')

        expected_response =  {"status": "404 Page not found", "errors": {"detail": "The requested page was not found"}}


        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)


    def test_get_service_options_sla(self):
        response_name = self.client_stub.get('/v1/portfolio/services/B2SAFE/service_details/3.0/service_options/sla/ad0f70f4-4285-4072-a95c-57053f2ac084/')
        response_uuid = self.client_stub.get('/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0/service_options/sla/ad0f70f4-4285-4072-a95c-57053f2ac084/')

        expected_response = {"status": "200 OK",
                             "info": "service SLA information",
                             "data": {
                                 "id": "ad0f70f4-4285-4072-a95c-57053f2ac084",
                                 "name": "Test SLA"
                             }}

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)


    def test_get_service_options_sla_invalid_uuid(self):
        response_name = self.client_stub.get('/v1/portfolio/services/B2SAFE/service_details/3.0/service_options/sla/ad0f70f4-4285-4072-a95c-57053f2as084/')
        response_uuid = self.client_stub.get('/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0/service_options/sla/ad0f70f4-4285-4072-a95c-57053f2as084/')

        expected_response = {"status": "404 Not Found",
                             "errors": {
                                 "detail": "An invalid service sla UUID was supplied"
                             }}

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)


    def test_get_service_options_sla_not_exits(self):
        response_name = self.client_stub.get('/v1/portfolio/services/B2SAFE/service_details/3.0/service_options/sla/ad0f70f4-4285-4072-a95c-57053f2aa084/')
        response_uuid = self.client_stub.get('/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0/service_options/sla/ad0f70f4-4285-4072-a95c-57053f2aa084/')

        expected_response = {"status": "404 Not Found",
                             "errors": {
                                 "detail": "The requested SLA object was not found"
                             }}

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)


    def test_get_service_options_sla_parameter(self):
        response_name = self.client_stub.get('/v1/portfolio/services/B2SAFE/service_details/3.0/service_options/sla/ad0f70f4-4285-4072-a95c-57053f2ac084/sla_parameter/ce9da07f-4b48-4d64-9dcc-2aeb41cec177/parameter')
        response_uuid = self.client_stub.get('/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0/service_options/sla/ad0f70f4-4285-4072-a95c-57053f2ac084/sla_parameter/ce9da07f-4b48-4d64-9dcc-2aeb41cec177/parameter')

        expected_response = {"status": "200 OK",
                             "info": "service SLA paramter information",
                             "data": {
                                 "expression": "param",
                                 "type": "param",
                                 "id": "ce9da07f-4b48-4d64-9dcc-2aeb41cec177",
                                 "name": "param"}}

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)


    def test_get_service_options_sla_parameter_not_exists(self):
        response_name = self.client_stub.get('/v1/portfolio/services/B2SAFE/service_details/3.0/service_options/sla/ad0f70f4-4285-4072-a95c-57053f2ac084/sla_parameter/ce9da07f-4b48-4d64-9dcc-2aeb41cec277/parameter')
        response_uuid = self.client_stub.get('/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0/service_options/sla/ad0f70f4-4285-4072-a95c-57053f2ac084/sla_parameter/ce9da07f-4b48-4d64-9dcc-2aeb41cec277/parameter')

        expected_response = {"status": "404 Not Found",
                             "errors": {
                                 "detail": "The requested SLA parameter does not belong to the specified service"
                             }}

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)