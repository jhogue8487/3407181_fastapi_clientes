from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Crear clase llamado MODELO
class Cliente(BaseModel):
    id: int
    nombre: str
    edad: int
    descripcion: str


lista_clientes: list[Cliente] = []


# endpoint
@app.get("/clientes", response_model=list[Cliente])
def listar_clientes():
    return lista_clientes


# endpoint
@app.post("/clientes", response_model=Cliente)
def crear_clientes(datos_cliente: Cliente):
    cliente_val = Cliente.model_validate(datos_cliente.model_dump())
    lista_clientes.append(cliente_val)
    return cliente_val


# endpoint
@app.put("/clientes/{id}", response_model=Cliente)
def editar_clientes(id: int, datos_cliente: Cliente):
    for i, obj_cliente in enumerate(lista_clientes):
        if obj_cliente.id == id:
            cliente_val = Cliente.model_validate(datos_cliente.model_dump())
            lista_clientes[i] = cliente_val

    return cliente_val


# endpoint
@app.delete("/clientes/{id}")
def eliminar_clientes():
    return {"mensaje": "Cliente eliminado"}
