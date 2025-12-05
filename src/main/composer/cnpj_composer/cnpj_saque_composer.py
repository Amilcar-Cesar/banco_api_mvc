from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repository.cnpj_repository import CnpjRepository
from src.controller.cnpj_controller.cnpj_saque_extrato_controller import CnpjSaqueExtratoController
from src.view.cnpj_view.cnpj_saque_view import CnpjSaqueView

def cnpj_saque_composer():

    model = CnpjRepository(db_connection_handler)
    controller = CnpjSaqueExtratoController(model)
    view = CnpjSaqueView(controller)

    return view
