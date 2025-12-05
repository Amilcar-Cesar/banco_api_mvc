from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repository.cpf_repository import CpfRepository
from src.controller.cpf_controller.cpf_list_accounts_controller import CpfListAccountsController
from src.view.cpf_view.cpf_list_accounts_view import CpfListAccountView

def cpf_list_account_composer():

    model = CpfRepository(db_connection_handler)
    controller = CpfListAccountsController(model)
    view = CpfListAccountView(controller)

    return view
