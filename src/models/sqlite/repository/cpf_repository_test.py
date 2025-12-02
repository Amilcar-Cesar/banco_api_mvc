from src.models.sqlite.settings.connection import db_connection_handler
from .cpf_repository import CpfRepository
from src.models.sqlite.entities.pessoa_fisica import CpfTable
import pytest

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interaçao com o banco de dados")
def test_get_account():
    """Testa se consegue recuperar uma conta existente de CPF"""
    renda_mensal = 3000.00
    idade = 30
    nome_completo = "João Silva"
    celular = "21999999999"
    email = "joao@gmail.com"
    categoria = "CPF"
    saldo = 25000.0
    
    cpf_repo = CpfRepository(db_connection_handler)
    
    # Criar conta
    cpf_repo.create_account(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
    
    # Buscar a conta criada
    with db_connection_handler as database:
        conta = database.session.query(CpfTable).filter_by(email=email).first()
        cliente_id = conta.id
    
    # Recuperar a conta pelo ID
    account = cpf_repo.get_account(cliente_id)
    
    assert account is not None
    assert account.nome_completo == nome_completo
    assert account.email == email
    assert account.saldo == saldo

@pytest.mark.skip(reason="interaçao com o banco de dados")
def test_get_account_not_found():
    """Testa se retorna None quando tenta buscar conta inexistente de CPF"""
    cpf_repo = CpfRepository(db_connection_handler)
    
    account = cpf_repo.get_account(999999)
    assert account is None

@pytest.mark.skip(reason="interaçao com o banco de dados")
def test_atualizar_saldo_cpf():
    """Testa atualização de saldo para CPF"""
    renda_mensal = 4000.00
    idade = 28
    nome_completo = "Maria Santos"
    celular = "21988888888"
    email = "maria@gmail.com"
    categoria = "CPF"
    saldo_inicial = 15000.0
    
    cpf_repo = CpfRepository(db_connection_handler)
    
    # Criar conta
    cpf_repo.create_account(renda_mensal, idade, nome_completo, celular, email, categoria, saldo_inicial)
    
    # Buscar a conta para pegar o ID
    with db_connection_handler as database:
        conta = database.session.query(CpfTable).filter_by(email=email).first()
        cliente_id = conta.id
    
    # Atualizar saldo
    novo_saldo = 10000.0
    cpf_repo.atualizar_saldo(cliente_id, novo_saldo)
    
    # Verificar se foi atualizado
    account_atualizado = cpf_repo.get_account(cliente_id)
    assert account_atualizado.saldo == novo_saldo
