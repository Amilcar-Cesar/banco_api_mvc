from .types.http_bad_request import HttpBadRequest
from .types.http_not_found import HttpNotFound
from .types.http_forbiden import HttpForbidden
from src.view.http_types.http_response import HttpResponse

def handle_error(error: Exception):
    if isinstance(error, HttpBadRequest):
        return HttpResponse(status_code=error.status_code, body={"status": "error", "message": error.message})
    elif isinstance(error, HttpNotFound):
        return HttpResponse(status_code=error.status_code, body={"status": "error", "message": error.message})
    elif isinstance(error, HttpForbidden):
        return HttpResponse(status_code=error.status_code, body={"status": "error", "message": error.message})
    else:
        return HttpResponse(status_code=500, body={"status": "error", "message": "An unexpected error occurred."})