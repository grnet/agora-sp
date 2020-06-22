#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: delete_responses.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from time import sleep


def delete_success(delete_button):
    """
    Delete a saved form.

    It tries to delete the form and checks the response from the page.
    @return: True if the form returns an success message otherwise False.
    """
    sleep(0.5)
    delete_button.find_element_by_xpath('//button[text()="delete"]').click()
    sleep(1)

    delete_button.find_element_by_xpath('//button[text()="OK"]').click()
    sleep(0.5)
    form_response_message = delete_button.find_element_by_class_name("toast-level-success").text.split("\n")[0]
    assert "Form Saved" in form_response_message
    if delete_button.find_element_by_class_name("toast-level-success"):
        print("[Delete form status] {0:>30} \t\t{1}".format(form_response_message, "Success"))
        return True
