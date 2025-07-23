from fastapi import APIRouter, HTTPException
from sqlalchemy import select

from almacen.db.connection import db
from almacen.db.tables import Producto
from almacen.models import RequestProducto
from almacen.models.models import ProductoDTO

router = APIRouter()


@router.get("/")
def get_productos() -> list[ProductoDTO]:
    with db.get_session() as session:
        query = select(Producto).order_by(Producto.id)
        result = session.execute(query).scalars().all()
        return [ProductoDTO.from_producto_orm(producto) for producto in result]


@router.get("/{producto_id}")
def get_producto(producto_id: int) -> ProductoDTO:
    with db.get_session() as session:
        query = select(Producto).where(Producto.id == producto_id)
        producto = session.execute(query).scalar_one_or_none()
        if not producto:
            raise HTTPException(
                status_code=404, detail=f"Producto with id {producto_id} not found"
            )
        return ProductoDTO.from_producto_orm(producto)


@router.post("/")
def create_producto(request: RequestProducto):
    with db.get_session() as session:
        producto = Producto(
            nombre=request.nombre,
            descripcion=request.descripcion,
            precio=request.precio,
            stock=request.stock,
            categoria=request.categoria,
        )
        session.add(producto)
        session.commit()
        return ProductoDTO.from_producto_orm(producto)


@router.put("/{producto_id}")
def update_producto(producto_id: int, request: RequestProducto):
    with db.get_session() as session:
        query = select(Producto).where(Producto.id == producto_id)
        producto = session.execute(query).scalar_one_or_none()
        if not producto:
            raise HTTPException(
                status_code=404, detail=f"Producto with id {producto_id} not found"
            )
        producto.nombre = request.nombre
        producto.descripcion = request.descripcion
        producto.precio = request.precio
        producto.stock = request.stock
        producto.categoria = request.categoria
        session.commit()
        return ProductoDTO.from_producto_orm(producto)


@router.delete("/{producto_id}")
def delete_producto(producto_id: int):
    with db.get_session() as session:
        query = select(Producto).where(Producto.id == producto_id)
        producto = session.execute(query).scalar_one_or_none()
        if not producto:
            raise HTTPException(
                status_code=404, detail=f"Producto with id {producto_id} not found"
            )
        session.delete(producto)
        session.commit()
        return {"message": f"Producto with id {producto_id} deleted successfully"}
