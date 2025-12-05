from abc import ABC, abstractmethod


class CnpjControllerInterface(ABC):

    @abstractmethod
    def create_account(self, account_data: dict) -> dict:
        pass

    @abstractmethod
    def list(self) -> dict:
        pass
