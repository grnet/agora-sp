from __future__ import unicode_literals
import os
from agora import  settings
from django.db import models
import uuid
from owner.models import ServiceOwner, ContactInformation, Institution
from common import helper
from collections import OrderedDict
from accounts.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from agora.utils import SERVICE_ADMINSHIP_STATES


class ServiceArea(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True, null=True)
    icon = models.ImageField(default=settings.SERVICE_AREA_ICON,
            upload_to=helper.service_area_image_path)

    @property
    def icon_absolute_path(self):
        if self.icon:
            path = self.icon.url
        else:
            path = settings.MEDIA_URL+settings.SERVICE_AREA_ICON
        return helper.current_site_baseurl()+'/'+path

    class Meta:
        verbose_name_plural = "06. Service Areas (settings)"

    def __unicode__(self):
        return str(self.name)


class ServiceTrl(models.Model):

    class Meta:
        verbose_name_plural = "10. Service Technology Readiness Level (settings)"
        ordering = [
            "order",
        ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    value = models.CharField(max_length=255, default=None, blank=False)
    order = models.IntegerField(default=None, blank=False)

    def __unicode__(self):
        return str(self.value)

    def as_json(self):
        return OrderedDict([
            ("uuid", self.id),
            ("value", self.value),
            ("order", self.order),
        ])

    def save(self, *args, **kwargs):
        super(ServiceTrl, self).save(*args, **kwargs)

class Service(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True, unique=True)
    short_description = RichTextUploadingField(default=None, blank=True, null=True)
    description_external = RichTextUploadingField(default=None, blank=True, null=True)
    description_internal = RichTextUploadingField(default=None, blank=True, null=True)
    service_area = models.ForeignKey(ServiceArea, blank=False, null=True)
    service_type = models.CharField(max_length=255, default=None, blank=True, null=True)
    service_trl = models.ForeignKey(ServiceTrl, null=True)
    request_procedures = RichTextUploadingField(default=None, blank=True, null=True)
    funders_for_service = RichTextUploadingField(default=None, blank=True, null=True)
    value_to_customer = RichTextUploadingField(default=None, blank=True, null=True)
    risks = RichTextUploadingField(default=None, blank=True, null=True)
    competitors = RichTextUploadingField(default=None, blank=True, null=True)
    id_service_owner = models.ForeignKey(ServiceOwner, null=True)
    #This is the id of the external contact information
    id_contact_information = models.ForeignKey(ContactInformation, null=True, related_name="external_contact_info")
    #This is the id of the internal contact information
    id_contact_information_internal = models.ForeignKey(ContactInformation, null=True, related_name="internal_contact_info")
    logo = models.ImageField(default=settings.SERVICE_LOGO,
            upload_to=helper.service_image_path)
    customer_facing = models.BooleanField(default=False)
    internal = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "01. Services"

    def __unicode__(self):
        return str(self.name)
    
    @property
    def service_admins_ids(self):
        service_adminships = ServiceAdminship.objects.filter(
            service=self,
            state="approved")
        res = []
        for s in service_adminships:
            res.append(str(s.admin.pk))

        return ','.join(res)

    @property
    def pending_service_admins_ids(self):
        service_adminships = ServiceAdminship.objects.filter(
            service=self,
            state="pending")
        res = []
        for s in service_adminships:
            res.append(str(s.admin.pk))

        return ','.join(res)

    @property
    def rejected_service_admins_ids(self):
        service_adminships = ServiceAdminship.objects.filter(
            service=self,
            state="rejected")
        res = []
        for s in service_adminships:
            res.append(str(s.admin.pk))

        return ','.join(res)


    def save(self, *args, **kwargs):
        if not self.description_internal or self.description_internal == "":
            self.description_internal = None
        if not self.description_external or self.description_external == "":
            self.description_external = None
        if not self.service_area or self.service_area == "":
            self.service_area = None
        if not self.service_type or self.service_type == "":
            self.service_type = None
        if not self.request_procedures or self.request_procedures == "":
            self.request_procedures = None
        if not self.funders_for_service or self.funders_for_service == "":
            self.funders_for_service = None
        if not self.value_to_customer or self.value_to_customer == "":
            self.value_to_customer = None
        if not self.request_procedures or self.request_procedures == "":
            self.request_procedures = None
        if not self.risks or self.risks == "":
            self.risks = None
        if not self.competitors or self.competitors == "":
            self.competitors = None

        super(Service, self).save(*args, **kwargs)

    @property
    def logo_absolute_path(self):
        if self.logo:
            path = self.logo.url
        else:
            path = settings.MEDIA_URL+settings.SERVICE_LOGO
        return helper.current_site_baseurl()+'/'+path

    @property
    def user_customers_names(self):
        res = []
        users = UserCustomer.objects.filter(service_id=self.pk)
        for user in users:
            res.append(user.name.name)
        return ','.join(res)

    def get_distinct_service_area(self):

        return self.service_area

    def get_service_area_name(self):
        if self.service_area:
            return self.service_area.name
        return None

    def get_service_details(self, complete=False, url=False, catalogue=False):

        services = []
        if not catalogue:
            servs = ServiceDetails.objects.filter(id_service=self.pk)
        else:
            servs = ServiceDetails.objects.filter(id_service=self.pk, is_in_catalogue=True)
        for s in servs:
            if catalogue:
                services.append(s.as_catalogue())
            else:
                if complete:
                    services.append(s.as_complete(url=url))
                else:
                    services.append(s.as_short())

        return services

    def get_service_details_by_version(self, version):
        return ServiceDetails.objects.get(id_service=self.pk, version=version)

    def get_user_customers(self):
        return [c.as_json() for c in UserCustomer.objects.filter(service_id=self.pk)]

    def get_service_owners(self):
        return ServiceOwner.objects.get(id=self.id_service_owner.pk).as_json() if self.id_service_owner is not None else None

    def get_service_owner_object(self):
        return ServiceOwner.objects.get(id=self.id_service_owner.pk) if self.id_service_owner is not None else None

    def get_service_institution(self):
        return Institution.objects.get(pk=ServiceOwner.objects.
                                       get(id=self.id_service_owner.pk).id_service_owner.pk).as_json()

    def get_service_external_dependencies(self):
        return [ExternalService.objects.get(id=dependency.id_external_service.pk).as_json()
                for dependency in Service_ExternalService.objects.filter(id_service=self.id)]

    # This method acquires the external contact information
    def get_service_contact_information(self):
        if self.id_contact_information is not None:
            return self.id_contact_information.get_external()
        return {
            "external_contact_information": None
        }

    # This method acquires the external contact information object
    def get_service_contact_information_object(self):
        return ContactInformation.objects.get(id=self.id_contact_information.pk) if self.id_contact_information is \
                                                                                    not None else None

    # This method acquires the internal contact information
    def get_service_contact_information_internal(self):
        if self.id_contact_information_internal is not None:
            return self.id_contact_information_internal.get_internal()
        return {
            "internal_contact_information": None
        }

    # This method acquires the internal contact information object
    def get_service_contact_information_object_internal(self):
        return ContactInformation.objects.get(id=self.id_contact_information_internal.pk) if self.id_contact_information_internal is \
                                                                                    not None else None

    def get_service_dependencies(self):
        dependencies = Service_DependsOn_Service.objects.filter(id_service_one=self.pk)
        service_dependencies = []

        for d in dependencies:
            service = Service.objects.get(id=d.id_service_two.pk)
            service_dependencies.append({
                "service": OrderedDict([
                    ("name", service.name),
                    ("uuid", service.id),
                    ("links", {
                        "self":helper.current_site_url() + "/v1/portfolio/services/" + str(
                            Service.objects.get(pk=d.id_service_two.pk).name)
                    }),
                ])
            })

        return service_dependencies

    def get_service_dependencies_with_graphics(self):
        dependencies = Service_DependsOn_Service.objects.filter(id_service_one=self.pk)
        service_dependencies = []

        for d in dependencies:
            service = Service.objects.get(id=d.id_service_two.pk)
            service_dependencies.append({
                "service": OrderedDict([
                    ("name", service.name),
                    ("uuid", service.id),
                    ("logo", str(service.logo.name.split("/")[-1])),
                    ("short_description", service.short_description),
                    ("description", service.description_external),
                    ("links", {
                        "self":helper.current_site_url() + "/v1/portfolio/services/" + str(
                            Service.objects.get(pk=d.id_service_two.pk).name)
                    }),
                ])
            })

        return service_dependencies

    def get_service_logo(self):
        return self.logo.path

    def as_service_picker_compliant(self):
        return OrderedDict([
            ("uuid", self.id),
            ("name", self.name),
            ("short_description", self.short_description),
            ("description_external", self.description_external),
            ("service_area", self.get_service_area_name()),
            ("value_to_customer", self.value_to_customer),
            ("service_type", self.service_type),
            ("logo",  "/static/img/logos/"+self.logo.name.split("/")[-1])
        ])

    def as_complete_portfolio(self):
        service_dependencies = self.get_service_dependencies()

        external = Service_ExternalService.objects.filter(id_service=self.pk)
        external_services = []

        for e in external:
            external_services.append({
                "uuid": e.id_external_service.pk,
                "name": e.id_external_service.name

            })

        users_customers = self.get_user_customers()
        service_details = self.get_service_details(complete=True, url=True)

        contact_information = self.get_service_contact_information_object_internal()
        if contact_information is not None:
            contact_information = OrderedDict([
                ("uuid", contact_information.id),
                ("links", {
                    "self": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name) + "/contact_information" #  .replace(" ", "_") + "/contact_information",
                })
            ])

        service_owner = self.get_service_owner_object()
        if service_owner is not None:
            service_owner = OrderedDict([
                ("uuid", service_owner.id),
                ("email", service_owner.email),
                ("first_name", service_owner.first_name),
                ("last_name", service_owner.last_name),
                ("links", {
                    "self": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name) + "/service_owner" # .replace(" ", "_"),
                })
            ])


        return OrderedDict([
            ("uuid", self.id),
            ("name", self.name),
            ("short_description", self.short_description),
            ("description_external", self.description_external),
            ("description_internal", self.description_internal),
            ("service_owner", service_owner),
            ("contact_information", contact_information),
            ("service_area", self.get_service_area_name()),
            ("user_customers_list", {
                "count": len(users_customers),
                "user_customers": users_customers
            }),
            ("dependencies_list", {
                "count": len(service_dependencies),
                # "links": {
                #     "related": {
                #         "href": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name).replace(" ", "_")
                #                 + "/service_dependencies",
                #         "meta": {
                #             "desc": "A list of links to the service dependencies"
                #         }
                #     }
                #
                # },
                "services": service_dependencies
            }),
            ("external", {
                "count": len(external_services),
               "links": {
                    "related": {
                        "href": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name) + "/service_external_dependencies", # .replace(" ", "_"),
                        "meta": {
                            "desc": "Links to external services that this service uses."
                        }}
                },

                "external_services": external_services
            }),
            ("funders_for_service", self.funders_for_service),
            ("value_to_customer", self.value_to_customer),
            ("risks", self.risks),
            ("competitors", self.competitors),
            ("service_type", self.service_type),
            ("request_procedures", self.request_procedures),
            ("service_details_list", {
                "count": len(service_details),
                "service_details": service_details
            }),
            ("service_complete_link", {
                "related": {
                    "href": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name) # .replace(" ", "_")
                            + "?view=complete",
                    "meta": {
                        "desc": "Portfolio level details about this service."
                    }
                }}),
            ("logo", self.logo_absolute_path)
        ])


    def as_complete_contact_portfolio(self):
        service_dependencies = self.get_service_dependencies()

        external = Service_ExternalService.objects.filter(id_service=self.pk)
        external_services = []

        for e in external:
            external_services.append({
                "uuid": e.id_external_service.pk,
                "name": e.id_external_service.name

            })

        users_customers = self.get_user_customers()
        service_details = self.get_service_details(complete=True, url=True)

        internal = self.id_contact_information_internal.as_json() if self.id_contact_information_internal is not None else None
        external = self.id_contact_information.as_json() if self.id_contact_information is not None else None
        contact_information = {
            "internal_contact_information": internal,
            "external_contact_information": external
        }

        service_owner = self.get_service_owner_object()
        if service_owner is not None:
            service_owner = OrderedDict([
                ("uuid", service_owner.id),
                ("email", service_owner.email),
                ("first_name", service_owner.first_name),
                ("last_name", service_owner.last_name),
                ("links", {
                    "self": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name) # .replace(" ", "_")
                            + "/service_owner",
                })
            ])


        return OrderedDict([
            ("uuid", self.id),
            ("name", self.name),
            ("short_description", self.short_description),
            ("description_external", self.description_external),
            ("description_internal", self.description_internal),
            ("service_owner", service_owner),
            ("contact_information", contact_information),
            ("service_area", self.get_service_area_name()),
            ("user_customers_list", {
                "count": len(users_customers),
                "user_customers": users_customers
            }),
            ("dependencies_list", {
                "count": len(service_dependencies),
                # "links": {
                #     "related": {
                #         "href": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name).replace(" ", "_")
                #                 + "/service_dependencies",
                #         "meta": {
                #             "desc": "A list of links to the service dependencies"
                #         }
                #     }
                #
                # },
                "services": service_dependencies
            }),
            ("external", {
                "count": len(external_services),
               "links": {
                    "related": {
                        "href": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name) # .replace(" ", "_")
                                + "/service_external_dependencies",
                        "meta": {
                            "desc": "Links to external services that this service uses."
                        }}
                },

                "external_services": external_services
            }),
            ("funders_for_service", self.funders_for_service),
            ("value_to_customer", self.value_to_customer),
            ("risks", self.risks),
            ("competitors", self.competitors),
            ("service_type", self.service_type),
            ("request_procedures", self.request_procedures),
            ("service_details_list", {
                "count": len(service_details),
                "service_details": service_details
            }),
            ("service_complete_link", {
                "related": {
                    "href": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name) # .replace(" ", "_")
                            + "?view=complete",
                    "meta": {
                        "desc": "Portfolio level details about this service."
                    }
                }}),
            ("logo", self.logo_absolute_path)
        ])


    def as_portfolio(self):

        users_customers = self.get_user_customers()
        service_details = self.get_service_details(complete=True, url=True)

        contact_information = self.get_service_contact_information_object_internal()
        if contact_information is not None:
            contact_information = OrderedDict([
                ("uuid", contact_information.id),
                ("links", {
                    "self": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name) # .replace(" ", "_")
                            + "/contact_information",
                })
            ])

        service_owner = self.get_service_owner_object()
        if service_owner is not None:
            service_owner = OrderedDict([
                ("uuid", service_owner.id),
                ("email", service_owner.email),
                ("first_name", service_owner.first_name),
                ("last_name", service_owner.last_name),
                ("links", {
                    "self": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name) # .replace(" ", "_")
                            + "/service_owner",
                })
            ])

        return OrderedDict([
            ("uuid", self.id),
            ("name", self.name),
            ("short_description", self.short_description),
            ("description_external", self.description_external),
            ("description_internal", self.description_internal),
            ("service_owner", service_owner),
            ("contact_information", contact_information),
            ("service_area", self.get_service_area_name()),
            ("user_customers_list", {
                "count": len(users_customers),
                "user_customers": users_customers
            }),
            ("funders_for_service", self.funders_for_service),
            ("value_to_customer", self.value_to_customer),
            ("risks", self.risks),
            ("competitors", self.competitors),
            ("service_type", self.service_type),
            ("request_procedures", self.request_procedures),
            ("service_details_list", {
                "count": len(service_details),
                "service_details": service_details
            }),
            ("service_complete_link", {
                "related": {
                    "href": helper.current_site_url() + "/v1/portfolio/services/" + str(self.name) # .replace(" ", "_")
                            + "?view=complete",
                    "meta": {
                        "desc": "Portfolio level details about this service."
                    }
                }}),
            ("logo", self.logo_absolute_path)
        ])

    def as_catalogue(self):

        users_customers = self.get_user_customers()
        service_details = self.get_service_details(complete=True, url=True, catalogue=True)

        contact_information = self.get_service_contact_information_object()
        if contact_information is not None:
            contact_information = OrderedDict([
                ("uuid", contact_information.id),
                ("links", {
                    "self": helper.current_site_url() + "/v1/catalogue/services/" + str(self.name) # .replace(" ", "_")
                            + "/contact_information",
                })
            ])

        return OrderedDict([
            ("uuid", self.id),
            ("name", self.name),
            ("short_description", self.short_description),
            ("description_external", self.description_external),
            ("service_area", self.get_service_area_name()),
            ("value_to_customer", self.value_to_customer),
            ("request_procedures", self.request_procedures),
            ("service_type", self.service_type),
            ("contact_information", contact_information),
            ("user_customers_list", {
                "count": len(users_customers),
                "user_customers": users_customers
            }),
            ("service", {
                "name": self.name,
                "links": {
                "self": helper.current_site_url() + "/v1/catalogue/services/" + str(self.name), # .replace(" ", "_"),
                }}),
            ("service_details_list", {
                "count": len(service_details),
                "service_details": service_details
            }),
            ("logo", self.logo_absolute_path)
        ])


class ServiceStatus(models.Model):

    class Meta:
        verbose_name_plural = "09. Service Status (settings)"
        ordering = [
            "order",
        ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    value = models.CharField(max_length=255, default=None, blank=False, unique=True)
    order = models.IntegerField(default=None, blank=False)

    def __unicode__(self):
        return str(self.value)

    def as_json(self):
        return OrderedDict([
            ("uuid", self.id),
            ("value", self.value),
            ("order", self.order),
        ])

    def save(self, *args, **kwargs):
        super(ServiceStatus, self).save(*args, **kwargs)



class ServiceDetails(models.Model):

    class Meta:
        unique_together = (("id_service", "version"))
        verbose_name_plural = "02. Service Versions"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    id_service = models.ForeignKey(Service)
    version = models.CharField(max_length=255, default=None, blank=True)
    status = models.ForeignKey(ServiceStatus, default=None, blank=True) # allow empty field
    features_current = RichTextUploadingField(default=None, blank=True, null=True)
    features_future = RichTextUploadingField(default=None, blank=True, null=True)
    usage_policy_has = models.BooleanField(default=False, blank=True)
    usage_policy_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    privacy_policy_has = models.BooleanField(default=False, blank=True)
    privacy_policy_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    user_documentation_has = models.BooleanField(default=False, blank=True)
    user_documentation_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    operations_documentation_has = models.BooleanField(default=False, blank=True)
    operations_documentation_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    monitoring_has = models.BooleanField(default=False, blank=True)
    monitoring_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    accounting_has = models.BooleanField(default=False, blank=True)
    accounting_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    business_continuity_plan_has = models.BooleanField(default=False, blank=True)
    business_continuity_plan_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    disaster_recovery_plan_has = models.BooleanField(default=False, blank=True)
    disaster_recovery_plan_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    decommissioning_procedure_has = models.BooleanField(default=False, blank=True)
    decommissioning_procedure_url = models.CharField(max_length=255, default=None, blank=True, null=True)
    cost_to_run = models.CharField(max_length=255, default=None, blank=True, null=True)
    cost_to_build = models.CharField(max_length=255, default=None, blank=True, null=True)
    use_cases = RichTextUploadingField(default=None, blank=True, null=True)
    is_in_catalogue = models.BooleanField(default=False)

    def __unicode__(self):
        primary_key = self.id_service.pk
        srv = Service.objects.get(pk=primary_key)
        return str(srv.name) + " " + str(self.version)

    def save(self, *args, **kwargs):
        if not self.features_current or self.features_current == "":
            self.features_current = None
        if not self.features_future or self.features_future == "":
            self.features_future = None
        if not self.cost_to_run or self.cost_to_run == "":
            self.cost_to_run = None
        if not self.cost_to_build or self.cost_to_build == "":
            self.cost_to_build = None
        if not self.use_cases or self.use_cases == "":
            self.use_cases = None

        if not self.usage_policy_has:
            self.usage_policy_url = None
        if not self.user_documentation_has:
            self.user_documentation_url = None
        if not self.operations_documentation_has:
            self.operations_documentation_url = None
        if not self.monitoring_has:
            self.monitoring_url = None
        if not self.accounting_has:
            self.accounting_url = None
        if not self.business_continuity_plan_has:
            self.business_continuity_plan_url = None
        if not self.disaster_recovery_plan_has:
            self.disaster_recovery_plan_url = None
        if not self.decommissioning_procedure_has:
            self.decommissioning_procedure_url = None
        if not self.privacy_policy_has:
            self.privacy_policy_url = None

        if not self.usage_policy_url or self.usage_policy_url == "":
            self.usage_policy_url = None

        if not self.privacy_policy_url or self.privacy_policy_url == "":
            self.privacy_policy_url = None

        if not self.user_documentation_url or self.user_documentation_url == "":
            self.user_documentation_url = None

        if not self.operations_documentation_url or self.operations_documentation_url == "":
            self.operations_documentation_url = None

        if not self.monitoring_url or self.monitoring_url == "":
            self.monitoring_url = None

        if not self.accounting_url or self.accounting_url == "":
            self.accounting_url = None

        if not self.business_continuity_plan_url or self.business_continuity_plan_url == "":
            self.business_continuity_plan_url = None

        if not self.disaster_recovery_plan_url or self.disaster_recovery_plan_url == "":
            self.disaster_recovery_plan_url = None

        if not self.decommissioning_procedure_url or self.decommissioning_procedure_url == "":
            self.decommissioning_procedure_url = None

        super(ServiceDetails, self).save(*args, **kwargs)

    def as_short(self):

        return OrderedDict([
            ("uuid", self.id),
            ("version", self.version),
            ("service_status", self.status.value),
            ("features_current", self.features_current),
            ("features_future", self.features_future),
            ("privacy_policy_has", self.privacy_policy_has),
            ("privacy_policy_link", {
                "related": {
                    "href": self.privacy_policy_url,
                    "meta": {
                        "desc": "A link to the privacy policy for this service."
                    }
                }}),
            ("service_details", {
                "version": self.version,
                "status": self.status,
                "in_catalogue": self.is_in_catalogue,
                "links": {
                "self": helper.current_site_url() + "/v1/portfolio/services/" + str(self.id_service.name)
                        # replace(" ", "_")
                        + "/service_details/" + self.version,
                }
            })
        ])


    def as_catalogue(self, url=False):

        service_dependencies = self.id_service.get_service_dependencies()

        details = OrderedDict([
            ("uuid", self.id),
            ("version", self.version),
            ("service_status", self.status.value),
            ("use_cases", self.use_cases),
            ("features_current", self.features_current),
            ("features_future", self.features_future),
            ("dependencies_list", {
                "count": len(service_dependencies),
                # "links": {
                #     "related": {
                #         "href": helper.current_site_url() + "/v1/portfolio/services/" + str(self.id_service.name).replace(" ", "_")
                #                 + "/service_dependencies",
                #         "meta": {
                #             "desc": "A list of links to the service dependencies"
                #         }
                #     }
                #
                # },
                "services": service_dependencies
            }),
            ("usage_policy_has", self.usage_policy_has),
            ("usage_policy_link", {
                "related": {
                    "href": self.usage_policy_url,
                    "meta": {
                        "desc": "A link to the usage policy for this service."
                    }
                }}),
            ("privacy_policy_has", self.privacy_policy_has),
            ("privacy_policy_link", {
                "related": {
                    "href": self.privacy_policy_url,
                    "meta": {
                        "desc": "A link to the privacy policy for this service."
                    }
                }}),
            ("user_documentation_has", self.user_documentation_has),
            ("user_documentation_link",  {
                "related": {
                    "href": self.user_documentation_url,
                    "meta": {
                        "desc": "A link to the user documentation for this service."
                    }
                }}),
            ("cost_to_run", self.cost_to_run),
            ("cost_to_build", self.cost_to_build),
            ("service_details_type", "Catalogue" if self.is_in_catalogue else "Portfolio"),
            ("in_catalogue", self.is_in_catalogue)
        ])


        if url:
            details.update({
                "links": {
                    "self": helper.current_site_url() + "/v1/portfolio/services/" + str(self.id_service.name)
                            # replace(" ", "_")
                            + "/service_details/" + self.version,
                }
            })

        return details


    def as_complete(self, url=False):

        service_dependencies = self.id_service.get_service_dependencies()

        details = OrderedDict([
            ("uuid", self.id),
            ("version", self.version),
            ("service_status", self.status.value),
            ("use_cases", self.use_cases),
            ("features_current", self.features_current),
            ("features_future", self.features_future),
            ("dependencies_list", {
                "count": len(service_dependencies),
                # "links": {
                #     "related": {
                #         "href": helper.current_site_url() + "/v1/portfolio/services/" + str(self.id_service.name).replace(" ", "_")
                #                 + "/service_dependencies",
                #         "meta": {
                #             "desc": "A list of links to the service dependencies"
                #         }
                #     }
                #
                # },
                "services": service_dependencies
            }),
            ("usage_policy_has", self.usage_policy_has),
            ("usage_policy_link", {
                "related": {
                    "href": self.usage_policy_url,
                    "meta": {
                        "desc": "A link to the usage policy for this service."
                    }
                }}),
            ("privacy_policy_has", self.privacy_policy_has),
            ("privacy_policy_link", {
                "related": {
                    "href": self.privacy_policy_url,
                    "meta": {
                        "desc": "A link to the privacy policy for this service."
                    }
                }}),
            ("user_documentation_has", self.user_documentation_has),
            ("user_documentation_link",  {
                "related": {
                    "href": self.user_documentation_url,
                    "meta": {
                        "desc": "A link to the user documentation for this service."
                    }
                }}),
            ("operations_documentation_has", self.operations_documentation_has),
            ("operations_documentation_link", {
                "related": {
                    "href": self.operations_documentation_url,
                    "meta": {
                        "desc": "A link to the operations documentation for this service."
                    }
                }}),
            ("monitoring_has", self.monitoring_has),
            ("monitoring_link", {
                "related": {
                    "href": self.monitoring_url,
                    "meta": {
                        "desc": "A link to the monitoring system for this service."
                    }
                }}),
            ("accounting_has", self.accounting_has),
            ("accounting_link",  {
                "related": {
                    "href": self.accounting_url,
                    "meta": {
                        "desc": "A link to the accounting system for this service."
                    }
                }}),
            ("business_continuity_plan_has", self.business_continuity_plan_has),
            ("business_continuity_plan_link", {
                "related": {
                    "href": self.business_continuity_plan_url,
                    "meta": {
                        "desc": "A link to the business continuity plan for this service."
                    }
                }}),
            ("disaster_recovery_plan_has", self.disaster_recovery_plan_has),
            ("disaster_recovery_plan_link", {
                "related": {
                    "href": self.disaster_recovery_plan_url,
                    "meta": {
                        "desc": "A link to the disaster recovery plan for this service."
                    }
                }}),
            ("decommissioning_procedure_has", self.decommissioning_procedure_has),
            ("decommissioning_procedure_link",  {
                "related": {
                    "href": self.decommissioning_procedure_url,
                    "meta": {
                        "desc": "A link to the decommissioning procedure for this service."
                    }
                }}),
            ("cost_to_run", self.cost_to_run),
            ("cost_to_build", self.cost_to_build),
            ("service_details_type", "Catalogue" if self.is_in_catalogue else "Portfolio"),
            ("in_catalogue", self.is_in_catalogue)
        ])


        if url:
            details.update({
                "links": {
                    "self": helper.current_site_url() + "/v1/portfolio/services/" + str(self.id_service.name)
                            # replace(" ", "_")
                            + "/service_details/" + self.version,
                }
            })

        return details

    def as_json(self):
        return OrderedDict([
            ("uuid", self.id),
            ("version", self.version),
            ("service_status", self.status.value),
            ("features_current", self.features_current),
            ("features_future", self.features_future)
        ])

    def as_portfolio_view(self):
        dict = self.as_complete()
        dict["service"] = {
            "name": self.id_service.name,
            "uuid": self.id_service.pk
        }

        return dict


class ExternalService(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, default=None, blank=True, unique=True)
    description = RichTextUploadingField(default=None, blank=True, null=True)
    service = models.CharField(max_length=255, default=None, blank=True, null=True)
    details = models.CharField(max_length=255, default=None, blank=True, null=True)

    class Meta:
        verbose_name_plural = "04. External Services"

    def __unicode__(self):
        return str(self.name)

    def as_json(self):
        return OrderedDict([
            ("id", self.id),
            ("name", self.name),
            ("description", self.description),
            ("service", self.service),
            ("details", self.details)
        ])

    def save(self, *args, **kwargs):
        if not self.description or self.description == "":
            self.description = none
        super(ExternalService, self).save(*args, **kwargs)


class Service_DependsOn_Service(models.Model):

    class Meta:
        unique_together = (('id_service_one', 'id_service_two'),)
        verbose_name_plural = "03. Internal Dependencies"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_service_one = models.ForeignKey(Service, related_name='service_one')
    id_service_two = models.ForeignKey(Service, related_name='service_two')

    def __unicode__(self):
        primary_key_one = self.id_service_one.pk
        primary_key_two = self.id_service_two.pk

        srv1 = Service.objects.get(pk=primary_key_one)
        srv2 = Service.objects.get(pk=primary_key_two)

        return str(srv1.name) + " " + str(srv2.name)

    def as_json(self):
        return {
            "service": self.id_service_one.name,
            "dependency": self.id_service_two.name
        }

    def as_full(self):
        return {
            "service": {
                "uuid": self.id_service_one.pk,
                "name": self.id_service_one.name
            },
            "service_dependency": {
                "uuid": self.id_service_two.pk,
                "name": self.id_service_two.name
            }
        }


class Service_ExternalService(models.Model):

    class Meta:
        unique_together = (('id_service', 'id_external_service'),)
        verbose_name_plural = "05. External Dependencies"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_service = models.ForeignKey(Service)
    id_external_service = models.ForeignKey(ExternalService)

    def __unicode__(self):
        primary_key_one = self.id_service.pk

        external_primary_key_one = self.id_external_service.pk

        srv1 = Service.objects.get(pk=primary_key_one)
        srv2 = ExternalService.objects.get(pk=external_primary_key_one)

        return str(srv1.name) + " " + str(srv2.name)

    def as_json(self):
        return {
            "service": self.id_service.pk,
            "external_service": self.id_external_service.pk
        }

    def as_full(self):
        return {
            "service": {
                "uuid": self.id_service.pk,
                "name": self.id_service.name
            },
            "external_service": {
                "uuid": self.id_external_service.pk,
                "name": self.id_external_service.name
            }
        }


class UserRole(models.Model):

    class Meta:
        verbose_name_plural = "07. User Roles (settings)"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, blank=True)
    name = models.CharField(max_length=255, default=None, unique=True)

    def __unicode__(self):
        return str(self.name)

    def as_json(self):
        return OrderedDict([
            ("uuid", self.id),
            ("name", self.name)
        ])

    def save(self, *args, **kwargs):
        super(UserRole, self).save(*args, **kwargs)


class UserCustomer(models.Model):

    class Meta:
        verbose_name_plural = "08. Users / Customers of a Service"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.ForeignKey(UserRole)
    role = RichTextUploadingField(default=None, blank=True, null=True)
    service_id = models.ForeignKey(Service)

    def __unicode__(self):
        return str(self.name) + " as " + str(self.role) + " for " + str(self.service_id)

    def as_json(self):
        return OrderedDict([
            ("uuid", self.pk),
            ("name", self.name.name),
            ("role", self.role)
        ])

    def as_full(self):
        return OrderedDict([
            ("uuid", self.pk),
            ("name", self.name.name),
            ("role", self.role),
            ("service", {
                "name": self.service_id.name,
                "uuid": self.service_id.pk
            })
        ])

    def save(self, *args, **kwargs):
        if not self.role or self.role == "":
            self.role = None
        super(UserCustomer, self).save(*args, **kwargs)


class Roles(models.Model):

    id_user = models.ForeignKey(User)
    id_service = models.ForeignKey(Service)
    role = models.CharField(('role'), max_length=90, unique=True, default="spectator")


class ServiceAdminship(models.Model):
    service = models.ForeignKey(Service)
    admin = models.ForeignKey(User)
    state = models.CharField(
            choices=SERVICE_ADMINSHIP_STATES,
            max_length=30,
            default='pending')

    class Meta:
        unique_together = (("service", "admin"),)

def post_create_service(service, context):
    user = context.extract(b'auth/user')
    ServiceAdminship.objects.create(
            service=service,
            admin=user,
            state='approved')
