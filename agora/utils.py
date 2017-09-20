import six
import logging
import json

from django.conf import settings

from agora.errors import AgoraError


logger = logging.getLogger(__name__)


def get_permissions():
    json_data = {}
    try:
        with open(settings.FILEPATH_PERMISSIONS) as file_permissions:
            json_data = json.load(file_permissions)
    except IOError as e:
        errmsg = "Failed to load permissions from file: {filepath}".format(
                filepath=settings.FILEPATH_PERMISSIONS)
        exc = AgoraError(errmsg)
        logger.exception(exc)
        six.raise_from(exc, e)

    return json_data


def get_rules():
    permissions = []

    json_data = get_permissions()
    for collection_name, collection_data in json_data.iteritems():
        for action_name, action_data in collection_data.iteritems():
            for role_name, role_data in action_data.iteritems():
                for field_name, field_data in role_data.iteritems():
                    for state_name, state_data in field_data.iteritems():
                        permissions.append(
                            (
                                collection_name,
                                action_name,
                                role_name,
                                field_name,
                                state_name)
                            )

    return permissions
