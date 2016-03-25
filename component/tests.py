from django.test import TestCase, Client
from django.test.client import RequestFactory
import json
from common import helper, strings
# Create your tests here.


class ComponentTestCase(TestCase):

    fixtures = ["test.json"]

    def setUp(self):
        self.factory = RequestFactory()
        self.client_stub = Client()
        self.maxDiff = None

    def test_get_service_components_empty(self):
        response = self.client_stub.get('/api/v1/portfolio/services/583ec8f2-9ef6-4e51-89bd-9af7f5fcea9c/service_details/1.0/service_components/')
        data = {"service_components_list": {"count": 0, "service_components": []}}
        expected_response = helper.get_response_info(strings.SERVICE_COMPONENTS_INFORMATION, data)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_service_components(self):
        response = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components')
        data =  {"service_components_list": {"count": 2, "service_components": [{"description": "Pero", "component_implementation_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/service_component_implementations", "meta": {"desc": "Link to the concrete service component implementations."}}}, "uuid": "af2f812b-eda6-497a-9d22-534f885b7034", "name": "Komponenta 1"}, {"description": "Python/Django", "component_implementation_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/3fa0bece-3e12-40ca-8345-1af82bf5f471/service_component_implementations", "meta": {"desc": "Link to the concrete service component implementations."}}}, "uuid": "3fa0bece-3e12-40ca-8345-1af82bf5f471", "name": "Application framework"}]}}
        expected_response = helper.get_response_info(strings.SERVICE_COMPONENTS_INFORMATION, data)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_service_component_implementations(self):
        response = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/service_component_implementations')
        data = {"service_component_implementations_list": {"count": 2, "service_component_implementations": [{"component_implementation_details_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/service_component_implementations/d01dcee5-eb04-4147-9bb0-54ed81567494/service_component_implementation_detail", "meta": {"desc": "Link to the concrete service component implementation details."}}}, "description": "Nesto", "uuid": "d01dcee5-eb04-4147-9bb0-54ed81567494", "name": "Implementacija 2"}, {"component_implementation_details_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/service_component_implementations/bac1cb25-f24e-4cea-a2e8-d94b27a2e169/service_component_implementation_detail", "meta": {"desc": "Link to the concrete service component implementation details."}}}, "description": "asdfasd", "uuid": "bac1cb25-f24e-4cea-a2e8-d94b27a2e169", "name": "Implementacija 1"}]}}
        expected_response = helper.get_response_info(strings.SERVICE_COMPONENT_IMPLEMENTATIONS_INFORMATION, data)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_service_component_implementations_nonmatching_uuid(self):
        response = self.client_stub.get('/api/v1/portfolio/services/B2HANDLE/service_details/0.1/service_components/3fa0bece-3e13-40ca-8345-1af82bf5f471/service_component_implementations')
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENTS_IMPLEMENTATION_NONMATCHING_UUID)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_service_component_implementation_invalid_uuid(self):
        response = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/3fa0bece-3e12-40ca-8345-1af82bf5f47/service_component_implementations')
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_INVALID_UUID)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_service_component_implementations_detail(self):
        response = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/service_component_implementations/d01dcee5-eb04-4147-9bb0-54ed81567494/service_component_implementation_detail')
        data = {"service_component_implementation_details_list": {"count": 1, "service_component_implementation_details": [{"version": "4", "uuid": "a1b4569c-b7eb-4881-9f93-2e37ee662c28", "configuration_parameters": "d"}]}}
        expected_response = helper.get_response_info(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS, data)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_service_component_implementations_detail_nonmatching_uuid(self):
        response = self.client_stub.get('/api/v1/portfolio/services/B2HANDLE/service_details/0.1/service_components/2fa0bece-3e12-40ca-8345-1af82bf5f471/service_component_implementations/5e27aa64-4668-464c-96c7-fbe5b4871219/service_component_implementation_detail')
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENTS_IMPLEMENTATION_NONMATCHING_UUID)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_service_component_implementations_detail_invalid_uuid(self):
        response = self.client_stub.get('/api/v1/portfolio/services/B2HANDLE/service_details/0.1/service_components/fa0bece-3e12-40ca-8345-1af82bf5f471/service_component_implementations/5e27aa64-4668-464c-96c7-fbe5b4871219/service_component_implementation_detail')
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_INVALID_UUID)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

        response = self.client_stub.get('/api/v1/portfolio/services/B2HANDLE/service_details/0.1/service_components/2fa0bece-3e12-40ca-8345-1af82bf5f471/service_component_implementations/e27aa64-4668-464c-96c7-fbe5b4871219/service_component_implementation_detail')
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_INVALID_UUID)
        self.assertJSONEqual(json.dumps(expected_response), response.content)
