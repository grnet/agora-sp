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

    def test_insert_service_component_no_name(self):
        post_data = {}
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/insert_component", post_data)

        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_NAME_NOT_PROVIDED, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_empty_name(self):
        post_data = {
            "name": "",
            "description": ""
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/insert_component", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_NAME_EMPTY, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_invalid_uuid(self):
        post_data = {
            "name": "Test name",
            "description": "Test description",
            "uuid": "af2f812b-eda6-497a-9d22-534f885b703G"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/insert_component", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_INVALID_UUID, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_existing_uuid(self):
        post_data = {
            "name": "Test name",
            "description": "Test description",
            "uuid": "56601d76-c1e2-488c-a812-dba8e5508c29"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/insert_component", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_UUID_EXISTS, status=strings.CONFLICT_409)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component(self):
        post_data = {
            "name": "Test name",
            "description": "Test description"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/insert_component", post_data)
        expected_response = helper.get_response_info(strings.SERVICE_COMPONENT_INSERTED, {}, status=strings.CREATED_201)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_with_uuid(self):
        post_data = {
            "name": "Test name",
            "description": "Test description",
            "uuid": "56601d76-c1e2-488c-a812-dba8e5508c2e"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/insert_component", post_data)
        expected_response = helper.get_response_info(strings.SERVICE_COMPONENT_INSERTED, {}, status=strings.CREATED_201)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_no_name(self):
        post_data = {}
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/insert_service_component_implementation", post_data)

        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_NAME_NOT_PROVIDED, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_empty_name(self):
        post_data = {
            "name": "",
            "description": ""
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/insert_service_component_implementation", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_NAME_EMPTY, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_invalid_comp_uuid(self):
        post_data = {
            "name": "Test name",
            "description": ""
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b703g/insert_service_component_implementation", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_INVALID_UUID, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_non_existing_comp_uuid(self):
        post_data = {
            "name": "Test name",
            "description": ""
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7031/insert_service_component_implementation", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_NOT_FOUND, status=strings.NOT_FOUND_404)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_invalid_uuid(self):
        post_data = {
            "name": "Test name",
            "description": "Test description",
            "uuid": "af2f812b-eda6-497a-9d22-534f885b703G"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/insert_service_component_implementation", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_INVALID_UUID, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_existing_uuid(self):
        post_data = {
            "name": "Test name",
            "description": "Test description",
            "uuid": "5e27aa64-4668-464c-96c7-fbe5b4871219"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/insert_service_component_implementation", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_UUID_EXISTS, status=strings.CONFLICT_409)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation(self):
        post_data = {
            "name": "Test name",
            "description": "Test description"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/insert_service_component_implementation", post_data)
        expected_response = helper.get_response_info(strings.SERVICE_COMPONENT_IMPLEMENTATION_INSERTED, {}, status=strings.CREATED_201)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_with_uuid(self):
        post_data = {
            "name": "Test name",
            "description": "Test description",
            "uuid": "56601d76-c1e2-488c-a812-dba8e5508c2e"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/insert_service_component_implementation", post_data)
        expected_response = helper.get_response_info(strings.SERVICE_COMPONENT_IMPLEMENTATION_INSERTED, {}, status=strings.CREATED_201)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_details_no_version(self):
        post_data = {}
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/service_component_implementations/d01dcee5-eb04-4147-9bb0-54ed81567494/insert_service_component_implementation_detail", post_data)

        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_VERSION_NOT_PROVIDED, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_details_empty_version(self):
        post_data = {
            "version": "",
            "configuration_parameters": ""
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/service_component_implementations/d01dcee5-eb04-4147-9bb0-54ed81567494/insert_service_component_implementation_detail", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_VERSION_EMPTY, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_details_invalid_comp_uuid(self):
        post_data = {
            "version": "0.1.2",
            "configuration_parameters": ""
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b703G/service_component_implementations/d01dcee5-eb04-4147-9bb0-54ed81567494/insert_service_component_implementation_detail", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_INVALID_UUID, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_details_non_existing_comp_uuid(self):
        post_data = {
            "version": "0.1.2",
            "configuration_parameters": ""
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7032/service_component_implementations/d01dcee5-eb04-4147-9bb0-54ed81567494/insert_service_component_implementation_detail", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_NOT_FOUND, status=strings.NOT_FOUND_404)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_details_invalid_comp_imp_uuid(self):
        post_data = {
            "version": "0.1.2",
            "configuration_parameters": "<xml>Test configuration</xml>"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/service_component_implementations/V01dcee5-eb04-4147-9bb0-54ed81567494/insert_service_component_implementation_detail", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_INVALID_UUID, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_details_non_existing_comp_imp_uuid(self):
        post_data = {
            "version": "0.1.2",
            "configuration_parameters": "<xml>Test configuration</xml>"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/service_component_implementations/e01dcee5-eb04-4147-9bb0-54ed81567494/insert_service_component_implementation_detail", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_NOT_FOUND, status=strings.NOT_FOUND_404)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_details_invalid_uuid(self):
        post_data = {
            "version": "0.1.2",
            "configuration_parameters": "<xml>Test configuration</xml>",
            "uuid": "af2f812b-eda6-497a-9d22-534f885b703G"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/service_component_implementations/d01dcee5-eb04-4147-9bb0-54ed81567494/insert_service_component_implementation_detail", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_INVALID_UUID, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_details_existing_uuid(self):
        post_data = {
            "version": "0.1.2",
            "configuration_parameters": "<xml>Test configuration</xml>",
            "uuid": "309ffba9-dc3f-45c5-8a2e-150cd2e62c92"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/service_component_implementations/d01dcee5-eb04-4147-9bb0-54ed81567494/insert_service_component_implementation_detail", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_EXISTS, status=strings.CONFLICT_409)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_details(self):
        post_data = {
            "version": "0.1.2",
            "configuration_parameters": "<xml>Test configuration</xml>"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/service_component_implementations/d01dcee5-eb04-4147-9bb0-54ed81567494/insert_service_component_implementation_detail", post_data)
        expected_response = helper.get_response_info(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_INSERTED, {}, status=strings.CREATED_201)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_component_implementation_details_with_uuid(self):
        post_data = {
            "version": "0.1.2",
            "configuration_parameters": "<xml>Test configuration</xml>",
            "uuid": "56601d76-c1e2-488c-a812-dba8e5508c2e"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/af2f812b-eda6-497a-9d22-534f885b7034/service_component_implementations/d01dcee5-eb04-4147-9bb0-54ed81567494/insert_service_component_implementation_detail", post_data)
        expected_response = helper.get_response_info(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_INSERTED, {}, status=strings.CREATED_201)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_details_component_no_uuid(self):
        post_data = {}
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/insert_service_details_component_implementation_details", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_UUID_NOT_PROVIDED, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_details_component_invalid_uuid(self):
        post_data = {
            "component_implementation_details_uuid": "af2f812b-eda6-497a-9d22-534f885b703G"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/insert_service_details_component_implementation_details", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAIL_INVALID_UUID, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_details_component_non_existing_comp_imp_det(self):
        post_data = {
            "component_implementation_details_uuid": "af2f812b-eda6-497a-9d22-534f885b7032"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/insert_service_details_component_implementation_details", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_COMPONENT_IMPLEMENTATION_DETAILS_NOT_FOUND, strings.NOT_FOUND_404)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_details_component_existing_record(self):
        post_data = {
            "component_implementation_details_uuid": "a1b4569c-b7eb-4881-9f93-2e37ee662c28"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/insert_service_details_component_implementation_details", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_DETAILS_COMPONENT_EXISTS, strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_details_component(self):
        post_data = {
            "component_implementation_details_uuid": "309ffba9-dc3f-45c5-8a2e-150cd2e62c92"
        }
        response = self.client_stub.post("/api/v1/portfolio/services/B2SAFE/service_details/3.0/service_components/insert_service_details_component_implementation_details", post_data)
        expected_response = helper.get_response_info(strings.SERVICE_DETAILS_COMPONENT_INSERTED, {}, status=strings.OK_200)
        self.assertJSONEqual(json.dumps(expected_response), response.content)








