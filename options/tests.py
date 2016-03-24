from django.test import TestCase, Client
from django.test.client import RequestFactory
from common import helper, strings
import json

# Create your tests here.
class OptionsTestCase(TestCase):

    fixtures = ["test.json"]

    def setUp(self):
        self.factory = RequestFactory()
        self.client_stub = Client()
        self.maxDiff = None

    def test_get_service_options(self):
        response_name = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_options')
        response_uuid = self.client_stub.get('/api/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0/service_options/')

        data = {"service_options_list": {"count": 2, "service_options": [{"pricing": "Not specified yet", "SLA_link": {"related": {"href": "", "meta": {"desc": "A link to the SLA for this service."}}}, "description": "If we consider the DPM as part of the B2SAFE, then it would be more clear to define an explicit option which include it", "uuid": "0eb16991-f687-438e-9476-9ae45708d385", "name": "With Data Policy Manager"}, {"pricing": "Not specified yet", "SLA_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_options/sla/2ad2b14a-0874-44af-94be-e00093fc3e3c", "meta": {"desc": "A link to the SLA for this service."}}}, "description": "Standard options", "uuid": "61c31958-412f-43cf-be19-1f59ea89d0ee", "name": "Standard"}]}}
        expected_response = helper.get_response_info(strings.SERVICE_OPTIONS, data)

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)

    def test_get_service_options_invalid_version(self):
        response_name = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_details/5.0/service_options')
        response_uuid = self.client_stub.get('/api/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/12.0/service_options/')

        expected_response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)

    def test_get_service_options_invalid_url(self):
        response_name = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_details/5.0/service_optionsasdfasd/')
        response_uuid = self.client_stub.get('/api/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/12.0/service_optionsasdfsdfs/')

        expected_response = helper.page_not_found()

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)

    def test_get_service_options_sla(self):
        response_name = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_options/sla/2ad2b14a-0874-44af-94be-e00093fc3e3c/')
        response_uuid = self.client_stub.get('/api/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0/service_options/sla/2ad2b14a-0874-44af-94be-e00093fc3e3c/')

        data = {"parameters_list": {"count": 2, "parameters": [{"expression": "param", "SLA_parameter_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_options/sla/2ad2b14a-0874-44af-94be-e00093fc3e3c/sla_parameter/ce9da07f-4b48-4d64-9dcc-2aeb41cec177/parameter", "meta": {"desc": "A link to the SLA parameters."}}}, "type": "param", "id": "ce9da07f-4b48-4d64-9dcc-2aeb41cec177", "name": "param"}, {"expression": "Param 1", "SLA_parameter_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_options/sla/2ad2b14a-0874-44af-94be-e00093fc3e3c/sla_parameter/8ebdb0ca-fdeb-41d1-a2bd-d5abab31fb16/parameter", "meta": {"desc": "A link to the SLA parameters."}}}, "type": "Param 1", "id": "8ebdb0ca-fdeb-41d1-a2bd-d5abab31fb16", "name": "Param 1"}]}, "id": "2ad2b14a-0874-44af-94be-e00093fc3e3c", "name": "Test SLA"}
        expected_response = helper.get_response_info(strings.SLA_INFORMATION, data)

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)

    def test_get_service_options_sla_invalid_uuid(self):
        response_name = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_options/sla/ad0f70f4-4285-4072-a95c-57053f2as084/')
        response_uuid = self.client_stub.get('/api/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0/service_options/sla/ad0f70f4-4285-4072-a95c-57053f2as084/')

        expected_response = helper.get_error_response(strings.SLA_INVALID_UUID)

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)

    def test_get_service_options_sla_not_exits(self):
        response_name = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_options/sla/ad0f70f4-4285-4072-a95c-57053f2aa084/')
        response_uuid = self.client_stub.get('/api/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0/service_options/sla/ad0f70f4-4285-4072-a95c-57053f2aa084/')

        expected_response = helper.get_error_response(strings.SLA_NOT_FOUND)

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)

    def test_get_service_options_sla_parameter(self):
        response_name = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_options/sla/2ad2b14a-0874-44af-94be-e00093fc3e3c/sla_parameter/ce9da07f-4b48-4d64-9dcc-2aeb41cec177/parameter')
        response_uuid = self.client_stub.get('/api/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0/service_options/sla/2ad2b14a-0874-44af-94be-e00093fc3e3c/sla_parameter/ce9da07f-4b48-4d64-9dcc-2aeb41cec177/parameter')

        data = {"expression": "param", "SLA_parameter_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_options/sla/2ad2b14a-0874-44af-94be-e00093fc3e3c/sla_parameter/ce9da07f-4b48-4d64-9dcc-2aeb41cec177/parameter", "meta": {"desc": "A link to the SLA parameters."}}}, "type": "param", "id": "ce9da07f-4b48-4d64-9dcc-2aeb41cec177", "name": "param"}
        expected_response = helper.get_response_info(strings.SLA_PARAMETER_INFORMATION, data)

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)

    def test_get_service_options_sla_parameter_not_exists(self):
        response_name = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_options/sla/2ad2b14a-0874-44af-94be-e00093fc3e3c/sla_parameter/ce9da07f-4b48-4d64-9dcc-2aeb41cec277/parameter')
        response_uuid = self.client_stub.get('/api/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0/service_options/sla/2ad2b14a-0874-44af-94be-e00093fc3e3c/sla_parameter/ce9da07f-4b48-4d64-9dcc-2aeb41cec277/parameter')

        expected_response = helper.get_error_response(strings.SLA_PARAMETER_NOT_FOUND)

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)