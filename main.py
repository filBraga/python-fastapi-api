from fastapi import FastAPI, HTTPException

# http://localhost:8000/docs
app = FastAPI()

# Banco de dados em memória
db = {}

@app.get("/items")
def read_all_items():
    return db

@app.post("/items/{item_id}")
def create_item(item_id: str, item: dict):
    if item_id in db:
        raise HTTPException(status_code=400, detail="Item já existe")
    db[item_id] = item
    return {"message": "Item criado com sucesso"}

@app.get("/items/{item_id}")
def read_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return db[item_id]

@app.put("/items/{item_id}")
def update_item(item_id: str, item: dict):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    db[item_id] = item
    return {"message": "Item atualizado com sucesso"}

@app.delete("/items/{item_id}")
def delete_item(item_id: str):
    if item_id not in db:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    del db[item_id]
    return {"message": "Item removido com sucesso"}
