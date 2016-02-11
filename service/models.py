from __future__ import unicode_literals

from django.db import models
import uuid
from owner.models import ServiceOwner, ContactInformation

class Service(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None)
    description_external = models.TextField(default=None)
    description_internal = models.TextField(default=None)
    service_area = models.CharField(max_length=255, default=None)
    users_customers = models.CharField(max_length=255, default=None)
    service_type = models.CharField(max_length=255, default=None)
    request_procedures = models.CharField(max_length=255, default=None)
    funders_for_service = models.CharField(max_length=255, default=None)
    value_to_customer = models.CharField(max_length=255, default=None)
    risks = models.CharField(max_length=255, default=None)
    competitors = models.CharField(max_length=255, default=None)
    id_service_owner = models.ForeignKey(ServiceOwner)
    id_contact_information = models.ForeignKey(ContactInformation)
1
class ServiceDetails(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_service = models.ForeignKey(Service)
    version = models.CharField(max_length=255, default=None)
    status = models.CharField(max_length=255, default=None)
    features_current = models.CharField(max_length=255, default=None)
    features_future = models.CharField(max_length=255, default=None)
    usage_policy_has = models.BooleanField(default=False)
    usage_policy_url = models.CharField(max_length=255, default=None)
    user_documentation_has = models.BooleanField(default=False)
    user_documentation_url = models.CharField(max_length=255, default=None)
    monitoring_has = models.BooleanField(default=False)
    monitoring_url = models.CharField(max_length=255, default=None)
    accounting_has = models.BooleanField(default=False)
    accounting_url = models.CharField(max_length=255, default=None)
    business_continuity_plan_has = models.BooleanField(default=False)
    business_continuity_plan_url = models.CharField(max_length=255, default=None)
    disaster_recovery_plan_has = models.BooleanField(default=False)
    disaster_recovery_plan_url = models.CharField(max_length=255, default=None)
    decommissioning_procedure_has = models.BooleanField(default=False)
    decommissioning_procedure_url = models.CharField(max_length=255, default=None)
    cost_to_run = models.CharField(max_length=255, default=None)
    cost_to_build = models.CharField(max_length=255, default=None)

class ExternalService(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)
    service = models.CharField(max_length=255, default=None)
    details = models.CharField(max_length=255, default=None)

class Service_DependsOn_Service(models.Model):

    class Meta:
          unique_together = (('id_service_one', 'id_service_two'),)

    id_service_one = models.ForeignKey(Service, related_name='service_one')
    id_service_two = models.ForeignKey(Service, related_name='service_two')

class Service_ExternalService(models.Model):

    class Meta:
          unique_together = (('id_service', 'id_external_service'),)

    id_service = models.ForeignKey(Service)
    id_external_service = models.ForeignKey(ExternalService)