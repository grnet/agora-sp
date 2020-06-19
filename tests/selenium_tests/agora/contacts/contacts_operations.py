#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: contacts_operators.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from agora.contacts.contacts import Contacts


class ContactsOperations(Contacts):
    """
    Operations on list view of Contact Information.

    This class is responsible for checking the following:
        * Edit option on ContactsListView is available.
        * Details option on ContactsListView is available.
        * TODO : Delete
    """

    def __init__(self, driver, headless=True, instance="https://testvm.agora.grnet.gr/"):
        """
        Initialization.

        This method ensures that all the prerequisites will be met, so that you can go to Contact Information list view
        page.
        @param driver: Which browser will be used.
        @param headless: If you want headless browser - without GUI.
        @param instance: The website instance of the Agora project to be used for the tests.
        """
        super().__init__(driver, headless, instance)
        print("\n# Edit a contact record.")
        super().edit_from_listView()
        # Go again to Contact Information list view page.
        self.driver.find_element_by_xpath("//a[@href='/ui/contact-information']").click()
        print("\n# Details of a contact record.")
        super().details_from_listView()
        self.close()
