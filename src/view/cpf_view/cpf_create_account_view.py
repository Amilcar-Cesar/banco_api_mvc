from src.view.http_types.http_request import HttpRequest
from src.view.http_types.http_response import HttpResponse
from src.errors.error_handler import handle_error

class CpfCreateAccountView:
    def __init__(self, controller) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        try:
            account_data = http_request.body
            body_response = self.__controller.create_account(account_data)

            return HttpResponse(status_code=201, body=body_response)
        except Exception as error:
            return handle_error(error)
