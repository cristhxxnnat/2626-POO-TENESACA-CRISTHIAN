from __future__ import annotations

from typing import Optional

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario


class Restaurante:
    """Administra las colecciones y operaciones del restaurante."""

    def __init__(self, nombre_restaurante: str = "La Mesa de Cristi") -> None:
        self.nombre_restaurante: str = nombre_restaurante
        self.productos: list[Producto] = []
        self.usuarios: list[Usuario] = []

    def cargar_productos(self, productos: list[Producto]) -> None:
        """Entrega al servicio los productos recuperados por ArchivoServicio."""
        self.productos = list(productos)

    def registrar_producto(self, producto: Producto) -> bool:
        if self._existe_codigo_producto(producto.codigo):
            raise ValueError(f"El código del producto '{producto.codigo}' ya está registrado.")
        self.productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for producto in self.productos:
            if producto.codigo.lower() == codigo.lower():
                return producto
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nuevo_nombre: str,
        nueva_categoria: str,
        nuevo_precio: float,
    ) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError(f"No existe un producto con el código '{codigo}'.")
        producto.nombre = nuevo_nombre
        producto.categoria = nueva_categoria
        producto.precio = nuevo_precio
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        if self.buscar_producto(codigo) is None:
            raise ValueError(f"No existe un producto con el código '{codigo}'.")
        self.productos = [
            producto for producto in self.productos
            if producto.codigo.lower() != codigo.lower()
        ]
        return True

    def listar_productos(self) -> list[Producto]:
        return list(self.productos)

    def registrar_usuario(self, usuario: Usuario) -> bool:
        if any(
            existente.identificacion.lower() == usuario.identificacion.lower()
            for existente in self.usuarios
        ):
            raise ValueError(
                f"La identificación del usuario '{usuario.identificacion}' ya está registrada."
            )
        self.usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> list[Usuario]:
        return list(self.usuarios)

    def obtener_categorias(self) -> set[str]:
        return {producto.categoria for producto in self.productos}

    def _existe_codigo_producto(self, codigo: str) -> bool:
        return any(producto.codigo.lower() == codigo.lower() for producto in self.productos)
