from src.models.sqlite.interface.cpf_repository import CpfRepositoryInterface
from src.models.sqlite.entities.pessoa_fisica import CpfTable
from typing import List


class CpfListAccountsController:
    def __init__(self, cpf_repository: CpfRepositoryInterface) -> None:
        self.__cpf_repository = cpf_repository

    def list(self) -> dict:
        accounts = self.__get_accounts_in_db()
        response = self.__format_response(accounts)

        return response

    def __get_accounts_in_db(self) -> list:
        accounts = self.__cpf_repository.list_accounts()
        return accounts
    
    def __format_response(self, accounts: List[CpfTable]) -> dict:
        formated_accounts = []

        for account in accounts:
            formated_accounts.append({"nome_completo": account.nome_completo,
                                      "email": account.email,
                                      })
        
        return {
            "data": {
                "type": "CPF",
                "count": len(formated_accounts),
                "attributes": formated_accounts
            }
        }
