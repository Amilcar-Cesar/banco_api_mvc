from src.models.sqlite.entities.pessoa_fisica import CpfTable

class CpfRepository():
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create_account(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                account_data = CpfTable(
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
                accounts = database.session.query(CpfTable.nome_completo, CpfTable.email).all()
                
                return accounts
            except Exception:
                return []
            
    def get_account(self, cliente_id: int):
        with self.__db_connection as database:
            try:
                account = database.session.query(CpfTable).filter_by(id=cliente_id).first()
                return account
            except Exception:
                raise ValueError("Conta não existe.")
    
    def get_saldo(self,cliente_id: int):
        with self.__db_connection as database:
            account = database.session.query(CpfTable).filter_by(id=cliente_id).first()
            return account.saldo

    def atualizar_saldo(self, cliente_id: int, novo_saldo: float):
        with self.__db_connection as database:
            cliente = database.session.query(CpfTable).filter_by(id=cliente_id).first()
            cliente.saldo = novo_saldo
            database.session.commit()