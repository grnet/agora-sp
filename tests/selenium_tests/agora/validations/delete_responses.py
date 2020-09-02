#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: delete_responses.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def delete_success(delete_button):
    """
    Delete a saved form.

    It tries to delete the form and checks the response from the page.
    @return: True if the form returns an success message otherwise False.
    """
    # Wait at most 5 seconds.
    wait = WebDriverWait(delete_button, 5)
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="delete"]')))
    delete_button.find_element_by_xpath('//button[text()="delete"]').click()

    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="OK"]')))
    delete_button.find_element_by_xpath('//button[text()="OK"]').click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'toast-level-success')))
    form_response_message = delete_button.find_element_by_class_name("toast-level-success").text.split("\n")[0]

    assert "Form Saved" in form_response_message
    if delete_button.find_element_by_class_name("toast-level-success"):
        # Close toast-level-*
        delete_button.find_element_by_xpath('//md-toast//div//button[text()="close"]').click()
        print("[Delete form status] {0:>30} \t\t{1}".format(form_response_message, "Success"))
        return True


def delete_from_listView(page):
    """
    Delete a record from ListView.

    @attention: ListView must be have only one record.
    @precondition: ListView should have only one entry/record, so it is advisable to use this method only when searching
    for a specific entry.
    @param page: The object with which I can handle the page.
    @return: If the record is deleted or not.
    """
    wait = WebDriverWait(page, 5)

    wait.until(EC.presence_of_element_located((By.XPATH, '//md-icon[text()="delete_forever"]')))
    page.find_element_by_xpath('//md-icon[text()="delete_forever"]').click()

    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="OK"]')))
    page.find_element_by_xpath('//button[text()="OK"]').click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'toast-level-success')))
    form_response_message = page.find_element_by_class_name("toast-level-success").text.split("\n")[0]

    assert "Form Saved" in form_response_message
    if page.find_element_by_class_name("toast-level-success"):
        # Close toast-level-*
        page.find_element_by_xpath('//md-toast//div//button[text()="close"]').click()
        print("[Delete form status] {0:>30} \t\t{1}".format(form_response_message, "Success"))
        return True
