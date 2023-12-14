from fastapi import FastAPI

app = FastAPI() # instância do FastApi

@app.get("/") # decorador para declarar as rotas
async def read_root():
  return {"Hello": "World"} # retornando Json

@app.get("/items/{item_id}") # {} para capturar parâmetros
async def read_item(item_id : int, q : str = None):
  return {"item_id": item_id, "q": q}
