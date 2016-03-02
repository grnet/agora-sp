from __future__ import unicode_literals

import uuid
from django.db import models
from service.models import Service, ServiceDetails

class ServiceOption(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True)
    description = models.TextField(default=None, blank=True)
    pricing = models.CharField(max_length=255, default=None, blank=True)

    def __unicode__(self):
        return str(self.name)



class SLA(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_option_id = models.ForeignKey(ServiceOption)
    name = models.CharField(max_length=255, default=None, blank=True)

    def __unicode__(self):
        return str(self.name)



class Parameter(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True)
    type = models.CharField(max_length=255, default=None, blank=True)
    expression = models.CharField(max_length=255, default=None, blank=True)

    def __unicode__(self):
        return str(self.name)



class SLAParameter(models.Model):
    class Meta:
        unique_together = (('parameter_id', 'sla_id', 'service_option_id'),)

    parameter_id = models.ForeignKey(Parameter)
    sla_id = models.ForeignKey(SLA)
    service_option_id = models.ForeignKey(ServiceOption)

    def __unicode__(self):
        param = Parameter.objects.get(pk=self.parameter_id.pk)
        sla = SLA.objects.get(pk=self.sla_id.pk)
        service = ServiceOption.objects.get(pk=self.service_option_id.pk)
        return str(param) + " " + str(sla) + " " + str(service)



class ServiceDetailsOption(models.Model):
    class Meta:
        unique_together = (('service_id', 'service_details_id', 'service_options_id'),)

    service_id = models.ForeignKey(Service)
    service_details_id = models.ForeignKey(ServiceDetails)
    service_options_id = models.ForeignKey(ServiceOption)

    def __unicode__(self):
        service = Service.objects.get(pk=self.service_id.pk)
        service_details = ServiceDetails.objects.get(pk=self.service_details_id.pk)
        service_options = ServiceOption.objects.get(pk=self.service_options_id.pk)
        return str(service) + " " + str(service_details) + " " + str(service_options)

