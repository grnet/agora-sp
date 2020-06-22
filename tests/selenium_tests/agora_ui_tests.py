#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Filename: agora_unit_tests.py

__version__ = '0.3'
__copyright__ = 'Copyleft 2020, Agora UI tests'
__maintainer__ = 'Tas-sos'
__author__ = 'Tas-sos'
__email__ = 'tasos@admin.grnet.gr'

from agora.contacts.contact_form_validations import ContactFormValidations
from agora.contacts.contacts_create import ContactCreate
from agora.contacts.contacts_operations import ContactsOperations
from agora.providers.provider_create import CreateProvider
from agora.providers.provider_form_validations import ProviderFormValidations
from agora.providers.providers_operations import ProvidersOperations
from agora.resources.resource_create import ResourceCreate
from agora.resources.resource_form_validations import ResourceFormValidations
from agora.resources.resources_operations import ResourcesOperations
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL of the host to execute on the selenium tests", required=True)
    args = parser.parse_args()

    # Field Validations.
    ContactFormValidations("Firefox", headless=True, instance=args.url)
    ProviderFormValidations("Firefox", headless=True, instance=args.url)
    ResourceFormValidations("Firefox", headless=True, instance=args.url)

    # ListView operations.
    ContactsOperations("Firefox", headless=True, instance=args.url)
    ProvidersOperations("Firefox", headless=True, instance=args.url)
    ResourcesOperations("Firefox", headless=True, instance=args.url)

    # Create new records.
    contact = ContactCreate("Firefox", headless=True, instance=args.url)
    contact.create_new_contact()

    provider = CreateProvider("Firefox", headless=True, instance=args.url)
    provider.create_new_provider(required_only=False)

    resource = ResourceCreate("Firefox", headless=True, instance=args.url)
    resource.create_new_resource(required_only=False)
