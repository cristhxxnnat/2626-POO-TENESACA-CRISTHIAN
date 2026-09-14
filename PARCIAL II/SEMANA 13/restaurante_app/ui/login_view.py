from __future__ import annotations

from tkinter import messagebox
import tkinter as tk
from typing import Callable


class LoginView:
    """Vista de inicio de sesión del restaurante."""

    def __init__(self, root: tk.Tk, on_login: Callable[[str, str], None]) -> None:
        self.root = root
        self.on_login = on_login
        self.frame = tk.Frame(root, padx=30, pady=30, bg="#f0f4f8")

        self.title_label = tk.Label(
            self.frame,
            text="Restaurante App",
            font=("Arial", 20, "bold"),
            bg="#f0f4f8",
            fg="#1f3a5f",
        )
        self.title_label.pack(pady=(0, 20))

        tk.Label(self.frame, text="Usuario", bg="#f0f4f8").pack(anchor="w")
        self.usuario_entry = tk.Entry(self.frame, width=30)
        self.usuario_entry.pack(fill="x", pady=(0, 10))

        tk.Label(self.frame, text="Contraseña", bg="#f0f4f8").pack(anchor="w")
        self.password_entry = tk.Entry(self.frame, width=30, show="*")
        self.password_entry.pack(fill="x", pady=(0, 20))

        self.login_button = tk.Button(
            self.frame,
            text="Ingresar",
            command=self._handle_login,
            bg="#2d6cdf",
            fg="white",
            font=("Arial", 10, "bold"),
            width=20,
        )
        self.login_button.pack()

        self.message_var = tk.StringVar(value="")
        self.message_label = tk.Label(
            self.frame,
            textvariable=self.message_var,
            fg="#b22222",
            bg="#f0f4f8",
            font=("Arial", 9, "bold"),
        )
        self.message_label.pack(pady=(15, 0))

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
