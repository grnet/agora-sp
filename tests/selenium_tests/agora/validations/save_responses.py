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
import re


def save_success(save_button):
    """
    Save a valid form.

    It tries to save the form and checks the response from the page.
    @return: True if the form returns an success message otherwise False.
    """
    # Wait at most 10 seconds.
    wait = WebDriverWait(save_button, 30)
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//button[text()="save"]')))
    wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//button[text()="save"]')))
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="save"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="save"]'))).click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//a//md-icon[@md-font-icon='edit']")))

def save_success_double(save_button):
    """
    Save a valid form.

    It tries to save the form and checks the response from the page.
    @return: True if the form returns an success message otherwise False.
    """
    # Wait at most 10 seconds.
    wait = WebDriverWait(save_button, 30)
    
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//button[text()="save"]')))
    wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//button[text()="save"]')))
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="save"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="save"]'))).click()

    wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//button[text()="save"]')))
    wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//button[text()="save"]')))
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="save"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="save"]'))).click()

    wait.until(EC.element_to_be_clickable((By.XPATH, "//a//md-icon[@md-font-icon='edit']")))

def save_invalid(save_button):
    """
    Save a form with invalid input input fields.

    If the fields in the form are invalid :
        * an error message appears below the wrong field
        * the form will not be able saved and will return a invalid message: "Form Invalid".

    @return: True if the form returns an invalid message otherwise False.
    """
    # Wait at most 10 seconds.
    wait = WebDriverWait(save_button, 30)
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="save"]'))).click()

    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'toast-level-warning')))


def save_error():
    """
    TODO :
    @return:
    """
    pass
