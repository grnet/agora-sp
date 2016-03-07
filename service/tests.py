from django.test import TestCase, Client
from django.test.client import RequestFactory
from models import *
from views import *
from django.core.urlresolvers import reverse
import json

# Create your tests here.


class ServiceTestCase(TestCase):


    fixtures = ["test.json"]


    def setUp(self):
        self.factory = RequestFactory()
        self.client_stub = Client()
        self.maxDiff = None


    def test_invalid_url(self):
        response = self.client_stub.get('/')

        expected_response = {
            "status": "404 Page not found",
            "errors": {
                "detail": "The requested page was not found"
            }
        }

        self.assertJSONEqual(json.dumps(expected_response), response.content)

        response = self.client_stub.get("/ved/defea")
        self.assertJSONEqual(json.dumps(expected_response), response.content)


    def test_list_service_invalid_parameter(self):
        pass


    def test_get_service_invalid_name(self):
        response = self.client_stub.get('/v1/portfolio/services/B2SAFISH')

        expected_response = {
            "status": "404 Not Found",
            "errors": {
                "detail": "The requested service was not found"
            }
        }

        self.assertJSONEqual(json.dumps(expected_response), response.content)


    def test_get_service_invalid_uuid(self):
        response = self.client_stub.get('/v1/portfolio/services/583ec8f2-9ef6-4e51-89bd-9af7f5fcea9r')

        expected_response = {
            "status": "404 Not Found",
            "errors": {
                "detail": "The requested service was not found"
            }
        }

        self.assertJSONEqual(json.dumps(expected_response), response.content)


    def test_get_service_nonexistent_uuid(self):
        response = self.client_stub.get('/v1/portfolio/services/583ec8f2-9ef6-4e51-89bd-9af7f5fcea9d')

        expected_response = {
            "status": "404 Not Found",
            "errors": {
                "detail": "The requested service was not found"
            }
        }

        self.assertJSONEqual(json.dumps(expected_response), response.content)


    def test_get_service_invalid_query_parameter(self):
        response = self.client_stub.get('/v1/portfolio/services/583ec8f2-9ef6-4e51-89bd-9af7f5fcea9c?view=full')

        expected_response = {
            "status": "404 Not Found",
            "errors": {
                "detail": "The query parameter is invalid"
            }
        }

        self.assertJSONEqual(json.dumps(expected_response), response.content)


    def test_get_service(self):
        response_name = self.client_stub.get('/v1/portfolio/services/B2SAFE')
        response_uuid = self.client_stub.get('/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a')

        expected_response = {"status": "200 OK", "info": "service information", "data": {"id_service_owner": "a9976cd2-14e4-47b7-9353-7e9faba2f200", "funders_for_service": "/", "value_to_customer": "Data replication  and safe storage  of your community data between geographically distributed centres", "description_internal": "\"B2SAFE is a robust, safe and highly available service which allows community and departmental repositories to implement data management policies on their research data across multiple administrative domains in a trustworthy manner.  \r\nabstraction layer of large scale, heterogeneous data storages\r\nguards against data loss in long-term archiving\r\nallows to optimize access for users (e.g. from different regions)\r\nbrings data closer to facilities for compute-intensive analysis\r\n\"", "request_procedures": "Joining the EUDAT CDI", "name": "B2SAFE", "uuid": "88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a", "description_external": "\"B2SAFE is a robust, safe and highly available service which allows community and departmental repositories to implement data management policies on their research data across multiple administrative domains in a trustworthy manner.  \nabstraction layer of large scale, heterogeneous data storages\nguards against data loss in long-term archiving\nallows to optimize access for users (e.g. from different regions)\nbrings data closer to facilities for compute-intensive analysis\n\"", "service_area": "Data hosting & management", "url": "/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a", "competitors": "/", "id_contact_information": "cb1a2e50-e49b-4b8d-b88b-d12fbc30f41b", "risks": "/", "user_customers": [], "service_details": [{"features_future": "Futurs Features:                                                                                                                          - data policies are centrally managed via a Data Policy Manager, and the policy rules are implemented and enforced by", "uuid": "aa37cd70-c3e3-4334-a719-d467c22aed81", "url": "/catalogue/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0", "version": "3.0", "service_status": "Active", "features_current": "\"Features:     - based on the execution of auditable data policy rules and the use of persistent identifiers (PIDs)    -  respects the rights of the data owners to define the access rights for their data and to decide how and when it is made publicly refe"}]}}

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)


    def test_get_service_query_parameter(self):
        response_short = self.client_stub.get('/v1/portfolio/services/B2SAFE?view=short')
        response_complete = self.client_stub.get('/v1/portfolio/services/B2SAFE?view=complete')

        expected_response_short = {"status": "200 OK", "info": "service information", "data": {"id_service_owner": "a9976cd2-14e4-47b7-9353-7e9faba2f200", "funders_for_service": "/", "value_to_customer": "Data replication  and safe storage  of your community data between geographically distributed centres", "description_internal": "\"B2SAFE is a robust, safe and highly available service which allows community and departmental repositories to implement data management policies on their research data across multiple administrative domains in a trustworthy manner.  \r\nabstraction layer of large scale, heterogeneous data storages\r\nguards against data loss in long-term archiving\r\nallows to optimize access for users (e.g. from different regions)\r\nbrings data closer to facilities for compute-intensive analysis\r\n\"", "request_procedures": "Joining the EUDAT CDI", "name": "B2SAFE", "uuid": "88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a", "description_external": "\"B2SAFE is a robust, safe and highly available service which allows community and departmental repositories to implement data management policies on their research data across multiple administrative domains in a trustworthy manner.  \nabstraction layer of large scale, heterogeneous data storages\nguards against data loss in long-term archiving\nallows to optimize access for users (e.g. from different regions)\nbrings data closer to facilities for compute-intensive analysis\n\"", "service_area": "Data hosting & management", "url": "/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a", "competitors": "/", "id_contact_information": "cb1a2e50-e49b-4b8d-b88b-d12fbc30f41b", "risks": "/", "user_customers": [], "service_details": [{"features_future": "Futurs Features:                                                                                                                          - data policies are centrally managed via a Data Policy Manager, and the policy rules are implemented and enforced by", "uuid": "aa37cd70-c3e3-4334-a719-d467c22aed81", "url": "/catalogue/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0", "version": "3.0", "service_status": "Active", "features_current": "\"Features:     - based on the execution of auditable data policy rules and the use of persistent identifiers (PIDs)    -  respects the rights of the data owners to define the access rights for their data and to decide how and when it is made publicly refe"}]}}
        expected_response_complete = {"status": "200 OK", "info": "service information", "data": {"funders_for_service": "/", "uuid": "88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a", "url": "/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a", "value_to_customer": "Data replication  and safe storage  of your community data between geographically distributed centres", "service_area": "Data hosting & management", "service_owner": {"phone": "000", "first_name": "Claudio", "last_name": "Cacciari", "uuid": "a9976cd2-14e4-47b7-9353-7e9faba2f200", "email": "c.cacciari@cineca.it"}, "components": [], "contact_information": {"phone": "000", "first_name": "Claudio", "last_name": "Cacciari", "uuid": "cb1a2e50-e49b-4b8d-b88b-d12fbc30f41b", "email": "eudat-safereplication@postit.csc.fi"}, "description_external": "\"B2SAFE is a robust, safe and highly available service which allows community and departmental repositories to implement data management policies on their research data across multiple administrative domains in a trustworthy manner.  \nabstraction layer of large scale, heterogeneous data storages\nguards against data loss in long-term archiving\nallows to optimize access for users (e.g. from different regions)\nbrings data closer to facilities for compute-intensive analysis\n\"", "competitors": "/", "dependencies": {"count": 1, "services": [{"uuid": "9985c4ee-bef1-46d5-ae00-e501bfa7bdd0"}]}, "risks": "/", "description_internal": "\"B2SAFE is a robust, safe and highly available service which allows community and departmental repositories to implement data management policies on their research data across multiple administrative domains in a trustworthy manner.  \r\nabstraction layer of large scale, heterogeneous data storages\r\nguards against data loss in long-term archiving\r\nallows to optimize access for users (e.g. from different regions)\r\nbrings data closer to facilities for compute-intensive analysis\r\n\"", "user_customers": [], "service_details": [{"monitoring_has": True, "service_status": "Active", "user_documentation_url": "http://eudat.eu/services/userdoc/configure-b2safe", "features_current": "\"Features:     - based on the execution of auditable data policy rules and the use of persistent identifiers (PIDs)    -  respects the rights of the data owners to define the access rights for their data and to decide how and when it is made publicly refe", "decommissioning_procedure_has": False, "cost_to_run": "Not specified", "uuid": "aa37cd70-c3e3-4334-a719-d467c22aed81", "accounting_has": False, "version": "3.0", "operations_documentation_has": False, "business_continuity_plan_has": False, "disaster_recovery_plan_url": "/", "usage_policy_url": "/", "cost_to_build": "Not specified", "use_cases": "", "disaster_recovery_plan_has": False, "accounting_url": "/", "features_future": "Futurs Features:                                                                                                                          - data policies are centrally managed via a Data Policy Manager, and the policy rules are implemented and enforced by", "business_continuity_plan_url": "/", "monitoring_url": "https://cmon.eudat.eu/nagvis_in_a_box.html", "usage_policy_has": False, "url": "/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a/service_details/3.0", "operations_documentation_url": "", "user_documentation_has": True, "decommissioning_procedure_url": "/"}], "request_procedures": "Joining the EUDAT CDI", "name": "B2SAFE"}}

        self.assertJSONEqual(json.dumps(expected_response_short), response_short.content)
        self.assertJSONEqual(json.dumps(expected_response_complete), response_complete.content)


