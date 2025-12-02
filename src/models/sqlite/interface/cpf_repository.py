from abc import ABC,abstractmethod
from src.models.sqlite.entities.pessoa_fisica import CpfTable


class CpfRepositoryInterface(ABC):

    @abstractmethod
    def create_account(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        pass 

    @abstractmethod
    def list_accounts(self) -> CpfTable:
        pass