#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: providers.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from agora.Agora import Agora
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Providers(Agora):
    """
    Automated tests at Providers in the Agora project.

    This class is responsible for checking the following:
        * Providers (left) menu.
        * Go to the Providers page ( https://testvm.agora.grnet.gr/ui/providers ).
        * Create new provider link.
        * TODO : Providers view details.
        * TODO : Providers edit a already exist record.
        * TODO : Providers delete a already exist record.
    """

    def __init__(self, driver, headless=True, instance="https://testvm.agora.grnet.gr/"):
        """
        Initialization.

        This method ensures that all the prerequisites will be met, so that you can go to Providers page.
        @param driver: Which browser will be used.
        @param headless: If you want headless browser - without GUI.
        @param instance: The website instance of the Agora project to be used for the tests.
        """
        super().__init__(driver, headless, instance)
        self.providers_page()

    def providers_page(self):
        """
        Private method which is responsible for going to the Providers page.

        The Providers page is here: https://testvm.agora.grnet.gr/ui/providers
        @requires the successful execution of the following methods :
            1. basic_authentication
        """
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/ui/providers']")))
        self.driver.find_element_by_xpath("//a[@href='/ui/providers']").click()

    def provider_create_new_page(self):
        """
        Method which is responsible for going to the create a Provider page.

        The create new Provider page is here: https://testvm.agora.grnet.gr/ui/providers/create
        @requires the successful execution of the following methods :
            1. basic_authentication
            2. providers_page
        Checks if the following exist:
            - Create (href)
        """
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//a[@href='/ui/providers/create']")))
        self.driver.find_element_by_xpath("//a[@href='/ui/providers/create']").click()
