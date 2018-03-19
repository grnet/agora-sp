import os
import json
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
    for rule in RULES:
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


def get_rules():
    return RULES


from agora.spec import DEPLOY_CONFIG
_root_url = DEPLOY_CONFIG[':root_url']

def get_root_url():
    return _root_url


RESOURCES = load_resources()
USER_ROLES = RESOURCES['USER_ROLES']
