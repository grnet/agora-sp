import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField
from agora.utils import USER_ROLES, LIFECYCLE_STATUSES ,clean_html_fields, PROVIDER_STATES
from apimas.base import ProcessorFactory
from common import helper

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password,
                     is_staff, is_superuser, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')

        if not username:
            raise ValueError('The given username must be set')

        email = self.normalize_email(email)
        user = self.model(email=email,
                          username=username,
                          is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):

        return self._create_user(username, email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):

        return self._create_user(username, email, password, True, True,
                                 **extra_fields)

# Smaller models used to provide other information for provider fields

class Network(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=60, default=None)
    eosc_id = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Network, self).save(*args, **kwargs)

class Structure(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default=None, blank=True, null=True)
    eosc_id = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Structure, self).save(*args, **kwargs)

class Affiliation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    eosc_id = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Affiliation, self).save(*args, **kwargs)

class EsfriDomain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(default=None, blank=True, null=True)
    eosc_id = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(EsfriDomain, self).save(*args, **kwargs)

class EsfriType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    eosc_id = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(EsfriType, self).save(*args, **kwargs)

class Activity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    eosc_id = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Activity, self).save(*args, **kwargs)

class Challenge(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    eosc_id = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Challenge, self).save(*args, **kwargs)

class Domain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    eosc_id = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Domain, self).save(*args, **kwargs)

class MerilDomain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    eosc_id = models.CharField(max_length=255, blank=True, null=True)

class Subdomain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    domain = models.ForeignKey('accounts.Domain', blank=True, null=True, related_name='domain_subdomain')
    name = models.CharField(max_length=255, unique=True)
    eosc_id = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(Subdomain, self).save(*args, **kwargs)

class MerilSubdomain(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    domain = models.ForeignKey('accounts.MerilDomain', blank=True, null=True, related_name='merildomain_merilsubdomain')
    name = models.CharField(max_length=255, unique=False)
    description = models.TextField(default=None, blank=True, null=True)
    eosc_id = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(MerilSubdomain, self).save(*args, **kwargs)

class LegalStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, unique=True)
    eosc_id = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        super(LegalStatus, self).save(*args, **kwargs)

class Organisation(models.Model):
    """
    The organisation providing the Service
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    epp_bai_id = models.CharField(unique=True, max_length=100)
    epp_bai_name = models.CharField(unique=True, max_length=100)
    epp_bai_abbreviation = models.CharField(max_length=30, default=None, blank=False, null=True)
    epp_bai_website = models.TextField(default=None, blank=True, null=True)

    epp_bai_legal_entity = models.BooleanField(default=False)
    epp_bai_legal_status =  models.ForeignKey(
        'accounts.LegalStatus',
        blank=True,
        null=True,
        related_name='legalstatus_providers')
    epp_bai_hosting_legal_entity = models.CharField(max_length=80, default=None, blank=True, null=True)

    # Classification section
    epp_cli_scientific_domain = models.ManyToManyField(
        Domain,
        blank=True,
        related_name='domain_providers')

    epp_cli_scientific_subdomain = models.ManyToManyField(
        Subdomain,
        blank=True,
        related_name='subdomain_providers')

    epp_cli_tags = models.TextField(default=None, blank=True, null=True)


    # Location section
    epp_loi_1_street_name_and_number = models.CharField(max_length=50, default=None, blank=True, null=True)
    epp_loi_2_postal_code = models.CharField(max_length=20, default=None, blank=True, null=True)
    epp_loi_3_city = models.CharField(max_length=50, default=None, blank=True, null=True)
    epp_loi_4_region = models.CharField(max_length=50, default=None, blank=True, null=True)
    epp_loi_5_country_or_territory = models.CharField(max_length=50, default=None, blank=True, null=True)

    # Marketing section
    epp_mri_1_description = RichTextUploadingField(max_length=1000, default=None, blank=True, null=True)
    epp_mri_2_logo = models.TextField(default=None, blank=True, null=True)
    epp_mri_3_multimedia = models.TextField(default=None, blank=True, null=True)

    # Contact Information
    main_contact = models.ForeignKey('owner.ContactInformation', blank=True, null=True, related_name="main_contact_provders")
    public_contact = models.ForeignKey('owner.ContactInformation', blank=True, null=True, related_name="public_contact_providers")

    # Maturity Information
    epp_mti_1_life_cycle_status = models.CharField(max_length=255,
                                                  default=None, blank=True, null=True,
                                                  choices=LIFECYCLE_STATUSES)

    epp_mti_2_certifications = models.TextField(default=None, blank=True, null=True)

   # Other information section
    epp_oth_participating_countries = models.TextField(default=None, blank=True, null=True)

    epp_oth_affiliations = models.ManyToManyField(
        Affiliation,
        blank=True,
        related_name='affiliated_providers')

    epp_oth_networks = models.ManyToManyField(
        Network,
        blank=True,
        related_name='networked_providers')

    epp_oth_structure_type = models.ManyToManyField(
        Structure,
        blank=True,
        related_name='structured_providers')

    epp_oth_esfri_domain = models.ManyToManyField(
        EsfriDomain,
        blank=True,
        related_name='esfridomain_providers')

    epp_oth_esfri_type = models.ForeignKey(
        'accounts.EsfriType',
        blank=True,
        null=True,
        related_name='esfritype_providers')

    epp_oth_meril_scientific_domain = models.ManyToManyField(
        MerilDomain,
        blank=True,
        related_name='meril_domain_providers')

    epp_oth_meril_scientific_subdomain = models.ManyToManyField(
        MerilSubdomain,
        blank=True,
        related_name='meril_subdomain_providers')

    epp_oth_areas_of_activity = models.ManyToManyField(
        Activity,
        blank=True,
        related_name='activity_providers')

    epp_oth_societal_grand_challenges = models.ManyToManyField(
        Challenge,
        blank=True,
        related_name='challenge_providers')

    epp_oth_national_roadmaps = models.CharField(max_length=80, default=None, blank=True, null=True)

    state = models.CharField(
            choices=PROVIDER_STATES,
            max_length=30,
            default='draft')

    # Datetime fields
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)

    eosc_id = models.CharField(max_length=255, blank=True, null=True)
    eosc_published_at = models.DateTimeField(blank=True, null=True)
    eosc_updated_at = models.DateTimeField(blank=True, null=True)
    eosc_state = models.CharField(max_length=255, blank=True, null=True)

    @property
    def epp_oth_affiliations_verbose(self):
        return ", ".join(o.name for o in self.epp_oth_affiliations.all())

    @property
    def epp_oth_networks_verbose(self):
        return ", ".join(o.name + " (" + o.abbreviation + ")" for o in self.epp_oth_networks.all())

    @property
    def epp_oth_structure_type_verbose(self):
        return ", ".join(o.name for o in self.epp_oth_structure_type.all())

    @property
    def epp_oth_esfri_domain_verbose(self):
        return ", ".join(o.name for o in self.epp_oth_esfri_domain.all())

    @property
    def epp_oth_areas_of_activity_verbose(self):
        return ", ".join(o.name for o in self.epp_oth_areas_of_activity.all())

    @property
    def epp_oth_societal_grand_challenges_verbose(self):
        return ", ".join(o.name for o in self.epp_oth_societal_grand_challenges.all())

    @property
    def epp_cli_scientific_domain_verbose(self):
        return ", ".join(o.name for o in self.epp_cli_scientific_domain.all())

    @property
    def epp_cli_scientific_subdomain_verbose(self):
        return ", ".join(o.name for o in self.epp_cli_scientific_subdomain.all())

    @property
    def epp_oth_meril_scientific_domain_verbose(self):
        return ", ".join(o.name for o in self.epp_oth_meril_scientific_domain.all())

    @property
    def epp_oth_meril_scientific_subdomain_verbose(self):
        return ", ".join(o.name for o in self.epp_oth_meril_scientific_subdomain.all())

    @property
    def epp_loi_5_country_or_territory_capitalize(self):
        """
        This will transform 'bulgaria (bg)' to 'Bulgaria (BG)'
        """
        if self.epp_loi_5_country_or_territory:
            el = self.epp_loi_5_country_or_territory.replace(')', '')
            country_lower, code  = el.split('(')
            country_lower = country_lower.split(' ')
            country = [];
            for word in country_lower:
                if word not in ['and', 'of', 'da', 'the']:
                    word = word.capitalize()
                country.append(word)
            country = ' '.join(country)
            code = code.upper()
            return '%s (%s)' % (country, code)
        else:
            return ''

    def save(self, *args, **kwargs):
        clean_html_fields(self)
        if self.state == 'published' and not self.published_at:
            self.published_at = timezone.now()
        super(Organisation, self).save(*args, **kwargs)


class User(AbstractBaseUser, PermissionsMixin):
    """
    A fully featured User model with admin-compliant permissions

    """
    username = models.CharField(('username'), max_length=30, unique=True,
                                default=None)
    email = models.EmailField(('email address'), max_length=254, unique=True)
    first_name = models.CharField(('first name'), max_length=30, blank=True)
    last_name = models.CharField(('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    shibboleth_id = models.CharField(max_length=255,
                                     unique=True, null=True, default=None)
    role = models.CharField(choices=USER_ROLES, max_length=20, default='observer')
    organisations = models.ManyToManyField(Organisation, blank=True)
    organisation = models.ForeignKey(Organisation,
                                      blank=True,
                                      null=True,
                                      on_delete=models.PROTECT,
                                      related_name='organisation_users')

    # Unused fields
    is_staff = models.BooleanField(('staff status'), default=False)
    is_active = models.BooleanField(('active'), default=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'role']

    @property
    def apimas_roles(self):
        return [self.role]

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def __unicode__(self):
        return str(self.email)


class ProviderAudit(models.Model):
    provider = models.ForeignKey(Organisation, related_name="provideraudittable")
    updater = models.ForeignKey(User)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (("provider", "updated_at"),)


class PostUpdateProvider(ProcessorFactory):
    def process(self, data):
        user = data['auth/user']
        provider = data['backend/raw_response']
        ProviderAudit.objects.create(
                provider=provider,
                updater=user)
        return {}