from __future__ import unicode_literals

import uuid
from django.db import models
from service.models import Service, ServiceDetails
from ckeditor_uploader.fields import RichTextUploadingField
from agora import settings
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
            default=settings.SERVICE_CATEGORY_ICON
    )

    def __unicode__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(ServiceComponent, self).save(*args, **kwargs)


class ServiceComponentImplementation(models.Model):

    class Meta:
        unique_together = (('component_id', "name"))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    component_id = models.ForeignKey(ServiceComponent)
    name = models.CharField(max_length=255, default=None, blank=True)
    description = RichTextUploadingField(default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(ServiceComponentImplementation, self).save(*args, **kwargs)


class ServiceComponentImplementationDetail(models.Model):

    class Meta:
        unique_together = (('component_implementation_id', 'version'))

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    component_id = models.ForeignKey(ServiceComponent)
    component_implementation_id = models.ForeignKey(
        ServiceComponentImplementation, on_delete=models.CASCADE
    )
    version = models.CharField(max_length=255, default=None, blank=True)

    def __unicode__(self):
        return str(self.component_implementation_id.name)

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
        return str(self.service_id.name) + " " + \
               str(self.service_details_id.version) + " " + \
               str(self.service_component_implementation_detail_id)

    @property
    def service_admins_ids(self):
        return self.service_id.service_admins_ids

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(ServiceDetailsComponent, self).save(*args, **kwargs)
