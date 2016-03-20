from __future__ import unicode_literals

import uuid
from django.db import models
from service.models import Service, ServiceDetails

class ServiceComponent(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True)
    description = models.TextField(default=None, blank=True)


    def __unicode__(self):
         return str(self.name)


    def as_json(self):
        return {
            "uuid": self.id,
            "name": self.name,
            "description": self.description,
            "component_implementations": [sci.as_json() for sci in ServiceComponentImplementation.objects.filter(component_id=self.pk)]
        }


class ServiceComponentImplementation(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    component_id = models.ForeignKey(ServiceComponent)
    name = models.CharField(max_length=255, default=None, blank=True)
    description = models.TextField(default=None, blank=True)


    def __unicode__(self):
         return str(self.name)


    def as_json(self):
        return {
            "uuid": self.id,
            "name": self.name,
            "description": self.description,
            "component_implementation_details": [scid.as_json() for scid in ServiceComponentImplementationDetail.objects.
                                filter(component_id=self.component_id.pk, component_implementation_id=self.pk)]
        }


class ServiceComponentImplementationDetail(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    component_id = models.ForeignKey(ServiceComponent)
    component_implementation_id = models.ForeignKey(ServiceComponentImplementation, on_delete=models.CASCADE)
    version = models.CharField(max_length=255, default=None, blank=True)
    configuration_parameters = models.TextField(default=None, blank=True)

    def __unicode__(self):
         return str(self.component_implementation_id.name) + " " +  str(self.version)

    def as_json(self):
        return {
            "uuid": self.id,
            "version": self.version,
            "configuration_parameters": self.configuration_parameters
        }


# class ServiceDetailsComponent(models.Model):
#
#     class Meta:
#         unique_together = (('service_id', 'service_details_id'),)
#
#     service_id = models.ForeignKey(Service)
#     service_details_id = models.ForeignKey(ServiceDetails)
#
#     def __unicode__(self):
#
#         return str(self.service_id.name) + " "  + str(self.service_details_id.version)

class ServiceDetailsComponent(models.Model):

    class Meta:
        unique_together = (('service_id', 'service_details_id', 'service_component_implementation_detail_id'),)

    service_id = models.ForeignKey(Service)
    service_details_id = models.ForeignKey(ServiceDetails)
    service_component_implementation_detail_id = models.ForeignKey(ServiceComponentImplementationDetail)

    def __unicode__(self):

        return str(self.service_id.name) + " "  + str(self.service_details_id.version) + \
               " " + str(self.service_component_implementation_detail_id.version)
