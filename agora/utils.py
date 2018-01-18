import os
import json

from django.conf import settings
from agora.permissions import RULES

from collections import defaultdict


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

def get_rules():

    return RULES


def get_root_url():
    global _root_url
    if not _root_url:
        from agora.construct import adapter
        _root_url = adapter.spec['.meta']['root_url']
    return _root_url


RESOURCES = load_resources()
USER_ROLES = RESOURCES['USER_ROLES']
