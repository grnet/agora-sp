from __future__ import unicode_literals

from django.db import models
from accounts.models import User as CustomUser
import uuid


class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True)
    address = models.CharField(max_length=255, default=None, blank=True, null=True)
    country = models.CharField(max_length=255, default=None, blank=True, null=True)
    department = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    def as_json(self):
        return {
            "uuid": self.id,
            "name": self.name,
            "address": self.address,
            "country": self.country,
            "department": self.department
        }


class ServiceOwner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    email = models.EmailField(default=None, blank=True)
    phone = models.CharField(max_length=255, default=None, blank=True, null=True)
    id_service_owner = models.ForeignKey(Institution)

    id_account = models.ForeignKey(CustomUser, null=True, blank=True, default=None)

    def __unicode__(self):
        return str(self.first_name) + " " + str(self.last_name)

    def get_institution(self):
        return Institution.objects.get(id=self.id_service_owner.pk).as_json()

    def as_json(self):
        return {
            "uuid": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "institution": self.id_service_owner.as_json(),
            "account_id": self.id_account_id
        }


class ContactInformation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    email = models.EmailField(default=None, blank=True, null=True)
    phone = models.CharField(max_length=255, default=None, blank=True, null=True)
    url = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.first_name) + " " + str(self.last_name)

    def as_json(self):
        return {
            "uuid": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "phone": self.phone,
            "url": self.url
        }


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


class AditionalUsernames(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_service_owner = models.ForeignKey(ServiceOwner)
    username = models.CharField(max_length=255, default=None, blank=True)

    def as_json(self):
        return {
            "uuid": self.id,
            "service_owner": self.id_service_owner,
            "username": self.username
        }
