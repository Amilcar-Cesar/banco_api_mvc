import pytest
from unittest.mock import Mock
from src.controller.cnpj_controller.cnpj_list_controller import CnpjListAccountsController


class TestCnpjListController:
    
    @pytest.fixture
    def mock_repository(self):
        return Mock()
    
    @pytest.fixture
    def controller(self, mock_repository):
        return CnpjListAccountsController(mock_repository)
    
    def test_list_accounts_com_contas(self, controller, mock_repository):
        mock_account1 = Mock(nome_completo="João Silva", idade=30, categoria="PJ", celular="11999999999")
        mock_account2 = Mock(nome_completo="Maria Santos", idade=28, categoria="PJ", celular="11988888888")
        
        mock_repository.list_accounts.return_value = [mock_account1, mock_account2]
        
        resultado = controller.list()
        
        assert resultado["data"]["type"] == "CNPJ"
        assert resultado["data"]["count"] == 2
        assert len(resultado["data"]["attributes"]) == 2
        assert resultado["data"]["attributes"][0]["nome_completo"] == "João Silva"
        assert resultado["data"]["attributes"][1]["nome_completo"] == "Maria Santos"
    
    def test_list_accounts_sem_contas(self, controller, mock_repository):
        mock_repository.list_accounts.return_value = []
        
        resultado = controller.list()
        
        assert resultado["data"]["type"] == "CNPJ"
        assert resultado["data"]["count"] == 0
        assert resultado["data"]["attributes"] == []
    
    def test_list_accounts_uma_conta(self, controller, mock_repository):
        mock_account = Mock(nome_completo="João Silva", idade=30, categoria="PJ", celular="11999999999")
        
        mock_repository.list_accounts.return_value = [mock_account]
        
        resultado = controller.list()
        
        assert resultado["data"]["count"] == 1
        assert resultado["data"]["attributes"][0]["idade"] == 30
        assert resultado["data"]["attributes"][0]["categoria"] == "PJ"
    
    def test_list_accounts_formato_resposta(self, controller, mock_repository):
        mock_account = Mock(nome_completo="Test", idade=25, categoria="PJ", celular="11111111111")
        
        mock_repository.list_accounts.return_value = [mock_account]
        
        resultado = controller.list()
        
        assert "data" in resultado
        assert "type" in resultado["data"]
        assert "count" in resultado["data"]
        assert "attributes" in resultado["data"]
