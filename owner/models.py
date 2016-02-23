from __future__ import unicode_literals

from django.db import models
import uuid

class Institution(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None)
    address = models.CharField(max_length=255, default=None)
    country = models.CharField(max_length=255, default=None)
    department = models.CharField(max_length=255, default=None)

    def __unicode__(self):
        return str(self.name)

class ServiceOwner(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    email = models.EmailField(default=None)
    phone = models.CharField(max_length=255, default=None)
    id_service_owner = models.ForeignKey(Institution)

    def __unicode__(self):
        return str(self.first_name) + " " + str(self.last_name)

class ContactInformation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, default=None)
    last_name = models.CharField(max_length=255, default=None)
    email = models.EmailField(default=None)
    phone = models.CharField(max_length=255, default=None)
    url = models.CharField(max_length=255, default=None)

    def __unicode__(self):
        return str(self.first_name) + " " + str(self.last_name)

class Internal(models.Model):

    id_contact_info = models.ForeignKey(ContactInformation)

    def __unicode__(self):
        cont_info = ContactInformation.objects.get(pk=self.id_contact_info.pk)
        return str(cont_info)

class External(models.Model):

    id_contact_info = models.ForeignKey(ContactInformation)

    def __unicode__(self):
        cont_info = ContactInformation.objects.get(pk=self.id_contact_info.pk)
        return str(cont_info)