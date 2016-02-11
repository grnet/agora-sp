from __future__ import unicode_literals

import uuid
from django.db import models
from service.models import Service, ServiceDetails

class ServiceComponent(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)


class ServiceComponentImplementation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    component_id = models.ForeignKey(ServiceComponent)
    name = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)


class ServiceComponentImplementationDetail(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    component_id = models.ForeignKey(ServiceComponent)
    component_implementation_id = models.ForeignKey(ServiceComponentImplementation, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)


class ServiceDetailsComponent(models.Model):
    class Meta:
        unique_together = (('service_id', 'service_details_id', 'service_component_id'),)

    service_id = models.ForeignKey(Service)
    service_details_id = models.ForeignKey(ServiceDetails)
    service_component_id = models.ForeignKey(ServiceComponent)