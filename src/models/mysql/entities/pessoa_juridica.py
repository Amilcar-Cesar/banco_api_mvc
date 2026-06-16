from sqlalchemy import Column, String, Integer, DECIMAL
from src.models.mysql.settings.base import Base

class CnpjTable(Base):
    __tablename__ = "pessoa_juridica"

    id = Column(Integer, primary_key=True)
    renda_mensal = Column(DECIMAL(12, 2))
    idade = Column(Integer)
    nome_completo = Column(String(255))
    celular = Column(String(50))
    email = Column(String(255))
    categoria = Column(String(50))
    saldo = Column(DECIMAL(12, 2))
