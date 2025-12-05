import re
from src.models.sqlite.interface.cnpj_repository import CnpjRepositoryInterface
from src.controller.interface.cnpj_controller_interface import CnpjControllerInterface

class CnpjCreateAccountController(CnpjControllerInterface):
    def __init__(self, cnpj_repository: CnpjRepositoryInterface) -> None:
        self.__cnpj_repository = cnpj_repository

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
        
        invalid_caracteres = re.compile(r'[0-9@#$%&*]')

        if invalid_caracteres.search(nome_completo):
            raise ValueError("Nome da pessoa inválido!")

    def __create(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float):
         self.__cnpj_repository.create_account(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)

    def __format_response(self, account_data) -> dict:
         return {
              "data": {
                   "type": "CNPJ",
                   "count": 1,
                   "attributes": account_data
              }
         }