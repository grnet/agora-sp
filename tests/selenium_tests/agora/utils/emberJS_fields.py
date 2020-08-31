#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: emberJS_fields.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


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
    wait = WebDriverWait(page, 50)
    wait.until(EC.presence_of_element_located((By.XPATH, "//md-content[@data-form-field-name='" + field_name + "']")))

    suggestion_input = page.find_element_by_xpath("//md-content[@data-form-field-name='" + field_name + "']")
    suggestion_input.find_element_by_tag_name("input").send_keys(text)
    page.find_element_by_tag_name("md-virtual-repeat-container").click()

    # Fix - Release field.
    page.find_element_by_xpath("//body").click()
    #sleep(0.1)

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
    wait = WebDriverWait(page, 50)
    wait.until(EC.presence_of_element_located((By.XPATH, "//md-content[@data-form-field-name='" + field_name + "']")))
    textarea = page.find_element_by_xpath("//md-content[@data-form-field-name='" + field_name + "']")

    wait.until(EC.presence_of_element_located((By.TAG_NAME, "iframe")))
    textarea.find_element_by_tag_name("iframe").click()
    textarea.find_element_by_tag_name("iframe").send_keys(text)

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
    wait = WebDriverWait(page, 50)
    wait.until(EC.visibility_of_element_located((By.XPATH,
                                   "//md-content[@data-form-field-name='" + field_name + "']//button[text()='add']")))
    wait.until(EC.element_to_be_clickable((By.XPATH,
                                   "//md-content[@data-form-field-name='" + field_name + "']//button[text()='add']"))).click()
    # sleep(2)
    # page.find_element_by_xpath("//md-content[@data-form-field-name='" + field_name + "']//button[text()='add']").click()

    wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "md-checkbox")))
    # wait.until(EC.visibility_of_all_elements_located((By.TAG_NAME, "md-dialog")))
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//md-dialog-content//tr//md-checkbox")))
    wait.until(EC.element_to_be_clickable((By.XPATH, "//md-dialog//md-checkbox")))
    wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "md-checkbox")))
    #sleep(15)

    want = page.find_elements_by_xpath("//md-dialog-content//tr")[position]
    print(want.text)

    # page.find_elements_by_class_name("md-checkbox")[position].click()
    # wait.until(EC.element_to_be_clickable((By.XPATH, "//md-dialog//md-checkbox")))[position].click()
    wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//md-dialog//md-checkbox")))[position].click()
    page.find_element_by_xpath('//md-dialog-actions//button[text()="Add"]').click()

    # Fix - Release field.
    page.find_element_by_xpath("//body").click()
    #sleep(0.1)

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
    wait = WebDriverWait(page, 50)
    wait.until(EC.presence_of_element_located((By.XPATH, "//md-content[@data-form-field-name='" + field_name + "']")))
    page.find_element_by_xpath("//md-content[@data-form-field-name='" + field_name + "']").click()

    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "[class='picker__footer']")))
    page.find_element_by_css_selector("[class='picker__footer']") \
        .find_element_by_xpath('//button[text()="Today"]').click()

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
    wait = WebDriverWait(page, 50)
    wait.until(EC.presence_of_element_located((By.XPATH, "//md-content[@data-form-field-name='" + field_name + "']")))
    checkbox = page.find_element_by_xpath("//md-content[@data-form-field-name='" + field_name + "']")
    checkbox.find_element_by_tag_name("md-checkbox").click()
    # assert field_name in page.find_element_by_name(field_name)
    print("{0:<40} Found and filled \t{1}".format('[' + field_name + ']', "Success"))

