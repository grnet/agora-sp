from __future__ import unicode_literals

import uuid
from django.db import models
from service.models import Service, ServiceDetails

class ServiceOption(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)
    pricing = models.CharField(max_length=255, default=None)


class SLA(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_option_id = models.ForeignKey(ServiceOption)
    name = models.CharField(max_length=255, default=None)


class Parameter(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None)
    type = models.CharField(max_length=255, default=None)
    expression = models.CharField(max_length=255, default=None)


class SLAParameter(models.Model):
    class Meta:
        unique_together = (('parameter_id', 'sla_id', 'service_option_id'),)

    parameter_id = models.ForeignKey(Parameter)
    sla_id = models.ForeignKey(SLA)
    service_option_id = models.ForeignKey(ServiceOption)


class ServiceDetailsOption(models.Model):
    class Meta:
        unique_together = (('service_id', 'service_details_id', 'service_options_id'),)

    service_id = models.ForeignKey(Service)
    service_details_id = models.ForeignKey(ServiceDetails)
    service_options_id = models.ForeignKey(ServiceOption)

