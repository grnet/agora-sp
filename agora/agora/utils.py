import os
import json
import re
from collections import defaultdict
from HTMLParser import HTMLParseError
from bs4 import BeautifulSoup, Comment
from ckeditor_uploader.fields import RichTextUploadingField

from argo_ams_library import ArgoMessagingService, AmsMessage, AmsException

from django.conf import settings
import accounts.models
from agora.permissions import get_rules
from agora.settings import (
    AMS_TOKEN,
    AMS_ENDPOINT,
    AMS_PROJECT,
    AMS_TOPIC,
)


_root_url = None


def rule_to_dict(data, args):
    if len(args) == 1:
        return args[0]

    key = args.pop(0)
    for k in key.split(","):
        k = k.strip()
        data[k] = data[k] if k in data else {}
        partial = {
            k: rule_to_dict(data[k], args)
        }
        data.update(partial)
    return data


def load_permissions():
    PERMISSIONS = defaultdict(lambda: dict)
    for rule in transform_rules(get_rules()):
        rule_to_dict(PERMISSIONS, list(rule))
    return PERMISSIONS


def load_resources():
    with open(os.path.join(settings.PATH_RESOURCES, 'common.json')) \
            as json_file:
        return json.load(json_file)


def djoser_verifier(token):
    user = accounts.models.User.objects.filter(auth_token=token).first()
    if user is None or not user.is_active:
        return None
    return user


def userid_extractor(user, context):
    return user


def transform_rules(rules):
    new_rules = []
    for r in rules:
        el = list(r)
        if el[5] == "*":
            new_l = (el[0], el[1], el[2], el[5], el[4], el[6])
            new_rules.append(new_l)
        else:
            fields = el[5].split(",")
            for f in fields:
                new_l = (el[0], el[1], el[2], f, el[4], el[6])
                new_rules.append(new_l)
    return new_rules


config_file = os.path.join(settings.SETTINGS_DIR, 'deployment.conf')
with open(config_file) as f:
    deploy_config = json.load(f)

_root_url = deploy_config[':root_url']


def get_root_url():
    return _root_url


def publish_message(service, action):
    """
    Send a message using argo messaging service when an action upon a service
    takes place.
    """
    service_id = str(service.get('id'))
    service_name = service.get('name')
    service_data = service.get('data', {})
    ams = ArgoMessagingService(endpoint=AMS_ENDPOINT,
                               project=AMS_PROJECT,
                               token=AMS_TOKEN)
    endpoint = '{0}/api/v2/ext-services/{1}'.format(get_root_url(), service_id)
    # The value of the data property must be unicode in order to be
    # encoded in base64 format in AmsMessage
    data = json.dumps(service_data)

    try:
        if not ams.has_topic(AMS_TOPIC):
            ams.create_topic(AMS_TOPIC)
    except AmsException as e:
        print e
        raise SystemExit(1)

    msg = AmsMessage(data=data,
                     attributes={
                         "method": action,
                         "service_id": service_id,
                         "service_name": service_name,
                         "endpoint": endpoint
                     }).dict()
    try:
        ret = ams.publish(AMS_TOPIC, msg)
        print ret
    except AmsException as e:
        print e


def clean_html_fields(instance):
    class_fields = instance.__class__._meta.get_fields()
    fields_to_clean = [field for field in class_fields
                       if isinstance(field, RichTextUploadingField)]
    for field in fields_to_clean:
        old_value = getattr(instance, field.name)
        setattr(instance, field.name, safe_html(old_value))


def safe_html(html):
    if not html:
        return html

    # remove these tags, complete with contents.
    blacklist = ["script", "style", "audio", "video"]

    whitelist = [
        "div", "span", "p", "br", "pre",
        "table", "tbody", "thead", "tr", "td", "a",
        "blockquote", "code",
        "ul", "li", "ol",
        "b", "em", "i", "strong", "u", "font",
        "h1", "h2", "h3", "h4", "h5", "h6",
        "dl", "dt", "dd",
        "footer", "header", "nav"
        "br", "caption", "img",
        ]

    try:
        # BeautifulSoup is catching out-of-order and unclosed tags, so markup
        # can't leak out of comments and break the rest of the page.
        soup = BeautifulSoup(html, 'html.parser')
    except HTMLParseError:
        return html

    # now strip HTML we don't like.
    for tag in soup.findAll():
        if tag.name.lower() in blacklist:
            # blacklisted tags are removed in their entirety
            tag.extract()
        elif tag.name.lower() in whitelist:
            # tag is allowed
            tag.attrs = dict((attr, safe_css(attr, css))
                             for (attr, css) in tag.attrs.items())
        else:
            # not a whitelisted tag. I'd like to remove it from the tree
            # and replace it with its children. But that's hard. It's much
            # easier to just replace it with an empty span tag.
            tag.name = "span"
            tag.attrs = []

    # scripts can be executed from comments in some cases
    comments = soup.findAll(text=lambda text: isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    return unicode(soup)


def safe_css(attr, css):
    if attr == "style":
        return re.sub("(width|height):[^;]+;", "", css)
    return css


RESOURCES = load_resources()
USER_ROLES = RESOURCES['USER_ROLES']
LEGAL_STATUSES = RESOURCES["LEGAL_STATUSES"]
LIFECYCLE_STATUSES = RESOURCES["PROVIDER_LIFE_CYCLE_STATUSES"]
SERVICE_ADMINSHIP_STATES = RESOURCES['SERVICE_ADMINSHIP_STATES']
