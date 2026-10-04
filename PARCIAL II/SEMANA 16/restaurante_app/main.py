from __future__ import annotations

import sys
import tkinter as tk
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.modelos.venta import Venta
from restaurante_app.servicios.archivo_servicio import ArchivoServicio
from restaurante_app.servicios.restaurante_servicio import RestauranteServicio
from restaurante_app.ui.login_view import LoginView
from restaurante_app.ui.main_view import MainView


class App:
    """Aplicación principal con una única ventana y cambio de vistas."""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Restaurante App - Semana 16")
        self.root.geometry("1180x720")
        self.root.minsize(980, 620)

        self.ruta_base = Path(__file__).resolve().parent
        self.ruta_datos = self.ruta_base / "datos"
        self.icon_image = tk.PhotoImage(file=str(self.ruta_base / "assets" / "icon_restaurante.png"))
        self.root.iconphoto(True, self.icon_image)

        self.archivo_servicio = ArchivoServicio(
            self.ruta_datos / "productos.json",
            self.ruta_datos / "usuarios.json",
            self.ruta_datos / "ventas.json",
        )

        self.restaurante_servicio = RestauranteServicio(
            "La Mesa de Cristi",
            guardar_usuarios=self.archivo_servicio.guardar_usuarios,
        )
        self.restaurante_servicio.cargar_productos(self.archivo_servicio.cargar_productos())
        self.restaurante_servicio.cargar_usuarios(self.archivo_servicio.cargar_usuarios())
        self.restaurante_servicio.cargar_ventas(self.archivo_servicio.cargar_ventas())

        self.login_view = LoginView(self.root, self._handle_login)
        self.main_view = MainView(
            self.root,
            self._handle_logout,
            self._handle_guardar_producto,
            self._handle_buscar_producto,
            self._handle_actualizar_producto,
            self._handle_eliminar_producto,
            self._handle_registrar_venta,
            self._handle_consultar_usuario,
            self._handle_registrar_usuario,
            self._handle_actualizar_usuario,
            self._handle_eliminar_usuario,
            self._handle_cambio_rol_usuario,
        )

        self.login_view.mostrar()
        self.root.mainloop()

    def _handle_login(self, identificacion: str, password: str) -> None:
        if not self.restaurante_servicio.validar_acceso(identificacion, password):
            self.login_view.message_var.set("Credenciales incorrectas. Intente nuevamente.")
            return

        usuario = self.restaurante_servicio.buscar_usuario(identificacion)
        if usuario is None:
            self.login_view.message_var.set("No se encontró el usuario autenticado.")
            return
        self.main_view.establecer_usuario_actual(usuario)
        self.login_view.ocultar()
        self._actualizar_vistas_principales()
        self.main_view.mostrar()

    def _handle_logout(self) -> None:
        self.main_view.ocultar()
        self.main_view.establecer_usuario_actual(None)
        self.main_view.limpiar_formulario()
        self.main_view.limpiar_formulario_usuarios()
        self.main_view.mostrar_usuarios(self.restaurante_servicio.listar_usuarios())
        self.main_view.mostrar_mensaje_venta("")
        self.login_view.message_var.set("")
        self.login_view.usuario_entry.delete(0, tk.END)
        self.login_view.password_entry.delete(0, tk.END)
        self.login_view.mostrar()

    def _actualizar_vistas_principales(self) -> None:
        self.main_view.mostrar_productos(self.restaurante_servicio.listar_productos())
        self.main_view.mostrar_usuarios(self.restaurante_servicio.listar_usuarios())
        self.main_view.mostrar_ventas(self.restaurante_servicio.listar_ventas())
        self.main_view.actualizar_selecciones(
            self.restaurante_servicio.listar_usuarios(),
            self.restaurante_servicio.listar_productos(),
        )

    def _handle_consultar_usuario(self, identificacion: str) -> None:
        usuario = self.restaurante_servicio.buscar_usuario(identificacion)
        if usuario is None:
            self.main_view.mostrar_mensaje_usuario("No se encontró el usuario seleccionado.")
            return
        self.main_view.cargar_usuario_en_formulario(usuario)

    def _handle_registrar_usuario(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        password: str,
        rol: str,
    ) -> None:
        try:
            usuario = Usuario(identificacion, nombre, correo, password, rol)
            administrador_id = self.main_view.usuario_actual.identificacion
            self.restaurante_servicio.registrar_usuario(usuario, administrador_id)
            self._actualizar_usuarios()
            self.main_view.limpiar_formulario_usuarios()
            self.main_view.mostrar_mensaje_usuario(f"Usuario '{usuario.identificacion}' registrado correctamente.")
        except (ValueError, OSError) as error:
            self.main_view.mostrar_mensaje_usuario(str(error))

    def _handle_actualizar_usuario(
        self,
        identificacion: str,
        nombre: str,
        correo: str,
        password: str,
        rol: str,
    ) -> None:
        try:
            administrador_id = self.main_view.usuario_actual.identificacion
            usuario = self.restaurante_servicio.actualizar_usuario(
                identificacion,
                administrador_id,
                nombre,
                correo,
                password,
                rol,
            )
            if usuario is None:
                self.main_view.mostrar_mensaje_usuario("No se encontró el usuario para actualizar.")
                return
            self._actualizar_usuarios()
            self.main_view.limpiar_formulario_usuarios()
            self.main_view.mostrar_mensaje_usuario(f"Usuario '{usuario.identificacion}' actualizado correctamente.")
        except (ValueError, OSError) as error:
            self.main_view.mostrar_mensaje_usuario(str(error))

    def _handle_eliminar_usuario(self, identificacion: str) -> None:
        try:
            administrador_id = self.main_view.usuario_actual.identificacion
            usuario = self.restaurante_servicio.eliminar_usuario(identificacion, administrador_id)
            if usuario is None:
                self.main_view.mostrar_mensaje_usuario("No se encontró el usuario para eliminar.")
                return
            self._actualizar_usuarios()
            self.main_view.limpiar_formulario_usuarios()
            self.main_view.mostrar_mensaje_usuario(f"Usuario '{usuario.identificacion}' eliminado correctamente.")
        except (ValueError, OSError) as error:
            self.main_view.mostrar_mensaje_usuario(str(error))

    def _handle_cambio_rol_usuario(self, rol: str) -> None:
        self.main_view.mostrar_mensaje_usuario(f"Rol seleccionado: {rol}.")

    def _actualizar_usuarios(self) -> None:
        usuarios = self.restaurante_servicio.listar_usuarios()
        self.main_view.mostrar_usuarios(usuarios)
        self.main_view.actualizar_selecciones(usuarios, self.restaurante_servicio.listar_productos())

    def _handle_guardar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: str,
        stock: str,
    ) -> None:
        try:
            producto = Producto(codigo.strip(), nombre.strip(), categoria.strip(), float(precio), int(stock))
            self.restaurante_servicio.registrar_producto(producto)
            self.archivo_servicio.guardar_productos(self.restaurante_servicio.listar_productos())
            self.main_view.mostrar_productos(self.restaurante_servicio.listar_productos())
            self.main_view.actualizar_selecciones(
                self.restaurante_servicio.listar_usuarios(),
                self.restaurante_servicio.listar_productos(),
            )
            self.main_view.limpiar_formulario()
            self.main_view.mostrar_mensaje(f"Producto '{producto.nombre}' registrado correctamente.")
        except ValueError as error:
            self.main_view.mostrar_mensaje(str(error))
        except Exception as error:
            self.main_view.mostrar_mensaje(f"Error: {error}")

    def _handle_buscar_producto(self, codigo: str) -> None:
        try:
            producto = self.restaurante_servicio.buscar_producto(codigo.strip())
            if producto is None:
                self.main_view.mostrar_mensaje("No se encontró un producto con ese código.")
                return
            self.main_view.codigo_var.set(producto.codigo)
            self.main_view.nombre_var.set(producto.nombre)
            self.main_view.categoria_var.set(producto.categoria)
            self.main_view.precio_var.set(str(producto.precio))
            self.main_view.stock_var.set(str(producto.stock))
            self.main_view.mostrar_mensaje(f"Producto encontrado: {producto.nombre}")
        except ValueError as error:
            self.main_view.mostrar_mensaje(str(error))

    def _handle_actualizar_producto(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: str,
        stock: str,
    ) -> None:
        if not codigo.strip():
            self.main_view.mostrar_mensaje("Debe ingresar el código del producto a actualizar.")
            return

        try:
            producto_actualizado = self.restaurante_servicio.actualizar_producto(
                codigo.strip(),
                nombre=nombre.strip() or None,
                categoria=categoria.strip() or None,
                precio=float(precio) if precio.strip() else None,
                stock=int(stock) if stock.strip() else None,
            )
            if producto_actualizado is None:
                self.main_view.mostrar_mensaje("No se encontró el producto para actualizar.")
                return
            self.archivo_servicio.guardar_productos(self.restaurante_servicio.listar_productos())
            self.main_view.mostrar_productos(self.restaurante_servicio.listar_productos())
            self.main_view.actualizar_selecciones(
                self.restaurante_servicio.listar_usuarios(),
                self.restaurante_servicio.listar_productos(),
            )
            self.main_view.mostrar_mensaje(f"Producto '{producto_actualizado.nombre}' actualizado correctamente.")
        except ValueError as error:
            self.main_view.mostrar_mensaje(str(error))
        except Exception as error:
            self.main_view.mostrar_mensaje(f"Error: {error}")

    def _handle_eliminar_producto(self, codigo: str) -> None:
        try:
            producto_eliminado = self.restaurante_servicio.eliminar_producto(codigo.strip())
            if producto_eliminado is None:
                self.main_view.mostrar_mensaje("No se encontró el producto a eliminar.")
                return
            self.archivo_servicio.guardar_productos(self.restaurante_servicio.listar_productos())
            self.main_view.mostrar_productos(self.restaurante_servicio.listar_productos())
            self.main_view.actualizar_selecciones(
                self.restaurante_servicio.listar_usuarios(),
                self.restaurante_servicio.listar_productos(),
            )
            self.main_view.limpiar_formulario()
            self.main_view.mostrar_mensaje(f"Producto '{producto_eliminado.nombre}' eliminado correctamente.")
        except ValueError as error:
            self.main_view.mostrar_mensaje(str(error))

    def _handle_registrar_venta(self, usuario_id: str, producto_codigo: str, cantidad: str) -> None:
        try:
            venta = self.restaurante_servicio.registrar_venta(
                usuario_id.strip(),
                producto_codigo.strip(),
                int(cantidad.strip() or 1),
            )
            self.archivo_servicio.guardar_ventas(self.restaurante_servicio.listar_ventas())
            self.main_view.mostrar_ventas(self.restaurante_servicio.listar_ventas())
            self.main_view.mostrar_mensaje_venta(
                f"Venta registrada: usuario {venta.usuario_id}, producto {venta.producto_codigo}, cantidad {venta.cantidad}."
            )
        except ValueError as error:
            self.main_view.mostrar_mensaje_venta(str(error))
        except Exception as error:
            self.main_view.mostrar_mensaje_venta(f"Error: {error}")


if __name__ == "__main__":
    App()
