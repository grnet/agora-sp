#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: contacts_create.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from agora.contacts.contacts import Contacts
from agora.utils.emberJS_fields import input_field, suggestion_input_field
from agora.validations.delete_responses import delete_success
from agora.validations.save_responses import save_success
from time import sleep


class ContactCreate(Contacts):
    """
    Create a new Contact Information.

    This class is responsible for checking the following:
        * Go to the crete a resource page ( https://testvm.agora.grnet.gr/ui/resources/create ).
        * Checks if all the following input fields of the form exist :
            - First Name
            - Last Name
            - Email
            - Phone
            - Position
            - Provider
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
        super().contacts_create_new_page()
        self.fields_prefix = "erp_"

    def create_new_contact(self):
        """
        Method of creating a new resource.

        The create new Resource page is here: https://testvm.agora.grnet.gr/ui/providers/create
        It calls all the methods they undertake to fill all the areas of the form.

        @return:
        """
        print("\n# Create a new contact.")
        self.basic_information()
        save_success(self.driver)
        delete_success(self.driver)
        self.close()

    def basic_information(self):
        """
        Fill in the fields of "Basic information" area.

        In this form, all fields are required.
        @return: True if all goes well otherwise False.
        """
        # First Name
        input_field(self.driver, "first_name", "selenium - First Name")
        # Last Name
        input_field(self.driver, "last_name", "selenium - Last Name")
        # Email
        input_field(self.driver, "email", "selenium@email.com")
        # Phone
        input_field(self.driver, "phone", "0123456789")
        # Position
        input_field(self.driver, "position", "Automatic UI tests")
        # Provider
        suggestion_input_field(self.driver, "organisation", "EGI Foundation")
