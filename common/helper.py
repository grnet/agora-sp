import responses


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