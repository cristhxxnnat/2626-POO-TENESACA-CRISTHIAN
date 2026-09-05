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
        self._productos_por_codigo: dict[str, Producto] = {}
        self._usuarios_por_identificacion: dict[str, Usuario] = {}
        self._ventas_por_usuario: dict[str, list[Venta]] = {}
        self._categorias: set[str] = set()

    @staticmethod
    def _clave(valor: str) -> str:
        """Normaliza claves para conservar las búsquedas sin distinguir mayúsculas."""
        return valor.strip().casefold()

    def _reconstruir_indice_productos(self) -> None:
        """Reconstruye el índice de productos y el conjunto de categorías."""
        self._productos_por_codigo = {
            self._clave(producto.codigo): producto for producto in self._productos
        }
        self._categorias = {producto.categoria for producto in self._productos}

    def _reconstruir_indice_usuarios(self) -> None:
        """Reconstruye el índice de usuarios a partir de la lista principal."""
        self._usuarios_por_identificacion = {
            self._clave(usuario.identificacion): usuario for usuario in self._usuarios
        }

    def _reconstruir_indice_ventas(self) -> None:
        """Agrupa ventas por usuario para consultas directas."""
        self._ventas_por_usuario = {}
        for venta in self._ventas:
            clave_usuario = self._clave(venta.usuario_id)
            self._ventas_por_usuario.setdefault(clave_usuario, []).append(venta)

    # ==================== PRODUCTOS ====================

    def cargar_productos(self, productos: list[Producto]) -> None:
        """Entrega al servicio los productos recuperados por ArchivoServicio."""
        self._productos = list(productos)
        self._reconstruir_indice_productos()

    def registrar_producto(self, producto: Producto) -> bool:
        """Registra un nuevo producto si el código no está duplicado."""
        if self._existe_codigo_producto(producto.codigo):
            raise ValueError(f"El código del producto '{producto.codigo}' ya está registrado.")
        self._productos.append(producto)
        self._productos_por_codigo[self._clave(producto.codigo)] = producto
        self._categorias.add(producto.categoria)
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        """Busca un producto por su código (case-insensitive)."""
        return self._productos_por_codigo.get(self._clave(codigo))

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
        categoria_anterior = producto.categoria
        producto.nombre = nuevo_nombre
        producto.categoria = nueva_categoria
        producto.precio = nuevo_precio
        if nuevo_stock is not None:
            producto.stock = nuevo_stock
        self._categorias.discard(categoria_anterior)
        self._categorias.add(producto.categoria)
        self._categorias.update(
            producto_registrado.categoria for producto_registrado in self._productos
        )
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        """Elimina un producto por su código."""
        producto = self._productos_por_codigo.get(self._clave(codigo))
        if producto is None:
            raise ValueError(f"No existe un producto con el código '{codigo}'.")
        self._productos.remove(producto)
        del self._productos_por_codigo[self._clave(codigo)]
        self._categorias = {producto_registrado.categoria for producto_registrado in self._productos}
        return True

    def listar_productos(self) -> list[Producto]:
        """Retorna una copia de la lista de productos."""
        return list(self._productos)

    def _existe_codigo_producto(self, codigo: str) -> bool:
        """Verifica si un código de producto ya existe."""
        return self._clave(codigo) in self._productos_por_codigo

    # ==================== USUARIOS ====================

    def cargar_usuarios(self, usuarios: list[Usuario]) -> None:
        """Entrega al servicio los usuarios recuperados por ArchivoServicio."""
        self._usuarios = list(usuarios)
        self._reconstruir_indice_usuarios()

    def registrar_usuario(self, usuario: Usuario) -> bool:
        """Registra un nuevo usuario si la identificación no está duplicada."""
        clave_usuario = self._clave(usuario.identificacion)
        if clave_usuario in self._usuarios_por_identificacion:
            raise ValueError(
                f"La identificación del usuario '{usuario.identificacion}' ya está registrada."
            )
        self._usuarios.append(usuario)
        self._usuarios_por_identificacion[clave_usuario] = usuario
        return True

    def buscar_usuario(self, identificacion: str) -> Optional[Usuario]:
        """Busca un usuario por su identificación (case-insensitive)."""
        return self._usuarios_por_identificacion.get(self._clave(identificacion))

    def listar_usuarios(self) -> list[Usuario]:
        """Retorna una copia de la lista de usuarios."""
        return list(self._usuarios)

    # ==================== VENTAS ====================

    def cargar_ventas(self, ventas: list[Venta]) -> None:
        """Entrega al servicio las ventas recuperadas por ArchivoServicio."""
        self._ventas = list(ventas)
        self._reconstruir_indice_ventas()

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
        self._ventas_por_usuario.setdefault(self._clave(venta.usuario_id), []).append(venta)
        producto.vender(cantidad)
        return True

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> list[Venta]:
        """
        Retorna las ventas asociadas a un usuario usando el índice por identificación.
        """
        return list(self._ventas_por_usuario.get(self._clave(identificacion_usuario), []))

    def listar_ventas(self) -> list[Venta]:
        """Retorna una copia de la lista de todas las ventas."""
        return list(self._ventas)

    # ==================== CONSULTAS ====================

    def obtener_categorias(self) -> set[str]:
        """Retorna el conjunto de categorías disponibles."""
        return set(self._categorias)
