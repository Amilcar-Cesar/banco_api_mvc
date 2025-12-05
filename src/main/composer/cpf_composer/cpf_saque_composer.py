from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repository.cpf_repository import CpfRepository
from src.controller.cpf_controller.cpf_saque_extrato_controller import CpfSaqueExtratoController
from src.view.cpf_view.cpf_saque_view import CpfSaqueView

def cpf_saque_composer():

    model = CpfRepository(db_connection_handler)
    controller = CpfSaqueExtratoController(model)
    view = CpfSaqueView(controller)

    return view
