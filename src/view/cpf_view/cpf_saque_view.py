from src.controller.interface.cliente_interface import ClienteInterface
from view.http_types.http_request import HttpRequest
from view.http_types.http_response import HttpResponse

class CpfSaqueView:
    def __init__(self, controller: ClienteInterface) -> None:
        self.__controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:

        cliente_id = http_request.param["id"]
        valor_saque = http_request.body["valor_saque"]
        body_response = self.__controller.saque(cliente_id, valor_saque)

        return HttpResponse(status_code=201, body=body_response)