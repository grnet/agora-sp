from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from common.helper import current_site_baseurl

import logging
logger = logging.getLogger('apimas')


def get_login_url():
    return current_site_baseurl() + settings.TOKEN_LOGIN_URL


def send_email_shib_user_created(user, http_host):
    tpl_subject = 'emails/shib_user_created_subject.txt'
    tpl_body = 'emails/shib_user_created_body.txt'
    tpl_context = {
        'user': user,
        'http_host': http_host
    }
    subject = render_to_string(tpl_subject, tpl_context).replace('\n', ' ')
    body = render_to_string(tpl_body, tpl_context)
    sender = settings.DEFAULT_FROM_EMAIL
    recipient_list = settings.USER_CREATION_EMAIL_LIST
    send_mail(
        subject,
        body,
        sender,
        recipient_list,
        fail_silently=True
    )


def send_user_email(user, tpl_subject, tpl_body, extra_context=()):
    tpl_context = {
        'user': user,
        'login_url': get_login_url()
    }
    if extra_context:
        tpl_context.update(extra_context)

    subject = render_to_string(tpl_subject, tpl_context).replace('\n', ' ')
    body = render_to_string(tpl_body, tpl_context)
    sender = settings.DEFAULT_FROM_EMAIL
    send_mail(
        subject,
        body,
        sender,
        [user.email],
        fail_silently=False
    )
    logger.info('%s email sent to %s' % (tpl_body, str(user.id)))


def serviceadminship_context(sa):
    return {
        'applicant': sa.admin,
        'service': sa.service,
        'service_url': current_site_baseurl() + '/services/'+str(sa.service.pk),
        'service_admins_url': current_site_baseurl() + '/service-admins/'
    }


def send_email_application_created(sa, http_host):
    recipients = sa.service.service_admins
    extra_context = serviceadminship_context(sa)
    extra_context['http_host'] = http_host

    for recipient in recipients:
        send_user_email(
            recipient,
            'emails/application_created_subject.txt',
            'emails/application_created_body.txt',
            extra_context
        )


def send_email_sa_admins_applicant(sa, http_host, tpl_subject, tpl_body_admins,
                                   tpl_body_applicant):
    recipients = sa.service.service_admins
    if sa.admin in recipients:
        recipients.remove(sa.admin)
    extra_context = serviceadminship_context(sa)
    extra_context['http_host'] = http_host

    # Send email to new admin
    send_user_email(
        sa.admin,
        tpl_subject,
        tpl_body_applicant,
        extra_context
    )

    # Send email to other admins
    for recipient in recipients:
        send_user_email(
            recipient,
            tpl_subject,
            tpl_body_admins,
            extra_context
        )


def send_email_service_admin_assigned(sa, http_host):
    tpl_subject = 'emails/service_admin_assigned_subject.txt'
    tpl_body_admins = 'emails/service_admin_assigned_to_admins_body.txt'
    tpl_body_applicant = 'emails/service_admin_assigned_to_applicant_body.txt'

    send_email_sa_admins_applicant(sa, http_host, tpl_subject, tpl_body_admins,
                                   tpl_body_applicant)


def send_email_application_evaluated(sa, http_host):
    if sa.state == 'approved':
        tpl_subject = 'emails/application_approved_subject.txt'
        tpl_body_admins = 'emails/application_approved_to_admins_body.txt'
        tpl_body_applicant = 'emails/application_approved_to_applicant_body.txt'

        send_email_sa_admins_applicant(sa, http_host, tpl_subject,
                                       tpl_body_admins,
                                       tpl_body_applicant)

    if sa.state == 'rejected':
        tpl_subject = 'emails/application_rejected_subject.txt'
        tpl_body_admins = 'emails/application_rejected_to_admins_body.txt'
        tpl_body_applicant = 'emails/application_rejected_to_applicant_body.txt'

        send_email_sa_admins_applicant(sa, http_host, tpl_subject,
                                       tpl_body_admins,
                                       tpl_body_applicant)
