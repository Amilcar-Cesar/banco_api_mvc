from src.models.sqlite.settings.connection import db_connection_handler
from .cnpj_repository import CnpjRepository
from src.models.sqlite.entities.pessoa_juridica import CnpjTable
import pytest

#db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="interaçao com o banco de dados")
def test_get_account_cnpj():
    """Testa se consegue recuperar uma conta existente de CNPJ"""
    renda_mensal = 15000.00
    idade = 35
    nome_completo = "Empresa XYZ LTDA"
    celular = "21987654321"
    email = "empresa@gmail.com"
    categoria = "CNPJ"
    saldo = 100000.0
    
    cnpj_repo = CnpjRepository(db_connection_handler)
    
    # Criar conta
    cnpj_repo.create_account(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)
    
    # Buscar a conta criada
    with db_connection_handler as database:
        conta = database.session.query(CnpjTable).filter_by(email=email).first()
        cliente_id = conta.id
    
    # Recuperar a conta pelo ID
    account = cnpj_repo.get_account(cliente_id)
    
    assert account is not None
    assert account.nome_completo == nome_completo
    assert account.email == email
    assert account.saldo == saldo

@pytest.mark.skip(reason="interaçao com o banco de dados")
def test_get_account_not_found_cnpj():
    """Testa se retorna None quando tenta buscar conta inexistente de CNPJ"""
    cnpj_repo = CnpjRepository(db_connection_handler)
    
    account = cnpj_repo.get_account(999999)
    assert account is None

@pytest.mark.skip(reason="interaçao com o banco de dados")
def test_atualizar_saldo_cnpj():
    """Testa atualização de saldo para CNPJ"""
    renda_mensal = 20000.00
    idade = 40
    nome_completo = "Empresa ABC Incorporated"
    celular = "21912345678"
    email = "abc@gmail.com"
    categoria = "CNPJ"
    saldo_inicial = 50000.0
    
    cnpj_repo = CnpjRepository(db_connection_handler)
    
    # Criar conta
    cnpj_repo.create_account(renda_mensal, idade, nome_completo, celular, email, categoria, saldo_inicial)
    
    # Buscar a conta para pegar o ID
    with db_connection_handler as database:
        conta = database.session.query(CnpjTable).filter_by(email=email).first()
        cliente_id = conta.id
    
    # Atualizar saldo
    novo_saldo = 35000.0
    cnpj_repo.atualizar_saldo(cliente_id, novo_saldo)
    
    # Verificar se foi atualizado
    account_atualizado = cnpj_repo.get_account(cliente_id)
    assert account_atualizado.saldo == novo_saldo