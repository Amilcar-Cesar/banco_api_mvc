from src.models.sqlite.interface.cnpj_repository import CnpjRepositoryInterface
from src.controller.interface.cliente_interface import ClienteInterface

class CnpjSaqueExtratoController(ClienteInterface):
    def __init__(self, cnpj_repository: CnpjRepositoryInterface) -> None:
        self.__cnpj_repository = cnpj_repository

    def saque(self, cliente_id: int, valor_saque: float) -> dict:
        self.__validar_cliente(cliente_id)
        saldo_result = self.__saldo_suficiente(cliente_id, valor_saque)
        self.__limite_saque(valor_saque)

        novo_saldo = saldo_result["novo_saldo"]
        self.__cnpj_repository.atualizar_saldo(cliente_id, novo_saldo)

        return {"sucesso": True, "novo_saldo": novo_saldo}

    def __validar_cliente(self, cliente_id: int):
        try:
            account = self.__cnpj_repository.get_account(cliente_id)
            if not account:
                raise ValueError("Conta não existe.")
            return account
        except ValueError as e:
            raise e
        except Exception as e:
            raise ValueError("Erro ao validar cliente.") from e

    def __saldo_suficiente(self, cliente_id: int, valor_saque: float):
        saldo_atual = self.__cnpj_repository.get_saldo(cliente_id)

        if saldo_atual < valor_saque:
            raise ValueError("Saldo insuficiente")

        if valor_saque <= 0:
            raise ValueError("Valor deve ser maior que zero")

        return {"sucesso": True,
                "novo_saldo": saldo_atual - valor_saque}

    def __limite_saque(self, valor_saque: float):
        if valor_saque > float(10000.0):
            raise ValueError("Valor de saque excede o limite!")
        return None


    def extrato(self, cliente_id: int) -> dict:
        self.__validar_cliente(cliente_id)
        saldo = self.__cnpj_repository.get_saldo(cliente_id)

        return {"mensagem": "Saldo atual da conta",
                "saldo": saldo}
