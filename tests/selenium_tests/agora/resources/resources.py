#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: resources.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from agora.Agora import Agora
from time import sleep
from abc import abstractmethod


class Resources(Agora):
    """
    Automated tests at Resources in the Agora project.

    This class is responsible for checking the following:
        * Resource (left) menu.
        * Go to the Resource page ( https://testvm.agora.grnet.gr/ui/resources ).
        * Create new resource link.
        * TODO : Resources view details.
        * TODO : Resources edit a already exist record.
        * TODO : Resources delete a already exist record.
    """

    def __init__(self, driver, headless=True, instance="https://testvm.agora.grnet.gr/"):
        """
        Initialization.

        This method ensures that all the prerequisites will be met, so that you can go to Resource page.
        @param driver: Which browser will be used.
        @param headless: If you want headless browser - without GUI.
        @param instance: The website instance of the Agora project to be used for the tests.
        """
        super().__init__(driver, headless, instance)
        self.resources_page()

    def resources_page(self):
        """
        Private method which is responsible for going to the Resources page.

        The Resources page is here: https://testvm.agora.grnet.gr/ui/resources
        @requires the successful execution of the following methods :
            1. basic_authentication
        """
        sleep(self.sleep_time)
        self.driver.find_element_by_xpath("//a[@href='/ui/resources']").click()
        sleep(self.sleep_time)

    def resources_create_new_page(self):
        """
        Method which is responsible for going to the create a Resource page.

        The create new Resource page is here: https://testvm.agora.grnet.gr/ui/resources/create
        @requires the successful execution of the following methods :
            1. basic_authentication
            2. resources_page
        Checks if the following exist:
            - Create (href)
        """
        assert "create" in self.driver.find_element_by_xpath("//a[@href='/ui/resources/create']").text
        self.driver.find_element_by_xpath("//a[@href='/ui/resources/create']").click()
        sleep(self.sleep_time)

