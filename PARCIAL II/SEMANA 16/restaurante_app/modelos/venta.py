from __future__ import annotations

from datetime import datetime
from typing import Any


class Venta:
    """Registra una venta realizada entre un usuario y un producto."""

    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int = 1, fecha: str | None = None) -> None:
        self.usuario_id: str = usuario_id
        self.producto_codigo: str = producto_codigo
        self.cantidad: int = cantidad
        self.fecha: str = fecha or datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    @property
    def usuario_id(self) -> str:
        return self._usuario_id

    @usuario_id.setter
    def usuario_id(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La identificación del usuario no puede estar vacía.")
        self._usuario_id = valor.strip()

    @property
    def producto_codigo(self) -> str:
        return self._producto_codigo

    @producto_codigo.setter
    def producto_codigo(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El código del producto no puede estar vacío.")
        self._producto_codigo = valor.strip()

    @property
    def cantidad(self) -> int:
        return self._cantidad

    @cantidad.setter
    def cantidad(self, valor: int) -> None:
        if isinstance(valor, bool):
            raise ValueError("La cantidad de la venta debe ser un número entero positivo.")
        try:
            cantidad = int(valor)
        except (TypeError, ValueError) as error:
            raise ValueError("La cantidad de la venta debe ser un número entero positivo.") from error
        if cantidad <= 0:
            raise ValueError("La cantidad de la venta debe ser mayor que cero.")
        self._cantidad = cantidad

    @property
    def fecha(self) -> str:
        return self._fecha

    @fecha.setter
    def fecha(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La fecha de la venta no puede estar vacía.")
        self._fecha = valor.strip()

    def a_dict(self) -> dict[str, object]:
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
            "fecha": self.fecha,
        }

    @classmethod
    def desde_dict(cls, datos: dict[str, Any]) -> "Venta":
        try:
            return cls(
                usuario_id=datos["usuario_id"],
                producto_codigo=datos["producto_codigo"],
                cantidad=datos.get("cantidad", 1),
                fecha=datos.get("fecha", datetime.now().strftime("%Y-%m-%d %H:%M:%S")),
            )
        except KeyError as error:
            raise KeyError(f"Falta la clave requerida en el registro: {error}") from error

    def __str__(self) -> str:
        return (
            f"Venta(usuario_id={self.usuario_id}, producto_codigo={self.producto_codigo}, "
            f"cantidad={self.cantidad}, fecha={self.fecha})"
        )

    def __repr__(self) -> str:
        return self.__str__()
