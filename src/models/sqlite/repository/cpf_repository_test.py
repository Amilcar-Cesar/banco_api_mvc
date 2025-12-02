from src.models.sqlite.settings.connection import db_connection_handler
from .cpf_repository import CpfRepository

db_connection_handler.connect_to_db()

def test_create_account():
    renda_mensal = 2000.00
    idade = 25
    nome_completo = "Maria Eduarda"
    celular = "21979412345"
    email = "email1@gmail.com"
    categoria = "Pessoa física"
    saldo = 10.00

    cpf_repo = CpfRepository(db_connection_handler)
    cpf_repo.create_account(renda_mensal, idade, nome_completo, celular, email, categoria, saldo)

def test_list_accounts():
    cpf_repo = CpfRepository(db_connection_handler)

    cpf_repo.list_accounts()