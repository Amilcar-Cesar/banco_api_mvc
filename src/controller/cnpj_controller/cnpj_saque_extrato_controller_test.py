import pytest
from unittest.mock import Mock
from src.controller.cnpj_controller.cnpj_saque_extrato_controller import CnpjSaqueExtratoController


class TestCnpjSaqueExtratoController:
    
    @pytest.fixture
    def mock_repository(self):
        return Mock()
    
    @pytest.fixture
    def controller(self, mock_repository):
        return CnpjSaqueExtratoController(mock_repository)
    
    def test_saque_sucesso(self, controller, mock_repository):
        cliente_id = 1
        valor_saque = 1000.0
        saldo_atual = 5000.0
        
        mock_repository.get_account.return_value = Mock(id=cliente_id)
        mock_repository.get_saldo.return_value = saldo_atual
        
        resultado = controller.saque(cliente_id, valor_saque)
        
        assert resultado["sucesso"] == True
        assert resultado["novo_saldo"] == 4000.0
        mock_repository.atualizar_saldo.assert_called_once_with(cliente_id, 4000.0)
    
    def test_saque_saldo_insuficiente(self, controller, mock_repository):
        cliente_id = 1
        valor_saque = 10000.0
        saldo_atual = 5000.0
        
        mock_repository.get_account.return_value = Mock(id=cliente_id)
        mock_repository.get_saldo.return_value = saldo_atual
        
        with pytest.raises(ValueError, match="Saldo insuficiente"):
            controller.saque(cliente_id, valor_saque)
    
    def test_saque_limite_excedido(self, controller, mock_repository):
        cliente_id = 1
        valor_saque = 15000.0
        
        mock_repository.get_account.return_value = Mock(id=cliente_id)
        mock_repository.get_saldo.return_value = 50000.0
        
        with pytest.raises(ValueError, match="Valor de saque excede o limite"):
            controller.saque(cliente_id, valor_saque)
    
    def test_saque_cliente_nao_existe(self, controller, mock_repository):
        cliente_id = 999
        valor_saque = 1000.0
        
        mock_repository.get_account.side_effect = ValueError("Conta não existe.")
        
        with pytest.raises(ValueError, match="Conta não existe"):
            controller.saque(cliente_id, valor_saque)
    
    def test_saque_valor_negativo(self, controller, mock_repository):
        cliente_id = 1
        valor_saque = -100.0
        
        mock_repository.get_account.return_value = Mock(id=cliente_id)
        mock_repository.get_saldo.return_value = 5000.0
        
        with pytest.raises(ValueError, match="Valor deve ser maior que zero"):
            controller.saque(cliente_id, valor_saque)
    
    def test_saque_valor_exato_ao_limite(self, controller, mock_repository):
        cliente_id = 1
        valor_saque = 10000.0
        saldo_atual = 15000.0
        
        mock_repository.get_account.return_value = Mock(id=cliente_id)
        mock_repository.get_saldo.return_value = saldo_atual
        
        resultado = controller.saque(cliente_id, valor_saque)
        
        assert resultado["sucesso"] == True
        assert resultado["novo_saldo"] == 5000.0
    
    def test_extrato_sucesso(self, controller, mock_repository):
        cliente_id = 1
        saldo_atual = 5500.75
        
        mock_repository.get_account.return_value = Mock(id=cliente_id)
        mock_repository.get_saldo.return_value = saldo_atual
        
        resultado = controller.extrato(cliente_id)
        
        assert resultado["mensagem"] == "Saldo atual da conta"
        assert resultado["saldo"] == 5500.75
    
    def test_extrato_cliente_nao_existe(self, controller, mock_repository):
        cliente_id = 999
        
        mock_repository.get_account.side_effect = ValueError("Conta não existe.")
        
        with pytest.raises(ValueError, match="Conta não existe"):
            controller.extrato(cliente_id)
    
    def test_extrato_saldo_zero(self, controller, mock_repository):
        cliente_id = 1
        saldo_atual = 0.0
        
        mock_repository.get_account.return_value = Mock(id=cliente_id)
        mock_repository.get_saldo.return_value = saldo_atual
        
        resultado = controller.extrato(cliente_id)
        
        assert resultado["saldo"] == 0.0
