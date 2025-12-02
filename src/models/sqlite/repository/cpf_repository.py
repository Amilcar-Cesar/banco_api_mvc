from src.models.sqlite.entities.clientes import ClienteTable
from src.models.sqlite.interface.cliente_interface import ClienteInterface

class CpfRepository(ClienteInterface):
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create_account(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                account_data = ClienteTable(
                    renda_mensal=renda_mensal,
                    idade=idade,
                    nome_completo=nome_completo,
                    celular=celular,
                    email=email,
                    categoria=categoria,
                    saldo=saldo
                )
                database.session.add(account_data)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception
    
    def list_accounts(self):
        with self.__db_connection as database:
            try:
                accounts = database.session.query(CPFTable.nome_completo, CPFTable.email).all()
                
                return accounts
            except Exception:
                return []