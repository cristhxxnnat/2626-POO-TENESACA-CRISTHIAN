from __future__ import annotations

import sys
import tkinter as tk
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from restaurante_app.modelos.producto import Producto
from restaurante_app.servicios.archivo_servicio import ArchivoServicio
from restaurante_app.servicios.restaurante_servicio import RestauranteServicio
from restaurante_app.ui.login_view import LoginView
from restaurante_app.ui.main_view import MainView


class App:
    """Aplicación principal con una única ventana y cambio de vistas."""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Restaurante App - Semana 14")
        self.root.geometry("1100x680")
        self.root.minsize(900, 560)

        self.ruta_base = Path(__file__).resolve().parent
        self.ruta_datos = self.ruta_base / "datos"

        self.archivo_servicio = ArchivoServicio(
            self.ruta_datos / "productos.json",
            self.ruta_datos / "usuarios.json",
        )

        self.restaurante_servicio = RestauranteServicio("La Mesa de Cristi")
        self.restaurante_servicio.cargar_productos(self.archivo_servicio.cargar_productos())
        self.restaurante_servicio.cargar_usuarios(self.archivo_servicio.cargar_usuarios())

        self.login_view = LoginView(self.root, self._handle_login)
        self.main_view = MainView(
            self.root,
            self._handle_logout,
            self._handle_guardar_producto,
            self._handle_buscar_producto,
            self._handle_actualizar_producto,
            self._handle_eliminar_producto,
        )

        self.login_view.mostrar()
        self.root.mainloop()

    def _guardar_productos_json(self) -> None:
        if self.archivo_servicio.guardar_productos(self.restaurante_servicio.listar_productos()):
            self.main_view.mostrar_mensaje("Producto guardado correctamente.")

    def _handle_login(self, identificacion: str, password: str) -> None:
        if not self.restaurante_servicio.validar_acceso(identificacion, password):
            self.login_view.message_var.set("Credenciales incorrectas. Intente nuevamente.")
            return

        self.login_view.ocultar()
        self.main_view.mostrar_productos(self.restaurante_servicio.listar_productos())
        self.main_view.mostrar_usuarios(self.restaurante_servicio.listar_usuarios())
        self.main_view.mostrar()

    def _handle_logout(self) -> None:
        self.main_view.ocultar()
        self.main_view.limpiar_formulario()
        self.login_view.message_var.set("")
        self.login_view.usuario_entry.delete(0, tk.END)
        self.login_view.password_entry.delete(0, tk.END)
        self.login_view.mostrar()

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
            self.main_view.limpiar_formulario()
            self.main_view.mostrar_mensaje(f"Producto '{producto_eliminado.nombre}' eliminado correctamente.")
        except ValueError as error:
            self.main_view.mostrar_mensaje(str(error))


if __name__ == "__main__":
    App()
