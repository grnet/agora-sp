from __future__ import unicode_literals
import uuid
from django.db import models
from accounts.models import User as CustomUser, Organisation

class Institution(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True, unique=True)
    address = models.CharField(max_length=255, default=None, blank=True, null=True)
    country = models.CharField(max_length=255, default=None, blank=True, null=True)
    department = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)


class ServiceOwner(models.Model):
    """
    Unused model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    last_name = models.CharField(max_length=255, default=None, blank=True, null=True)
    email = models.EmailField(default=None, blank=True, unique=True)
    phone = models.CharField(max_length=255, default=None, blank=True, null=True)
    id_service_owner = models.ForeignKey(Institution, null=True)
    id_account = models.ForeignKey(CustomUser, null=True, blank=True, default=None)


class ContactInformation(models.Model):
    id = models.UUIDField(              primary_key=True,   default=uuid.uuid4,     editable=False)
    first_name = models.CharField(      verbose_name='PD.COI.1',     max_length=50,  default=None,   blank=False,    null=True)
    last_name = models.CharField(       verbose_name='PD.COI.2',     max_length=50,  default=None,   blank=False,    null=True)
    email = models.EmailField(          verbose_name='PD.COI.3',     default=None,   blank=False,    null=False)
    phone = models.CharField(           verbose_name='PD.COI.4',     max_length=20,  default=None,   blank=True, null=True)
    position = models.CharField(        verbose_name='PD.COI.5',     max_length=50,  default=None,   blank=True, null=True)
    organisation = models.ForeignKey(   verbose_name='PD.COI.1',     Organisation,   related_name="contacts")

class Internal(models.Model):
    """
    Unused model
    """
    id_contact_info = models.ForeignKey(ContactInformation)


class External(models.Model):
    """
    Unused model
    """
    id_contact_info = models.ForeignKey(ContactInformation)


class AditionalUsernames(models.Model):
    """
    Unused model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_service_owner = models.ForeignKey(ServiceOwner)
    username = models.CharField(max_length=255, default=None, blank=True)
