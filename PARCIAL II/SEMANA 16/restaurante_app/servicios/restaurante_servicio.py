from __future__ import annotations

from typing import Callable, Optional

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.modelos.venta import Venta


class RestauranteServicio:
    """Administra las reglas del restaurante y las operaciones de usuarios."""

    def __init__(
        self,
        nombre_restaurante: str = "La Mesa de Cristi",
        guardar_usuarios: Callable[[list[Usuario]], bool] | None = None,
    ) -> None:
        self.nombre_restaurante: str = nombre_restaurante
        self._productos: list[Producto] = []
        self._usuarios: list[Usuario] = []
        self._ventas: list[Venta] = []
        self._guardar_usuarios = guardar_usuarios

    @staticmethod
    def _clave(valor: str) -> str:
        return valor.strip().casefold()

    def cargar_productos(self, productos: list[Producto]) -> None:
        self._productos = list(productos)

    def cargar_usuarios(self, usuarios: list[Usuario]) -> None:
        self._usuarios = list(usuarios)

    def cargar_ventas(self, ventas: list[Venta]) -> None:
        self._ventas = list(ventas)

    def validar_acceso(self, identificacion: str, password: str) -> bool:
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return False
        return usuario.password == password

    def listar_productos(self) -> list[Producto]:
        return list(self._productos)

    def listar_usuarios(self) -> list[Usuario]:
        return list(self._usuarios)

    def listar_ventas(self) -> list[Venta]:
        return list(self._ventas)

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

    def _validar_administrador(self, administrador_id: str) -> Usuario:
        administrador = self.buscar_usuario(administrador_id)
        if administrador is None or administrador.rol != "Administrador":
            raise ValueError("Solo un Administrador puede gestionar usuarios.")
        return administrador

    def _guardar_cambios_usuarios(self) -> None:
        if self._guardar_usuarios is not None and not self._guardar_usuarios(self.listar_usuarios()):
            raise OSError("No se pudieron guardar los cambios en usuarios.json.")

    def registrar_usuario(self, usuario: Usuario, administrador_id: str) -> Usuario:
        self._validar_administrador(administrador_id)
        if usuario.rol == "Administrador":
            raise ValueError("La gestión administrativa solo permite registrar Empleados y Clientes.")
        if self.buscar_usuario(usuario.identificacion) is not None:
            raise ValueError(f"El identificador '{usuario.identificacion}' ya está registrado.")
        if any(self._clave(registrado.correo) == self._clave(usuario.correo) for registrado in self._usuarios):
            raise ValueError("Ya existe un usuario registrado con ese correo.")

        self._usuarios.append(usuario)
        try:
            self._guardar_cambios_usuarios()
        except OSError:
            self._usuarios.remove(usuario)
            raise
        return usuario

    def actualizar_usuario(
        self,
        identificacion: str,
        administrador_id: str,
        nombre: str,
        correo: str,
        password: str | None,
        rol: str,
    ) -> Optional[Usuario]:
        self._validar_administrador(administrador_id)
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return None
        if usuario.rol == "Administrador":
            raise ValueError("La cuenta Administrador no puede modificarse desde esta sección.")

        usuario_actualizado = Usuario(identificacion, nombre, correo, password or usuario.password, rol)
        if usuario_actualizado.rol == "Administrador":
            raise ValueError("La gestión administrativa solo permite asignar Empleado o Cliente.")
        if any(
            registrado is not usuario
            and self._clave(registrado.correo) == self._clave(usuario_actualizado.correo)
            for registrado in self._usuarios
        ):
            raise ValueError("Ya existe un usuario registrado con ese correo.")

        anterior = usuario.a_dict()
        usuario.nombre = usuario_actualizado.nombre
        usuario.correo = usuario_actualizado.correo
        usuario.password = usuario_actualizado.password
        usuario.rol = usuario_actualizado.rol
        try:
            self._guardar_cambios_usuarios()
        except OSError:
            usuario.nombre = anterior["nombre"]
            usuario.correo = anterior["correo"]
            usuario.password = anterior["password"]
            usuario.rol = anterior["rol"]
            raise
        return usuario

    def eliminar_usuario(self, identificacion: str, administrador_id: str) -> Optional[Usuario]:
        self._validar_administrador(administrador_id)
        if self._clave(identificacion) == self._clave(administrador_id):
            raise ValueError("No puede eliminar la cuenta Administrador actualmente autenticada.")
        usuario = self.buscar_usuario(identificacion)
        if usuario is None:
            return None
        if usuario.rol == "Administrador":
            raise ValueError("La cuenta Administrador no puede eliminarse desde esta sección.")

        self._usuarios.remove(usuario)
        try:
            self._guardar_cambios_usuarios()
        except OSError:
            self._usuarios.append(usuario)
            raise
        return usuario

    def registrar_venta(self, usuario_id: str, producto_codigo: str, cantidad: int = 1) -> Venta:
        usuario = self.buscar_usuario(usuario_id)
        if usuario is None:
            raise ValueError("Debe seleccionar un usuario válido para registrar la venta.")

        producto = self.buscar_producto(producto_codigo)
        if producto is None:
            raise ValueError("Debe seleccionar un producto válido para registrar la venta.")

        if cantidad <= 0:
            raise ValueError("La cantidad de la venta debe ser mayor que cero.")

        if producto.stock < cantidad:
            raise ValueError(
                f"No hay suficiente stock de '{producto.nombre}'. Disponible: {producto.stock}."
            )

        producto.vender(cantidad)
        venta = Venta(usuario_id=usuario.identificacion, producto_codigo=producto.codigo, cantidad=cantidad)
        self._ventas.append(venta)
        return venta

    def consultar_ventas_usuario(self, identificacion_usuario: str) -> list[Venta]:
        usuario = self.buscar_usuario(identificacion_usuario)
        if usuario is None:
            return []
        return [venta for venta in self._ventas if self._clave(venta.usuario_id) == self._clave(usuario.identificacion)]

    def obtener_total_productos(self) -> int:
        return len(self._productos)

    def obtener_total_usuarios(self) -> int:
        return len(self._usuarios)

    def obtener_total_ventas(self) -> int:
        return len(self._ventas)
