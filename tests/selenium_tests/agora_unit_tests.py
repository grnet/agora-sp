#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: agora_unit_tests.py

__version__ = '0.5'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

import unittest
import os
import argparse
import pytest

from agora.contacts.contacts_operations import ContactsOperations
from agora.providers.provider_create import CreateProvider
from agora.providers.providers_operations import ProvidersOperations
from agora.resources.resource_create import ResourceCreate
from agora.contacts.contacts_create import ContactCreate
from agora.contacts.contact_form_validations import ContactFormValidations
from agora.providers.provider_form_validations import ProviderFormValidations
from agora.resources.resource_form_validations import ResourceFormValidations
from agora.resources.resources_operations import ResourcesOperations

@pytest.mark.usefixtures("driver_class")
class AgoraUI(unittest.TestCase):
  def setUp(self):
    super().setUp()

  # Field Validations.
  def test_contact_form_validations(self):
    ContactFormValidations("Firefox", headless=True, instance="http://localhost:3333/")
    assert True

  def test_provider_form_validations(self):
    ProviderFormValidations("Firefox", headless=True, instance="http://localhost:3333/")
    assert True

  def test_resource_form_validations(self):
    ResourceFormValidations("Firefox", headless=True, instance="http://localhost:3333/")
    assert True


  # ListView operations.
  def test_contacts_operations(self):
    ContactsOperations("Firefox", headless=True, instance="http://localhost:3333/")
    assert True

  def test_providers_operations(self):
    ProvidersOperations("Firefox", headless=True, instance="http://localhost:3333/")
    assert True

  def test_resources_operations(self):
    ResourcesOperations("Firefox", headless=True, instance="http://localhost:3333/")
    assert True


  # Create new records.
  def test_contact_create(self):
    contact = ContactCreate("Firefox", headless=True, instance="http://localhost:3333/")
    contact.create_new_contact()
    assert True

  def test_provider_create(self):
    provider = CreateProvider("Firefox", headless=True, instance="http://localhost:3333/")
    provider.create_new_provider(required_only=False)
    assert True

  def test_resource_create(self):
    resource = ResourceCreate("Firefox", headless=True, instance="http://localhost:3333/")
    resource.create_new_resource(required_only=False)
    assert True


  def tearDown(self):
    super().tearDown()


if __name__ == '__main__':
  unittest.main()
