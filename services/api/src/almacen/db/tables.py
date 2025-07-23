from sqlalchemy import Float, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseEntity(DeclarativeBase):
    pass


class Producto(BaseEntity):
    __tablename__ = "productos"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(200))
    descripcion: Mapped[str] = mapped_column(String(350))
    precio: Mapped[float] = mapped_column(Float(precision=2))
    stock: Mapped[int] = mapped_column(Integer())
    categoria: Mapped[str] = mapped_column(String(100))

    def __repr__(self) -> str:
        return f"<Producto(id={self.id}, nombre='{self.nombre}', descripcion='{self.descripcion}', precio={self.precio}, stock={self.stock}, categoria='{self.categoria}')>"
