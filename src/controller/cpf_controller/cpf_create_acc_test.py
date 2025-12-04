import pytest
from unittest.mock import Mock, MagicMock
from .cpf_create_account_controller import CpfCreateAccountController


class TestCpfCreateAccountController:
    
    @pytest.fixture
    def mock_repository(self):
        
        return Mock()
    
    @pytest.fixture
    def controller(self, mock_repository):
        
        return CpfCreateAccountController(mock_repository)
    
    @pytest.fixture
    def valid_account_data(self):
        
        return {
            "renda_mensal": 5000.00,
            "idade": 30,
            "nome_completo": "JoaoSilvaSantos",
            "celular": "21999999999",
            "email": "joao@example.com",
            "categoria": "CPF",
            "saldo": 10000.0
        }
    
    
    def test_create_account_success(self, controller, mock_repository, valid_account_data):
        
        response = controller.create_account(valid_account_data)
        
        mock_repository.create_account.assert_called_once()
        
        assert response is not None
        assert "data" in response
    
    def test_response_format_structure(self, controller, mock_repository, valid_account_data):
     
        response = controller.create_account(valid_account_data)
        
        assert "data" in response
        assert isinstance(response["data"], dict)
        
        data = response["data"]
        assert "type" in data
        assert "count" in data
        assert "attributes" in data
    
    
    def test_response_attributes_contains_account_data(self, controller, mock_repository, valid_account_data):
        
        response = controller.create_account(valid_account_data)
        attributes = response["data"]["attributes"]
        
        assert attributes["renda_mensal"] == valid_account_data["renda_mensal"]
        assert attributes["idade"] == valid_account_data["idade"]
        assert attributes["nome_completo"] == valid_account_data["nome_completo"]
        assert attributes["celular"] == valid_account_data["celular"]
        assert attributes["email"] == valid_account_data["email"]
        assert attributes["categoria"] == valid_account_data["categoria"]
        assert attributes["saldo"] == valid_account_data["saldo"]
    
    # ============= TESTES DE VALIDAÇÃO DO NOME =============
    
    def test_validate_invalid_name_with_symbols(self, controller, mock_repository, valid_account_data):
        """Testa validação com símbolos no nome"""
        valid_account_data["nome_completo"] = "Joao Silva!"
        
        with pytest.raises(ValueError, match="Nome da pessoa inválido!"):
            controller.create_account(valid_account_data)
    
    def test_validate_invalid_name_with_spaces(self, controller, mock_repository, valid_account_data):
        """Testa validação rejeita nomes com espaços"""
        valid_account_data["nome_completo"] = "Joao 123 Silva"
        
        with pytest.raises(ValueError, match="Nome da pessoa inválido!"):
            controller.create_account(valid_account_data)
    
    # ============= TESTES DO CHAMADO AO REPOSITORY =============
    
    def test_repository_called_with_correct_parameters(self, controller, mock_repository, valid_account_data):
        """Testa se o repository é chamado com os parâmetros corretos"""
        controller.create_account(valid_account_data)
        
        mock_repository.create_account.assert_called_once_with(
            valid_account_data["renda_mensal"],
            valid_account_data["idade"],
            valid_account_data["nome_completo"],
            valid_account_data["celular"],
            valid_account_data["email"],
            valid_account_data["categoria"],
            valid_account_data["saldo"]
        )
    