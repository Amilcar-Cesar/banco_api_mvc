import pytest
from unittest.mock import Mock
from src.controller.cnpj_controller.cnpj_create_account_controller import CpfCreateAccountController


class TestCnpjCreateAccountController:
    
    @pytest.fixture
    def mock_repository(self):
        return Mock()
    
    @pytest.fixture
    def controller(self, mock_repository):
        return CpfCreateAccountController(mock_repository)
    
    def test_create_account_sucesso(self, controller, mock_repository):
        account_data = {
            "renda_mensal": 5000.0,
            "idade": 30,
            "nome_completo": "João Silva Santos",
            "celular": "11999999999",
            "email": "joao@email.com",
            "categoria": "PJ",
            "saldo": 1000.0
        }
        
        resultado = controller.create_account(account_data)
        
        assert resultado["data"]["type"] == "CNPJ"
        assert resultado["data"]["count"] == 1
        assert resultado["data"]["attributes"] == account_data
        mock_repository.create_account.assert_called_once()
    
    def test_create_account_nome_invalido_com_numeros(self, controller, mock_repository):
        account_data = {
            "renda_mensal": 5000.0,
            "idade": 30,
            "nome_completo": "João Silva 123",
            "celular": "11999999999",
            "email": "joao@email.com",
            "categoria": "PJ",
            "saldo": 1000.0
        }
        
        with pytest.raises(ValueError, match="Nome da pessoa inválido"):
            controller.create_account(account_data)
    
    def test_create_account_nome_invalido_com_caracteres_especiais(self, controller, mock_repository):
        account_data = {
            "renda_mensal": 5000.0,
            "idade": 30,
            "nome_completo": "João Silva@",
            "celular": "11999999999",
            "email": "joao@email.com",
            "categoria": "PJ",
            "saldo": 1000.0
        }
        
        with pytest.raises(ValueError, match="Nome da pessoa inválido"):
            controller.create_account(account_data)
    
