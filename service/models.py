from __future__ import unicode_literals

from django.db import models
import uuid
from owner.models import ServiceOwner, ContactInformation, Institution


class Service(models.Model):


    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(max_length=255, default=None, blank=True)
    description_external = models.TextField(default=None, blank=True)
    description_internal = models.TextField(default=None, blank=True)
    service_area = models.CharField(max_length=255, default=None, blank=True)
    service_type = models.CharField(max_length=255, default=None, blank=True)
    request_procedures = models.CharField(max_length=255, default=None, blank=True)
    funders_for_service = models.CharField(max_length=255, default=None, blank=True)
    value_to_customer = models.CharField(max_length=255, default=None, blank=True)
    risks = models.CharField(max_length=255, default=None, blank=True)
    competitors = models.CharField(max_length=255, default=None, blank=True)
    id_service_owner = models.ForeignKey(ServiceOwner)
    id_contact_information = models.ForeignKey(ContactInformation)

    def __unicode__(self):
         return str(self.name)


    def get_service_details(self, complete=False):
        services = []
        servs = ServiceDetails.objects.filter(id_service =self.pk)
        for s in servs:
            if complete:
                services.append(s.as_complete())
            else:
                services.append(s.as_short())

        return services


    def get_user_customers(self):
        return [c.as_json() for c in UserCustomer.objects.filter(service_id=self.pk)]


    def get_service_owners(self):
        return ServiceOwner.objects.get(id=self.id_service_owner.pk).as_json()


    def get_service_institution(self):
        return Institution.objects.get(pk=ServiceOwner.objects.get(id=self.id_service_owner.pk).id_service_owner.pk).as_json()


    def as_complete_portfolio(self):
        dependencies = Service_DependsOn_Service.objects.filter(id_service_one=self.pk)
        service_dependencies = []

        for d in dependencies:
            service_dependencies.append({
                "uuid": Service.objects.get(pk=d.id_service_two.pk).id
            })

        return {
            "uuid": str(self.pk),
            "url": "/portfolio/services/" + str(self.pk),
            "name": self.name,
            "description_external": self.description_external,
            "description_internal": self.description_internal,
            "service_area": self.service_area,
            "request_procedures": self.request_procedures,
            "funders_for_service": self.funders_for_service,
            "value_to_customer": self.value_to_customer,
            "risks": self.risks,
            "competitors": self.competitors,
            "user_customers": self.get_user_customers(),
            "service_details": self.get_service_details(complete=True),
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
            "url": "/portfolio/services/" + str(self.pk),
            "name": self.name,
            "description_external": self.description_external,
            "description_internal": self.description_internal,
            "service_area": self.service_area,
            "request_procedures": self.request_procedures,
            "funders_for_service": self.funders_for_service,
            "value_to_customer": self.value_to_customer,
            "risks": self.risks,
            "service_details": self.get_service_details(),
            "competitors": self.competitors,
            "user_customers": self.get_user_customers(),
            "id_service_owner": self.id_service_owner.pk,
            "id_contact_information": self.id_contact_information.pk
        }


    def as_catalogue(self):

        return {
            "uuid": self.id,
            "url": "/catalogue/services/" + str(self.pk),
            "name": self.name,
            "description_external": self.description_external,
            "description_internal": self.description_internal,
            "service_area": self.service_area,
            "value_to_customer": self.value_to_customer,
        }
1

class ServiceDetails(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    id_service = models.ForeignKey(Service)
    version = models.CharField(max_length=255, default=None, blank=True)
    status = models.CharField(max_length=255, default=None, blank=True)
    features_current = models.CharField(max_length=255, default=None, blank=True)
    features_future = models.CharField(max_length=255, default=None, blank=True)
    usage_policy_has = models.BooleanField(default=False, blank=True)
    usage_policy_url = models.CharField(max_length=255, default=None, blank=True)
    user_documentation_has = models.BooleanField(default=False, blank=True)
    user_documentation_url = models.CharField(max_length=255, default=None, blank=True)
    operations_documentation_has = models.BooleanField(default=False, blank=True)
    operations_documentation_url = models.CharField(max_length=255, default=None, blank=True)
    monitoring_has = models.BooleanField(default=False, blank=True)
    monitoring_url = models.CharField(max_length=255, default=None, blank=True)
    accounting_has = models.BooleanField(default=False, blank=True)
    accounting_url = models.CharField(max_length=255, default=None, blank=True)
    business_continuity_plan_has = models.BooleanField(default=False, blank=True)
    business_continuity_plan_url = models.CharField(max_length=255, default=None, blank=True)
    disaster_recovery_plan_has = models.BooleanField(default=False, blank=True)
    disaster_recovery_plan_url = models.CharField(max_length=255, default=None, blank=True)
    decommissioning_procedure_has = models.BooleanField(default=False, blank=True)
    decommissioning_procedure_url = models.CharField(max_length=255, default=None, blank=True)
    cost_to_run = models.CharField(max_length=255, default=None, blank=True)
    cost_to_build = models.CharField(max_length=255, default=None, blank=True)

    def __unicode__(self):

        primary_key = self.id_service.pk
        srv = Service.objects.get(pk=primary_key)

        return str(srv.name)+" "+str(self.version)

    def as_short(self):
            return {
                "uuid": self.id,
                "url": "/catalogue/services/" + str(self.id_service.pk) + "/service_details/" + str(self.version),
                "version": self.version,
                "service_status": self.status,
                "features_current": self.features_current,
                "features_future": self.features_future
            }

    def as_complete(self):
        return {
            "uuid": self.id,
            "url": "/portfolio/services/" + str(self.id_service.pk) + "/service_details/" + str(self.version),
            "version": self.version,
            "service_status": self.status,
            "features_current": self.features_current,
            "features_future": self.features_future,
            "usage_policy_has": self.usage_policy_has,
            "usage_policy_url": self.usage_policy_url,
            "user_documentation_has": self.user_documentation_has,
            "user_documentation_url": self.user_documentation_url,
            "operations_documentation_has": self.operations_documentation_has,
            "operations_documentation_url": self.operations_documentation_url,
            "monitoring_has": self.monitoring_has,
            "monitoring_url": self.monitoring_url,
            "accounting_has": self.accounting_has,
            "accounting_url": self.accounting_url,
            "business_continuity_plan_has": self.business_continuity_plan_has,
            "business_continuity_plan_url": self.business_continuity_plan_url,
            "disaster_recovery_plan_has": self.disaster_recovery_plan_has,
            "disaster_recovery_plan_url": self.disaster_recovery_plan_url,
            "decommissioning_procedure_has": self.decommissioning_procedure_has,
            "decommissioning_procedure_url": self.decommissioning_procedure_url,
            "cost_to_run": self.cost_to_run,
            "cost_to_build": self.cost_to_build,
        }


    def as_json(self):
        return {
            "uuid" : self.id,
            "version": self.version,
            "service_status": self.status,
            "features_current": self.features_current,
            "features_future": self.features_future
        }


class ExternalService(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True)
    description = models.TextField(default=None, blank=True)
    service = models.CharField(max_length=255, default=None, blank=True)
    details = models.CharField(max_length=255, default=None, blank=True)

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


class UserCustomer(models.Model):
    USER_TYPES = (
        ("Individual Researchers", "Individual Researchers"),
        ("Community manager", "Community manager"),
        ("Service provider", "Service provider"),
        ("Data Project Principle Investigator (PI)", "Data Project Principle Investigator (PI)")
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, choices=USER_TYPES, blank=True)
    role = models.CharField(max_length=255, default=None, blank=True)
    service_id = models.ForeignKey(Service)

    def __unicode__(self):
        return str(self.name) + " as " + str(self.role) + " for " + str(self.service_id)


    def as_json(self):
        return {
            "id": self.pk,
            "name": self.name,
            "role": self.role
        }