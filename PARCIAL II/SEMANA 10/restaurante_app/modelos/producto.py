from __future__ import annotations

from typing import Any


class Producto:
    """Representa un producto del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio

    @property
    def codigo(self) -> str:
        return self._codigo

    @codigo.setter
    def codigo(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El código del producto no puede estar vacío.")
        self._codigo = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float) -> None:
        if isinstance(valor, bool):
            raise ValueError("El precio debe ser un número mayor que cero.")
        try:
            precio = float(valor)
        except (TypeError, ValueError) as error:
            raise ValueError("El precio debe ser un número mayor que cero.") from error
        if precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = precio

    def a_dict(self) -> dict[str, object]:
        """Convierte el objeto a una estructura compatible con JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
        }

    @classmethod
    def desde_dict(cls, datos: dict[str, Any]) -> Producto:
        """Reconstruye un Producto y deja que sus validaciones actúen."""
        try:
            return cls(
                codigo=datos["codigo"],
                nombre=datos["nombre"],
                categoria=datos["categoria"],
                precio=datos["precio"],
            )
        except KeyError as error:
            raise KeyError(f"Falta la clave requerida: {error.args[0]}") from error

    def __str__(self) -> str:
        return (
            f"Producto(codigo={self.codigo}, nombre={self.nombre}, "
            f"categoria={self.categoria}, precio=${self.precio:.2f})"
        )
