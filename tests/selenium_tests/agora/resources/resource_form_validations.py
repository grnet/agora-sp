#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: resource_form_validations.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from agora.resources.resource_create import ResourceCreate
from agora.validations.invalid_fields import url_input_validation, email_input_validation
from agora.validations.save_responses import save_invalid


class ResourceFormValidations(ResourceCreate):
    """
    Validation checks of resource form.

    Data validation checks in input fields. The fields are checked if they display the correct error message if they
    have wrong input data.
    """
    def __init__(self, driver, headless=True, instance="https://testvm.agora.grnet.gr/"):
        """
        Initialization.

        This method ensures that all the prerequisites will be met, so that the validations checks
        can be done correctly.
        @requires The required fields of the form must be filled, in order to avoid submission problems due to the
        required fields.
        @param driver: Which browser will be used.
        @param headless: If you want headless browser - without GUI.
        @param instance: The website instance of the Agora project to be used for the tests.
        """
        super().__init__(driver, headless, instance)
        print("\n# Validations in the Resource form.")
        self.valid_url_fields()
        self.valid_email_fields()
        save_invalid(self.driver)
        self.close()

    def valid_url_fields(self):
        """
        Check fields that require a valid URL.

        In these fields, invalid URLs are assigned and the purpose is to have the following two responses from form:
            1. Under these fields the message : "The field must be a valid url"
            2. When the form is submitted, we will get the message : "Form Invalid"
        @return: True if the messages for all fields appear, otherwise False.
        """
        # *.BAI.4 - Webpage
        url_input_validation(self.driver, self.fields_prefix + "bai_4_webpage")

        # *.MRI.3 - Logo
        url_input_validation(self.driver, self.fields_prefix + "mri_3_logo")
        # *.MRI.4 - Mulitimedia
        url_input_validation(self.driver, self.fields_prefix + "mri_4_mulitimedia")
        # *.MRI.5 - Use Cases
        url_input_validation(self.driver, self.fields_prefix + "mri_5_use_cases")

        # *.MGI.1 - Heldesk Page
        url_input_validation(self.driver, self.fields_prefix + "mgi_1_helpdesk_webpage")
        # *.MGI.2 - User Manual
        url_input_validation(self.driver, self.fields_prefix + "mgi_2_user_manual")
        # *.MGI.3 - Terms of Use
        url_input_validation(self.driver, self.fields_prefix + "mgi_3_terms_of_use")
        # *.MGI.4 - Privacy Policy
        url_input_validation(self.driver, self.fields_prefix + "mgi_4_privacy_policy")
        # *.MGI.5 - Access Policy
        url_input_validation(self.driver, self.fields_prefix + "mgi_5_access_policy")
        # *.MGI.6 - Service Level
        url_input_validation(self.driver, self.fields_prefix + "mgi_6_sla_specification")
        # *.MGI.7 - Training Information
        url_input_validation(self.driver, self.fields_prefix + "mgi_7_training_information")
        # *.MGI.8 - Status Monitoring
        url_input_validation(self.driver, self.fields_prefix + "mgi_8_status_monitoring")
        # *.MGI.9 - Maintenance
        url_input_validation(self.driver, self.fields_prefix + "mgi_9_maintenance")

        # *.AOI.2 - Order
        url_input_validation(self.driver, self.fields_prefix + "aoi_2_order")

        # ERP.FNI.1 - Payment Model
        url_input_validation(self.driver, self.fields_prefix + "fni_1_payment_model")
        # ERP.FNI.2 - Pricing
        url_input_validation(self.driver, self.fields_prefix + "fni_2_pricing")

    def valid_email_fields(self):
        """
        Check fields that require a valid Email.

        In these fields, invalid Email are assigned and the purpose is to have the following two responses from form:
            1. Under these fields the message : "The field must be a valid Email"
            2. When the form is submitted, we will get the message : "Form Invalid"
        @return: True if the messages for all fields appear, otherwise False.
        """
        # *.COI.13 - Helpdesk Email
        email_input_validation(self.driver, self.fields_prefix + "coi_13_helpdesk_email")
        # *.COI.14 - Security Contact Email
        email_input_validation(self.driver, self.fields_prefix + "coi_14_security_contact_email")

    # def delete(self):
    #     self.driver.find_element_by_xpath('//button[text()="delete"]').click()
    #     self.driver.find_element_by_xpath('//md-dialog-actions//button[text()="OK"]').click()
