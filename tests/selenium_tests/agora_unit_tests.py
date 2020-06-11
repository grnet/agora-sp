#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: agora_unit_tests.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

import unittest

from agora.providers.provider_create import CreateProvider
from agora.resources.resource_create import ResourceCreate
from agora.contacts.contacts_create import ContactCreate
from agora.contacts.contact_form_validations import ContactFormValidations
from agora.providers.provider_form_validations import ProviderFormValidations
from agora.resources.resource_form_validations import ResourceFormValidations


class AgoraUI(unittest.TestCase):

    def setUp(self):
        super().setUp()

    def test_contacts_validations(self):
        ContactFormValidations("Firefox", headless=True, instance="https://testvm.agora.grnet.gr/")

    def test_contacts_creation(self):
        contact = ContactCreate("Firefox", headless=True, instance="https://testvm.agora.grnet.gr/")
        contact.create_new_contact()

    def test_providers_validations(self):
        ProviderFormValidations("Firefox", headless=True, instance="https://testvm.agora.grnet.gr/")

    def test_providers_creation(self):
        provider = CreateProvider("Firefox", headless=True, instance="https://testvm.agora.grnet.gr/")
        provider.create_new_provider(required_only=True)

    def test_resources_validations(self):
        ResourceFormValidations("Firefox", headless=True, instance="https://testvm.agora.grnet.gr/")

    def test_resources_creation(self):
        resource = ResourceCreate("Firefox", headless=True, instance="https://testvm.agora.grnet.gr/")
        resource.create_new_resource(required_only=True)

    def tearDown(self):
        super().tearDown()


if __name__ == '__main__':
    unittest.main()
