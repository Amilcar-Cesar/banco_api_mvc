from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repository.cnpj_repository import CnpjRepository
from src.controller.cnpj_controller.cnpj_list_controller import CnpjListAccountsController
from src.view.cnpj_view.cnpj_list_accounts_view import CnpjListAccountView

def cnpj_list_account_composer():

    model = CnpjRepository(db_connection_handler)
    controller = CnpjListAccountsController(model)
    view = CnpjListAccountView(controller)

    return view
