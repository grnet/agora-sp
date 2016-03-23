import responses
from django.contrib.sites.models import Site

def get_error_response(code):
    return {
        "status": "404 Not Found",
        "errors": {
            "detail": responses.ERROR_MESSAGES[code]
        }
    }


def get_response_info(code, data):
    return {
        "status": "200 OK",
        "info": responses.INFO_MESSAGES[code],
        "data": data
    }

def current_site_url():
    """Returns fully qualified URL (no trailing slash) for the current site."""

    current_site = Site.objects.get_current()
    url = 'http://%s' % (current_site.domain+"/api")

    return url

def build_list_object(name, objects):
    return {
        name + "_list" : {
            "count": len(objects),
            name: objects
        }
    }