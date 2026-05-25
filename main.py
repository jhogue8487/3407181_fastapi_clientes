from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

lista_clientes = []


# Crear clase llamado MODELO
class Cliente(BaseModel):
    id: int
    nombre: str
    edad: int
    descripcion: str


# endpoint
@app.get("/clientes")
def listar_clientes():
    return {"clientes": lista_clientes}


# endpoint
@app.post("/clientes")
def crear_clientes(datos_cliente: Cliente):
    lista_clientes.append(datos_cliente)
    return {"mensaje": "Cliente creado"}


# endpoint
@app.put("/clientes")
def editar_clientes():
    return {"mensaje": "Cliente Editado"}


# endpoint
@app.delete("/clientes")
def eliminar_clientes():
    return {"mensaje": "Cliente eliminado"}
