from __future__ import unicode_literals

import uuid
import os
from agora import settings
from django.db import models
from service.models import Service, ServiceDetails
from common import helper
from collections import OrderedDict
from ckeditor_uploader.fields import RichTextUploadingField
from agora.utils import clean_html_fields


class ServiceComponent(models.Model):

    id = models.UUIDField(
            primary_key=True,
            default=uuid.uuid4,
            editable=False
    )
    name = models.CharField(
            max_length=255,
            default=None,
            blank=True,
            unique=True
    )
    description = RichTextUploadingField(default=None, blank=True, null=True)
    logo = models.ImageField(
            upload_to=("components"),
            default=settings.SERVICE_AREA_ICON
    )

    class Meta:
        verbose_name_plural = "1. Service Components"

    def __unicode__(self):
        return str(self.name)

    def as_json(self):
        component_implementations = [
            sci.as_json() for sci in ServiceComponentImplementation.objects
            .filter(component_id=self.pk)
        ]

        return OrderedDict([
            ("uuid", str(self.id)),
            ("name", self.name),
            ("description", self.description),
            ("logo",  "/static/img/logos/"+self.logo.name.split("/")[-1]),
            ("component_implementations_list", {
                "count": len(component_implementations),
                "component_implementations": component_implementations
            })
        ])

    def as_shorter(self):
        return OrderedDict([
            ("uuid", str(self.id)),
            ("name", self.name)
        ])

    def as_short(self, service_id, service_details_version):

        service = Service.objects.get(id=service_id)

        return {
            "component": OrderedDict([
                ("uuid", str(self.id)),
                ("name", self.name),
                ("description", self.description),
                ("logo",  "/static/img/logos/"+self.logo.name.split("/")[-1]),
                ("service_component_implementations_link", {
                  "related": {
                    "href": helper.current_site_url()
                    + "/v1/portfolio/services/" + str(service.name)
                    + "/service_details/" + str(service_details_version)
                    + "/service_components/" + str(self.pk)
                    + "/service_component_implementations",
                    "meta": "A link to the service component "
                    + "implementations list"
                  }
                })
            ])
        }

    def as_view_compatible(self, version):

        component_implementations = [
            sci.as_json() for sci in ServiceComponentImplementation.objects
            .filter(component_id=self.pk)
        ]

        return {
            "component": OrderedDict([
                ("uuid", str(self.id)),
                ("name", self.name),
                ("version", version),
                ("logo",  "/static/img/logos/"+self.logo.name.split("/")[-1]),
                ("description", self.description),
                ("component_implementations_list", {
                    "count": len(component_implementations),
                    "component_implementations": component_implementations
                })
            ])
        }

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        if not self.description or self.description == "":
            self.description = None
        super(ServiceComponent, self).save(*args, **kwargs)


class ServiceComponentImplementation(models.Model):

    class Meta:
        unique_together = (('component_id', "name"))
        verbose_name_plural = "2. Service Components Implementations"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    component_id = models.ForeignKey(ServiceComponent)
    name = models.CharField(max_length=255, default=None, blank=True)
    description = RichTextUploadingField(default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    def as_full(self):
        component_implementation_details = [
            scid.as_json() for scid in ServiceComponentImplementationDetail.objects
                .filter(component_id=self.component_id.pk, component_implementation_id=self.pk)
        ]

        return OrderedDict([
            ("uuid", str(self.id)),
            ("name", self.name),
            ("description", self.description),
            ("component", self.component_id.as_shorter()),
            ("component_implementation_details_list", {
                "count": len(component_implementation_details),
                "component_implementation_details": component_implementation_details
            })
        ])

    def as_json(self):
        component_implementation_details = [
            scid.as_json() for scid in ServiceComponentImplementationDetail.objects
                .filter(component_id=self.component_id.pk, component_implementation_id=self.pk)
        ]

        return OrderedDict([
            ("uuid", str(self.id)),
            ("name", self.name),
            ("description", self.description),
            ("component_implementation_details_list", {
                "count": len(component_implementation_details),
                "component_implementation_details": component_implementation_details
            })
        ])

    def as_json_up(self):

        return OrderedDict([
            ("uuid", str(self.id)),
            ("name", self.name),
            ("description", self.description),
            ("component", self.component_id.as_shorter())
        ])

    def as_short(self, service_id, service_details_version):

        service = Service.objects.get(id=service_id)

        component_implementation_details = [
            scid.as_json() for scid in ServiceComponentImplementationDetail.objects
                .filter(component_id=self.component_id.pk, component_implementation_id=self.pk)
        ]

        return OrderedDict([
            ("uuid", str(self.id)),
            ("name", self.name),
            ("description", self.description),
            ("component_implementation_details_link", {

               "related": {

                "href":  helper.current_site_url()
                + "/v1/portfolio/services/"
                + str(service.name)  # .replace(" ", "_")
                + "/service_details/"
                + str(service_details_version)
                + "/service_components/"
                + str(self.component_id.pk)
                + "/service_component_implementations/"
                + str(self.pk)
                + "/service_component_implementation_detail",
                "meta": {
                    "desc": "A list of the service component"
                    + " implementation details."
                }
                    }})
        ])

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        if not self.description or self.description == "":
            self.description = None
        super(ServiceComponentImplementation, self).save(*args, **kwargs)


class ServiceComponentImplementationDetail(models.Model):

    class Meta:
        unique_together = (('component_implementation_id', 'version'))
        verbose_name_plural = "3. Service Components Implementations Details"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    component_id = models.ForeignKey(ServiceComponent)
    component_implementation_id = models.ForeignKey(
        ServiceComponentImplementation, on_delete=models.CASCADE
    )
    version = models.CharField(max_length=255, default=None, blank=True)

    def __unicode__(self):
        return str(self.component_implementation_id.name)
        + " "
        + str(self.version)

    def get_configuration_parameters_list(self):
        return self.servicedetailscomponent_set.first().configuration_parameters
        # return map(
        #         lambda sdc: sdc.configuration_parameters,
        #         self.servicedetailscomponent_set.all())

    def as_json(self):
        return OrderedDict([
            ("uuid", str(self.id)),
            ("version", self.version),
            ("configuration_parameters", self.get_configuration_parameters_list()),
        ])

    def as_full(self):
        return OrderedDict([
            ("uuid", str(self.id)),
            ("version", self.version),
            ("configuration_parameters", self.get_configuration_parameters_list()),
            ("service_component", {
                "uuid": self.component_id.pk,
                "name": self.component_id.name
            }),
            ("service_component_implementation", {
                "uuid": self.component_implementation_id.pk,
                "name": self.component_implementation_id.name
            })
        ])

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(ServiceComponentImplementationDetail, self).save(*args, **kwargs)


class ServiceDetailsComponent(models.Model):

    class Meta:
        unique_together = (
            (
                'service_id',
                'service_details_id',
                'service_component_implementation_detail_id'
            ),
        )
        verbose_name_plural = "5. Service Components Implementations Details Link"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_id = models.ForeignKey(Service)
    service_details_id = models.ForeignKey(ServiceDetails)
    service_component_implementation_detail_id = models.ForeignKey(
        ServiceComponentImplementationDetail
    )
    service_type = models.CharField(
            max_length=255,
            default=None,
            blank=True,
            null=True,
            unique=True
    )
    configuration_parameters = RichTextUploadingField(
        default=None,
        blank=True,
        null=True
    )

    def __unicode__(self):
        return str(self.service_id.name) + " "  + str(self.service_details_id.version) + " " + \
               str(self.service_component_implementation_detail_id)

    def as_json(self):
        return {
            "service_uuid": self.service_id.name,
            "service_details_version": self.service_details_id.version,
            "service_component_implementation_detail_uuid": self.service_component_implementation_detail_id.pk,
            "configuration_parameters": self.configuration_parameters,
        }

    def as_full(self):
        return {
            "service": {
                "uuid": self.service_id.pk,
                "name": self.service_id.name
            },
            "service_details": {
                "uuid": self.service_details_id.pk,
                "version": self.service_details_id.version,
                "service": {
                    "uuid": self.service_details_id.id_service.pk,
                    "name": self.service_details_id.id_service.name
                }
            },
            "component_implementation_details": {
                "uuid": self.service_component_implementation_detail_id.pk,
                "version": self.service_component_implementation_detail_id.version,
                "configuration_parameters": self.configuration_parameters,
                "component": {
                    "uuid": self.service_component_implementation_detail_id.component_id.pk,
                    "name": self.service_component_implementation_detail_id.component_id.name
                },
                "component_implementation": {
                    "uuid": self.service_component_implementation_detail_id.component_implementation_id.pk,
                    "name": self.service_component_implementation_detail_id.component_implementation_id.name,
                    "configuration_parameters": self.configuration_parameters,
                }
            }
        }

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(ServiceDetailsComponent, self).save(*args, **kwargs)
