#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: provider_create.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from agora.providers.providers import Providers
from agora.utils.emberJS_fields import input_field, suggestion_input_field, table_select_field, textarea_field, \
    checkbox_field
from agora.validations.delete_responses import delete_success, delete_from_listView
from agora.validations.save_responses import save_success_double


class CreateProvider(Providers):
    """
    Create a new Provider.

    This class is responsible for checking the following:
        * Go to the crete a resource page ( https://testvm.agora.grnet.gr/ui/providers/create ).
        * Checks if all the following input fields of the form exist :
            Basic information
            - *.BAI.0 - ID
            - *.BAI.1 - Name
            - *.BAI.2 - Abbreviation
            - *.BAI.3 - Website
            - *.BAI.4 - Legal Entity
            - *.BAI.5 - Legal Status

            Classification Information
            - *.CLI.1 - Scientific Domain
            - *.CLI.2 - Scientific Subdomain
            - *.CLI.3 - Tags

            Location information
            - *.LOI.1 - Street Name and Number
            - *.LOI.2 - Postal Code
            - *.LOI.3 - City
            - *.LOI.4 - Region
            - *.LOI.5 - Country or Territory

            Marketing Information
            - *.MRI.1 - Description
            - *.MRI.2 - Logo
            - *.MRI.3 - Multimedia

            Maturity Information
            - *.MTI.1 - Life Cycle Status
            - *.MTI.2 - Certifications

            Contact Information
            Main Contact/Resource Owner
            Public Contact

            Other Information
            - *.OTH.1 - Hosting Legal Entity
            - *.OTH.2 - Participating Countries
            - *.OTH.3 - Affiliations
            - *.OTH.4 - Networks
            - *.OTH.5 - Structure Type
            - *.OTH.6 - ESFRI Domain
            - *.OTH.7 - ESFRI Type
            - *.OTH.8 - MERIL Scientific Domain
            - *.OTH.9 - MERIL Scientific Subdomain
            - *.OTH.10 - Areas of activity
            - *.OTH.11 - Societal Grand challenges
            - *.OTH.12 - National Roadmaps
        * Check submission form with only filling in the required form fields.
        * Check submission form with filling in all the form fields.
        * TODO : If the invalid messages improve, it should be better handled here as well.
        * TODO : If the warning messages improve, it should be better handled here as well.
        * TODO : If the error messages improve, it should be better handled here as well.
    """

    def __init__(self, driver, headless=True, instance="https://testvm.agora.grnet.gr/"):
        """
        Initialization.

        This method ensures that all the prerequisites will be met, so that you can go to create a new provider page.
        @param driver: Which browser will be used.
        @param headless: If you want headless browser - without GUI.
        @param instance: The website instance of the Agora project to be used for the tests.
        """
        super().__init__(driver, headless, instance)
        super().provider_create_new_page()
        self.fields_prefix = "epp_"

    def create_new_provider(self, required_only=False):
        """
        Method of creating a new provider.

        The create new provider page is here: https://testvm.agora.grnet.gr/ui/providers/create
        It calls all the methods they undertake to fill all the areas of the form.

        @param required_only: Fill in only the required fields or not?
        @return: True if all goes well otherwise False.
        """
        print("\n# Create a new provider.")
        self.basic_information(required_only)
        self.classification_information(required_only)
        self.location_information(required_only)
        self.marketing_information(required_only)
        if not required_only:
            self.maturity_information(required_only)
            self.contact_information(required_only)
            self.other_information(required_only)

        save_success_double(self.driver)

        # Search
        self.providers_page()
        self.search_field()
        delete_from_listView(self.driver)
        # delete_success(self.driver)
        self.close()

    def basic_information(self, required_only=False):
        """
        Fill in the fields of "Basic information" area.

        This method is responsible for filling in all the fields in the "Basic information" area from the
        "https://testvm.agora.grnet.gr/ui/providers/create" page.

        @param required_only: Fill in only the required fields or not?
        @return: True if all goes well otherwise False.
        """
        # *.BAI.0 - ID
        input_field(self.driver, self.fields_prefix + "bai_0_id", "selenium-PROVIDER")
        # *.BAI.1 - Name
        input_field(self.driver, self.fields_prefix + "bai_1_name", "SeleniumHQ Browser Automation - PROVIDER")
        # *.BAI.2 - Abbreviation
        input_field(self.driver, self.fields_prefix + "bai_2_abbreviation", "SeleniumHQ-PROVIDER")

        if not required_only:
            # *.BAI.3 - Website
            input_field(self.driver, self.fields_prefix + "bai_3_website", "https://www.selenium.dev")
            # *.BAI.4 - Legal Entity
            checkbox_field(self.driver, self.fields_prefix + "bai_4_legal_entity")
            # *.BAI.5 - Legal Status
            suggestion_input_field(self.driver, self.fields_prefix +  "bai_5_legal_status", "Foundation")


    def classification_information(self, required_only=False):
        """
        Fill in the fields of "Classification Information" area.

        This method is responsible for filling in all the fields in the "Classification Information" area from the
        "https://testvm.agora.grnet.gr/ui/providers/create" page.

        @param required_only: Fill in only the required fields or not?
        @return: True if all goes well otherwise False.
        """
        # *.CLi.1 - Scientific Domain
        table_select_field(self.driver, self.fields_prefix + "cli_1_scientific_domain", 3)
        # *.CLI.2 - Scientific Subdomain
        table_select_field(self.driver, self.fields_prefix + "cli_2_scientific_subdomain", 5)

        if not required_only:
            # *.CLI.3 - Tags
            input_field(self.driver, self.fields_prefix + "cli_3_tags", "selenium,")

    def location_information(self, required_only=False):
        """
        Fill in the fields of "Location information" area.

        This method is responsible for filling in all the fields in the "Location information" area from the
        "https://testvm.agora.grnet.gr/ui/providers/create" page.

        @param required_only: Fill in only the required fields or not?
        @return: True if all goes well otherwise False.
        """
        # *.LOI.1 - Street Name and Number
        input_field(self.driver, self.fields_prefix + "loi_1_street_name_and_number", "Λεωφ. Κηφισίας 7")
        # *.LOI.2 - Postal Code
        input_field(self.driver, self.fields_prefix + "loi_2_postal_code", "115 23")
        # *.LOI.3 - City
        input_field(self.driver, self.fields_prefix + "loi_3_city", "Αθήνα")
        # *.LOI.5 - Country or Territory
        suggestion_input_field(self.driver, self.fields_prefix + "loi_5_country_or_territory", "Greece")

        if not required_only:
            # *.LOI.4 - Region
            input_field(self.driver, self.fields_prefix + "loi_4_region", "Αττική")

    def marketing_information(self, required_only=False):
        """
        Fill in the fields of "Marketing Information" area.

        This method is responsible for filling in all the fields in the "Marketing Information" area from the
        "https://testvm.agora.grnet.gr/ui/providers/create" page.

        @param required_only: Fill in only the required fields or not?
        @return: True if all goes well otherwise False.
        """
        # *.MRI.1 - Description
        textarea_field(self.driver, self.fields_prefix + "mri_1_description", "Selenium - Περιγραφή.")
        # *.MRI.2 - Logo
        input_field(self.driver, self.fields_prefix + "mri_2_logo", "https://www.selenium.dev/images/selenium_logo_large.png")

        if not required_only:
            # *.MRI.3 - Multimedia
            input_field(self.driver, self.fields_prefix + "mri_3_multimedia", "https://github.com/SeleniumHQ/selenium")

    def maturity_information(self, required_only=False):
        """
        Fill in the fields of "Maturity Information" area.

        This method is responsible for filling in all the fields in the "Maturity Information" area from the
        "https://testvm.agora.grnet.gr/ui/providers/create" page.

        @param required_only: Fill in only the required fields or not?
        @return: True if all goes well otherwise False.
        """
        # *.MTI.1 - Life Cycle Status
        suggestion_input_field(self.driver, self.fields_prefix + "mti_1_life_cycle_status", "Other")

        # *.MTI.2 - Certifications
        input_field(self.driver, self.fields_prefix + "mti_2_certifications", "ISO-1234")

    def contact_information(self, required_only=False):
        """
        Fill in the fields of "Contact Information" area.

        This method is responsible for filling in all the fields in the "Contact Information" area from the
        "https://testvm.agora.grnet.gr/ui/providers/create" page.

        @param required_only: Fill in only the required fields or not?
        @return: True if all goes well otherwise False.
        """
        # Main Contact/Resource Owner
        suggestion_input_field(self.driver, "main_contact", "Owen Appleton")
        # Public Contact
        suggestion_input_field(self.driver, "public_contact", "Public Contact (EGI Foundation)")

    def other_information(self, required_only=False):
        """
        Fill in the fields of "Other Information" area.

        This method is responsible for filling in all the fields in the "Other Information" area from the
        "https://testvm.agora.grnet.gr/ui/providers/create" page.

        @param required_only: Fill in only the required fields or not?
        @return: True if all goes well otherwise False.
        """
        # *.OTH.1 - Hosting Legal Entity
        input_field(self.driver, self.fields_prefix + "oth_1_hosting_legal_entity", "Something")
        # *.OTH.2 - Participating Countries
        suggestion_input_field(self.driver, self.fields_prefix + "oth_2_participating_countries", "Greece")
        # *.OTH.3 - Affiliations
        table_select_field(self.driver, self.fields_prefix + "oth_3_affiliations", 5)
        # *.OTH.4 - Networks
        table_select_field(self.driver, self.fields_prefix + "oth_4_networks", 25)
        # *.OTH.5 - Structure Type
        table_select_field(self.driver, self.fields_prefix + "oth_5_structure_type", 1)
        # *.OTH.6 - ESFRI Domain
        table_select_field(self.driver, self.fields_prefix + "oth_6_esfri_domain", 3)
        # *.OTH.7 - ESFRI Type
        suggestion_input_field(self.driver, self.fields_prefix + "oth_7_esfri_type", "Not an ESFRI project or landmark")
        # *.OTH.8 - MERIL Scientific Domain
        table_select_field(self.driver, self.fields_prefix + "oth_8_meril_scientific_domain", 1)
        # *.OTH.9 - MERIL Scientific Subdomain
        table_select_field(self.driver, self.fields_prefix + "oth_9_meril_scientific_subdomain", 5)
        # *.OTH.10 - Areas of activity
        table_select_field(self.driver, self.fields_prefix + "oth_10_areas_of_activity", 2)
        # *.OTH.11 - Societal Grand challenges
        table_select_field(self.driver, self.fields_prefix + "oth_11_societal_grand_challenges", 5)
        # *.OTH.12 - National Roadmaps
        input_field(self.driver, self.fields_prefix + "oth_12_national_roadmaps", "SELENIUM")

