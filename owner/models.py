from __future__ import unicode_literals

from django.db import models
import uuid

class ServiceOwner(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    email = models.EmailField(default=None)
    phone = models.CharField(max_length=255, default=None)
    id_service_owner = models.ForeignKey(Institution)

class Institution(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None)
    address = models.CharField(max_length=255, default=None)
    country = models.CharField(max_length=255, default=None)
    department = models.CharField(max_length=255, default=None)

class ContactInformation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    email = models.EmailField(default=None)
    phone = models.CharField(max_length=255, default=None)
    url = models.CharField(max_length=255, default=None)

class Internal(models.Model):

    id_contact_info = models.ForeignKey(ContactInformation)

class External(models.Model):

    id_contact_info = models.ForeignKey(ContactInformation)