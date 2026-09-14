from __future__ import annotations

from typing import Any


class Producto:
    """Representa un producto del restaurante con control de stock."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, stock: int = 0) -> None:
        self.codigo: str = codigo
        self.nombre: str = nombre
        self.categoria: str = categoria
        self.precio: float = precio
        self.stock: int = stock

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

    @property
    def stock(self) -> int:
        return self._stock

    @stock.setter
    def stock(self, valor: int) -> None:
        if isinstance(valor, bool):
            raise ValueError("El stock debe ser un número entero no negativo.")
        try:
            stock = int(valor)
        except (TypeError, ValueError) as error:
            raise ValueError("El stock debe ser un número entero no negativo.") from error
        if stock < 0:
            raise ValueError("El stock no puede ser negativo.")
        self._stock = stock

    def vender(self, cantidad: int) -> None:
        """Reduce el stock del producto en la cantidad vendida."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero.")
        if self.stock < cantidad:
            raise ValueError(f"Stock insuficiente. Disponible: {self.stock}, Solicitado: {cantidad}.")
        self._stock -= cantidad

    def a_dict(self) -> dict[str, object]:
        """Convierte el objeto a una estructura compatible con JSON."""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio,
            "stock": self.stock,
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
                stock=datos.get("stock", 0),
            )
        except KeyError as error:
            raise KeyError(f"Falta la clave requerida en el registro: {error}") from error

    def __str__(self) -> str:
        return (
            f"Producto(codigo={self.codigo}, nombre={self.nombre}, "
            f"categoria={self.categoria}, precio={self.precio}, stock={self.stock})"
        )

    def __repr__(self) -> str:
        return self.__str__()
