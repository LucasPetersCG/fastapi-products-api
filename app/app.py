from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from models.products import Product, CreateProduct, UpdateProduct
from typing import List

# Inicialização da aplicação FastAPI
app = FastAPI(
    title="Products API",
    description="API REST para gerenciamento de produtos",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuração do CORS para permitir requisições de diferentes origens
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Banco de dados em memória (simulado)
products_db: List[Product] = [
    Product(
        id=1, 
        nome="Smartphone Samsung Galaxy S23", 
        descricao="Smartphone Android com tela de 6.1 polegadas e câmera de 50MP", 
        preco=2999.99,
        categoria="Eletrônicos",
        estoque=15
    ),
    Product(
        id=2, 
        nome="Notebook Dell Inspiron 15", 
        descricao="Notebook com processador Intel i7 e 16GB de RAM", 
        preco=4599.99,
        categoria="Informática",
        estoque=8
    ),
    Product(
        id=3, 
        nome="Fone de Ouvido Sony WH-1000XM4", 
        descricao="Fone de ouvido sem fio com cancelamento de ruído", 
        preco=1299.99,
        categoria="Acessórios",
        estoque=25
    ),
]

# Contador para IDs únicos
next_id = len(products_db) + 1

@app.get("/")
def read_root():
    """
    Endpoint raiz da API.
    """
    return {
        "message": "Bem-vindo à Products API!",
        "version": "1.0.0",
        "docs": "/docs"
    }

@app.get("/api/products", response_model=List[Product])
def get_products():
    """
    Retorna todos os produtos cadastrados.
    """
    return products_db

@app.get("/api/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: int):
    """
    Retorna um produto específico pelo ID.
    """
    for product in products_db:
        if product.id == product_id:
            return product
    
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.post("/api/products", response_model=Product, status_code=201)
def create_product(product: CreateProduct):
    """
    Cria um novo produto.
    """
    global next_id
    
    new_product = Product(
        id=next_id,
        **product.dict()
    )
    
    products_db.append(new_product)
    next_id += 1
    
    return new_product

@app.put("/api/products/{product_id}", response_model=Product)
def update_product(product_id: int, product_update: UpdateProduct):
    """
    Atualiza um produto existente.
    """
    for i, product in enumerate(products_db):
        if product.id == product_id:
            # Atualiza apenas os campos fornecidos
            update_data = product_update.dict(exclude_unset=True)
            updated_product = product.copy(update=update_data)
            products_db[i] = updated_product
            
            return updated_product
    
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.delete("/api/products/{product_id}")
def delete_product(product_id: int):
    """
    Remove um produto do sistema.
    """
    for i, product in enumerate(products_db):
        if product.id == product_id:
            deleted_product = products_db.pop(i)
            return {
                "message": "Produto deletado com sucesso",
                "deleted_product": deleted_product
            }
    
    raise HTTPException(status_code=404, detail="Produto não encontrado")

@app.get("/api/products/search/{query}")
def search_products(query: str):
    """
    Busca produtos por nome ou descrição.
    """
    query_lower = query.lower()
    results = [
        product for product in products_db 
        if query_lower in product.nome.lower() or query_lower in product.descricao.lower()
    ]
    
    return {
        "query": query,
        "results": results,
        "total": len(results)
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
