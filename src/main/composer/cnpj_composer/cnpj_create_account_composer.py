from src.models.sqlite.settings.connection import db_connection_handler
from src.models.sqlite.repository.cnpj_repository import CnpjRepository
from src.controller.cnpj_controller.cnpj_create_account_controller import CnpjCreateAccountController
from src.view.cnpj_view.cnpj_create_account_view import CnpjCreateAccountView

def cnpj_create_account_composer():

    model = CnpjRepository(db_connection_handler)
    controller = CnpjCreateAccountController(model)
    view = CnpjCreateAccountView(controller)

    return view
