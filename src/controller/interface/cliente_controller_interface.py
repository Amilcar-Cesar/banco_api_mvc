from abc import ABC, abstractmethod

class ClienteControllerInterface(ABC):
    
    @abstractmethod
    def sacar(self, saldo):
        pass

    @abstractmethod
    def extrato(self):
        pass