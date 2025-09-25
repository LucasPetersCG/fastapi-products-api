from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    """
    Modelo de dados para um produto.
    Atributos:
    - id: Identificador único do produto.
    - nome: Nome do produto.
    - descricao: Descrição do produto.
    - preco: Preço do produto.
    - categoria: Categoria do produto (opcional).
    - estoque: Quantidade em estoque (opcional).
    """

    id: int
    nome: str
    descricao: str
    preco: float
    categoria: Optional[str] = None
    estoque: Optional[int] = None


class CreateProduct(BaseModel):
    """
    Modelo para criação de um novo produto.
    """
    nome: str
    descricao: str
    preco: float
    categoria: Optional[str] = None
    estoque: Optional[int] = None


class UpdateProduct(BaseModel):
    """
    Modelo para atualização de um produto existente.
    Todos os campos são opcionais para permitir atualizações parciais.
    """
    nome: Optional[str] = None
    descricao: Optional[str] = None
    preco: Optional[float] = None
    categoria: Optional[str] = None
    estoque: Optional[int] = None
