#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: resource_create.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from agora.resources.resources import Resources
from agora.utils.emberJS_fields import input_field, suggestion_input_field, table_select_field, textarea_field, \
    date_field
from agora.validations.delete_responses import delete_success, delete_from_listView
from agora.validations.save_responses import save_success_double


class ResourceCreate(Resources):
    """
    Create a new Resource.

    This class is responsible for checking the following:
        * Go to the crete a resource page ( https://testvm.agora.grnet.gr/ui/resources/create ).
        * Checks if all the following input fields of the form exist :
            Basic information
            - *.BAI.0 - ID
            - *.BAI.1 - Name
            - *.BAI.2 - Resource Organisation
            - *.BAI.3 - Resource Providers
            - *.BAI.4 - Webpage

            Marketing Information
            - *.MRI.1 - Description
            - *.MRI.2 - Tagline
            - *.MRI.3 - Logo
            - *.MRI.4 - Mulitimedia
            - *.MRI.5 - Use Cases

            Classification Information
            - *.CLI.1 - Scientific Domain
            - *.CLI.2 - Scientific Subdomain
            - *.CLI.3 - Category
            - *.CLI.4 - Subcategory
            - *.CLI.5 - Target Users
            - *.CLI.6 - Access Type
            - *.CLI.7 - Access Mode
            - *.CLI.8 - Tags

            Management Information
            - *.MGI.1 - Heldesk Page
            - *.MGI.2 - User Manual
            - *.MGI.3 - Terms of Use
            - *.MGI.4 - Privacy Policy
            - *.MGI.5 - Access Policy
            - *.MGI.6 - Service Level
            - *.MGI.7 - Training Information
            - *.MGI.8 - Status Monitoring
            - *.MGI.9 - Maintenance

            Geographical and Language Availability Information
            - *.GLA.1 - Geographical Availability
            - *.GLA.2 - Language Availability

            Resource Location Information
            - *.RLI.1 - Resource Geographic Location

            Contact Information
            * Main Contact/Resource Owner
            * Public Contact
            - *.COI.13 - Helpdesk Email
            - *.COI.14 - Security Contact Email

            Maturity Information
            - *.MTI.1 - Technology Readinness Level
            - *.MTI.2 - Life Cycle Status
            - *.MTI.3 - Certifications
            - *.MTI.4 - Standards
            - *.MTI.5 - Open Source Technologies
            - *.MTI.6 - Version
            - *.MTI.7 - Last Update
            - *.MTI.8 - Changelog

            Dependencies Information
            - *.DEI.1 - Required Resources
            - *.DEI.2 - Related Resources
            - *.DEI.3 - Related Platforms

            Attribution Information
            - *.ATI.1 - Funding Body
            - *.ATI.2 - Funding Program
            - *.ATI.3 - Grant/Project Name

            Access and Order Information
            - *.AOI.1 - Order Type
            - *.AOI.2 - Order

            Financial Information
            - *.FNI.1 - Payment Model
            - *.FNI.2 - Pricing
        * Check submission form with only filling in the required form fields.
        * Check submission form with filling in all the form fields.
        * TODO : If the invalid messages improve, it should be better handled here as well.
        * TODO : If the warning messages improve, it should be better handled here as well.
        * TODO : If the error messages improve, it should be better handled here as well.
    """

    def __init__(self, driver, headless=True, instance="https://testvm.agora.grnet.gr/"):
        """
        Initialization.

        This method ensures that all the prerequisites will be met, so that you can go to create a new resource page.
        @param driver: Which browser will be used.
        @param headless: If you want headless browser - without GUI.
        @param instance: The website instance of the Agora project to be used for the tests.
        """
        super().__init__(driver, headless, instance)
        super().resources_create_new_page()
        self.fields_prefix = "erp_"

    def create_new_resource(self, required_only=False):
        """
        Method of creating a new resource.

        The create new Resource page is here: https://testvm.agora.grnet.gr/ui/providers/create
        It calls all the methods they undertake to fill all the areas of the form.

        @param required_only: Fill in only the required fields or not?
        @return:
        """
        print("\n# Create a new resource.")
        self.basic_information(required_only)
        self.classification_information(required_only)
        if not required_only:
            self.marketing_information(required_only)
            self.management_information(required_only)
            self.geographical_and_language_availability_information(required_only)
            self.resource_location_information()
            self.contact_information(required_only)
            self.maturity_information()
            self.dependencies_information()
            self.attribution_information()
            self.access_and_order_information()
            self.financial_information()

        save_success_double(self.driver)

        # Search
        self.resources_page()
        self.search_field()
        delete_from_listView(self.driver)
        # delete_success(self.driver)
        self.close()

    def basic_information(self, required_only=False):
        """
        Fill in the fields of "Basic information" area.

        @param required_only: Fill in only the required fields or not?
        @return: True if all goes well otherwise False.
        """
        # *.BAI.0 - ID
        input_field(self.driver, self.fields_prefix + "bai_0_id", "selenium-RESOURCE")
        # *.BAI.1 - Name
        input_field(self.driver, self.fields_prefix + "bai_1_name", "SeleniumHQ Browser Automation - RESOURCE")
        # *.BAI.2 - Service Organisation
        suggestion_input_field(self.driver, self.fields_prefix + "bai_2_service_organisation", "EGI Foundation")

        if not required_only:
            # *.BAI.3 - Service Providers
            table_select_field(self.driver, self.fields_prefix + "bai_3_service_providers", 1)
            # *.BAI.4 - Webpage
            input_field(self.driver, self.fields_prefix + "bai_4_webpage", "https://www.selenium.dev")


    def marketing_information(self, required_only=False):
        """
        Fill in the fields of "Marketing Information" area.

        @param required_only: Fill in only the required fields or not?
        @return: True if all goes well otherwise False.
        """
        # *.MRI.1 - Description
        textarea_field(self.driver, self.fields_prefix + "mri_1_description", "Selenium - Περιγραφή.")
        # *.MRI.2 - Tagline
        input_field(self.driver, self.fields_prefix + "mri_2_tagline", "selenium - tagline")
        # *.MRI.3 - Logo
        input_field(self.driver, self.fields_prefix + "mri_3_logo",
                    "https://www.selenium.dev/images/selenium_logo_large.png")
        # *.MRI.4 - Mulitimedia
        input_field(self.driver, self.fields_prefix + "mri_4_mulitimedia",
                    "https://www.youtube.com/channel/UCbDlgX_613xNMrDqCe3QNEw")
        # *.MRI.5 - Use Cases
        input_field(self.driver, self.fields_prefix + "mri_5_use_cases", "https://gitlab.grnet.gr/devs/agora/agora-sp/")

    def classification_information(self, required_only=False):
        """
        Fill in the fields of "Classification Information" area.

        @param required_only: Fill in only the required fields or not?
        @return: True if all goes well otherwise False.
        """
        # *.CLI.1 - Scientific Domain
        table_select_field(self.driver, self.fields_prefix + "cli_1_scientific_domain", 4)
        # *.CLI.2 - Scientific Subdomain
        table_select_field(self.driver, self.fields_prefix + "cli_2_scientific_subdomain", 15)
        # *.CLI.3 - Category
        table_select_field(self.driver, self.fields_prefix + "cli_3_category", 10)
        # *.CLI.4 - Subcategory
        table_select_field(self.driver, self.fields_prefix + "cli_4_subcategory", 22)

        if not required_only:
            # *.CLI.5 - Target Users
            table_select_field(self.driver, self.fields_prefix + "cli_5_target_users", 7)
            # *.CLI.6 - Access Types
            table_select_field(self.driver, self.fields_prefix + "cli_6_access_type", 1)
            # *.CLI.7 - Access Mode
            table_select_field(self.driver, self.fields_prefix + "cli_7_access_mode", 1)
            # *.CLI.8 - Tags
            input_field(self.driver, self.fields_prefix + "cli_8_tags", "selenium CLI,")

    def management_information(self, required_only=False):
        """
        Fill in the fields of "Management Information" area.

        @param required_only: Fill in only the required fields or not?
        @return: True if all goes well otherwise False.
        """
        # *.MGI.1 - Heldesk Webpage
        input_field(self.driver, self.fields_prefix + "mgi_1_helpdesk_webpage", "https://www.selenium.dev/helpdesk")
        # *.MGI.2 - User Manual
        input_field(self.driver, self.fields_prefix + "mgi_2_user_manual", "https://www.selenium.dev/userManual")
        # *.MGI.3 - Terms of Use
        input_field(self.driver, self.fields_prefix + "mgi_3_terms_of_use", "https://www.selenium.dev/terms-of-use")
        # *.MGI.4 - Privacy Policy
        input_field(self.driver, self.fields_prefix + "mgi_4_privacy_policy", "https://www.selenium.dev/accessPolicy")
        # *.MGI.5 - Access Policy
        input_field(self.driver, self.fields_prefix + "mgi_5_access_policy", "https://www.selenium.dev/policy")
        # *.MGI.6 - Service Level Agreement/Specification
        input_field(self.driver, self.fields_prefix + "mgi_6_sla_specification", "https://www.selenium.dev/sla")
        # *.MGI.7 - Training Information
        input_field(self.driver, self.fields_prefix + "mgi_7_training_information", "https://www.selenium.dev/training")
        # *.MGI.8 - Status Monitoring
        input_field(self.driver, self.fields_prefix + "mgi_8_status_monitoring", "https://www.selenium.dev/status")
        # *.MGI.9 - Maintenance
        input_field(self.driver, self.fields_prefix + "mgi_9_maintenance", "https://www.selenium.dev/maintenance")

    def geographical_and_language_availability_information(self, required_only=False):
        """
        Fill in the fields of "Geographical and Language Availability Information" area.

        @param required_only: Fill in only the required fields or not?
        @return: True if all goes well otherwise False.
        """
        # *.GLA.1 - Geographical Availability
        suggestion_input_field(self.driver, self.fields_prefix + "gla_1_geographical_availability", "Greece")
        # *.GLA.2 - Language
        suggestion_input_field(self.driver, self.fields_prefix + "gla_2_language", "el")

    def resource_location_information(self):
        """
        Fill in the fields of "Resource Location Information" area.

        @return: True if all goes well otherwise False.
        """
        # *.RLI.1 - Resource Geographic Location
        suggestion_input_field(self.driver, self.fields_prefix + "rli_1_geographic_location", "Greece")

    def contact_information(self, required_only=False):
        """
        Fill in the fields of "Contact Information" area.

        @param required_only: Fill in only the required fields or not?
        @return: True if all goes well otherwise False.
        """
        # Main Contact/Service Owner.
        suggestion_input_field(self.driver, "main_contact", "Owen Appleton")
        # Public Contact
        suggestion_input_field(self.driver, "public_contact", "Public Contact (EGI Foundation)")
        # *.COI.13 - Helpdesk Email
        input_field(self.driver, self.fields_prefix + "coi_13_helpdesk_email", "helpdesk@selenium.dev")
        # *.COI.14 - Security Contact Email
        input_field(self.driver, self.fields_prefix + "coi_14_security_contact_email", "security@selenium.dev")

    def maturity_information(self):
        """
        Fill in the fields of "Maturity Information" area.

        @return: True if all goes well otherwise False.
        """
        # *.ERP.MTI.1 - Technology Readinness Level
        suggestion_input_field(self.driver, self.fields_prefix + "mti_1_technology_readiness_level", "TRL1")
        # *.MTI.2 - Life Cycle Status
        suggestion_input_field(self.driver, self.fields_prefix + "mti_2_life_cycle_status", "Design")
        # *.MTI.3 - Certifications
        textarea_field(self.driver, self.fields_prefix + "mti_3_certifications", "Cert 1.")
        # *.MTI.4 - Standards
        textarea_field(self.driver, self.fields_prefix + "mti_4_standards", "Standard 1.")
        # *.MTI.5 - Open Source Technologies
        textarea_field(self.driver, self.fields_prefix + "mti_5_open_source_technologies", "GNU/Linux.")
        # *.ERP.MTI.6 - Version
        input_field(self.driver, self.fields_prefix + "mti_6_version", "v0.3")
        # *.ERP.MTI.7 - Last Update
        date_field(self.driver, self.fields_prefix + "mti_7_last_update")
        # *.MTI.8 - Changelog
        textarea_field(self.driver, self.fields_prefix + "mti_8_changelog", "Selenium 3.141.0 \n"
                                                         "https://github.com/SeleniumHQ/selenium/releases/tag"
                                                         "/selenium-3.141.0")

    def dependencies_information(self):
        """
        Fill in the fields of "Dependencies Information" area.

        @return: True if all goes well otherwise False.
        """
        # *.DEI.1 - Required Resources
        table_select_field(self.driver, "required_resources", 1)
        # *.DEI.2 - Related Resources
        table_select_field(self.driver, "related_resources", 1)
        # *.DEI.3 - Related Platforms
        input_field(self.driver, self.fields_prefix + "dei_3_related_platforms", "GNU/Linux")

    def attribution_information(self):
        """
        Fill in the fields of "Attribution Information" area.

        @return: True if all goes well otherwise False.
        """
        # *.ATI.1 - Funding Body
        table_select_field(self.driver, self.fields_prefix + "ati_1_funding_body", 45)
        # *.ATI.2 - Funding Program
        table_select_field(self.driver, self.fields_prefix + "ati_2_funding_program", 29)
        # *.ATI.3 - Grant/Project Name
        input_field(self.driver, self.fields_prefix + "ati_3_grant_project_name", "SELENIUM")

    def access_and_order_information(self):
        """
        Fill in the fields of "Access and Order Information" area.

        @return: True if all goes well otherwise False.
        """
        # *.AOI.1 - Order Type
        suggestion_input_field(self.driver, self.fields_prefix + "aoi_1_order_type", "Fully open access")
        # *.AOI.2 - Order
        input_field(self.driver, self.fields_prefix + "aoi_2_order", "https://www.selenium.dev/order")

    def financial_information(self):
        """
        Fill in the fields of "Financial Information" area.

        @return: True if all goes well otherwise False.
        """
        # *.FNI.1 - Payment Model
        input_field(self.driver, self.fields_prefix + "fni_1_payment_model", "https://www.selenium.dev/payments_model")
        # *.FNI.2 - Pricing
        input_field(self.driver, self.fields_prefix + "fni_2_pricing", "https://www.selenium.dev/pricing")
