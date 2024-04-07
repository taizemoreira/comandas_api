from fastapi import APIRouter
from mod_produto.Produto import Produto
import db
from mod_produto.ProdutoModel import ProdutoDB
from typing import Annotated
from fastapi import Depends
from security import get_current_active_user, User

# router = APIRouter()
# dependências de forma global
router = APIRouter( dependencies=[Depends(get_current_active_user)] )

# Criar os endpoints de Produto: GET, POST, PUT, DELETE
@router.get("/produto/", tags=["Produto"])
def get_produto(current_user:Annotated[User, Depends(get_current_active_user)]):
    try:
        session = db.Session()

        # busca um com filtro
        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).all()

        return dados, 200

    except Exception as e:
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.post("/produto/", tags=["Produto"])
def post_produto(corpo: Produto, current_user:Annotated[User, Depends(get_current_active_user)]):
    try:
        session = db.Session()

        dados = ProdutoDB(None, corpo.nome, corpo.descricao, corpo.foto, corpo.valor_unitario)

        session.add(dados)
        # session.flush()
        session.commit()

        return {"id": dados.id_produto}, 200

    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.put("/produto/{id}", tags=["Produto"])
def put_produto(id: int, p: Produto):
    return {"msg": "put executado", "id": p.id_produto, "nome": p.nome, "descricao": p.descricao, "foto": p.valor_unitario, "valor_unitario": p.valor_unitario}, 201

@router.put("/produto/{id}", tags=["Produto"])
def put_cliente(id: int, corpo: Produto, current_user:Annotated[User, Depends(get_current_active_user)]):
    try:
        session = db.Session()

        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()

        dados.nome = corpo.nome
        dados.descricao = corpo.descricao
        dados.foto = corpo.foto
        dados.valor_unitario = corpo.valor_unitario

        session.add(dados)
        session.commit()

        return {"id": dados.id_produto}, 200

    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()

@router.delete("/produto/{id}", tags=["Produto"])
def delete_produto(id: int, current_user:Annotated[User, Depends(get_current_active_user)]):
    try:
        session = db.Session()

        dados = session.query(ProdutoDB).filter(ProdutoDB.id_produto == id).one()
        session.delete(dados)
        session.commit()

        return {"id": dados.id_produto}, 200
        
    except Exception as e:
        session.rollback()
        return {"erro": str(e)}, 400
    finally:
        session.close()