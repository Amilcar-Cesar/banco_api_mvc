from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repository.cpf_repository import CpfRepository
from src.controller.cpf_controller.cpf_saque_extrato_controller import CpfSaqueExtratoController
from src.view.cpf_view.cpf_extrato_view import CpfExtratoView

def cpf_extrato_composer():

    model = CpfRepository(db_connection_handler)
    controller = CpfSaqueExtratoController(model)
    view = CpfExtratoView(controller)

    return view
