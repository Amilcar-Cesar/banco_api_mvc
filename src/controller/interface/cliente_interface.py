from abc import ABC, abstractmethod


class ClienteInterface(ABC):

    @abstractmethod
    def saque(self, cliente_id: int, valor_saque: float) -> dict:
        pass

    @abstractmethod
    def extrato(self, cliente_id: int) -> dict:
        pass
