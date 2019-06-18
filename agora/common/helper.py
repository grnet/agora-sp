""" Helper functions"""
from agora.utils import get_root_url


def current_site_url():
    return get_root_url()+"/api"


def current_site_baseurl():
    return get_root_url()


def service_area_image_path(instance, filename):
    # file uploaded to MEDIA_ROOT/service_categories/resource_<id>/<filename>
    return 'service_categories/{0}/{1}'.format(instance.pk, filename)


def service_image_path(instance, filename):
    # file uploaded to MEDIA_ROOT/services/resource_<id>/<filename>
    return 'services/{0}/{1}'.format(instance.pk, filename)


def organisation_image_path(instance, filename):
    # file uploaded to MEDIA_ROOT/organisations/resource_<id>/<filename>
    return 'organisations/{0}/{1}'.format(instance.pk, filename)


def federation_member_image_path(instance, filename):
    # file uploaded to MEDIA_ROOT/federation_members/resource_<id>/<filename>
    return 'federation_members/{0}/{1}'.format(instance.pk, filename)
