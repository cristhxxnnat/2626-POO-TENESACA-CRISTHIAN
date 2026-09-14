from __future__ import annotations

from tkinter import ttk
import tkinter as tk

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario


class MainView:
    """Vista principal de la aplicación con acceso a productos y usuarios."""

    def __init__(self, root: tk.Tk, on_logout: callable) -> None:
        self.root = root
        self.on_logout = on_logout
        self.frame = tk.Frame(root, padx=20, pady=20, bg="#eef2f7")

        top_bar = tk.Frame(self.frame, bg="#dfeaf7")
        top_bar.pack(fill="x", pady=(0, 20))

        title = tk.Label(
            top_bar,
            text="Panel del Restaurante",
            font=("Arial", 16, "bold"),
            bg="#dfeaf7",
            fg="#1d3557",
        )
        title.pack(side="left", padx=15, pady=10)

        logout_btn = tk.Button(
            top_bar,
            text="Cerrar sesión",
            command=self.on_logout,
            bg="#d9534f",
            fg="white",
            font=("Arial", 10, "bold"),
        )
        logout_btn.pack(side="right", padx=15, pady=10)

        self.tabs = ttk.Notebook(self.frame)
        self.tabs.pack(fill="both", expand=True)

        self.productos_tab = tk.Frame(self.tabs, padx=10, pady=10)
        self.tabs.add(self.productos_tab, text="Productos")

        self.usuarios_tab = tk.Frame(self.tabs, padx=10, pady=10)
        self.tabs.add(self.usuarios_tab, text="Usuarios")

        self.ventas_tab = tk.Frame(self.tabs, padx=10, pady=10)
        self.tabs.add(self.ventas_tab, text="Ventas")

        self.productos_tree = ttk.Treeview(
            self.productos_tab,
            columns=("codigo", "nombre", "categoria", "precio", "stock"),
            show="headings",
        )
        for col, text in (
            ("codigo", "Código"),
            ("nombre", "Nombre"),
            ("categoria", "Categoría"),
            ("precio", "Precio"),
            ("stock", "Stock"),
        ):
            self.productos_tree.heading(col, text=text)
            self.productos_tree.column(col, width=130, anchor="center")
        self.productos_tree.pack(fill="both", expand=True)

        self.usuarios_tree = ttk.Treeview(
            self.usuarios_tab,
            columns=("identificacion", "nombre", "correo"),
            show="headings",
        )
        for col, text in (
            ("identificacion", "Identificación"),
            ("nombre", "Nombre"),
            ("correo", "Correo"),
        ):
            self.usuarios_tree.heading(col, text=text)
            self.usuarios_tree.column(col, width=180, anchor="center")
        self.usuarios_tree.pack(fill="both", expand=True)

        self.ventas_label = tk.Label(
            self.ventas_tab,
            text="Ventas (pendiente en esta etapa)",
            font=("Arial", 12, "bold"),
            fg="#6c757d",
            bg="#eef2f7",
        )
        self.ventas_label.pack(anchor="center", pady=60)

    def mostrar(self) -> None:
        self.frame.pack(fill="both", expand=True)

    def ocultar(self) -> None:
        self.frame.pack_forget()

    def mostrar_productos(self, productos: list[Producto]) -> None:
        for item in self.productos_tree.get_children():
            self.productos_tree.delete(item)

        for producto in productos:
            self.productos_tree.insert(
                "",
                tk.END,
                values=(
                    producto.codigo,
                    producto.nombre,
                    producto.categoria,
                    f"${producto.precio:,.0f}",
                    producto.stock,
                ),
            )

    def mostrar_usuarios(self, usuarios: list[Usuario]) -> None:
        for item in self.usuarios_tree.get_children():
            self.usuarios_tree.delete(item)

        for usuario in usuarios:
            self.usuarios_tree.insert(
                "",
                tk.END,
                values=(usuario.identificacion, usuario.nombre, usuario.correo),
            )
