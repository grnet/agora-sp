from __future__ import unicode_literals

import uuid
from django.db import models
from service.models import Service, ServiceDetails
from django.contrib.sites.models import Site

class ServiceOption(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True)
    description = models.TextField(default=None, blank=True)
    pricing = models.CharField(max_length=255, default=None, blank=True)

    def __unicode__(self):
        return str(self.name)


    def current_site_url(self):
        """Returns fully qualified URL (no trailing slash) for the current site."""

        current_site = Site.objects.get_current()
        url = 'http://%s' % (current_site.domain+"/api")

        return url


    def as_json(self, service_name, service_details_version):
        sla = SLA.objects.filter(service_option_id=self.pk)
        if len(sla) == 1:
            sla_url = self.current_site_url()+"/v1/portfolio/services/" + service_name.replace(" ", "_") + "/service_details/" + service_details_version \
                      + "/service_options/sla/" + str(sla[0].pk)
        else:
            sla_url = ""

        return {
            "uuid": self.id,
            "name": self.name,
            "description": self.description,
            "pricing": self.pricing,
            "SLA_link": {
                "related": {
                    "href": sla_url,
                    "meta": {
                        "desc": "A link to the SLA for this service."
                    }
                }}
        }


class SLA(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_option_id = models.ForeignKey(ServiceOption)
    name = models.CharField(max_length=255, default=None, blank=True)

    def __unicode__(self):
        return str(self.name)

    def current_site_url(self):
        """Returns fully qualified URL (no trailing slash) for the current site."""

        current_site = Site.objects.get_current()
        url = 'http://%s' % (current_site.domain+"/api")

        return url


    def as_json(self, service_name, service_details_version):
        return {
            "id": self.id,
            "name": self.name,
            "parameters": [sp.parameter_id.as_json(service_name.replace(" ", "_"), service_details_version, self.pk) for sp in SLAParameter.objects.
                filter(sla_id=self.pk, service_option_id=self.service_option_id.pk)]
        }



class Parameter(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True)
    type = models.CharField(max_length=255, default=None, blank=True)
    expression = models.CharField(max_length=255, default=None, blank=True)

    def __unicode__(self):
        return str(self.name)

    def current_site_url(self):
        """Returns fully qualified URL (no trailing slash) for the current site."""

        current_site = Site.objects.get_current()
        url = 'http://%s' % (current_site.domain+"/api")

        return url


    def as_json(self, service_name, service_details_version, sla_id):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "expression": self.expression,
            "SLA_parameter_link": {
                "related": {
                    "href": self.current_site_url() + "/v1/portfolio/services/" + service_name.replace(" ", "_") + "/service_details/" + service_details_version
                   + "/service_options/sla/" + str(sla_id) + "/sla_parameter/" + str(self.pk) + "/parameter",
                    "meta": {
                            "desc": "A link to the SLA parameters."
                }}
        }}

    def as_short(self):
        return {
            "id": self.id,
            "name": self.name,
            "type": self.type,
            "expression": self.expression
        }



class SLAParameter(models.Model):
    class Meta:
        unique_together = (('parameter_id', 'sla_id', 'service_option_id'),)

    parameter_id = models.ForeignKey(Parameter)
    sla_id = models.ForeignKey(SLA)
    service_option_id = models.ForeignKey(ServiceOption)

    def __unicode__(self):
        return str(self.parameter_id) + " " + str(self.sla_id) + " " + str(self.service_option_id)


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


