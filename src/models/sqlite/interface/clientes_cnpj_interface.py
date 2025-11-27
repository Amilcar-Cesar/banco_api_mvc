from abc import ABC, abstractmethod

class CnpjRepositoryInterface(ABC):
    
    @abstractmethod
    def sacar_dinheiro(self):
        pass

    @abstractmethod
    def realizar_extrato(self):
        pass
