from __future__ import unicode_literals
from agora import  settings
from django.db import models
import uuid
from owner.models import ContactInformation
from common import helper
from accounts.models import User, Organisation, Domain, Subdomain
from ckeditor_uploader.fields import RichTextUploadingField
from agora.utils import SERVICE_ADMINSHIP_STATES, clean_html_fields, \
    publish_message, RESOURCE_STATES
from agora.emails import send_email_application_created, \
    send_email_resource_admin_assigned, send_email_application_evaluated
from apimas.base import ProcessorFactory
from copy import deepcopy


class PostCreateResourceadminship(ProcessorFactory):
    def process(self, data):
        user = data['auth/user']
        http_host = data['request/meta/headers'].get('HTTP_HOST', 'Agora')

        sa = data['backend/raw_response']
        if sa.state == 'pending':
            send_email_application_created(sa, http_host)
        if sa.admin != user:
            send_email_resource_admin_assigned(sa, http_host)
        return {}


class PostPartialUpdateResourceadminship(ProcessorFactory):
    def process(self, data):
        http_host = data['request/meta/headers'].get('HTTP_HOST', 'Agora')
        send_email_application_evaluated(data['backend/raw_response'], http_host)
        return {}


class TargetUser(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.CharField(max_length=255, unique=True)
    description = RichTextUploadingField(default=None, blank=True, null=True)

    def __unicode__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(TargetUser, self).save(*args, **kwargs)

class Supercategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Supercategory, self).save(*args, **kwargs)

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    supercategory = models.ForeignKey('service.Supercategory', blank=True, null=True, related_name='supercategory_category')
    name = models.CharField(max_length=255, unique=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Category, self).save(*args, **kwargs)

class Subcategory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category = models.ForeignKey('service.Category', blank=True, null=True, related_name='category_subcategory')
    name = models.CharField(max_length=255)

    class Meta:
        unique_together = ('category', 'name')

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Subcategory, self).save(*args, **kwargs)


class OrderType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default=None, blank=True, null=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(OrderType, self).save(*args, **kwargs)

class FundingBody(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

class FundingProgram(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)

class AccessType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default=None, blank=True, null=True)


class AccessMode(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default=None, blank=True, null=True)

class TRL(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default=None, blank=True, null=True)

class LifeCycleStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default=None, blank=True, null=True)

class Resource(models.Model):

    # Basic Information fields
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    erp_bai_0_id = models.CharField(max_length=100, unique=True)
    erp_bai_1_name = models.CharField(max_length=100, unique=True)
    erp_bai_2_organisation = models.ForeignKey(Organisation,
            blank=False,
            null=True,
            related_name="organisation_services")
    erp_bai_3_providers = models.ManyToManyField(Organisation,
            blank=True,
            related_name="provided_services")
    erp_bai_4_webpage = models.EmailField(default=None, blank=False, null=True)

    # Marketing Information fields
    erp_mri_1_description = RichTextUploadingField(max_length=1000, default=None, blank=True,  null=True)
    erp_mri_2_tagline = models.TextField(max_length=100, default=None, blank=True, null=True)
    erp_mri_3_logo = models.EmailField(default=None, blank=True, null=True)
    erp_mri_4_mulitimedia = models.EmailField(default=None, blank=True, null=True)
    erp_mri_5_use_cases = models.TextField(default=None, blank=True, null=True)

    # Classification information
    erp_cli_1_scientific_domain = models.ManyToManyField(
        Domain,
        blank=True,
        related_name='domain_resources')

    erp_cli_2_scientific_subdomain = models.ManyToManyField(
        Subdomain,
        blank=True,
        related_name='subdomain_resources')

    erp_cli_3_category = models.ManyToManyField(
        Category,
        blank=True,
        related_name='categorized_resources')

    erp_cli_4_subcategory = models.ManyToManyField(
        Subcategory,
        blank=True,
        related_name='subcategorized_resources')
    erp_cli_5_target_users = models.ManyToManyField(TargetUser, blank=True)

    erp_cli_6_access_type = models.ManyToManyField(AccessType, blank=True)
    erp_cli_7_access_mode = models.ManyToManyField(AccessMode, blank=True)

    erp_cli_8_tags = models.TextField(max_length=255, default=None, blank=True, null=True)


    # Management Information
    erp_mgi_1_helpdesk_webpage       = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_2_user_manual            = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_3_terms_of_use           = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_4_privacy_policy         = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_5_access_policy          = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_6_sla_specification      = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_7_training_information   = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_8_status_monitoring      = models.URLField(max_length=255, default=None, blank=True, null=True)
    erp_mgi_9_maintenance            = models.URLField(max_length=255, default=None, blank=True, null=True)

    # Geographical and Language Availability fields
    erp_gla_1_geographical_availability = models.CharField(max_length=255,
        default=None,
        blank=True,
        null=True)
    erp_gla_2_language = models.TextField(default=None, blank=True, null=True)

    # Resource Location Information
    erp_rli_1_geographic_location = models.TextField(default='Other', blank=True, null=True)

    # Contact Information
    main_contact = models.ForeignKey(ContactInformation,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="main_contact_services")
    public_contact = models.ForeignKey(ContactInformation,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="public_contact_services")
    erp_coi_13_helpdesk_email = models.EmailField(default=None, blank=True, null=True)
    erp_coi_14_security_contact_email = models.EmailField(default=None, blank=True, null=True)

    # Maturity Information
    erp_mti_1_technology_readiness_level = models.ForeignKey(TRL, blank=False, null=True)
    erp_mti_2_life_cycle_status = models.ForeignKey(LifeCycleStatus, blank=False, null=True)
    erp_mti_3_certifications = RichTextUploadingField(default=None, blank=True, null=True)
    erp_mti_4_standards = RichTextUploadingField(default=None, blank=True, null=True)
    erp_mti_5_open_source_technologies = RichTextUploadingField(default=None, blank=True, null=True)
    erp_mti_6_version = models.CharField(max_length=255, default=None, blank=True, null=True)
    erp_mti_7_last_update = models.CharField(max_length=255, blank=True, null=True)
    erp_mti_8_changelog = RichTextUploadingField(default=None, blank=True, null=True)

    # Dependencies Information fields
    required_resources = models.ManyToManyField('self', blank=True,
                                               symmetrical=False,
                                               related_name='is_required_by')
    related_resources = models.ManyToManyField('self', blank=True,
                                              symmetrical=False,
                                              related_name='set_as_related_by')
    erp_dei_3_related_platforms = models.TextField(default=None, blank=True, null=True)

    # Attribution Information
    erp_ati_1_funding_body = models.ManyToManyField(
        FundingBody,
        blank=True,
        related_name='funded_body_resources')

    erp_ati_2_funding_program = models.ManyToManyField(
        FundingProgram,
        blank=True,
        related_name='funded_program_resources')
    erp_ati_3_grant_project_name = models.CharField(max_length=255,
        default=None,
        blank=True,
        null=True)

    # Access and Order Information
    erp_aoi_1_order_type = models.ForeignKey(OrderType,
                                              blank=True,
                                              null=True,
                                              related_name='resources')
    erp_aoi_2_order = models.URLField(default=None, blank=True, null=True)

    # Financial Information
    erp_fni_1_payment_model = models.URLField(default=None, blank=True, null=True)
    erp_fni_2_pricing = models.URLField(default=None, blank=True, null=True)

    state = models.CharField(
            choices=RESOURCE_STATES,
            max_length=30,
            default='draft')

    def __unicode__(self):
        return str(self.erp_bai_0_id)

    @property
    def category_names(self):
        return ", ".join(o.name for o in self.erp_cli_3_category.all())

    @property
    def subcategory_names(self):
        return ", ".join(o.name for o in self.erp_cli_4_subcategory.all())

    @property
    def domain_names(self):
        return ", ".join(o.name for o in self.erp_cli_1_scientific_domain.all())

    @property
    def subdomain_names(self):
        return ", ".join(o.name for o in self.erp_cli_2_scientific_subdomain.all())

    @property
    def providers_names(self):
        return ", ".join(o.epp_bai_1_name for o in self.erp_bai_3_providers.all())

    @property
    def required_resources_ids(self):
        return ", ".join(o.erp_bai_0_id for o in self.required_resources.all())

    @property
    def related_resources_ids(self):
        return ", ".join(o.erp_bai_0_id for o in self.related_resources.all())

    @property
    def erp_cli_5_target_users_verbose(self):
        return ", ".join(o.user for o in self.erp_cli_5_target_users.all())

    def save(self, *args, **kwargs):
        self.erp_bai_0_id = self.erp_bai_0_id.strip()
        self.erp_bai_1_name = self.erp_bai_1_name.strip()
        clean_html_fields(self)
        super(Resource, self).save(*args, **kwargs)

    @property
    def resource_admins_ids(self):
        resource_adminships = ResourceAdminship.objects.filter(
            resource=self,
            state="approved")
        res = []
        for r in resource_adminships:
            res.append(str(r.admin.pk))
        return ','.join(res)

    @property
    def resource_admins(self):
        resource_adminships = ResourceAdminship.objects.filter(
            resource=self,
            state="approved")
        res = []
        for r in resource_adminships:
            res.append(r.admin)
        return res

    @property
    def pending_resource_admins_ids(self):
        resource_adminships = ResourceAdminship.objects.filter(
            resource=self,
            state="pending")
        res = []
        for r in resource_adminships:
            res.append(str(r.admin.pk))
        return ','.join(res)

    @property
    def rejected_resource_admins_ids(self):
        resource_adminships = ResourceAdminship.objects.filter(
            resource=self,
            state="rejected")
        res = []
        for r in resource_adminships:
            res.append(str(r.admin.pk))
        return ','.join(res)


class ResourceAdminship(models.Model):
    resource = models.ForeignKey(Resource, related_name="resourceadminships")
    admin = models.ForeignKey(User)
    state = models.CharField(
            choices=SERVICE_ADMINSHIP_STATES,
            max_length=30,
            default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("resource", "admin"),)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(ResourceAdminship, self).save(*args, **kwargs)

class PostCreateResource(ProcessorFactory):
    def process(self, data):
        user = data['auth/user']
        resource = data['backend/raw_response']
        ResourceAdminship.objects.create(
                resource=resource,
                admin=user,
                state='approved')
        return {}
