from src.controller.interface.cnpj_controller_interface import CnpjControllerInterface
from view.http_types.http_request import HttpRequest
from view.http_types.http_response import HttpResponse

class CnpjListAccountView:
    def __init__(self, controller: CnpjControllerInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        body_response = self.__controller.list()
        return HttpResponse(status_code=200, body=body_response)