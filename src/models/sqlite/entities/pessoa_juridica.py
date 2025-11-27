from sqlalchemy import Column, String, Integer, REAL
from src.models.sqlite.settings.base import Base

class CNPJTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(Integer, primary_key=True)
    renda_mensal = Column(REAL)
    idade = Column(Integer)
    nome_completo = Column(String)
    celular = Column(String)
    email = Column(String)
    categoria = Column(String)
    saldo = Column(REAL)
