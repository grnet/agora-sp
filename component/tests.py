from django.test import TestCase, Client
from django.test.client import RequestFactory
import json
# Create your tests here.


class ComponentTestCase(TestCase):

    fixtures = ["test.json"]


    def setUp(self):
        self.factory = RequestFactory()
        self.client_stub = Client()
        self.maxDiff = None


    def test_get_service_components_empty(self):
        response = self.client_stub.get('/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/')
        expected_response = {"status": "200 OK", "info": "service components information", "data": []}
        self.assertJSONEqual(json.dumps(expected_response), response.content)


    def test_get_service_components(self):
        response = self.client_stub.get('/v1/portfolio/services/B2HANDLE/service_details/0.1/service_components')
        expected_response = {"status": "200 OK", "info": "service components information", "data": [{"component_implementations": [{"description": "Some sample description", "component_implementation_details": [{"description": "Another boring description", "uuid": "edbab031-04de-4ac4-a03a-b899d683c9a9", "name": "Apps framework"}], "uuid": "5e27aa64-4668-464c-96c7-fbe5b4871219", "name": "App framework"}], "description": "Python/Django", "uuid": "3fa0bece-3e12-40ca-8345-1af82bf5f471", "name": "Application framework"}]}
        self.assertJSONEqual(json.dumps(expected_response), response.content)


    def test_get_service_component_implementations(self):
        response = self.client_stub.get('/v1/portfolio/services/B2HANDLE/service_details/0.1/service_components/3fa0bece-3e12-40ca-8345-1af82bf5f471/service_component_implementations')
        expected_response = {"status": "200 OK", "info": "service component implementation information", "data": [{"description": "Some sample description", "component_implementation_details": [{"description": "Another boring description", "uuid": "edbab031-04de-4ac4-a03a-b899d683c9a9", "name": "Apps framework"}], "uuid": "5e27aa64-4668-464c-96c7-fbe5b4871219", "name": "App framework"}]}
        self.assertJSONEqual(json.dumps(expected_response), response.content)


    def test_get_service_component_implementations_nonmatching_uuid(self):
        response = self.client_stub.get('/v1/portfolio/services/B2HANDLE/service_details/0.1/service_components/3fa0bece-3e13-40ca-8345-1af82bf5f471/service_component_implementations')
        expected_response = {"status": "404 Not Found", "errors": {"detail": "A service component matching the specified service version does not exists"}}
        self.assertJSONEqual(json.dumps(expected_response), response.content)


    def test_get_service_component_implementation_invalid_uuid(self):
        response = self.client_stub.get('/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/3fa0bece-3e12-40ca-8345-1af82bf5f47/service_component_implementations')
        expected_response = {"status": "404 Not Found", "errors": {"detail": "An invalid service component UUID was supplied"}}
        self.assertJSONEqual(json.dumps(expected_response), response.content)


    def test_get_service_component_implementations_detail(self):
        response = self.client_stub.get('/v1/portfolio/services/B2HANDLE/service_details/0.1/service_components/3fa0bece-3e12-40ca-8345-1af82bf5f471/service_component_implementations/5e27aa64-4668-464c-96c7-fbe5b4871219/service_component_implementation_detail')
        expected_response = {"status": "200 OK", "info": "service component implementation detail", "data": [{"description": "Another boring description", "uuid": "edbab031-04de-4ac4-a03a-b899d683c9a9", "name": "Apps framework"}]}
        self.assertJSONEqual(json.dumps(expected_response), response.content)


    def test_get_service_component_implementations_detail_nonmatching_uuid(self):
        response = self.client_stub.get('/v1/portfolio/services/B2HANDLE/service_details/0.1/service_components/2fa0bece-3e12-40ca-8345-1af82bf5f471/service_component_implementations/5e27aa64-4668-464c-96c7-fbe5b4871219/service_component_implementation_detail')
        expected_response = {"status": "404 Not Found", "errors": {"detail": "A service component matching the specified service version does not exists"}}
        self.assertJSONEqual(json.dumps(expected_response), response.content)


    def test_get_service_component_implementations_detail_invalid_uuid(self):
        response = self.client_stub.get('/v1/portfolio/services/B2HANDLE/service_details/0.1/service_components/fa0bece-3e12-40ca-8345-1af82bf5f471/service_component_implementations/5e27aa64-4668-464c-96c7-fbe5b4871219/service_component_implementation_detail')
        expected_response = {"status": "404 Not Found", "errors": {"detail": "An invalid service component UUID was supplied"}}
        self.assertJSONEqual(json.dumps(expected_response), response.content)
        response = self.client_stub.get('/v1/portfolio/services/B2HANDLE/service_details/0.1/service_components/2fa0bece-3e12-40ca-8345-1af82bf5f471/service_component_implementations/e27aa64-4668-464c-96c7-fbe5b4871219/service_component_implementation_detail')
        expected_response = {"status": "404 Not Found", "errors": {"detail": "An invalid service component implementation UUID was supplied"}}
        self.assertJSONEqual(json.dumps(expected_response), response.content)


