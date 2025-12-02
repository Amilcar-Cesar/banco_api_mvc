from src.models.sqlite.settings.connection import db_connection_handler
from .cliente_repository import ClienteRepository

db_connection_handler.connect_to_db()

def test_create_account():
    renda_mensal = 5000.00
    idade = 25
    nome_completo = "Amilcar Cesar S."
    celular = "219794234234"
    email = "email@gmail.com"
    categoria = "CNPJ"
    saldo = 50000.0

    cpf_repo = ClienteRepository(db_connection_handler)
    cpf_repo.create_account(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)

def test_list_accounts():
    cpf_repo = ClienteRepository(db_connection_handler)

    lista = cpf_repo.list_accounts()
    print(lista)