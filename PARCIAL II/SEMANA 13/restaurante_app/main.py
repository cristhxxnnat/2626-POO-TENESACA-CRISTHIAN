from __future__ import annotations

import sys
import tkinter as tk
from pathlib import Path

if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from restaurante_app.servicios.archivo_servicio import ArchivoServicio
from restaurante_app.servicios.restaurante_servicio import RestauranteServicio
from restaurante_app.ui.login_view import LoginView
from restaurante_app.ui.main_view import MainView


class App:
    """Aplicación principal con una única ventana y cambio de vistas."""

    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title("Restaurante App - Semana 13")
        self.root.geometry("900x600")

        self.ruta_base = Path(__file__).resolve().parent
        self.ruta_datos = self.ruta_base / "datos"

        self.archivo_servicio = ArchivoServicio(
            self.ruta_datos / "productos.json",
            self.ruta_datos / "usuarios.json",
        )

        self.restaurante_servicio = RestauranteServicio("La Mesa de Cristi")

        productos = self.archivo_servicio.cargar_productos()
        usuarios = self.archivo_servicio.cargar_usuarios()

        self.restaurante_servicio.cargar_productos(productos)
        self.restaurante_servicio.cargar_usuarios(usuarios)

        self.login_view = LoginView(self.root, self._handle_login)
        self.main_view = MainView(self.root, self._handle_logout)

        self.login_view.mostrar()

        self.root.mainloop()

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
        self.login_view.message_var.set("")
        self.login_view.usuario_entry.delete(0, tk.END)
        self.login_view.password_entry.delete(0, tk.END)
        self.login_view.mostrar()


if __name__ == "__main__":
    App()
