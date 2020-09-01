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
    wait = WebDriverWait(delete_button, 30)
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="delete"]'))).click()

    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="OK"]'))).click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'toast-level-success')))


def delete_from_listView(page):
    """
    Delete a record from ListView.

    @attention: ListView must be have only one record.
    @precondition: ListView should have only one entry/record, so it is advisable to use this method only when searching
    for a specific entry.
    @param page: The object with which I can handle the page.
    @return: If the record is deleted or not.
    """
    wait = WebDriverWait(page, 30)

    wait.until(EC.presence_of_element_located((By.XPATH, '//md-icon[text()="delete_forever"]'))).click()

    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="OK"]'))).click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'toast-level-success')))
