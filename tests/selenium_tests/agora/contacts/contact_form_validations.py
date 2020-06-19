#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: contact_form_validations.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from agora.contacts.contacts_create import ContactCreate
from agora.validations.invalid_fields import email_input_validation, phone_input_validation
from agora.validations.save_responses import save_invalid


class ContactFormValidations(ContactCreate):
    """
    Validation checks of Contact form.

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
        print("\n# Validations in the Contact form.")
        self.valid_email_fields()
        self.valid_phone_fields()
        save_invalid(self.driver)
        self.close()

    def valid_email_fields(self):
        """
        Check fields that require a valid Email.

        In these fields, invalid Email are assigned and the purpose is to have the following two responses from form:
            1. Under these fields the message : "The field must be a valid Email"
            2. When the form is submitted, we will get the message : "Form Invalid"
        @return: True if the messages for all fields appear, otherwise False.
        """
        email_input_validation(self.driver, "email")

    def valid_phone_fields(self):
        """
        Check fields that require a valid Phone.

        In these fields, invalid Phone are assigned and the purpose is to have the following two responses from form:
            1. Under these fields the message :
                -   "The field must be a number"
                -   "The field must be between 10 and 20 characters"
            2. When the form is submitted, we will get the message : "Form Invalid"
        @return: True if the messages for all fields appear, otherwise False.
        """
        phone_input_validation(self.driver, "phone")
