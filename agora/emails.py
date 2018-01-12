from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string


def send_email_shib_user_created(user):
    template_subject = 'emails/shib_user_created_subject.txt'
    template_body = 'emails/shib_user_created_body.txt'
    template_context = {
        'user': user
    }
    subject = render_to_string(template_subject).replace('\n', ' ')
    body = render_to_string(template_body, template_context)
    sender = settings.DEFAULT_FROM_EMAIL
    recipient_list = settings.USER_CREATION_EMAIL_LIST
    send_mail(
        subject,
        body,
        sender,
        recipient_list,
        fail_silently=True
    )
