#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: provider_form_validations.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from agora.providers.provider_create import CreateProvider
from agora.validations.invalid_fields import url_input_validation
from agora.validations.save_responses import save_invalid


class ProviderFormValidations(CreateProvider):
    """
    Validation checks of provider form.

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
        print("\n# Validations in the Provider form.")
        self.valid_url_fields()
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
        # *.BAI.3 - Website
        url_input_validation(self.driver, self.fields_prefix + "bai_3_website")
        # *.MRI.2 - Logo
        url_input_validation(self.driver, self.fields_prefix + "mri_2_logo")
        # *.MRI.3 - Multimedia
        url_input_validation(self.driver, self.fields_prefix + "mri_3_multimedia")
