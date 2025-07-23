from pydantic import BaseModel

from almacen.db.tables import Producto


class RequestProducto(BaseModel):
    nombre: str
    descripcion: str
    precio: float
    stock: int
    categoria: str


class ProductoDTO(BaseModel):
    id: int
    nombre: str
    descripcion: str
    precio: float
    stock: int
    categoria: str

    class Config:
        orm_mode = (
            True  # Permite que Pydantic use los modelos de SQLAlchemy directamente
        )

    @staticmethod
    def from_producto_orm(producto: Producto) -> "ProductoDTO":
        return ProductoDTO(
            id=producto.id,
            nombre=producto.nombre,
            descripcion=producto.descripcion,
            precio=producto.precio,
            stock=producto.stock,
            categoria=producto.categoria,
        )
