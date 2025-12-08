from src.models.sqlite.entities.pessoa_juridica import CnpjTable

class CnpjRepository():
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def create_account(self, renda_mensal: float, idade: int, nome_completo: str, celular: str, email: str, categoria: str, saldo: float) -> None:
        with self.__db_connection as database:
            try:
                account_data = CnpjTable(
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
                # Retorna o objeto completo para evitar erros no controller
                accounts = database.session.query(CnpjTable).all()
                return accounts
            except Exception:
                return []

    def get_account(self, cliente_id: int):
        with self.__db_connection as database:
            try:
                account = database.session.query(CnpjTable).filter_by(id=cliente_id).first()
                if not account:
                    raise ValueError("Conta não existe.") 
                return account
            except Exception as e:
                raise e

    def get_saldo(self, cliente_id: int):
        with self.__db_connection as database:
            account = database.session.query(CnpjTable).filter_by(id=cliente_id).first()

            if not account:
                raise ValueError("Conta não encontrada para realizar o saque.")

            return account.saldo

    def atualizar_saldo(self, cliente_id: int, novo_saldo: float):
        with self.__db_connection as database:
            cliente = database.session.query(CnpjTable).filter_by(id=cliente_id).first()

            if not cliente:
                 raise ValueError("Conta não encontrada para atualizar saldo.")

            cliente.saldo = novo_saldo
            database.session.commit()