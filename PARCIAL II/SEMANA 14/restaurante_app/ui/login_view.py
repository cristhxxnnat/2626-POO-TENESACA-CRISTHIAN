from __future__ import annotations

import tkinter as tk
from tkinter import messagebox
from typing import Callable


class LoginView:
    """Vista de inicio de sesión del restaurante."""

    def __init__(self, root: tk.Tk, on_login: Callable[[str, str], None]) -> None:
        self.root = root
        self.on_login = on_login
        self.frame = tk.Frame(root, padx=40, pady=40, bg="#f3f6fb")

        self.title_label = tk.Label(
            self.frame,
            text="Restaurante App",
            font=("Arial", 22, "bold"),
            bg="#f3f6fb",
            fg="#1d3557",
        )
        self.title_label.pack(pady=(0, 25))

        form = tk.Frame(self.frame, bg="#f3f6fb")
        form.pack(fill="x")

        tk.Label(form, text="Usuario", bg="#f3f6fb", font=("Arial", 10, "bold")).pack(anchor="w")
        self.usuario_entry = tk.Entry(form, width=30, font=("Arial", 11))
        self.usuario_entry.pack(fill="x", pady=(0, 12))

        tk.Label(form, text="Contraseña", bg="#f3f6fb", font=("Arial", 10, "bold")).pack(anchor="w")
        self.password_entry = tk.Entry(form, width=30, show="*", font=("Arial", 11))
        self.password_entry.pack(fill="x", pady=(0, 18))

        self.login_button = tk.Button(
            form,
            text="Ingresar",
            command=self._handle_login,
            bg="#2d6cdf",
            fg="white",
            font=("Arial", 10, "bold"),
            bd=0,
            padx=12,
            pady=8,
            width=20,
        )
        self.login_button.pack()

        self.message_var = tk.StringVar(value="")
        self.message_label = tk.Label(
            self.frame,
            textvariable=self.message_var,
            fg="#b22222",
            bg="#f3f6fb",
            font=("Arial", 9, "bold"),
        )
        self.message_label.pack(pady=(18, 0))

    def mostrar(self) -> None:
        self.frame.pack(fill="both", expand=True)
        self.usuario_entry.focus_set()

    def ocultar(self) -> None:
        self.frame.pack_forget()

    def _handle_login(self) -> None:
        usuario = self.usuario_entry.get().strip()
        password = self.password_entry.get().strip()

        if not usuario or not password:
            self.message_var.set("Debe ingresar usuario y contraseña.")
            messagebox.showwarning("Datos incompletos", "Debe ingresar usuario y contraseña.")
            return

        self.on_login(usuario, password)
