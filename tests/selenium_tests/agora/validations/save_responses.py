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
    # save_button.implicitly_wait(2)
    # Wait at most 10 seconds.
    wait = WebDriverWait(save_button, 300)
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="save"]')))
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, '//button[text()="save"]')))
    wait.until(EC.visibility_of_any_elements_located((By.XPATH, '//button[text()="save"]')))
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="save"]')))
    # wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="save"]')))
    wait.until(EC.element_to_be_clickable((By.XPATH, '//button[text()="save"]'))).click()
    # save_button.find_element_by_xpath('//button[text()="save"]').click()

    # save = save_button.find_element_by_xpath('//button[text()="save"]')
    # save_button.execute_script("arguments[0].click();", save)  # https://stackoverflow.com/a/37880313

    # wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'toast-level-success')))
    # form_response_message = save_button.find_element_by_class_name("toast-level-success").text.split("\n")[0]

    # save_button.implicitly_wait(2)
    print(save_button.current_url)
    # http://localhost:8000/ui/contact-information/f04bd82a-710e-4831-a3cc-7f5703d177b6
    # http://localhost:8000/ui/contact-information/dadd79d5-938e-481c-9bdb-a50d13eae106
    # http://localhost:8000/ui/contact-information/da205bfa-f618-427a-9378-d6676b1675a4
    # http://localhost:8000/ui/contact-information/3ab17c0a-a34a-435b-b496-1fe08f670363
    # http://localhost:8000/ui/contact-information/7392ad47-6f14-4a47-8be2-9eb430850800
    # http://localhost:8000/ui/providers/ddf79745-1bcb-4c3a-ae40-70b0700d3cd4/edit
    # http://localhost:8000/ui/resources/9d7100e6-92ec-4ae0-b5b3-83a905e46f2c/edit
    # print( UUID('f04bd82a-710e-4831-a3cc-7f5703d177b6').version )
    # print( UUID('3ab17c0a-a34a-435b-b496-1fe08f670363').version )

    uuid = None
    # Fix small bug.
    if save_button.current_url.split('/')[-1] == 'edit':
        uuid = save_button.current_url.split('/')[-2]
    else:
        uuid = save_button.current_url.split('/')[-1]

    regex = re.compile("^[0-9A-F]{8}-[0-9A-F]{4}-[1-5][0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$", re.IGNORECASE)
    if regex.match(uuid):
        print("[Saving form status] {0:>30} \t\t{1}".format("Form saved", "Success"))
        return True
    else:
        print("[Saving form status] {0:>38} \t{1}".format("Form was not saved", "Failed"))
        return False

    # wait.until(EC.element_to_be_clickable((By.XPATH, "//a//md-icon[@md-font-icon='edit']")))
    # form_response_message = save_button.find_element_by_xpath("//a//md-icon[@md-font-icon='edit']").text

    # assert "edit" in form_response_message
    # if form_response_message == 'edit':
    #     print("[Saving form status] {0:>30} \t\t{1}".format("Form Saved", "Success"))
    #     return True


def save_invalid(save_button):
    """
    Save a form with invalid input input fields.

    If the fields in the form are invalid :
        * an error message appears below the wrong field
        * the form will not be able saved and will return a invalid message: "Form Invalid".

    @return: True if the form returns an invalid message otherwise False.
    """
    # Wait at most 10 seconds.
    wait = WebDriverWait(save_button, 300)
    wait.until(EC.presence_of_element_located((By.XPATH, '//button[text()="save"]'))).click()
    # save_button.find_element_by_xpath('//button[text()="save"]').click()

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
