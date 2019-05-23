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

        data =  {"first_name": "Claudio", "last_name": "Cacciari", "uuid": "a9976cd2-14e4-47b7-9353-7e9faba2f200", "email": "c.cacciari@cineca.it", "phone": "000", "institution": {"department": "Admin", "country": "ITALY", "address": "A", "uuid": "df3ab1f3-08d3-408a-bf00-532a41ccffa4", "name": "CINECA"}, "account_id": None}
        expected_response = helper.get_response_info(strings.SERVICE_OWNER_INFORMATION, data)

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)

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

    def test_insert_institution(self):

        post_data = {
            "name": "Test name",
            "address": "Test address",
            "country": "Test country",
            "department": "Test department",
            "uuid": "72eee88a-aaa4-4d7b-86a4-4124e3a9d99d"
        }

        response = self.client_stub.post("/api/v1/owner/institution/add", post_data)
        expected_data = {
            "name": post_data["name"],
            "address": post_data["address"],
            "country": post_data["country"],
            "department": post_data["department"],
            "uuid": post_data["uuid"]
        }

        expected_response = helper.get_response_info(strings.INSTITUTION_INSERTED, expected_data, status=strings.CREATED_201)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_existing_institution(self):

        post_data = {
            "name": "Test name",
            "address": "Test address",
            "country": "Test country",
            "department": "Test department",
            "uuid": "72eee88a-aaa4-4d7b-86a4-4124e3a9d99c"
        }

        response = self.client_stub.post("/api/v1/owner/institution/add", post_data)
        expected_response = helper.get_error_response(strings.INSTITUTION_UUID_EXISTS, strings.CONFLICT_409)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_non_existing_institution(self):

        post_data = {
            "name": "Test name",
            "address": "Test address",
            "country": "Test country",
            "department": "Test department",
            "uuid": "72eee88a-aaa4-4d7b-86a4-4124e3a9d99d"
        }

        response = self.client_stub.post("/api/v1/owner/institution/edit", post_data)
        expected_response = helper.get_error_response(strings.INSTITUTION_NOT_FOUND, strings.NOT_FOUND_404)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_institution_no_uuid(self):

        post_data = {
            "name": "Test name",
            "address": "Test address",
            "country": "Test country",
            "department": "Test department"
        }

        response = self.client_stub.post("/api/v1/owner/institution/edit", post_data)
        expected_response = helper.get_error_response(strings.INSTITUTION_UUID_NOT_PROVIDED, strings.REJECTED_406)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_institution(self):

        post_data = {
            "name": "Test name",
            "address": "Test address",
            "country": "Test country",
            "department": "Test department",
            "uuid": "56da9c1f-1842-4158-8dfd-e2d2d01ace08"
        }

        response = self.client_stub.post("/api/v1/owner/institution/edit", post_data)
        expected_data = {
            "name": post_data["name"],
            "address": post_data["address"],
            "country": post_data["country"],
            "department": post_data["department"],
            "uuid": post_data["uuid"]
        }

        expected_response = helper.get_response_info(strings.INSTITUTION_UPDATED, expected_data, status=strings.UPDATED_202)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_contact(self):

        post_data = {
            "first_name": "Test first name",
            "last_name": "Test last name",
            "email": "Test email",
            "phone": "Test phone",
            "url": "Test url",
            "uuid": "73eee88a-aaa4-4d7b-86a4-4124e3a9d99d"
        }

        response = self.client_stub.post("/api/v1/owner/contact_information/add", post_data)
        expected_data = {
            "first_name": post_data["first_name"],
            "last_name": post_data["last_name"],
            "email": post_data["email"],
            "phone": post_data["phone"],
            "uuid": post_data["uuid"]
        }

        expected_response = helper.get_response_info(strings.CONTACT_INFORMATION_INSERTED, expected_data, status=strings.CREATED_201)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_existing_contact(self):

        post_data = {
            "first_name": "Test first name",
            "last_name": "Test last name",
            "email": "Test email",
            "phone": "Test phone",
            "url": "Test url",
            "uuid": "7166dfad-082b-4e81-bf86-cae10af12cfd"
        }

        response = self.client_stub.post("/api/v1/owner/contact_information/add", post_data)
        expected_response = helper.get_error_response(strings.CONTACT_INFORMATION_UUID_EXISTS, strings.CONFLICT_409)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_non_existing_contact(self):

        post_data = {
            "first_name": "Test first name",
            "last_name": "Test last name",
            "email": "Test email",
            "phone": "Test phone",
            "url": "Test url",
            "uuid": "7166dfad-082b-4e81-bf86-cae10af12cfc"
        }

        response = self.client_stub.post("/api/v1/owner/contact_information/edit", post_data)
        expected_response = helper.get_error_response(strings.CONTACT_INFORMATION_NOT_FOUND, strings.NOT_FOUND_404)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_contact_no_uuid(self):

        post_data = {
            "first_name": "Test first name",
            "last_name": "Test last name",
            "email": "Test email",
            "phone": "Test phone",
            "url": "Test url"
        }

        response = self.client_stub.post("/api/v1/owner/contact_information/edit", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_CONTACT_INFORMATION_UUID_NOT_PROVIDED, strings.REJECTED_406)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_contact(self):

        post_data = {
            "first_name": "Test first name",
            "last_name": "Test last name",
            "email": "Test email",
            "phone": "Test phone",
            "url": "Test url",
            "uuid": "7166dfad-082b-4e81-bf86-cae10af12cfd"
        }

        response = self.client_stub.post("/api/v1/owner/contact_information/edit", post_data)
        expected_data = {
            "first_name": post_data["first_name"],
            "last_name": post_data["last_name"],
            "email": post_data["email"],
            "phone": post_data["phone"],
            "uuid": post_data["uuid"]
        }

        expected_response = helper.get_response_info(strings.CONTACT_INFORMATION_UPDATED, expected_data, status=strings.UPDATED_202)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_owner(self):

        post_data = {
            "first_name": "Test first name",
            "last_name": "Test last name",
            "email": "Test email",
            "phone": "Test phone",
            "institution_uuid": "224fe496-5023-49e6-8953-19d5b1331333",
            "uuid": "53eee88a-aaa4-4d7b-86a4-4124e3a9d99d"
        }

        response = self.client_stub.post("/api/v1/owner/add", post_data)
        expected_data = {
            "account_id": None,
            "first_name": post_data["first_name"],
            "last_name": post_data["last_name"],
            "email": post_data["email"],
            "phone": post_data["phone"],
            "institution": {
                "name": "GRNET",
                "address": "Mesogeon av.",
                "country": "GREECE",
                "department": "Admin",
                "uuid": "224fe496-5023-49e6-8953-19d5b1331333"
            },
            "uuid": post_data["uuid"]
        }

        expected_response = helper.get_response_info(strings.SERVICE_OWNER_INSERTED, expected_data, status=strings.CREATED_201)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_existing_owner(self):

        post_data = {
            "first_name": "Test first name",
            "last_name": "Test last name",
            "email": "Test email",
            "phone": "Test phone",
            "institution_uuid": "224fe496-5023-49e6-8953-19d5b1331333",
            "uuid": "a9976cd2-14e4-47b7-9353-7e9faba2f200"
        }

        response = self.client_stub.post("/api/v1/owner/add", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_OWNER_UUID_EXISTS, strings.CONFLICT_409)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_non_existing_owner(self):

        post_data = {
            "first_name": "Test first name",
            "last_name": "Test last name",
            "email": "Test email",
            "phone": "Test phone",
            "institution_uuid": "224fe496-5023-49e6-8953-19d5b1331333",
            "uuid": "a9976cd2-14e4-47b7-9353-7e9faba2f20d"
        }

        response = self.client_stub.post("/api/v1/owner/edit", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_OWNER_NOT_FOUND, strings.NOT_FOUND_404)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_owner_no_uuid(self):

        post_data = {
            "first_name": "Test first name",
            "last_name": "Test last name",
            "email": "Test email",
            "phone": "Test phone",
            "institution_uuid": "224fe496-5023-49e6-8953-19d5b1331333"
        }

        response = self.client_stub.post("/api/v1/owner/edit", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_OWNER_UUID_NOT_PROVIDED, strings.REJECTED_406)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_owner(self):

        post_data = {
            "first_name": "Test first name",
            "last_name": "Test last name",
            "email": "Test email",
            "phone": "Test phone",
            "institution_uuid": "224fe496-5023-49e6-8953-19d5b1331333",
            "uuid": "a9976cd2-14e4-47b7-9353-7e9faba2f200"
        }

        response = self.client_stub.post("/api/v1/owner/edit", post_data)
        expected_data = {
            "account_id": None,
            "first_name": post_data["first_name"],
            "last_name": post_data["last_name"],
            "email": post_data["email"],
            "phone": post_data["phone"],
            "institution": {
                "name": "GRNET",
                "address": "Mesogeon av.",
                "country": "GREECE",
                "department": "Admin",
                "uuid": "224fe496-5023-49e6-8953-19d5b1331333"
            },
            "uuid": post_data["uuid"]
        }

        expected_response = helper.get_response_info(strings.SERVICE_OWNER_UPDATED, expected_data, status=strings.UPDATED_202)
        self.assertJSONEqual(json.dumps(expected_response), response.content)