from __future__ import unicode_literals

from django.db import models
import uuid
from owner.models import ServiceOwner, ContactInformation
from django.core import serializers
import json


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

    def __unicode__(self):
         return str(self.name)


    def as_complete_portfolio(self):
        dependencies = Service_DependsOn_Service.objects.filter(id_service_one=self.pk)
        service_dependencies = []
        for d in dependencies:
            service_dependencies.append({
                "uuid": Service.objects.get(pk=d.id_service_two.pk).id
            })

        return {
            "uuid": self.id,
            "name": self.name,
            "description_external": self.description_external,
            "description_internal": self.description_internal,
            "service_area": self.service_area,
            "request_procedures": self.request_procedures,
            "funders_for_service": self.funders_for_service,
            "value_to_customer": self.value_to_customer,
            "risks": self.risks,
            "competitors": self.competitors,
            "service_details": ServiceDetails.objects.filter(id_service=self.pk)[0].as_json(),
            "service_owner": ServiceOwner.objects.get(id=self.id_service_owner.pk).as_json(),
            "dependencies": {
                "count": len(service_dependencies),
                "services": service_dependencies
            },
            "contact_information": ContactInformation.objects.get(id=self.id_contact_information.pk).as_json()
        }


    def as_portfolio(self):
        # return json.loads(serializers.serialize("json", [self, ]))[0]

        return {
            "uuid": self.id,
            "name": self.name,
            "description_external": self.description_external,
            "description_internal": self.description_internal,
            "service_area": self.service_area,
            "request_procedures": self.request_procedures,
            "funders_for_service": self.funders_for_service,
            "value_to_customer": self.value_to_customer,
            "risks": self.risks,
            "competitors": self.competitors,
            "id_service_owner": self.id_service_owner.pk,
            "id_contact_information": self.id_contact_information.pk
        }


    def as_catalogue(self):

        return {
            "uuid": self.id,
            "name": self.name,
            "description_external": self.description_external,
            "description_internal": self.description_internal,
            "service_area": self.service_area,
            "value_to_customer": self.value_to_customer,
        }
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

    def __unicode__(self):

        primary_key = self.id_service.pk
        srv = Service.objects.get(pk=primary_key)



    def as_json(self):
        return {
            "version": self.version,
            "service_status": self.status,
            "features_current": self.features_current,
            "features_future": self.features_future
        }

class ExternalService(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)
    service = models.CharField(max_length=255, default=None)
    details = models.CharField(max_length=255, default=None)

    def __unicode__(self):
        return str(self.name)

class Service_DependsOn_Service(models.Model):

    class Meta:
          unique_together = (('id_service_one', 'id_service_two'),)

    id_service_one = models.ForeignKey(Service, related_name='service_one')
    id_service_two = models.ForeignKey(Service, related_name='service_two')


    def __unicode__(self):

        primary_key_one = self.id_service_one.pk
        primary_key_two = self.id_service_two.pk

        srv1 = Service.objects.get(pk=primary_key_one)
        srv2 = Service.objects.get(pk=primary_key_two)

        return str(srv1.name) + " " +str(srv2.name)

class Service_ExternalService(models.Model):

    class Meta:
          unique_together = (('id_service', 'id_external_service'),)

    id_service = models.ForeignKey(Service)
    id_external_service = models.ForeignKey(ExternalService)

    def __unicode__(self):

        primary_key_one = self.id_service.pk

        external_primary_key_one = self.id_external_service.pk

        srv1 = Service.objects.get(pk=primary_key_one)
        srv2 = ExternalService.objects.get(pk=external_primary_key_one)

        return str(srv1.name) + " " +str(srv2.name)