from dataclasses import dataclass
from typing import Optional

@dataclass
class Cliente:
    id: Optional[int] = None
    nombre: Optional[str] = None
    apellidos: Optional[str] = None

@dataclass
class Producto:
    id: Optional[int] = None
    nombre: Optional[str] = None
    precio: Optional[str] = None

@dataclass
class Pedido:
    id: Optional[int] = None
    fecha: Optional[str] = None
    cliente_id: Optional[int] = None

    # FK1: cliente_id -> cliente.id

@dataclass
class Lineaspedido:
    id: Optional[int] = None
    fecha: Optional[str] = None
    pedido_id: Optional[int] = None
    producto_id: Optional[int] = None
    cantidad: Optional[str] = None

    # FK1: pedido_id -> pedido.id
    # FK2: producto_id -> producto.id
