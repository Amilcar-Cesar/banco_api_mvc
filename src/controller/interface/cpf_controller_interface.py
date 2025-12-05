from abc import ABC, abstractmethod


class CpfControllerInterface(ABC):

    @abstractmethod
    def create_account(self, account_data: dict) -> dict:
        pass

    @abstractmethod
    def list(self) -> dict:
        pass
