from __future__ import annotations

from typing import Any


class Venta:
    """Representa una venta de un producto a un usuario."""

    def __init__(self, usuario_id: str, producto_codigo: str, cantidad: int) -> None:
        self.usuario_id: str = usuario_id
        self.producto_codigo: str = producto_codigo
        self.cantidad: int = cantidad

    @property
    def usuario_id(self) -> str:
        return self._usuario_id

    @usuario_id.setter
    def usuario_id(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El ID del usuario no puede estar vacío.")
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
            raise ValueError("La cantidad debe ser un número entero mayor que cero.")
        try:
            cantidad = int(valor)
        except (TypeError, ValueError) as error:
            raise ValueError("La cantidad debe ser un número entero mayor que cero.") from error
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        self._cantidad = cantidad

    def a_dict(self) -> dict[str, object]:
        """Convierte el objeto a una estructura compatible con JSON."""
        return {
            "usuario_id": self.usuario_id,
            "producto_codigo": self.producto_codigo,
            "cantidad": self.cantidad,
        }

    @classmethod
    def desde_dict(cls, datos: dict[str, Any]) -> Venta:
        """Reconstruye una Venta y deja que sus validaciones actúen."""
        try:
            return cls(
                usuario_id=datos["usuario_id"],
                producto_codigo=datos["producto_codigo"],
                cantidad=datos["cantidad"],
            )
        except KeyError as error:
            raise KeyError(f"Falta la clave requerida en el registro: {error}") from error

    def __str__(self) -> str:
        return (
            f"Venta(usuario_id={self.usuario_id}, producto_codigo={self.producto_codigo}, "
            f"cantidad={self.cantidad})"
        )

    def __repr__(self) -> str:
        return self.__str__()
