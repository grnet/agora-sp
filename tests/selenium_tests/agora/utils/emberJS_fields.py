#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: emberJS_fields.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from time import sleep


def input_field(page, field_name, text, clear=False):
    """
    Function that fill in input fields.

    @param page: The object with which I can handle the page.
    @param field_name: The unique name of the input field with which you can search for it on the page.
    @param text: The text with which the field will be completed.
    @param clear: If it is true, it will clear it before it completes the field.
    @return: True if it finds the field and is completed without any problems or False if it cannot be found or
    supplemented.
    """
    # assert field_name in page.find_element_by_name(field_name)
    if clear:
        page.find_element_by_name(field_name).find_element_by_xpath("//input").clear()
        # page.find_element_by_name(field_name).clear()
    page.find_element_by_name(field_name).send_keys(text)
    print("{0:<40} Found and filled \t{1}".format('['+field_name+']', "Success"))


def suggestion_input_field(page, field_name, text):
    """
    Function that fill in input fields with "autocomplete" suggestions.

    @param page: The object with which I can handle the page.
    @param field_name: The unique name of the input field with which you can search for it on the page.
    @param text: The text with which the field will be completed.
    @return: True if it finds the field and is completed without any problems or False if it cannot be found or
    supplemented.
    """
    suggestion_input = page.find_element_by_xpath("//md-content[@data-form-field-name='" + field_name + "']")
    suggestion_input.find_element_by_tag_name("input").send_keys(text)
    page.find_element_by_tag_name("md-virtual-repeat-container").click()
    sleep(0.5)
    # assert field_name in page.find_element_by_name(field_name)
    print("{0:<40} Found and filled \t{1}".format('[' + field_name + ']', "Success"))


def textarea_field(page, field_name, text):
    """
    Function that fill in textarea fields.

    @param page: The object with which I can handle the page.
    @param field_name: The unique name of the input field with which you can search for it on the page.
    @param text: The text with which the field will be completed.
    @return: True if it finds the field and is completed without any problems or False if it cannot be found or
    supplemented.
    """
    textarea = page.find_element_by_xpath("//md-content[@data-form-field-name='" + field_name + "']")
    sleep(0.2)
    textarea.find_element_by_tag_name("iframe").click()
    textarea.find_element_by_tag_name("iframe").send_keys(text)
    sleep(0.5)
    # assert field_name in page.find_element_by_name(field_name)
    print("{0:<40} Found and filled \t{1}".format('[' + field_name + ']', "Success"))


def table_select_field(page, field_name, position):
    """
    Function that fill in EmberJS selecte table input fields.

    @param page: The object with which I can handle the page.
    @param field_name: The unique name of the input field with which you can search for it on the page.
    @param position: The position of the element to be selected.
    @return: True if it finds the field and is completed without any problems or False if it cannot be found or
    supplemented.
    """
    table = page.find_element_by_xpath("//md-content[@data-form-field-name='" + field_name + "']")
    table.find_element_by_tag_name("button").click()
    sleep(0.2)
    page.find_elements_by_class_name("md-checkbox")[position].click()
    page.find_element_by_xpath('//md-dialog-actions//button[text()="Add"]').click()
    sleep(0.5)
    # assert field_name in page.find_element_by_name(field_name)
    print("{0:<40} Found and filled \t{1}".format('[' + field_name + ']', "Success"))


def date_field(page, field_name):
    """
    Function that fill in EmberJS date input fields.

    @param page: The object with which I can handle the page.
    @param field_name: The unique name of the input field with which you can search for it on the page.
    @return: True if it finds the field and is completed without any problems or False if it cannot be found or
    supplemented.
    """
    page.find_element_by_xpath("//md-content[@data-form-field-name='" + field_name + "']").click()
    sleep(0.2)
    page.find_element_by_css_selector("[class='picker__footer']") \
        .find_element_by_xpath('//button[text()="Today"]').click()
    sleep(0.5)
    # assert field_name in page.find_element_by_name(field_name)
    print("{0:<40} Found and filled \t{1}".format('[' + field_name + ']', "Success"))


def checkbox_field(page, field_name):
    """
    Function that fill in EmberJS checkbox input fields.

    @param page: The object with which I can handle the page.
    @param field_name: The unique name of the checkbox input field with which you can search for it on the page.
    @return: True if it finds the field and is completed without any problems or False if it cannot be found or
    supplemented.
    """
    checkbox = page.find_element_by_xpath("//md-content[@data-form-field-name='" + field_name + "']")
    checkbox.find_element_by_tag_name("md-checkbox").click()
    # assert field_name in page.find_element_by_name(field_name)
    print("{0:<40} Found and filled \t{1}".format('[' + field_name + ']', "Success"))
