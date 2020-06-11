#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: Agora.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from abc import ABC
import sys
import unittest
from time import sleep
from selenium import webdriver


class Agora(ABC, unittest.TestCase):
    """
    Automatic UI tests for Agora project with Selenium

    The tests are done in some instance of Agora project.
    TODO: driver for Windows & MacOS.
    """
    def __init__(self, driver='Firefox', headless=True, instance="https://testvm.agora.grnet.gr/"):
        """
        Selenium initialization.

        Undertakes user connection to the website.

        @param driver: The driver ( browser ) to be used.
        @param headless: If you want headless browser - without GUI.
        @param instance: The website instance of the Agora project to be used for the tests.
        """
        super().__init__()

        if driver == 'Firefox':
            if headless:
                from selenium.webdriver.firefox.options import Options
                options = Options()
                options.headless = True
                self.driver = webdriver.Firefox(options=options,
                                                executable_path='./webDriver_binaries/linux64/geckodriver')
            else:
                self.driver = webdriver.Firefox(executable_path='./webDriver_binaries/linux64/geckodriver')

        elif driver == 'Chrome':
            if headless:
                from selenium.webdriver.chrome.options import Options
                options = Options()
                options.headless = True
                self.driver = webdriver.Firefox(options=options,
                                                executable_path='./webDriver_binaries/linux64/chromedriver_73.0.3683.68')
            else:
                self.driver = webdriver.Chrome(executable_path='./webDriver_binaries/linux64/chromedriver_73.0.3683.68')
        else:
            sys.exit("I don't know what driver you want!")

        self.page = instance
        self.sleep_time = 0.5

        self.basic_authentication()

    def basic_authentication(self):
        """
        Basic Authentication on Agora project.

        This method connects a user with his credentials in each instance you choose to do the tests.
        @return:
        """
        self.driver.get(self.page + "ui/auth/login")
        sleep(2)

        # Fill the input fields.
        self.driver.find_element_by_name("identification").send_keys("superadmin")
        self.driver.find_element_by_name("password").send_keys("12345")

        # Click to "LOGIN" button.
        self.driver.find_element_by_xpath('//md-content//button[text()="login"]').click()
        sleep(2)

    def edit_from_listView(self):
        """
        Method which is responsible to go to the edit page from the first record of a list view.

        The edit page of a record from list view is here: https://testvm.agora.grnet.gr/ui/SOMETHIG/58.../edit
        @requires the successful execution of the following methods :
            1. basic_authentication
            2. contacts_page
        """
        # assert "create" in self.driver.find_element_by_xpath("//a[@href='/ui/contact-information/create']").text
        actions = self.driver.find_element_by_css_selector("[class='row-actions ember-view md-cell']")
        actions.find_elements_by_css_selector("[class='gen-action']")[1].click()
        print("{0:<40} Found and visited \t{1}".format('[Edit page]', "Success"))

    def details_from_listView(self):
        """
        Method which is responsible to go to the detail page from the first record of a list view.

        The edit page of a record from list view is here: https://testvm.agora.grnet.gr/ui/SOMETHIG/58...
        @requires the successful execution of the following methods :
            1. basic_authentication
            2. contacts_page
        """
        # assert "create" in self.driver.find_element_by_xpath("//a[@href='/ui/contact-information/create']").text
        actions = self.driver.find_element_by_css_selector("[class='row-actions ember-view md-cell']")
        actions.find_elements_by_css_selector("[class='gen-action']")[0].click()
        print("{0:<40} Found and visited \t{1}".format('[Details page]', "Success"))

    def listView_operations(self):
        pass

    def close(self):
        """
        Just close the browser window.
        """
        self.driver.close()
        self.driver.quit()
