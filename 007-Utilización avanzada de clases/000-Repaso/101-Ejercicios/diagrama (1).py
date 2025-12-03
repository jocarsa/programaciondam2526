from typing import Optional

class Cliente:
    def __init__(self, id: Optional[int] = None, nombre: Optional[str] = None, apellidos: Optional[str] = None):
        self.id = id
        self.nombre = nombre
        self.apellidos = apellidos

    def __repr__(self):
        return f"Cliente(id={self.id!r}, nombre={self.nombre!r}, apellidos={self.apellidos!r})"

class Producto:
    def __init__(self, id: Optional[int] = None, nombre: Optional[str] = None, precio: Optional[str] = None):
        self.id = id
        self.nombre = nombre
        self.precio = precio

    def __repr__(self):
        return f"Producto(id={self.id!r}, nombre={self.nombre!r}, precio={self.precio!r})"

class Pedido:
    def __init__(self, id: Optional[int] = None, fecha: Optional[str] = None, cliente_id: Optional[int] = None):
        self.id = id
        self.fecha = fecha
        self.cliente_id = cliente_id

    def __repr__(self):
        return f"Pedido(id={self.id!r}, fecha={self.fecha!r}, cliente_id={self.cliente_id!r})"

    # FK1: cliente_id -> cliente.id

class Lineaspedido:
    def __init__(self, id: Optional[int] = None, fecha: Optional[str] = None, pedido_id: Optional[int] = None, producto_id: Optional[int] = None, cantidad: Optional[str] = None):
        self.id = id
        self.fecha = fecha
        self.pedido_id = pedido_id
        self.producto_id = producto_id
        self.cantidad = cantidad

    def __repr__(self):
        return f"Lineaspedido(id={self.id!r}, fecha={self.fecha!r}, pedido_id={self.pedido_id!r}, producto_id={self.producto_id!r}, cantidad={self.cantidad!r})"

    # FK1: pedido_id -> pedido.id
    # FK2: producto_id -> producto.id
