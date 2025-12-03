import re
from src.models.sqlite.interface.cpf_repository import CpfRepositoryInterface

class CpfCreateAccountController():
    def __init__(self, cpf_repository: CpfRepositoryInterface) -> None:
        self.__cpf_repository = cpf_repository

    def create_account(self, account_data: dict) -> dict:
            
            renda_mensal= account_data["renda_mensal"]
            idade= account_data["idade"]
            nome_completo= account_data["nome_completo"]
            celular= account_data["celular"]
            email= account_data["email"]
            categoria= account_data["categoria"]
            saldo= account_data["saldo"]

            self.__validate_full_name(nome_completo)
            self.__create(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
            formated_response = self.__format_response(account_data)

            return formated_response
        
    def __validate_full_name(self, nome_completo: str) -> None:
        
        non_valid_caracteres = re.compile(r'[^a-zA-Z]')

        if non_valid_caracteres.search(nome_completo):
            raise ValueError("Nome da pessoa inválido!")

    def __create(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float):
         self.__cpf_repository.create_account(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)

    def __format_response(self, account_data) -> dict:
         return {
              "data": {
                   "type": "CPF",
                   "count": 1,
                   "attributes": account_data
              }
         }