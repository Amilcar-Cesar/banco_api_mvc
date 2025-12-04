import pytest
from unittest.mock import Mock
from .cpf_list_accounts_controller import CpfListAccountsController
from src.models.sqlite.entities.pessoa_fisica import CpfTable


class TestCpfListAccountsController:
    
    @pytest.fixture
    def mock_repository(self):
        """Cria um mock do repository para testes"""
        return Mock()
    
    @pytest.fixture
    def controller(self, mock_repository):
        """Cria uma instância do controller com mock"""
        return CpfListAccountsController(mock_repository)
    
    @pytest.fixture
    def mock_account(self):
        """Cria um mock de uma conta CPF"""
        account = Mock(spec=CpfTable)
        account.nome_completo = "JoaoSilva"
        account.idade = 30
        account.categoria = "CPF"
        account.celular = "21999999999"
        return account
    
    @pytest.fixture
    def mock_multiple_accounts(self):
        """Cria mocks de múltiplas contas"""
        account1 = Mock(spec=CpfTable)
        account1.nome_completo = "JoaoSilva"
        account1.idade = 30
        account1.categoria = "CPF"
        account1.celular = "21999999999"
        
        account2 = Mock(spec=CpfTable)
        account2.nome_completo = "MariaOliveira"
        account2.idade = 28
        account2.categoria = "CPF"
        account2.celular = "21988888888"
        
        return [account1, account2]
    
    def test_list_single_account(self, controller, mock_repository, mock_account):
        """Testa listagem com uma conta"""
        mock_repository.list_accounts.return_value = [mock_account]
        
        response = controller.list()
        
        assert response is not None
        assert response["data"]["type"] == "CPF"
        assert response["data"]["count"] == 1
        assert len(response["data"]["attributes"]) == 1
    
    def test_list_multiple_accounts(self, controller, mock_repository, mock_multiple_accounts):
        """Testa listagem com múltiplas contas"""
        mock_repository.list_accounts.return_value = mock_multiple_accounts
        
        response = controller.list()
        
        assert response["data"]["count"] == 2
        assert len(response["data"]["attributes"]) == 2
    
    def test_list_empty_accounts(self, controller, mock_repository):
        """Testa listagem quando não há contas"""
        mock_repository.list_accounts.return_value = []
        
        response = controller.list()
        
        assert response["data"]["count"] == 0
        assert len(response["data"]["attributes"]) == 0
    
    def test_list_account_information_correct(self, controller, mock_repository, mock_account):
        """Testa se as informações da conta estão corretas na resposta"""
        mock_repository.list_accounts.return_value = [mock_account]
        
        response = controller.list()
        account_data = response["data"]["attributes"][0]
        
        assert account_data["nome_completo"] == "JoaoSilva"
        assert account_data["idade"] == 30
        assert account_data["categoria"] == "CPF"
        assert account_data["celular"] == "21999999999"
