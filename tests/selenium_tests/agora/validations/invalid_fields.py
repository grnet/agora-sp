#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: invalid_fields.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def url_input_validation(page, field_name):
    """
    Function that checks if the received field displays an invalid URL error message.

    @param page: The object with which I can handle the page.
    @param field_name: The unique name of the input field with which you can search for it on the page.
    @note: If there are more than one field, then a loop could be created so that all fields can be managed in one way.
    @return: True if it appears below the field, the message that should appear or False if it does not appear.
    """
    wait = WebDriverWait(page, 50)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='" + field_name + "']")))
    input_field = page.find_element_by_xpath("//input[@name='" + field_name + "']")
    input_field.clear()
    input_field.send_keys("123")

    field = input_field.find_element_by_xpath("./..")
    error_message = field.find_element_by_class_name("paper-input-error")
    if error_message:
        assert "The field must be a valid url" in error_message.text
        print("{0:<36} URL Input Validation \t{1}".format('[' + field.text.split()[0] + ']', "Success"))
        return True
    else:
        print("[{0}] \t\t URL Input Validation \t\t{1}".format(field.text.split()[0], "Failed"))
        return False


def email_input_validation(page, field_name):
    """
    Function that checks if the received field displays an invalid Email error message.

    @param page: The object with which I can handle the page.
    @param field_name: The unique name of the input field with which you can search for it on the page.
    @note: If there are more than one field, then a loop could be created so that all fields can be managed in one way.
    @return: True if it appears below the field, the message that should appear or False if it does not appear.
    """
    wait = WebDriverWait(page, 50)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='" + field_name + "']")))
    input_field = page.find_element_by_xpath("//input[@name='" + field_name + "']")
    input_field.clear()
    input_field.send_keys("123")

    # message = input_field.find_element_by_xpath("./..").find_element_by_class_name("paper-input-error")
    field = input_field.find_element_by_xpath("./..")
    error_message = field.find_element_by_class_name("paper-input-error")
    if error_message:
        assert "The field must be a valid email address" in error_message.text
        print("{0:<36} Email Input Validation \t{1}".format('[' + field.text.split()[0] + ']', "Success"))
        return True
    else:
        print("[{0}] Email Input Validation \t{1}".format(field.text.split()[0], "Failed"))
        return False


def phone_input_validation(page, field_name):
    """
    Function that checks if the received field displays an invalid number error message.

    @param page: The object with which I can handle the page.
    @param field_name: The unique name of the input field with which you can search for it on the page.
    @note: If there are more than one field, then a loop could be created so that all fields can be managed in one way.
    @return: True if it appears below the field, the message that should appear or False if it does not appear.
    """
    wait = WebDriverWait(page, 50)
    wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='" + field_name + "']")))
    input_field = page.find_element_by_xpath("//input[@name='" + field_name + "']")
    input_field.clear()
    input_field.send_keys("GNU/Linux")

    field = input_field.find_element_by_xpath("./..")
    error_messages = field.find_elements_by_class_name("paper-input-error")
    if error_messages:
        assert "The field must be a number" in error_messages[0].text
        assert "The field must be between 10 and 20 characters" in error_messages[1].text
        print("{0:<36} Phone Input Validation \t{1}".format('[' + field.text.split()[0] + ']', "Success"))
        return True
    else:
        print("[{0}] \t\t Phone Input Validation \t{1}".format(field.text.split()[0], "Failed"))
        return False
