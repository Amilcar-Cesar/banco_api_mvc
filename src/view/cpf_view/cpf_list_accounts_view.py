from src.controller.interface.cpf_controller_interface import CpfControllerInterface
from view.http_types.http_request import HttpRequest
from view.http_types.http_response import HttpResponse

class CpfListAccountView:
    def __init__(self, controller: CpfControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list()
        return HttpResponse(status_code=200, body=body_response)
