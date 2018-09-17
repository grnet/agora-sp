import os
import json
import re
from bs4 import BeautifulSoup, Comment
from HTMLParser import HTMLParseError
from ckeditor_uploader.fields import RichTextUploadingField

from collections import defaultdict

from django.conf import settings

from collections import defaultdict

from django.conf import settings
from agora.permissions import RULES
import accounts.models



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
    for rule in transform_rules(RULES):
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


def get_rules():
    return RULES


config_file = os.path.join(settings.SETTINGS_DIR, 'deployment.conf')
with open(config_file) as f:
    deploy_config = json.load(f)

_root_url = deploy_config[':root_url']


def get_root_url():
    return _root_url


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
            # tag is allowed. Make sure all the attributes are allowed.
            tag.attrs = dict((attr, safe_css(attr, css))
                             for (attr, css) in tag.attrs.items()
                             if _attr_name_whitelisted(attr))
        else:
            # not a whitelisted tag. I'd like to remove it from the tree
            # and replace it with its children. But that's hard. It's much
            # easier to just replace it with an empty span tag.
            tag.name = "span"
            tag.attrs = []

    # scripts can be executed from comments in some cases
    comments = soup.findAll(text=lambda text:isinstance(text, Comment))
    for comment in comments:
        comment.extract()

    return unicode(soup)


def _attr_name_whitelisted(attr_name):
    return attr_name.lower() in ["href", "style", "color", "size", "bgcolor", "border"]


def safe_css(attr, css):
    if attr == "style":
        return re.sub("(width|height):[^;]+;", "", css)
    return css


RESOURCES = load_resources()
USER_ROLES = RESOURCES['USER_ROLES']
SERVICE_ADMINSHIP_STATES = RESOURCES['SERVICE_ADMINSHIP_STATES']
