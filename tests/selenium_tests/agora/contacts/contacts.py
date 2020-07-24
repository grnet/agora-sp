#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: contacts.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'


from agora.Agora import Agora
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Contacts(Agora):
    """
    Automated tests at Contacts in the Agora project.

    This class is responsible for checking the following:
        * Owners -> Contact Information (left) menu.
        * Go to the Contact Information page ( https://testvm.agora.grnet.gr/ui/contact-information ).
        * Create new Contact Information link.
        * TODO : Contact view details.
        * TODO : Contact edit a already exist record.
        * TODO : Contact delete a already exist record.
    """

    def __init__(self, driver, headless=True, instance="https://testvm.agora.grnet.gr/"):
        """
        Initialization.

        This method ensures that all the prerequisites will be met, so that you can go to Contact Information page.
        @param driver: Which browser will be used.
        @param headless: If you want headless browser - without GUI.
        @param instance: The website instance of the Agora project to be used for the tests.
        """
        super().__init__(driver, headless, instance)
        self.contacts_page()

    def contacts_page(self):
        """
        Private method which is responsible for going to the Contact Information page.

        The Contact Information is here: https://testvm.agora.grnet.gr/ui/contact-information
        @requires the successful execution of the following methods :
            1. basic_authentication
        """
        # Owners
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[class=' group-item menu-item ember-view md-clickable']")))
        # self.wait.until(EC.element_to_be_clickable((By.TAG_NAME, "md-list-item")))
        self.driver.find_elements_by_tag_name("md-list-item")[3].click()
        # Contact Information
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/ui/contact-information']")))
        self.driver.find_element_by_xpath("//a[@href='/ui/contact-information']").click()

    def contacts_create_new_page(self):
        """
        Method which is responsible for going to the create a Contact Information page.

        The create new Contact Information page is here: https://testvm.agora.grnet.gr/ui/contact-information/create
        @requires the successful execution of the following methods :
            1. basic_authentication
            2. contacts_page
        Checks if the following exist:
            - Create (href)
        """
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/ui/contact-information/create']")))
        assert "create" in self.driver.find_element_by_xpath("//a[@href='/ui/contact-information/create']").text
        self.driver.find_element_by_xpath("//a[@href='/ui/contact-information/create']").click()
