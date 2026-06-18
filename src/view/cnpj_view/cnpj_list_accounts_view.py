from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.errors.error_handler import handle_error

class CnpjListAccountView:
    def __init__(self, controller) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:    
            body_response = self.__controller.list()
            return HttpResponse(status_code=200, body=body_response)
        except Exception as error:
            return handle_error(error)