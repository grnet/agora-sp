#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: save_responses.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def save_success(save_button):
    """
    Save a valid form.

    It tries to save the form and checks the response from the page.
    @return: True if the form returns an success message otherwise False.
    """
    # Wait at most 10 seconds.
    wait = WebDriverWait(save_button, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="save"]')))
    save_button.find_element_by_xpath('//button[text()="save"]').click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'toast-level-success')))
    form_response_message = save_button.find_element_by_class_name("toast-level-success").text.split("\n")[0]
    assert "Form Saved" in form_response_message
    if save_button.find_element_by_class_name("toast-level-success"):
        print("[Saving form status] {0:>30} \t\t{1}".format(form_response_message, "Success"))
        return True


def save_invalid(save_button):
    """
    Save a form with invalid input input fields.

    If the fields in the form are invalid :
        * an error message appears below the wrong field
        * the form will not be able saved and will return a invalid message: "Form Invalid".

    @return: True if the form returns an invalid message otherwise False.
    """
    # Wait at most 10 seconds.
    wait = WebDriverWait(save_button, 10)
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="save"]')))
    save_button.find_element_by_xpath('//button[text()="save"]').click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'toast-level-warning')))
    form_response_message = save_button.find_element_by_class_name("toast-level-warning").text.split("\n")[0]
    assert "Form Invalid" in form_response_message
    if save_button.find_element_by_class_name("toast-level-warning"):
        print("[Saving form status] {0:>32} \t\t{1}".format(form_response_message, "Success"))
        return True


def save_error():
    """
    TODO :
    @return:
    """
    pass
