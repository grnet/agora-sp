from __future__ import unicode_literals
import uuid
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from service.models import Service, ServiceDetails

class ServiceOption(models.Model):
    """
    Unused model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True, unique=True)
    description = RichTextUploadingField(default=None, blank=True, null=True)
    pricing = models.CharField(max_length=255, default=None, blank=True, null=True)


class SLA(models.Model):
    """
    Unused model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_option_id = models.ForeignKey(ServiceOption, null=True)
    name = models.CharField(max_length=255, default=None, blank=True, unique=True)


class Parameter(models.Model):
    """
    Unused model
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True, unique=True)
    type = models.CharField(max_length=255, default=None, blank=True, null=True)
    expression = models.CharField(max_length=255, default=None, blank=True, null=True)


class SLAParameter(models.Model):
    """
    Unused model
    """

    class Meta:
        unique_together = (('parameter_id', 'sla_id', 'service_option_id'),)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parameter_id = models.ForeignKey(Parameter)
    sla_id = models.ForeignKey(SLA)
    service_option_id = models.ForeignKey(ServiceOption)


class ServiceDetailsOption(models.Model):
    """
    Unused model
    """
    class Meta:
        unique_together = (('service_id', 'service_details_id', 'service_options_id'),)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_id = models.ForeignKey(Service)
    service_details_id = models.ForeignKey(ServiceDetails)
    service_options_id = models.ForeignKey(ServiceOption)
