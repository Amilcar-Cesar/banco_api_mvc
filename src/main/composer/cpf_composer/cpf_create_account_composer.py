from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repository.cpf_repository import CpfRepository
from src.controller.cpf_controller.cpf_create_account_controller import CpfCreateAccountController
from src.view.cpf_view.cpf_create_account_view import CpfCreateAccountView

def cpf_create_account_composer():

    model = CpfRepository(db_connection_handler)
    controller = CpfCreateAccountController(model)
    view = CpfCreateAccountView(controller)

    return view
