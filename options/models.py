from __future__ import unicode_literals

import uuid
from django.db import models
from service.models import Service, ServiceDetails
from django.contrib.sites.models import Site
from common import helper
from collections import OrderedDict

class ServiceOption(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True)
    description = models.TextField(default=None, blank=True, null=True)
    pricing = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    def as_json(self, service_name, service_details_version):
        sla = SLA.objects.filter(service_option_id=self.pk)

        if len(sla) > 0:
            sla_url = helper.current_site_url()+"/v1/portfolio/services/" + service_name.replace(" ", "_") + "/service_details/" + service_details_version \
                      + "/service_options/sla/" + str(sla[0].pk)
            return OrderedDict([
                ("uuid", self.id),
                ("name", self.name),
                ("description", self.description),
                ("pricing", self.pricing),
                ("SLA", {
                    "name": sla[0].name,
                    "links": {
                        "self": sla_url,
                        "meta": {
                            "desc": "A link to the SLA for this service."
                        }
                    }}
                 )
            ])
        else:
            sla_url = ""
            return OrderedDict([
                ("uuid", self.id),
                ("name", self.name),
                ("description", self.description),
                ("pricing", self.pricing),
                ("SLA", {
                    "name": "",
                    "link": {
                        "href": sla_url,
                        "meta": {
                            "desc": "A link to the SLA for this service."
                        }
                    }}
                )
            ])



    def save(self, *args, **kwargs):
        if not self.description:
            self.description = None
        if not self.pricing:
            self.pricing = None
        super(ServiceOption, self).save(*args, **kwargs)


class SLA(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_option_id = models.ForeignKey(ServiceOption, null=True)
    name = models.CharField(max_length=255, default=None, blank=True)

    def __unicode__(self):
        return str(self.name)

    def as_json(self, service_name, service_details_version):
        parameters = [sp.parameter_id.as_json(service_name.replace(" ", "_"), service_details_version, self.pk) for sp in SLAParameter.objects.
                filter(sla_id=self.pk, service_option_id=self.service_option_id.pk)]
        return {
            "id": self.id,
            "name": self.name,
            "parameters_list": {
                "count": len(parameters),
                "parameters": parameters
            }
        }

    def as_short(self):
        return {
            "id": self.id,
            "name": self.name,
            "service_option": self.service_option_id.id
        }


class Parameter(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True)
    type = models.CharField(max_length=255, default=None, blank=True, null=True)
    expression = models.CharField(max_length=255, default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    def as_json(self, service_name, service_details_version, sla_id):
        return OrderedDict([
            ("uuid", self.id),
            ("name", self.name),
            ("type", self.type),
            ("expression", self.expression),
            ("SLA_parameter", {
                "name": self.name,
                "links": {
                    "self": helper.current_site_url() + "/v1/portfolio/services/" + service_name.replace(" ", "_") + "/service_details/" + service_details_version
                   + "/service_options/sla/" + str(sla_id) + "/sla_parameter/" + str(self.pk) + "/parameter",
                }
            })
        ])

    def as_short(self):
        return OrderedDict([
            ("uuid", self.id),
            ("name", self.name),
            ("type", self.type),
            ("expression", self.expression)
        ])

    def save(self, *args, **kwargs):
        if not self.expression:
            self.expression = None
        if not self.type:
            self.type = None
        super(Parameter, self).save(*args, **kwargs)


class SLAParameter(models.Model):
    class Meta:
        unique_together = (('parameter_id', 'sla_id', 'service_option_id'),)

    parameter_id = models.ForeignKey(Parameter)
    sla_id = models.ForeignKey(SLA)
    service_option_id = models.ForeignKey(ServiceOption)

    def __unicode__(self):
        return str(self.parameter_id) + " " + str(self.sla_id) + " " + str(self.service_option_id)

    def as_json(self):
        return {
            "parameter_uuid": self.parameter_id,
            "sla_uuid": self.sla_id,
            "service_option_id": self.service_option_id
        }


class ServiceDetailsOption(models.Model):
    class Meta:
        unique_together = (('service_id', 'service_details_id', 'service_options_id'),)

    service_id = models.ForeignKey(Service)
    service_details_id = models.ForeignKey(ServiceDetails)
    service_options_id = models.ForeignKey(ServiceOption)

    def __unicode__(self):
        return str(self.service_id) + " " + str(self.service_details_id) + " " + str(self.service_options_id)

    def as_json(self):
        return self.service_options_id.as_json(self.service_id.name, self.service_details_id.version)


