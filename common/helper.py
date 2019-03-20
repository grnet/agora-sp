import responses
import datetime
from django.contrib.sites.models import Site
from agora.utils import get_root_url

def get_error_response(code, status=1, additional_status_msg=None):
    return {
        "status": responses.STATUS_CODES[status],
        "errors": {
            "detail": responses.ERROR_MESSAGES[code] if additional_status_msg is None else responses.ERROR_MESSAGES[code]
                                                                                       + additional_status_msg
        }
    }


def get_response_info(code, data, status=0):
    return {
        "status": responses.STATUS_CODES[status],
        "info": responses.INFO_MESSAGES[code],
        "data": data
    }


def current_site_url():
    return get_root_url()+"/api"


def current_site_baseurl():
    return get_root_url()


def build_list_object(name, objects):
    return {
        name + "_list" : {
            "count": len(objects),
            name: objects
        }
    }

def page_not_found():
    return {
        "status": "404 Page not found",
        "errors": {
            "detail": "The requested page was not found"
        }
    }

def generate_full_url(request):

    absolute_uri = request.build_absolute_uri()
    full_path = request.get_full_path()

    host_protocol = str(absolute_uri).replace(str(full_path),"")

    return str(host_protocol)

def get_last_url_part(request):
    url = request.get_full_path()
    url_parts = url.strip("/").split("/")
    return url_parts[-1]

def get_request_data(request):
    return request.data if request.META['CONTENT_TYPE'] == "application/json" else request.POST.copy()


def set_cookie(response, key, value):
    response.set_cookie(key, value)


def service_area_image_path(instance, filename):
    # file uploaded to MEDIA_ROOT/service_areas/resource_<id>/<filename>
    return 'service_areas/{0}/{1}'.format(instance.pk, filename)


def service_image_path(instance, filename):
    # file uploaded to MEDIA_ROOT/services/resource_<id>/<filename>
    return 'services/{0}/{1}'.format(instance.pk, filename)

def organisation_image_path(instance, filename):
    # file uploaded to MEDIA_ROOT/organisations/resource_<id>/<filename>
    return 'organisations/{0}/{1}'.format(instance.pk, filename)
