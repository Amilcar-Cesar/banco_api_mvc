from src.models.sqlite.interface.cnpj_repository import CnpjRepositoryInterface
from src.models.sqlite.entities.pessoa_juridica import CnpjTable
from typing import List


class CnpjListAccountsController():
    def __init__(self, cnpj_repository: CnpjRepositoryInterface) -> None:
        self.__cnpj_repository = cnpj_repository

    def list(self) -> dict:
        accounts = self.__get_accounts_in_db()
        response = self.__format_response(accounts)

        return response

    def __get_accounts_in_db(self) -> list:
        accounts = self.__cnpj_repository.list_accounts()
        return accounts
    
    def __format_response(self, accounts: List[CnpjTable]) -> dict:
        formated_accounts = []

        for account in accounts:
            formated_accounts.append({"nome_completo": account.nome_completo,
                                      "idade": account.idade,
                                      "categoria": account.categoria,
                                      "celular": account.celular})
        
        return {
            "data": {
                "type": "CNPJ",
                "count": len(formated_accounts),
                "attributes": formated_accounts
            }
        }
