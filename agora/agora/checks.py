from django.db.models import Q
from django.utils.translation import ugettext as _
from apimas.errors import ValidationError
from service.models import ResourceAdminship as sa_m
from service.models import Resource as r_m
from accounts.models import User as user_m


def resource_organisation_owned(backend_input, instance, context):
    """Servicadmins/ProviderAdmins must belong to Resource's organisation.

    The resource's organisations must be the same as the one the
    serviceadmin belongs to.
    """
    auth_user = context['auth/user']
    resource_org_id = str(backend_input.get('erp_bai_2_organisation_id'))
    user_org_id = str(auth_user.organisation.id)

    if not user_org_id == resource_org_id:
        raise ValidationError(_('Unauthorized organisation(s)'))


def contact_information_organisation_owned(backend_input, instance, context):
    """Servicadmins/ProviderAdmins must belong to the same Organisation as the
    Contact Information they are about to create/update.
    """
    auth_user = context['auth/user']
    user_org_id = str(auth_user.organisation.id)
    contact_org_id = str(backend_input.get('organisation_id'))

    if not contact_org_id == user_org_id:
        raise ValidationError(_('Unauthorized organisation(s)'))


class ResourceAdminship(object):

    @staticmethod
    def check_create_other(backend_input, instance, context):
        """Superadmins can create ResourceAdminships.

        Superadmins can create a new ResourceAdminship instance
        for a given resource and a given user, only if the user has role
        'serviceadmin', she/he does not already admin the resource and
        user's Organisation is the same as the Resource's Organisation.
        The ResourceAdminship created by Superadmins has state
        'approved'.
        """
        admin = user_m.objects.get(id=backend_input['admin_id'])
        if admin.role != 'serviceadmin':
            raise ValidationError(_('Wrong admin role'))

        resource = r_m.objects.get(pk=backend_input['resource_id'])

        resource_org_id = resource.erp_bai_2_organisation.pk
        if not admin.organisation:
            raise ValidationError(_('No organisation'))
        if resource_org_id != admin.organisation.id:
            raise ValidationError(_('Forbidden Resource Organisation'))
        try:
            sa_m.objects.get(admin=backend_input['admin_id'],
                             resource=backend_input['resource_id'])
            raise ValidationError(_('ResourceAdminship Object exists'))
        except sa_m.DoesNotExist:
            backend_input['state'] = 'approved'
            return

    @staticmethod
    def check_create_other_own_organisation(backend_input, instance, context):
        """Provider Admins can create ResourceAdminships.

        Provider Admins can create a new ResourceAdminship instance
        for a given resource and a given user, only if:
        - the user has role 'serviceadmin'
        - she/he does not already admin
        - the resource user's Organisation is the same as the Resource's Organisation
        - the Resource's Organsation is the same as the Provider Admins
        The ResourceAdminship created by Provider Admins has state
        'approved'.
        """
        auth_user = context['auth/user']
        user_org_id = auth_user.organisation.id
        admin = user_m.objects.get(id=backend_input['admin_id'])
        if admin.role != 'serviceadmin':
            raise ValidationError(_('Wrong admin role'))

        resource = r_m.objects.get(pk=backend_input['resource_id'])

        resource_org_id = resource.erp_bai_2_organisation.pk
        if not admin.organisation:
            raise ValidationError(_('No organisation'))
        if resource_org_id != admin.organisation.id:
            raise ValidationError(_('Forbidden Resource Organisation'))
        if resource_org_id != user_org_id:
            raise ValidationError(_('Forbidden Resource Organisation'))
        try:
            sa_m.objects.get(admin=backend_input['admin_id'],
                             resource=backend_input['resource_id'])
            raise ValidationError(_('ResourceAdminship Object exists'))
        except sa_m.DoesNotExist:
            backend_input['state'] = 'approved'
            return

    @staticmethod
    def check_create_self(backend_input, instance, context):
        """Serviceadmins can request ResourceAdminships.

        A user can create a ResourceAdminship instance only if she/he does not
        already admin the resource and user's Organisation is the same as the
        resource's Organisation.
        The ResourceAdminship created is not yet approved/rejected, so it is
        created with state 'pending'.
        """
        auth_user = context['auth/user']
        resource = r_m.objects.get(pk=backend_input['resource_id'])
        resource_org_id = resource.erp_bai_2_organisation.pk
        if not auth_user.organisation:
            raise ValidationError(_('No organisation'))
        if resource_org_id != auth_user.organisation.id:
            raise ValidationError(_('Forbidden Resource Organisation'))
        try:
            sa_m.objects.get(admin=auth_user.id,
                             resource=backend_input['resource_id'])
            raise ValidationError(_('ResourceAdminship Object exists'))
        except sa_m.DoesNotExist:
            backend_input['admin_id'] = auth_user.id
            backend_input['state'] = 'pending'
            return

    @staticmethod
    def is_involved(instance, context):
        """Serviceadmins retrieve ResourceAdminships they are involved in.

        Serviceadmins can retrieve ResourceAdminships of Resources they admin,
        so that they can reject/approve these ResourceAdminships.
        Serviceadmins can also retrieve the ResourceAdminship for which they
        are admins regardlress of the state, so that they can view a
        ResourceAdminship request or revoke one.
        """
        auth_user = context['auth/user']
        user_sa = sa_m.objects.filter(admin=auth_user, state='approved')
        user_resources = [x.resource for x in user_sa]
        if instance.resource in user_resources:
            return instance
        if instance.admin == auth_user:
            return instance
        return None

    @staticmethod
    def check_update(backend_input, instance, context):
        """Check allowed transitions between ResourceAdminship instances.

        The transition between 'approved' and 'rejected' must go via 'pending'.
        """
        TRANSITIONS = set([
            ('pending', 'approved'),
            ('pending', 'rejected'),
            ('rejected', 'pending'),
            ('approved', 'pending'),
        ])

        current_state = instance.state
        input_state = backend_input['state']

        if (current_state, input_state) not in TRANSITIONS:
            raise ValidationError(_('Transition not allowed'))

    @staticmethod
    def manages(context):
        """Serviceadmins can partially update some ResourceAdminships.

        A serviceadmin can partially update ResourceAdminships of resources
        he/she admins.
        """
        auth_user = context['auth/user']
        user_sa = sa_m.objects.filter(admin=auth_user, state='approved')
        user_resources = [x.resource for x in user_sa]

        return Q(resource__in=user_resources) & ~Q(admin=auth_user)

    @staticmethod
    def manages_or_self_pending(context):
        """Serviceadmins list a subset of ResourceAdminships.

        A serviceadmin can list ResourceAdminships if he/she has applied for
        a ResourceAdminship and is still in state 'pending' so that he/she can
        revoke it, if he/she has an approved ResourceAdminship, or if he/she
        admins the resource of the ResourceAdminship.
        """
        auth_user = context['auth/user']
        user_sa = sa_m.objects.filter(admin=auth_user, state='approved')
        resources = [x.resource for x in user_sa]
        self_pending = Q(admin=auth_user, state='pending')

        return (Q(resource__in=resources) & ~Q(admin=auth_user)) | self_pending

    @staticmethod
    def self_pending(context):
        """A serviceadmin can delete a ResourceAdminship.

        A serviceadmin can delete a ResourceAdminship so that she/he can
        revoke the ResourceAdminship application.
        The ResourceAdminship should still be in state 'pending' and the admin
        should be the user.
        """
        auth_user = context['auth/user']

        return Q(admin=auth_user, state='pending')

    @staticmethod
    def filter_my_provider(context):
        """
        A Provider Admin can only list Resource Adminships for his/her
        Organisation.
        """
        auth_user = context['auth/user']
        user_org_id = str(auth_user.organisation.id)

        return Q(resource__erp_bai_2_organisation_id=user_org_id)


class User(object):

    @staticmethod
    def me(context):
        """
        A serviceadmin can only retrieve herself.
        """
        auth_user = context['auth/user']
        return Q(id=auth_user.id)

    @staticmethod
    def filter_my_provider(context):
        """
        A Provider Admin can only list observers and serviceadmins that
        belong to his Organisation
        """
        auth_user = context['auth/user']
        user_org_id = str(auth_user.organisation.id)
        return (Q(role='serviceadmin') & Q(organisation_id=user_org_id)) | Q(role='observer')

    @staticmethod
    def filter_my_provider_me(context):
        """
        A Provider Admin can retrieve observers and serviceadmins that
        belong to his Organisation and himself
        """
        auth_user = context['auth/user']
        user_org_id = str(auth_user.organisation.id)
        return (Q(role='serviceadmin') & Q(organisation_id=user_org_id)) | \
               Q(role='observer') | \
               Q(id=auth_user.id)

    @staticmethod
    def check_unique(backend_input, instance, context):
        backend_email = backend_input['email']
        instance_email = instance.email

        if backend_email != instance_email:
            try:
                user_m.objects.get(email=backend_email)
                raise ValidationError(_('Email unique constraint failed'))
            except user_m.DoesNotExist:
                pass

        backend_username = backend_input['username']
        instance_username = instance.username

        if backend_username != instance_username:
            try:
                user_m.objects.get(username=backend_username)
                raise ValidationError(_('Username unique constraint failed'))
            except user_m.DoesNotExist:
                pass

        return




class Organisation(object):

    @staticmethod
    def update_organisation_owned(backend_input, instance, context):
        """
        Serviceproviders can edit the Organisation they belong to.
        """
        auth_user = context['auth/user']
        user_org_id = str(auth_user.organisation.id)
        org_id = str(instance.pk)

        if not org_id == user_org_id:
            raise ValidationError(_('Unauthorized organisation(s)'))


class Resource(object):

    @staticmethod
    def owned(backend_input, instance, context):
        """Servicadmins can update Resources they own.

        A serviceadmin owns a Resource if resource's resource_admins_ids
        computed property contains the id of the user.
        The resource's organisations must be the same as the one the
        serviceadmin belongs to.
        """
        auth_user = context['auth/user']
        auth_user_id = str(auth_user.id)
        service_admins_ids = instance.resource_admins_ids.split(",")
        resource_org_id = str(backend_input.get('erp_bai_2_organisation_id'))
        user_org_id = str(auth_user.organisation.id)

        if not user_org_id == resource_org_id:
            raise ValidationError(_('Unauthorized organisation(s)'))

        if auth_user_id in service_admins_ids:
            return
        else:
            raise ValidationError(_('Unauthorized action'))

    @staticmethod
    def create_organisation_owned(backend_input, instance, context):
        return resource_organisation_owned(backend_input, instance, context)

    @staticmethod
    def update_organisation_owned(backend_input, instance, context):
        return resource_organisation_owned(backend_input, instance, context)


class ContactInformation(object):

    @staticmethod
    def create_organisation_owned(backend_input, instance, context):
        return contact_information_organisation_owned(backend_input, instance, context)

    @staticmethod
    def update_organisation_owned(backend_input, instance, context):
        return contact_information_organisation_owned(backend_input, instance, context)
