from fastapi import FastAPI

app = FastAPI()

lista_clientes = [
    {"nombre": "Juan", "edad": 15, "descripcion": "N.A"},
    {"nombre": "Ana", "edad": 18, "descripcion": "N.A"},
    {"nombre": "Pepe", "edad": 16, "descripcion": "Nuevo cliente"},
]


@app.get("/clientes")
def listar_clientes():
    return {"clientes": lista_clientes}


@app.post("/clientes")
def crear_clientes():
    return {"mensaje": "Cliente creado"}


@app.put("/clientes")
def editar_clientes():
    return {"mensaje": "Cliente Editado"}


@app.delete("/clientes")
def eliminar_clientes():
    return {"mensaje": "Cliente eliminado"}
