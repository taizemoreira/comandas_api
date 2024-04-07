import db
from sqlalchemy import Column, VARCHAR, CHAR, Integer, LargeBinary, Numeric

# ORM

class ProdutoDB(db.Base):
    __tablename__ = 'tb_produto'
    
    id_produto = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(VARCHAR(100), nullable=False)
    descricao = Column(CHAR(100), nullable=False)
    foto = Column(LargeBinary)
    valor_unitario = Column(Numeric(precision=10, scale=2))

def __init__(self, id_produto, nome, descricao, foto, valor_unitario):
    self.id_produto = id_produto
    self.nome = nome
    self.descricao = descricao
    self.foto = foto
    self.valor_unitario = valor_unitario