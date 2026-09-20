from __future__ import annotations

import tkinter as tk
from tkinter import ttk

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario


class MainView:
    """Vista principal con navegación, formulario de productos y consulta de usuarios."""

    def __init__(self, root: tk.Tk, on_logout: callable, on_guardar_producto: callable, on_buscar_producto: callable, on_actualizar_producto: callable, on_eliminar_producto: callable) -> None:
        self.root = root
        self.on_logout = on_logout
        self.on_guardar_producto = on_guardar_producto
        self.on_buscar_producto = on_buscar_producto
        self.on_actualizar_producto = on_actualizar_producto
        self.on_eliminar_producto = on_eliminar_producto
        self.frame = tk.Frame(root, padx=20, pady=20, bg="#edf2f9")

        top_bar = tk.Frame(self.frame, bg="#dfeaf7", height=60)
        top_bar.pack(fill="x", pady=(0, 15))
        top_bar.pack_propagate(False)

        title = tk.Label(
            top_bar,
            text="Panel del Restaurante",
            font=("Arial", 16, "bold"),
            bg="#dfeaf7",
            fg="#1d3557",
        )
        title.pack(side="left", padx=15, pady=10)

        tk.Button(
            top_bar,
            text="Cerrar sesión",
            command=self.on_logout,
            bg="#d9534f",
            fg="white",
            font=("Arial", 10, "bold"),
            relief="flat",
        ).pack(side="right", padx=15, pady=10)

        self.tabs = ttk.Notebook(self.frame)
        self.tabs.pack(fill="both", expand=True)

        self.productos_tab = tk.Frame(self.tabs, padx=12, pady=12, bg="#ffffff")
        self.tabs.add(self.productos_tab, text="Productos")

        self.usuarios_tab = tk.Frame(self.tabs, padx=12, pady=12, bg="#ffffff")
        self.tabs.add(self.usuarios_tab, text="Usuarios")

        self._crear_seccion_productos()
        self._crear_seccion_usuarios()

    def _crear_seccion_productos(self) -> None:
        panel_izquierdo = tk.Frame(self.productos_tab, bg="#ffffff")
        panel_izquierdo.pack(side="left", fill="y", padx=(0, 12))

        form = tk.LabelFrame(panel_izquierdo, text="Formulario de producto", padx=12, pady=12, bg="#ffffff")
        form.pack(fill="y", ipadx=5, ipady=5)

        self.codigo_var = tk.StringVar()
        self.nombre_var = tk.StringVar()
        self.categoria_var = tk.StringVar()
        self.precio_var = tk.StringVar()
        self.stock_var = tk.StringVar()

        campos = [
            ("Código", self.codigo_var),
            ("Nombre", self.nombre_var),
            ("Categoría", self.categoria_var),
            ("Precio", self.precio_var),
            ("Stock", self.stock_var),
        ]

        for label_text, variable in campos:
            tk.Label(form, text=label_text, bg="#ffffff", font=("Arial", 10, "bold")).pack(anchor="w", pady=(8, 2))
            entry = tk.Entry(form, textvariable=variable, font=("Arial", 10))
            entry.pack(fill="x", padx=0, pady=(0, 6))

        acciones = tk.Frame(form, bg="#ffffff")
        acciones.pack(fill="x", pady=(10, 0))

        tk.Button(acciones, text="Registrar", command=self._handle_guardar, bg="#2e8b57", fg="white", font=("Arial", 9, "bold"), width=12).pack(side="left", padx=(0, 6))
        tk.Button(acciones, text="Buscar", command=self._handle_buscar, bg="#0078d7", fg="white", font=("Arial", 9, "bold"), width=12).pack(side="left", padx=(0, 6))
        tk.Button(acciones, text="Actualizar", command=self._handle_actualizar, bg="#f0ad4e", fg="white", font=("Arial", 9, "bold"), width=12).pack(side="left", padx=(0, 6))
        tk.Button(acciones, text="Eliminar", command=self._handle_eliminar, bg="#d9534f", fg="white", font=("Arial", 9, "bold"), width=12).pack(side="left")

        self.mensaje_var = tk.StringVar(value="")
        tk.Label(form, textvariable=self.mensaje_var, fg="#0b4f6c", bg="#ffffff", justify="left", wraplength=260, font=("Arial", 9, "bold")).pack(anchor="w", pady=(12, 0))

        panel_derecho = tk.Frame(self.productos_tab, bg="#ffffff")
        panel_derecho.pack(side="left", fill="both", expand=True)

        tabla_frame = tk.LabelFrame(panel_derecho, text="Productos registrados", padx=8, pady=8, bg="#ffffff")
        tabla_frame.pack(fill="both", expand=True)

        self.productos_tree = ttk.Treeview(
            tabla_frame,
            columns=("codigo", "nombre", "categoria", "precio", "stock"),
            show="headings",
            height=15,
        )
        for col, text in (
            ("codigo", "Código"),
            ("nombre", "Nombre"),
            ("categoria", "Categoría"),
            ("precio", "Precio"),
            ("stock", "Stock"),
        ):
            self.productos_tree.heading(col, text=text)
            self.productos_tree.column(col, width=120, anchor="center")
        self.productos_tree.pack(fill="both", expand=True)

    def _crear_seccion_usuarios(self) -> None:
        tk.Label(self.usuarios_tab, text="Usuarios del sistema", bg="#ffffff", font=("Arial", 12, "bold")).pack(anchor="w", pady=(0, 10))
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

    def _handle_guardar(self) -> None:
        self.on_guardar_producto(
            self.codigo_var.get(),
            self.nombre_var.get(),
            self.categoria_var.get(),
            self.precio_var.get(),
            self.stock_var.get(),
        )

    def _handle_buscar(self) -> None:
        self.on_buscar_producto(self.codigo_var.get())

    def _handle_actualizar(self) -> None:
        self.on_actualizar_producto(
            self.codigo_var.get(),
            self.nombre_var.get(),
            self.categoria_var.get(),
            self.precio_var.get(),
            self.stock_var.get(),
        )

    def _handle_eliminar(self) -> None:
        self.on_eliminar_producto(self.codigo_var.get())

    def limpiar_formulario(self) -> None:
        self.codigo_var.set("")
        self.nombre_var.set("")
        self.categoria_var.set("")
        self.precio_var.set("")
        self.stock_var.set("")
        self.mensaje_var.set("")

    def mostrar_mensaje(self, texto: str) -> None:
        self.mensaje_var.set(texto)
