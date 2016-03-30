import responses
from django.contrib.sites.models import Site

def get_error_response(code, status=1):
    return {
        "status": responses.STATUS_CODES[status],
        "errors": {
            "detail": responses.ERROR_MESSAGES[code]
        }
    }


def get_response_info(code, data, status=0):
    return {
        "status": responses.STATUS_CODES[status],
        "info": responses.INFO_MESSAGES[code],
        "data": data
    }

def current_site_url():

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