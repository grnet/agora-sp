from django.test import TestCase, Client
from django.test.client import RequestFactory
from common import helper, strings
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

        expected_response = helper.page_not_found()

        self.assertJSONEqual(json.dumps(expected_response), response.content)
        response = self.client_stub.get("/ved/defea")
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_service_invalid_name(self):
        response = self.client_stub.get('/api/v1/portfolio/services/B2SAFISH')

        expected_response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_service_invalid_uuid(self):
        response = self.client_stub.get('/api/v1/portfolio/services/583ec8f2-9ef6-4e51-89bd-9af7f5fcea9r')

        expected_response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_service_nonexistent_uuid(self):
        response = self.client_stub.get('/api/v1/portfolio/services/583ec8f2-9ef6-4e51-89bd-9af7f5fcea9d')

        expected_response = helper.get_error_response(strings.SERVICE_NOT_FOUND)

        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_service_invalid_query_parameter(self):
        response = self.client_stub.get('/api/v1/portfolio/services/583ec8f2-9ef6-4e51-89bd-9af7f5fcea9c?view=full')

        expected_response = helper.get_error_response(strings.INVALID_QUERY_PARAMETER)

        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_service(self):
        response_name = self.client_stub.get('/api/v1/portfolio/services/B2SAFE')
        response_uuid = self.client_stub.get('/api/v1/portfolio/services/88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a')

        data = {"funders_for_service": "/", "contact_information_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/contact_information", "meta": {"desc": "Link contact information about this service"}}}, "value_to_customer": "Data replication  and safe storage  of your community data between geographically distributed centres", "user_customers_list": {"count": 1, "user_customers": [{"role": "user", "id": "5fa10867-e6bf-4ad0-9ac9-784542053c69", "name": "Service provider"}]}, "description_internal": "\"B2SAFE is a robust, safe and highly available service which allows community and departmental repositories to implement data management policies on their research data across multiple administrative domains in a trustworthy manner.  \r\nabstraction layer of large scale, heterogeneous data storages\r\nguards against data loss in long-term archiving\r\nallows to optimize access for users (e.g. from different regions)\r\nbrings data closer to facilities for compute-intensive analysis\r\n\"", "request_procedures": "Joining the EUDAT CDI", "service_owner_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_owner", "meta": {"desc": "Service owner link"}}}, "name": "B2SAFE", "uuid": "88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a", "service_details_list": {"count": 2, "service_details": [{"accounting_link": {"related": {"href": "", "meta": {"desc": "A link to the accounting system for this service."}}}, "version": "3.2", "monitoring_has": False, "service_status": "a", "features_current": "s", "decommissioning_procedure_has": False, "is_in_catalogue": True, "cost_to_run": "4", "operations_documentation_link": {"related": {"href": "", "meta": {"desc": "A link to the operations documentation for this service."}}}, "user_documentation_link": {"related": {"href": "", "meta": {"desc": "A link to the user documentation for this service."}}}, "service_details_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.2", "meta": {"desc": "Service details link"}}}, "accounting_has": False, "business_continuity_plan_link": {"related": {"href": "", "meta": {"desc": "A link to the business continuity plan for this service."}}}, "usage_policy_link": {"related": {"href": "", "meta": {"desc": "A link to the usage policy for this service."}}}, "operations_documentation_has": False, "monitoring_link": {"related": {"href": "", "meta": {"desc": "A link to the monitoring system for this service."}}}, "business_continuity_plan_has": False, "disaster_recovery_plan_url": {"related": {"href": "", "meta": {"desc": "A link to the disaster recovery plan for this service."}}}, "cost_to_build": "3", "use_cases": "d", "dependencies": {"count": 1, "services": [{"service_link": {"meta": {"desc": "A list of service dependencies"}, "related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2HANDLE"}}, "uuid": "9985c4ee-bef1-46d5-ae00-e501bfa7bdd0", "name": "B2HANDLE"}], "service_dependencies_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_dependencies", "meta": {"desc": "A list of links to the service dependencies"}}}}, "disaster_recovery_plan_has": False, "uuid": "80557cf5-cdb9-4dc5-b9d3-993008e054e3", "features_future": "s", "usage_policy_has": False, "user_documentation_has": False, "decommissioning_procedure_url": {"related": {"href": "", "meta": {"desc": "A link to the decommissioning procedure for this service."}}}}, {"accounting_link": {"related": {"href": "/", "meta": {"desc": "A link to the accounting system for this service."}}}, "version": "3.0", "monitoring_has": True, "is_in_catalogue": False, "service_status": "Active", "features_current": "\"Features:     - based on the execution of auditable data policy rules and the use of persistent identifiers (PIDs)    -  respects the rights of the data owners to define the access rights for their data and to decide how and when it is made publicly refe", "decommissioning_procedure_has": False, "cost_to_run": "Not specified", "operations_documentation_link": {"related": {"href": "", "meta": {"desc": "A link to the operations documentation for this service."}}}, "user_documentation_link": {"related": {"href": "http://eudat.eu/services/userdoc/configure-b2safe", "meta": {"desc": "A link to the user documentation for this service."}}}, "service_details_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.0", "meta": {"desc": "Service details link"}}}, "accounting_has": False, "business_continuity_plan_link": {"related": {"href": "/", "meta": {"desc": "A link to the business continuity plan for this service."}}}, "usage_policy_link": {"related": {"href": "/", "meta": {"desc": "A link to the usage policy for this service."}}}, "operations_documentation_has": False, "monitoring_link": {"related": {"href": "https://cmon.eudat.eu/nagvis_in_a_box.html", "meta": {"desc": "A link to the monitoring system for this service."}}}, "business_continuity_plan_has": False, "disaster_recovery_plan_url": {"related": {"href": "/", "meta": {"desc": "A link to the disaster recovery plan for this service."}}}, "cost_to_build": "Not specified", "use_cases": "", "dependencies": {"count": 1, "services": [{"service_link": {"meta": {"desc": "A list of service dependencies"}, "related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2HANDLE"}}, "uuid": "9985c4ee-bef1-46d5-ae00-e501bfa7bdd0", "name": "B2HANDLE"}], "service_dependencies_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_dependencies", "meta": {"desc": "A list of links to the service dependencies"}}}}, "disaster_recovery_plan_has": False, "uuid": "aa37cd70-c3e3-4334-a719-d467c22aed81", "features_future": "Futurs Features:                                                                                                                          - data policies are centrally managed via a Data Policy Manager, and the policy rules are implemented and enforced by", "usage_policy_has": False, "user_documentation_has": True, "decommissioning_procedure_url": {"related": {"href": "/", "meta": {"desc": "A link to the decommissioning procedure for this service."}}}}]}, "description_external": "\"B2SAFE is a robust, safe and highly available service which allows community and departmental repositories to implement data management policies on their research data across multiple administrative domains in a trustworthy manner.  \nabstraction layer of large scale, heterogeneous data storages\nguards against data loss in long-term archiving\nallows to optimize access for users (e.g. from different regions)\nbrings data closer to facilities for compute-intensive analysis\n\"", "service_area": "Data hosting & management", "service_complete_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE?view=complete", "meta": {"desc": "Portfolio level details about this service."}}}, "competitors": "/", "risks": "/"}
        expected_response = helper.get_response_info(strings.SERVICE_INFORMATION, data)

        self.assertJSONEqual(json.dumps(expected_response), response_name.content)
        self.assertJSONEqual(json.dumps(expected_response), response_uuid.content)

    def test_get_service_query_parameter(self):
        response_short = self.client_stub.get('/api/v1/portfolio/services/B2SAFE?view=short')
        response_complete = self.client_stub.get('/api/v1/portfolio/services/B2SAFE?view=complete')

        data_short = {"funders_for_service": "/", "contact_information_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/contact_information", "meta": {"desc": "Link contact information about this service"}}}, "value_to_customer": "Data replication  and safe storage  of your community data between geographically distributed centres", "user_customers_list": {"count": 1, "user_customers": [{"role": "user", "id": "5fa10867-e6bf-4ad0-9ac9-784542053c69", "name": "Service provider"}]}, "description_internal": "\"B2SAFE is a robust, safe and highly available service which allows community and departmental repositories to implement data management policies on their research data across multiple administrative domains in a trustworthy manner.  \r\nabstraction layer of large scale, heterogeneous data storages\r\nguards against data loss in long-term archiving\r\nallows to optimize access for users (e.g. from different regions)\r\nbrings data closer to facilities for compute-intensive analysis\r\n\"", "request_procedures": "Joining the EUDAT CDI", "service_owner_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_owner", "meta": {"desc": "Service owner link"}}}, "name": "B2SAFE", "uuid": "88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a", "service_details_list": {"count": 2, "service_details": [{"accounting_link": {"related": {"href": "", "meta": {"desc": "A link to the accounting system for this service."}}}, "version": "3.2", "monitoring_has": False, "service_status": "a", "features_current": "s", "decommissioning_procedure_has": False, "is_in_catalogue": True, "cost_to_run": "4", "operations_documentation_link": {"related": {"href": "", "meta": {"desc": "A link to the operations documentation for this service."}}}, "user_documentation_link": {"related": {"href": "", "meta": {"desc": "A link to the user documentation for this service."}}}, "service_details_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.2", "meta": {"desc": "Service details link"}}}, "accounting_has": False, "business_continuity_plan_link": {"related": {"href": "", "meta": {"desc": "A link to the business continuity plan for this service."}}}, "usage_policy_link": {"related": {"href": "", "meta": {"desc": "A link to the usage policy for this service."}}}, "operations_documentation_has": False, "monitoring_link": {"related": {"href": "", "meta": {"desc": "A link to the monitoring system for this service."}}}, "business_continuity_plan_has": False, "disaster_recovery_plan_url": {"related": {"href": "", "meta": {"desc": "A link to the disaster recovery plan for this service."}}}, "cost_to_build": "3", "use_cases": "d", "dependencies": {"count": 1, "services": [{"service_link": {"meta": {"desc": "A list of service dependencies"}, "related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2HANDLE"}}, "uuid": "9985c4ee-bef1-46d5-ae00-e501bfa7bdd0", "name": "B2HANDLE"}], "service_dependencies_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_dependencies", "meta": {"desc": "A list of links to the service dependencies"}}}}, "disaster_recovery_plan_has": False, "uuid": "80557cf5-cdb9-4dc5-b9d3-993008e054e3", "features_future": "s", "usage_policy_has": False, "user_documentation_has": False, "decommissioning_procedure_url": {"related": {"href": "", "meta": {"desc": "A link to the decommissioning procedure for this service."}}}}, {"accounting_link": {"related": {"href": "/", "meta": {"desc": "A link to the accounting system for this service."}}}, "version": "3.0", "is_in_catalogue": False, "monitoring_has": True, "service_status": "Active", "features_current": "\"Features:     - based on the execution of auditable data policy rules and the use of persistent identifiers (PIDs)    -  respects the rights of the data owners to define the access rights for their data and to decide how and when it is made publicly refe", "decommissioning_procedure_has": False, "cost_to_run": "Not specified", "operations_documentation_link": {"related": {"href": "", "meta": {"desc": "A link to the operations documentation for this service."}}}, "user_documentation_link": {"related": {"href": "http://eudat.eu/services/userdoc/configure-b2safe", "meta": {"desc": "A link to the user documentation for this service."}}}, "service_details_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.0", "meta": {"desc": "Service details link"}}}, "accounting_has": False, "business_continuity_plan_link": {"related": {"href": "/", "meta": {"desc": "A link to the business continuity plan for this service."}}}, "usage_policy_link": {"related": {"href": "/", "meta": {"desc": "A link to the usage policy for this service."}}}, "operations_documentation_has": False, "monitoring_link": {"related": {"href": "https://cmon.eudat.eu/nagvis_in_a_box.html", "meta": {"desc": "A link to the monitoring system for this service."}}}, "business_continuity_plan_has": False, "disaster_recovery_plan_url": {"related": {"href": "/", "meta": {"desc": "A link to the disaster recovery plan for this service."}}}, "cost_to_build": "Not specified", "use_cases": "", "dependencies": {"count": 1, "services": [{"service_link": {"meta": {"desc": "A list of service dependencies"}, "related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2HANDLE"}}, "uuid": "9985c4ee-bef1-46d5-ae00-e501bfa7bdd0", "name": "B2HANDLE"}], "service_dependencies_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_dependencies", "meta": {"desc": "A list of links to the service dependencies"}}}}, "disaster_recovery_plan_has": False, "uuid": "aa37cd70-c3e3-4334-a719-d467c22aed81", "features_future": "Futurs Features:                                                                                                                          - data policies are centrally managed via a Data Policy Manager, and the policy rules are implemented and enforced by", "usage_policy_has": False, "user_documentation_has": True, "decommissioning_procedure_url": {"related": {"href": "/", "meta": {"desc": "A link to the decommissioning procedure for this service."}}}}]}, "description_external": "\"B2SAFE is a robust, safe and highly available service which allows community and departmental repositories to implement data management policies on their research data across multiple administrative domains in a trustworthy manner.  \nabstraction layer of large scale, heterogeneous data storages\nguards against data loss in long-term archiving\nallows to optimize access for users (e.g. from different regions)\nbrings data closer to facilities for compute-intensive analysis\n\"", "service_area": "Data hosting & management", "service_complete_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE?view=complete", "meta": {"desc": "Portfolio level details about this service."}}}, "competitors": "/", "risks": "/"}
        data_complete = {"funders_for_service": "/", "uuid": "88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a", "external": {"count": 1, "external_services": [{"uuid": "a42732fc-584e-429e-8df3-610caf2b1a50", "name": "First external"}], "external_services_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_external_dependencies", "meta": {"desc": "Links to external services that this service uses."}}}}, "description_external": "\"B2SAFE is a robust, safe and highly available service which allows community and departmental repositories to implement data management policies on their research data across multiple administrative domains in a trustworthy manner.  \nabstraction layer of large scale, heterogeneous data storages\nguards against data loss in long-term archiving\nallows to optimize access for users (e.g. from different regions)\nbrings data closer to facilities for compute-intensive analysis\n\"", "value_to_customer": "Data replication  and safe storage  of your community data between geographically distributed centres", "service_area": "Data hosting & management", "user_customers_list": {"count": 1, "user_customers": [{"role": "user", "id": "5fa10867-e6bf-4ad0-9ac9-784542053c69", "name": "Service provider"}]}, "service_details_list": {"count": 2, "service_details": [{"accounting_link": {"related": {"href": "", "meta": {"desc": "A link to the accounting system for this service."}}}, "version": "3.2", "monitoring_has": False, "service_status": "a", "features_current": "s", "decommissioning_procedure_has": False, "is_in_catalogue": True, "cost_to_run": "4", "operations_documentation_link": {"related": {"href": "", "meta": {"desc": "A link to the operations documentation for this service."}}}, "user_documentation_link": {"related": {"href": "", "meta": {"desc": "A link to the user documentation for this service."}}}, "service_details_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.2", "meta": {"desc": "Service details link"}}}, "accounting_has": False, "business_continuity_plan_link": {"related": {"href": "", "meta": {"desc": "A link to the business continuity plan for this service."}}}, "usage_policy_link": {"related": {"href": "", "meta": {"desc": "A link to the usage policy for this service."}}}, "operations_documentation_has": False, "monitoring_link": {"related": {"href": "", "meta": {"desc": "A link to the monitoring system for this service."}}}, "business_continuity_plan_has": False, "disaster_recovery_plan_url": {"related": {"href": "", "meta": {"desc": "A link to the disaster recovery plan for this service."}}}, "cost_to_build": "3", "use_cases": "d", "dependencies": {"count": 1, "services": [{"service_link": {"meta": {"desc": "A list of service dependencies"}, "related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2HANDLE"}}, "uuid": "9985c4ee-bef1-46d5-ae00-e501bfa7bdd0", "name": "B2HANDLE"}], "service_dependencies_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_dependencies", "meta": {"desc": "A list of links to the service dependencies"}}}}, "disaster_recovery_plan_has": False, "uuid": "80557cf5-cdb9-4dc5-b9d3-993008e054e3", "features_future": "s", "usage_policy_has": False, "user_documentation_has": False, "decommissioning_procedure_url": {"related": {"href": "", "meta": {"desc": "A link to the decommissioning procedure for this service."}}}}, {"accounting_link": {"related": {"href": "/", "meta": {"desc": "A link to the accounting system for this service."}}}, "version": "3.0", "monitoring_has": True, "service_status": "Active", "features_current": "\"Features:     - based on the execution of auditable data policy rules and the use of persistent identifiers (PIDs)    -  respects the rights of the data owners to define the access rights for their data and to decide how and when it is made publicly refe", "decommissioning_procedure_has": False, "cost_to_run": "Not specified", "operations_documentation_link": {"related": {"href": "", "meta": {"desc": "A link to the operations documentation for this service."}}}, "user_documentation_link": {"related": {"href": "http://eudat.eu/services/userdoc/configure-b2safe", "meta": {"desc": "A link to the user documentation for this service."}}}, "service_details_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.0", "meta": {"desc": "Service details link"}}}, "accounting_has": False, "business_continuity_plan_link": {"related": {"href": "/", "meta": {"desc": "A link to the business continuity plan for this service."}}}, "usage_policy_link": {"related": {"href": "/", "meta": {"desc": "A link to the usage policy for this service."}}}, "operations_documentation_has": False, "monitoring_link": {"related": {"href": "https://cmon.eudat.eu/nagvis_in_a_box.html", "meta": {"desc": "A link to the monitoring system for this service."}}}, "business_continuity_plan_has": False, "disaster_recovery_plan_url": {"related": {"href": "/", "meta": {"desc": "A link to the disaster recovery plan for this service."}}}, "cost_to_build": "Not specified", "use_cases": "", "dependencies": {"count": 1, "services": [{"service_link": {"meta": {"desc": "A list of service dependencies"}, "related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2HANDLE"}}, "uuid": "9985c4ee-bef1-46d5-ae00-e501bfa7bdd0", "name": "B2HANDLE"}], "service_dependencies_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_dependencies", "meta": {"desc": "A list of links to the service dependencies"}}}}, "disaster_recovery_plan_has": False, "is_in_catalogue": True, "uuid": "aa37cd70-c3e3-4334-a719-d467c22aed81", "features_future": "Futurs Features:                                                                                                                          - data policies are centrally managed via a Data Policy Manager, and the policy rules are implemented and enforced by", "usage_policy_has": False, "user_documentation_has": True, "decommissioning_procedure_url": {"related": {"href": "/", "meta": {"desc": "A link to the decommissioning procedure for this service."}}}}]}, "competitors": "/", "dependencies": {"count": 1, "services": [{"service_link": {"meta": {"desc": "A list of service dependencies"}, "related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2HANDLE"}}, "uuid": "9985c4ee-bef1-46d5-ae00-e501bfa7bdd0", "name": "B2HANDLE"}], "service_dependencies_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_dependencies", "meta": {"desc": "A list of links to the service dependencies"}}}}, "risks": "/", "description_internal": "\"B2SAFE is a robust, safe and highly available service which allows community and departmental repositories to implement data management policies on their research data across multiple administrative domains in a trustworthy manner.  \r\nabstraction layer of large scale, heterogeneous data storages\r\nguards against data loss in long-term archiving\r\nallows to optimize access for users (e.g. from different regions)\r\nbrings data closer to facilities for compute-intensive analysis\r\n\"", "request_procedures": "Joining the EUDAT CDI", "contact_information_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/contact_information", "meta": {"desc": "Link contact information about this service"}}}, "service_owner_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_owner", "meta": {"desc": "Service owner link"}}}, "name": "B2SAFE"}

        expected_response_short = helper.get_response_info(strings.SERVICE_INFORMATION, data_short)
        expected_response_complete = helper.get_response_info(strings.SERVICE_INFORMATION, data_complete)

        self.assertJSONEqual(json.dumps(expected_response_short), response_short.content)
        # self.assertJSONEqual(json.dumps(expected_response_complete), response_complete.content)

    def test_get_all_service_details(self):
        response = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_details/')
        data = {"count": 2, "service_details": [{"features_future": "s", "uuid": "80557cf5-cdb9-4dc5-b9d3-993008e054e3", "service_details_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.2", "meta": {"desc": "Service details access url."}}}, "version": "3.2", "service_status": "a", "features_current": "s"}, {"features_future": "Futurs Features:                                                                                                                          - data policies are centrally managed via a Data Policy Manager, and the policy rules are implemented and enforced by", "uuid": "aa37cd70-c3e3-4334-a719-d467c22aed81", "service_details_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2SAFE/service_details/3.0", "meta": {"desc": "Service details access url."}}}, "version": "3.0", "service_status": "Active", "features_current": "\"Features:     - based on the execution of auditable data policy rules and the use of persistent identifiers (PIDs)    -  respects the rights of the data owners to define the access rights for their data and to decide how and when it is made publicly refe"}]}
        expected_response = helper.get_response_info(strings.SERVICE_DETAIL_INFORMATION, data)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_all_service_details_empty(self):
        response = self.client_stub.get('/api/v1/portfolio/services/7d829471-4904-4da9-a831-c72f6b1c747e/service_details/')
        data = {"count": 0, "service_details": []}
        expected_response = helper.get_response_info(strings.SERVICE_DETAIL_INFORMATION, data)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_service_details_invalid_version(self):
        response = self.client_stub.get('/api/v1/portfolio/services/f6148f39-4951-4915-87d7-5c6ce47aa79F/service_details/0.2')
        expected_response = helper.get_error_response(strings.SERVICE_DETAILS_NOT_FOUND)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_get_service_details(self):
        response = self.client_stub.get('/api/v1/portfolio/services/f6148f39-4951-4915-87d7-5c6ce47aa79F/service_details/0.1')
        data = {"accounting_link": {"related": {"href": "/", "meta": {"desc": "A link to the accounting system for this service."}}}, "version": "0.1", "monitoring_has": False, "service_status": "Planned", "service_options_list": {"count": 1, "service_options": [{"pricing": "Not specified yet", "SLA_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/EUDAT_Service_Portfolio_Management_System/service_details/0.1/service_options/sla/2ad2b14a-0874-44af-94be-e00093fc3e3c", "meta": {"desc": "A link to the SLA for this service."}}}, "description": "Standard options", "uuid": "61c31958-412f-43cf-be19-1f59ea89d0ee", "name": "Standard"}], "service_options_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/EUDAT_Service_Portfolio_Management_System/service_details/0.1/service_options", "meta": {"desc": "Link to the service options"}}}}, "features_current": "Under development", "decommissioning_procedure_has": False, "cost_to_run": "Not speficied yet", "operations_documentation_link": {"related": {"href": "", "meta": {"desc": "A link to the operations documentation for this service."}}}, "user_documentation_link": {"related": {"href": "/", "meta": {"desc": "A link to the user documentation for this service."}}}, "accounting_has": False, "business_continuity_plan_link": {"related": {"href": "/", "meta": {"desc": "A link to the business continuity plan for this service."}}}, "usage_policy_link": {"related": {"href": "/", "meta": {"desc": "A link to the usage policy for this service."}}}, "operations_documentation_has": False, "is_in_catalogue": True, "monitoring_link": {"related": {"href": "/", "meta": {"desc": "A link to the monitoring system for this service."}}}, "business_continuity_plan_has": False, "disaster_recovery_plan_url": {"related": {"href": "/", "meta": {"desc": "A link to the disaster recovery plan for this service."}}}, "cost_to_build": "6PMs to cover EUDAT's requirements", "use_cases": "", "dependencies": {"count": 0, "services": [], "service_dependencies_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/EUDAT_Service_Portfolio_Management_System/service_dependencies", "meta": {"desc": "A list of links to the service dependencies"}}}}, "disaster_recovery_plan_has": False, "uuid": "a2c9c5e8-8df2-4f52-8e16-c0f57db86420", "features_future": "\"CRUD access to the service portfolio database RESTful API (JSON) provision Read only GUI to the service catalogue/portfolio Role Management and Authentication GUI for inserting information to the portfolio\"", "usage_policy_has": False, "user_documentation_has": False, "components": {"components": "This service has no service components."}, "decommissioning_procedure_url": {"related": {"href": "/", "meta": {"desc": "A link to the decommissioning procedure for this service."}}}}
        expected_response = helper.get_response_info(strings.SERVICE_DETAIL_INFORMATION, data)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_service_dependencies_empty(self):
        response = self.client_stub.get('/api/v1/portfolio/services/583ec8f2-9ef6-4e51-89bd-9af7f5fcea9c/service_dependencies')
        data = {"count": 0, "dependencies": []}
        expected_response = helper.get_response_info(strings.SERVICE_DEPENDENCIES_INFORMATION, data)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_service_dependencies(self):
        response = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_dependencies')
        data = {"count": 1, "dependencies": [{"service_link": {"meta": {"desc": "A list of service dependencies"}, "related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/B2HANDLE"}}, "uuid": "9985c4ee-bef1-46d5-ae00-e501bfa7bdd0", "name": "B2HANDLE"}]}
        expected_response = helper.get_response_info(strings.SERVICE_DEPENDENCIES_INFORMATION, data)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_external_service_dependencies_empty(self):
        response = self.client_stub.get('/api/v1/portfolio/services/B2HANDLE/service_external_dependencies')
        data = {"count": 0, "dependencies": []}
        expected_response = helper.get_response_info(strings.SERVICE_EXTERNAL_DEPENDENCIES_INFORMATION, data)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_external_service_dependencies(self):
        response = self.client_stub.get('/api/v1/portfolio/services/B2SAFE/service_external_dependencies')
        data = {"count": 1, "dependencies": [{"details": "details", "description": "Something", "id": "a42732fc-584e-429e-8df3-610caf2b1a50", "service": "Service one", "name": "First external"}]}
        expected_response = helper.get_response_info(strings.SERVICE_EXTERNAL_DEPENDENCIES_INFORMATION, data)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_external_service_name_not_provided(self):
        post_data = {
        }
        response = self.client_stub.post("/api/v1/services/external_service/add", post_data)
        expected_response = helper.get_error_response(strings.EXTERNAL_SERVICE_NAME_NOT_PROVIDED, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_external_service_name_empty(self):
        post_data = {
            "name": ""
        }
        response = self.client_stub.post("/api/v1/services/external_service/add", post_data)
        expected_response = helper.get_error_response(strings.EXTERNAL_SERVICE_NAME_EMPTY, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_external_service_invalid_uuid(self):
        post_data = {
            "name": "Test name",
            "uuid": "a42732fc-584e-429e-8df3-610caf2b1a5R"
        }
        response = self.client_stub.post("/api/v1/services/external_service/add", post_data)
        expected_response = helper.get_error_response(strings.EXTERNAL_SERVICE_INVALID_UUID, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_external_service_existing_uuid(self):
        post_data = {
            "name": "Test name",
            "uuid": "a42732fc-584e-429e-8df3-610caf2b1a50"
        }
        response = self.client_stub.post("/api/v1/services/external_service/add", post_data)
        expected_response = helper.get_error_response(strings.EXTERNAL_SERVICE_UUID_EXISTS, status=strings.CONFLICT_409)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_non_existing_external_service(self):
        post_data = {
            "name": "Test name",
            "uuid": "a42732fc-584e-429e-8df3-610caf2bea55"
        }
        response = self.client_stub.post("/api/v1/services/external_service/edit", post_data)
        expected_response = helper.get_error_response(strings.EXTERNAL_SERVICE_NOT_FOUND, status=strings.NOT_FOUND_404)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_external_service_no_uuid(self):
        post_data = {
            "name": "Test name"
        }
        response = self.client_stub.post("/api/v1/services/external_service/edit", post_data)
        expected_response = helper.get_error_response(strings.EXTERNAL_SERVICE_UUID_NOT_PROVIDED, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_external_service(self):
        post_data = {
            "name": "Test name",
            "description": "Test description",
            "service": "Test service",
            "details": "Test details",
            "uuid": "a42732fc-584e-429e-8df3-610caf2b1a50"
        }
        response = self.client_stub.post("/api/v1/services/external_service/edit", post_data)
        expected_data = {
            "id": post_data["uuid"],
            "name": post_data["name"],
            "description": post_data["description"],
            "service": post_data["service"],
            "details": post_data["details"]
        }
        expected_response = helper.get_response_info(strings.EXTERNAL_SERVICE_UPDATED, expected_data, status=strings.UPDATED_202)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_external_service(self):
        post_data = {
            "name": "Test name",
            "description": "Test description",
            "service": "Test service",
            "details": "Test details",
            "uuid": "a42732fc-584e-429e-8df3-610caf2b1a51"
        }
        response = self.client_stub.post("/api/v1/services/external_service/add", post_data)
        expected_data = {
            "id": post_data["uuid"],
            "name": post_data["name"],
            "description": post_data["description"],
            "service": post_data["service"],
            "details": post_data["details"]
        }
        expected_response = helper.get_response_info(strings.EXTERNAL_SERVICE_INSERTED, expected_data, status=strings.CREATED_201)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_dependency_no_dependency(self):
        post_data = {
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/service_dependencies/add", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_DEPENDENCY_UUID_NOT_PROVIDED, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_dependency_invalid_dependency_uuid(self):
        post_data = {
            "service_dependency": "a42732fc-584e-429e-8df3-610caf2b1a5R"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/service_dependencies/add", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_DEPENDENCY_INVALID_UUID, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_dependency_dependency_not_found(self):
        post_data = {
            "service_dependency": "a42732fc-584e-429e-8df3-610caf2b1a52"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/service_dependencies/add", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_DEPENDENCY_NOT_FOUND, status=strings.NOT_FOUND_404)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_dependency_dependency_exists(self):
        post_data = {
            "service_dependency": "9985c4ee-bef1-46d5-ae00-e501bfa7bdd0"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/service_dependencies/add", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_DEPENDENCY_EXISTS, status=strings.CONFLICT_409)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_dependency(self):
        post_data = {
            "service_dependency": "583ec8f2-9ef6-4e51-89bd-9af7f5fcea9c"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/service_dependencies/add", post_data)
        expected_data = {
            "service": "B2SAFE",
            "dependency": "EUDAT Central Monitoring service"
        }
        expected_response = helper.get_response_info(strings.SERVICE_DEPENDENCY_INSERTED, expected_data, status=strings.CREATED_201)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_external_service_dependency_no_dependency(self):
        post_data = {
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/service_external_dependencies/add", post_data)
        expected_response = helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_UUID_NOT_PROVIDED, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_external_service_dependency_invalid_dependency_uuid(self):
        post_data = {
            "external_service_dependency": "a42732fc-584e-429e-8df3-610caf2b1a5R"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/service_external_dependencies/add", post_data)
        expected_response = helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_INVALID_UUID, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_external_service_dependency_dependency_not_found(self):
        post_data = {
            "external_service_dependency": "a42732fc-584e-429e-8df3-610caf2b1a54"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/service_external_dependencies/add", post_data)
        expected_response = helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_NOT_FOUND, status=strings.NOT_FOUND_404)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_external_service_dependency_dependency_exists(self):
        post_data = {
            "external_service_dependency": "a42732fc-584e-429e-8df3-610caf2b1a50"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/service_external_dependencies/add", post_data)
        expected_response = helper.get_error_response(strings.EXTERNAL_SERVICE_DEPENDENCY_EXISTS, status=strings.CONFLICT_409)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_external_service_dependency(self):
        post_data = {
            "external_service_dependency": "a42732fc-584e-429e-8df3-610caf2b1a52"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/service_external_dependencies/add", post_data)
        expected_data = {
            "service": "88b35b0d-adc2-4a2e-b5fc-cae2d6f5456a",
            "external_service": post_data["external_service_dependency"]
        }
        expected_response = helper.get_response_info(strings.EXTERNAL_SERVICE_DEPENDENCY_INSERTED, expected_data, status=strings.CREATED_201)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_user_customer_params_not_provided(self):
        post_data = {}
        post_data1 = {
            "name": "Service provider"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/user_customer/add", post_data)
        response1 = self.client_stub.post("/api/v1/services/B2SAFE/user_customer/add", post_data1)
        expected_response = helper.get_error_response(strings.USER_CUSTOMER_NAME_NOT_PROVIDED, status=strings.REJECTED_405)
        expected_response1 = helper.get_error_response(strings.USER_CUSTOMER_ROLE_NOT_PROVIDED, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)
        self.assertJSONEqual(json.dumps(expected_response1), response1.content)

    def test_insert_user_customer_invalid_params(self):
        post_data = {
            "name": "",
            "role": "",
        }
        post_data1 = {
            "name": "Service provider",
            "role": ""
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/user_customer/add", post_data)
        response1 = self.client_stub.post("/api/v1/services/B2SAFE/user_customer/add", post_data1)
        expected_response1 = helper.get_error_response(strings.USER_CUSTOMER_ROLE_EMPTY, status=strings.REJECTED_405)
        expected_response = helper.get_error_response(strings.USER_CUSTOMER_NAME_INVALID,  status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)
        self.assertJSONEqual(json.dumps(expected_response1), response1.content)

    def test_insert_user_customer_invalid_uuid(self):
        post_data = {
            "name": "Service provider",
            "role": "User",
            "uuid": "a42732fc-584e-429e-8df3-610caf2b1a5K"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/user_customer/add", post_data)
        expected_response = helper.get_error_response(strings.USER_CUSTOMER_INVALID_UUID, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_user_customer_existing_uuid(self):
        post_data = {
            "name": "Service provider",
            "role": "User",
            "uuid": "5fa10867-e6bf-4ad0-9ac9-784542053c69"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/user_customer/add", post_data)
        expected_response = helper.get_error_response(strings.USER_CUSTOMER_EXISTS, status=strings.CONFLICT_409)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_user_customer_no_uuid(self):
        post_data = {
            "name": "Service provider",
            "role": "User"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/user_customer/edit", post_data)
        expected_response = helper.get_error_response(strings.USER_CUSTOMER_UUID_NOT_PROVIDED, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_non_existing_user_customer(self):
        post_data = {
            "name": "Service provider",
            "role": "User",
            "uuid": "5fa10867-e6bf-4ad0-9ac9-784542053c61"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/user_customer/edit", post_data)
        expected_response = helper.get_error_response(strings.USER_CUSTOMER_NOT_FOUND, status=strings.NOT_FOUND_404)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_user_customer(self):
        post_data = {
            "name": "Service provider",
            "role": "User",
            "uuid": "5fa10867-e6bf-4ad0-9ac9-784542053c69"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/user_customer/edit", post_data)
        expected_data = {
            "id": post_data["uuid"],
            "name": post_data["name"],
            "role": post_data["role"]
        }
        expected_response = helper.get_response_info(strings.USER_CUSTOMER_UPDATED, expected_data, status=strings.UPDATED_202)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_user_customer(self):
        post_data = {
            "name": "Service provider",
            "role": "User",
            "uuid": "5fa10867-e6bf-4ad0-9ac9-784542053c63"
        }
        response = self.client_stub.post("/api/v1/services/B2SAFE/user_customer/add", post_data)
        expected_data = {
            "id": post_data["uuid"],
            "name": post_data["name"],
            "role": post_data["role"]
        }
        expected_response = helper.get_response_info(strings.USER_CUSTOMER_INSERTED, expected_data, status=strings.CREATED_201)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_invalid_name(self):
        post_data = {}
        post_data1 = {
            "name": "",
            "service_owner_uuid": "",
            "service_contact_information_uuid": ""
        }
        response = self.client_stub.post("/api/v1/services/add", post_data)
        response1 = self.client_stub.post("/api/v1/services/add", post_data1)
        expected_response = helper.get_error_response(strings.SERVICE_NAME_NOT_PROVIDED, status=strings.REJECTED_405)
        expected_response1 = helper.get_error_response(strings.SERVICE_NAME_EMPTY, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)
        self.assertJSONEqual(json.dumps(expected_response1), response1.content)

    def test_insert_service_non_existing_owner(self):
        post_data = {
            "name": "Test service",
            "service_owner_uuid": "5fa10867-e6bf-4ad0-9ac9-784542053c69",
            "service_contact_information_uuid": "5fa10867-e6bf-4ad0-9ac9-784542053c69"
        }
        response = self.client_stub.post("/api/v1/services/add", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_OWNER_NOT_FOUND, status=strings.NOT_FOUND_404)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_non_existing_contact_info(self):
        post_data = {
            "name": "Test service",
            "service_owner_uuid": "3cac63c1-a8d1-4178-aa8a-cd149696532d",
            "service_contact_information_uuid": "5fa10867-e6bf-4ad0-9ac9-784542053c69"
        }
        response = self.client_stub.post("/api/v1/services/add", post_data)
        expected_response = helper.get_error_response(strings.CONTACT_INFORMATION_NOT_FOUND, status=strings.NOT_FOUND_404)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_invalid_uuid(self):
        post_data = {
            "name": "Test service",
            "service_owner_uuid": "3cac63c1-a8d1-4178-aa8a-cd149696532d",
            "service_contact_information_uuid": "264fbac7-2bf0-4b9a-b182-293e65d599ce",
            "uuid": "a42732fc-584e-429e-8df3-610caf2b1a5K"
        }
        response = self.client_stub.post("/api/v1/services/add", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_INVALID_UUID, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service_existing_uuid(self):
        post_data = {
            "name": "Test service",
            "service_owner_uuid": "3cac63c1-a8d1-4178-aa8a-cd149696532d",
            "service_contact_information_uuid": "264fbac7-2bf0-4b9a-b182-293e65d599ce",
            "uuid": "583ec8f2-9ef6-4e51-89bd-9af7f5fcea9c"
        }
        response = self.client_stub.post("/api/v1/services/add", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_UUID_EXISTS, status=strings.CONFLICT_409)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_service_existing_no_uuid(self):
        post_data = {
            "name": "Test service",
            "service_owner_uuid": "3cac63c1-a8d1-4178-aa8a-cd149696532d",
            "service_contact_information_uuid": "264fbac7-2bf0-4b9a-b182-293e65d599ce"
        }
        response = self.client_stub.post("/api/v1/services/edit", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_UUID_NOT_PROVIDED, status=strings.REJECTED_405)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_non_existing_service_existing(self):
        post_data = {
            "name": "Test service",
            "service_owner_uuid": "3cac63c1-a8d1-4178-aa8a-cd149696532d",
            "service_contact_information_uuid": "264fbac7-2bf0-4b9a-b182-293e65d599ce",
            "uuid": "583ec8f2-9ef6-4e51-89bd-9af7f5fcea9d"
        }
        response = self.client_stub.post("/api/v1/services/edit", post_data)
        expected_response = helper.get_error_response(strings.SERVICE_NOT_FOUND, status=strings.NOT_FOUND_404)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_edit_service(self):
        post_data = {
            "name": "EUDAT Central Monitoring service",
            "service_owner_uuid": "3cac63c1-a8d1-4178-aa8a-cd149696532d",
            "service_contact_information_uuid": "264fbac7-2bf0-4b9a-b182-293e65d599ce",
            "uuid": "583ec8f2-9ef6-4e51-89bd-9af7f5fcea9c",
            "description_external": "external",
            "description_internal": "description_internal",
            "service_area": "service_area",
            "service_type": "service_type",
            "request_procedures": "request_procedures",
            "funders_for_service": "funders_for_service",
            "value_to_customer": "value_to_customer",
            "risks": "risks",
            "competitors": "new competitors",
        }
        response = self.client_stub.post("/api/v1/services/edit", post_data)
        expected_data = {
            "uuid": post_data["uuid"],
            "service_complete_link": {
                "related": {
                    "href": helper.current_site_url() + "/v1/portfolio/services/" + post_data["name"].replace(" ", "_")
                            + "?view=complete",
                    "meta": {
                        "desc": "Portfolio level details about this service."
                    }
                }},
            "name": post_data["name"],
            "description_external": post_data["description_external"],
            "description_internal": post_data["description_internal"],
            "service_area": post_data["service_area"],
            "request_procedures": post_data["request_procedures"],
            "funders_for_service": post_data["funders_for_service"],
            "value_to_customer": post_data["value_to_customer"],
            "risks": post_data["risks"],
            "service_details_list": {
                "count": 1,
                "service_details": [{"accounting_link": {"related": {"href": "/", "meta": {"desc": "A link to the accounting system for this service."}}}, "version": "1.0", "monitoring_has": False, "service_status": "Active", "features_current": "http://eudat.eu/User%20Documentation%20-%20The%20EUDAT%20Monitoring%20system.html#UserDocumentation-TheEUDATMonitoringsystem-Features", "decommissioning_procedure_has": False, "cost_to_run": "/", "operations_documentation_link": {"related": {"href": "", "meta": {"desc": "A link to the operations documentation for this service."}}}, "user_documentation_link": {"related": {"href": "http://eudat.eu/User%20Documentation%20-%20Monitoring%20System%20Operator%20View.html", "meta": {"desc": "A link to the user documentation for this service."}}}, "service_details_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/EUDAT_Central_Monitoring_service/service_details/1.0", "meta": {"desc": "Service details link"}}}, "accounting_has": False, "business_continuity_plan_link": {"related": {"href": "/", "meta": {"desc": "A link to the business continuity plan for this service."}}}, "usage_policy_link": {"related": {"href": "/", "meta": {"desc": "A link to the usage policy for this service."}}}, "operations_documentation_has": False, "monitoring_link": {"related": {"href": "/", "meta": {"desc": "A link to the monitoring system for this service."}}}, "business_continuity_plan_has": False, "disaster_recovery_plan_url": {"related": {"href": "/", "meta": {"desc": "A link to the disaster recovery plan for this service."}}}, "cost_to_build": "/", "use_cases": "", "dependencies": {"count": 0, "services": [], "service_dependencies_link": {"related": {"href": "http://agora-dev.aris.grnet.gr/api/v1/portfolio/services/EUDAT_Central_Monitoring_service/service_dependencies", "meta": {"desc": "A list of links to the service dependencies"}}}}, "disaster_recovery_plan_has": False, "is_in_catalogue": True, "uuid": "823175e6-de78-43f0-a123-d756a2f2b7e5", "features_future": "/", "usage_policy_has": False, "user_documentation_has": True, "decommissioning_procedure_url": {"related": {"href": "/", "meta": {"desc": "A link to the decommissioning procedure for this service."}}}}]
            },
            "competitors": post_data["competitors"],
            "user_customers_list": {
                "count": 0,
                "user_customers": []
            },
            "service_owner_link": {
                "related": {
                    "href": helper.current_site_url() + "/v1/portfolio/services/" + post_data["name"].replace(" ", "_") + "/service_owner",
                    "meta": {
                        "desc": "Service owner link"
                    }
                }
            },
            "contact_information_link": {
                "related": {
                    "href": helper.current_site_url() + "/v1/portfolio/services/" + post_data["name"].replace(" ", "_") + "/contact_information",
                    "meta": {
                        "desc": "Link contact information about this service"
                    }
                }}
        }
        expected_response = helper.get_response_info(strings.SERVICE_UPDATED, expected_data, status=strings.UPDATED_202)
        self.assertJSONEqual(json.dumps(expected_response), response.content)

    def test_insert_service(self):
        post_data = {
            "name": "Test service",
            "service_owner_uuid": "3cac63c1-a8d1-4178-aa8a-cd149696532d",
            "service_contact_information_uuid": "264fbac7-2bf0-4b9a-b182-293e65d599ce",
            "uuid": "583ec8f2-9ef6-4e51-89bd-9af7f5fcea92",
            "description_external": "external",
            "description_internal": "description_internal",
            "service_area": "service_area",
            "service_type": "service_type",
            "request_procedures": "request_procedures",
            "funders_for_service": "funders_for_service",
            "value_to_customer": "value_to_customer",
            "risks": "risks",
            "competitors": "competitors",
        }
        response = self.client_stub.post("/api/v1/services/add", post_data)
        expected_data = {
            "uuid": post_data["uuid"],
            "service_complete_link": {
                "related": {
                    "href": helper.current_site_url() + "/v1/portfolio/services/" + post_data["name"].replace(" ", "_")
                            + "?view=complete",
                    "meta": {
                        "desc": "Portfolio level details about this service."
                    }
                }},
            "name": post_data["name"],
            "description_external": post_data["description_external"],
            "description_internal": post_data["description_internal"],
            "service_area": post_data["service_area"],
            "request_procedures": post_data["request_procedures"],
            "funders_for_service": post_data["funders_for_service"],
            "value_to_customer": post_data["value_to_customer"],
            "risks": post_data["risks"],
            "service_details_list": {
                "count": 0,
                "service_details": []
            },
            "competitors": post_data["competitors"],
            "user_customers_list": {
                "count": 0,
                "user_customers": []
            },
            "service_owner_link": {
                "related": {
                    "href": helper.current_site_url() + "/v1/portfolio/services/" + post_data["name"].replace(" ", "_") + "/service_owner",
                    "meta": {
                        "desc": "Service owner link"
                    }
                }
            },
            "contact_information_link": {
                "related": {
                    "href": helper.current_site_url() + "/v1/portfolio/services/" + post_data["name"].replace(" ", "_") + "/contact_information",
                    "meta": {
                        "desc": "Link contact information about this service"
                    }
                }}
        }
        expected_response = helper.get_response_info(strings.SERVICE_INSERTED, expected_data, status=strings.CREATED_201)
        self.assertJSONEqual(json.dumps(expected_response), response.content)