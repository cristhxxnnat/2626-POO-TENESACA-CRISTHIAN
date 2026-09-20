from __future__ import annotations

from typing import Optional

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario


class RestauranteServicio:
    """Administra productos y usuarios del restaurante para la capa de interfaz."""

    def __init__(self, nombre_restaurante: str = "La Mesa de Cristi") -> None:
        self.nombre_restaurante: str = nombre_restaurante
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []

    @staticmethod
    def _clave(valor: str) -> str:
        """Normaliza claves para búsquedas sin distinguir mayúsculas."""
        return valor.strip().casefold()

    def cargar_productos(self, productos: list[Producto]) -> None:
        self._productos = list(productos)

    def cargar_usuarios(self, usuarios: list[Usuario]) -> None:
        self._usuarios = list(usuarios)

    def validar_acceso(self, identificacion: str, password: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False
        return usuario.password == password

    def listar_productos(self) -> list[Producto]:
        return list(self._productos)

    def listar_usuarios(self) -> list[Usuario]:
        return list(self._usuarios)

    def registrar_producto(self, producto: Producto) -> Producto:
        if self.buscar_producto(producto.codigo) is not None:
            raise ValueError(f"El código del producto '{producto.codigo}' ya existe.")
        self._productos.append(producto)
        return producto

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for producto in self._productos:
            if self._clave(producto.codigo) == self._clave(codigo):
                return producto
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nombre: str | None = None,
        categoria: str | None = None,
        precio: float | None = None,
        stock: int | None = None,
    ) -> Optional[Producto]:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return None

        if nombre is not None:
            producto.nombre = nombre
        if categoria is not None:
            producto.categoria = categoria
        if precio is not None:
            producto.precio = precio
        if stock is not None:
            producto.stock = stock

        return producto

    def eliminar_producto(self, codigo: str) -> Optional[Producto]:
        producto = self.buscar_producto(codigo)
        if producto is None:
            return None
        self._productos.remove(producto)
        return producto

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        for usuario in self._usuarios:
            if self._clave(usuario.identificacion) == self._clave(identificacion):
                return usuario
        return None

    def obtener_total_productos(self) -> int:
        return len(self._productos)

    def obtener_total_usuarios(self) -> int:
        return len(self._usuarios)
