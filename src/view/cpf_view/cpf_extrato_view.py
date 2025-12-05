from src.controller.interface.cliente_interface import ClienteInterface
from view.http_types.http_request import HttpRequest
from view.http_types.http_response import HttpResponse

class CpfExtratoView:
    def __init__(self, controller: ClienteInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        cliente_id = http_request.param["id"]
        body_response = self.__controller.extrato(cliente_id)

        return HttpResponse(status_code=201, body=body_response)