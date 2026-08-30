from __future__ import annotations

from typing import Optional

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.modelos.venta import Venta


class Restaurante:
    """Administra las colecciones, búsquedas, ventas y operaciones del restaurante."""

    def __init__(self, nombre_restaurante: str = "La Mesa de Cristi") -> None:
        self.nombre_restaurante: str = nombre_restaurante
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []

    # ==================== PRODUCTOS ====================

    def cargar_productos(self, productos: list[Producto]) -> None:
        """Entrega al servicio los productos recuperados por ArchivoServicio."""
        self._productos = list(productos)

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un nuevo producto si el código no está duplicado."""
        if self._existe_codigo_producto(producto.codigo):
            raise ValueError(f"El código del producto '{producto.codigo}' ya está registrado.")
        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        """Busca un producto por su código (case-insensitive)."""
        for producto in self._productos:
            if producto.codigo.lower() == codigo.lower():
                return producto
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nuevo_nombre: str,
        nueva_categoria: str,
        nuevo_precio: float,
        nuevo_stock: Optional[int] = None,
    ) -> bool:
        """Actualiza los datos de un producto existente."""
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError(f"No existe un producto con el código '{codigo}'.")
        producto.nombre = nuevo_nombre
        producto.categoria = nueva_categoria
        producto.precio = nuevo_precio
        if nuevo_stock is not None:
            producto.stock = nuevo_stock
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto por su código."""
        if self.buscar_producto(codigo) is None:
            raise ValueError(f"No existe un producto con el código '{codigo}'.")
        self._productos = [
            producto for producto in self._productos
            if producto.codigo.lower() != codigo.lower()
        ]
        return True

    def listar_productos(self) -> list[Producto]:
        """Retorna una copia de la lista de productos."""
        return list(self._productos)

    def _existe_codigo_producto(self, codigo: str) -> bool:
        """Verifica si un código de producto ya existe."""
        return any(producto.codigo.lower() == codigo.lower() for producto in self._productos)

    # ==================== USUARIOS ====================

    def cargar_usuarios(self, usuarios: list[Usuario]) -> None:
        """Entrega al servicio los usuarios recuperados por ArchivoServicio."""
        self._usuarios = list(usuarios)

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un nuevo usuario si la identificación no está duplicada."""
        if any(
            existente.identificacion.lower() == usuario.identificacion.lower()
            for existente in self._usuarios
        ):
            raise ValueError(
                f"La identificación del usuario '{usuario.identificacion}' ya está registrada."
            )
        self._usuarios.append(usuario)
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        """Busca un usuario por su identificación (case-insensitive)."""
        for usuario in self._usuarios:
            if usuario.identificacion.lower() == identificacion.lower():
                return usuario
        return None

    def listar_usuarios(self) -> list[Usuario]:
        """Retorna una copia de la lista de usuarios."""
        return list(self._usuarios)

    # ==================== VENTAS ====================

    def cargar_ventas(self, ventas: list[Venta]) -> None:
        """Entrega al servicio las ventas recuperadas por ArchivoServicio."""
        self._ventas = list(ventas)

    def vender_producto(
        self,
        codigo_producto: str,
        identificacion_usuario: str,
        cantidad: int,
    ) -> bool:
        """
        Realiza una venta controlando validaciones, stock y persistencia.
        
        Pasos:
        1. Buscar usuario y producto
        2. Validar cantidad y stock
        3. Crear Venta
        4. Agregar a colección
        5. Reducir stock del producto
        6. Retornar éxito
        """
        usuario = self.buscar_usuario(identificacion_usuario)
        producto = self.buscar_producto(codigo_producto)

        if usuario is None or producto is None:
            return False

        if cantidad <= 0 or producto.stock < cantidad:
            return False

        venta = Venta(usuario.identificacion, producto.codigo, cantidad)
        self._ventas.append(venta)
        producto.vender(cantidad)
        return True

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> list[Venta]:
        """
        Retorna las ventas asociadas a un usuario.
        Filtra la colección de ventas comparando el usuario_id.
        """
        ventas_usuario: list[Venta] = []
        for venta in self._ventas:
            if venta.usuario_id.lower() == identificacion_usuario.lower():
                ventas_usuario.append(venta)
        return ventas_usuario

    def listar_ventas(self) -> list[Venta]:
        """Retorna una copia de la lista de todas las ventas."""
        return list(self._ventas)

    # ==================== CONSULTAS ====================

    def obtener_categorias(self) -> set[str]:
        """Retorna el conjunto de categorías disponibles."""
        return {producto.categoria for producto in self._productos}
