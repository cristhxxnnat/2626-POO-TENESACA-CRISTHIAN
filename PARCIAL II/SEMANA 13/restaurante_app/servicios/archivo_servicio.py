from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario


class ArchivoServicio:
    """Centraliza la lectura y escritura de productos y usuarios en formato JSON."""

    def __init__(self, ruta_productos: Path, ruta_usuarios: Path) -> None:
        self.ruta_productos: Path = ruta_productos
        self.ruta_usuarios: Path = ruta_usuarios
        self.ruta_productos.parent.mkdir(parents=True, exist_ok=True)

    def cargar_productos(self) -> list[Producto]:
        """Carga registros válidos de productos desde productos.json."""
        try:
            with open(self.ruta_productos, "r", encoding="utf-8") as archivo:
                datos: Any = json.load(archivo)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as error:
            print(f"Advertencia: productos.json no contiene JSON válido: {error}")
            return []
        except PermissionError:
            print("Advertencia: no hay permisos para leer productos.json.")
            return []

        if not isinstance(datos, list):
            print("Advertencia: productos.json debe contener una lista de productos.")
            return []

        productos: list[Producto] = []
        for numero_registro, registro in enumerate(datos, start=1):
            try:
                if not isinstance(registro, dict):
                    raise ValueError("el registro no es un objeto JSON")
                productos.append(Producto.desde_dict(registro))
            except (KeyError, TypeError, ValueError) as error:
                print(
                    f"Advertencia: se omitió el registro {numero_registro} en productos.json: {error}"
                )
        return productos

    def cargar_usuarios(self) -> list[Usuario]:
        """Carga registros válidos de usuarios desde usuarios.json."""
        try:
            with open(self.ruta_usuarios, "r", encoding="utf-8") as archivo:
                datos: Any = json.load(archivo)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as error:
            print(f"Advertencia: usuarios.json no contiene JSON válido: {error}")
            return []
        except PermissionError:
            print("Advertencia: no hay permisos para leer usuarios.json.")
            return []

        if not isinstance(datos, list):
            print("Advertencia: usuarios.json debe contener una lista de usuarios.")
            return []

        usuarios: list[Usuario] = []
        for numero_registro, registro in enumerate(datos, start=1):
            try:
                if not isinstance(registro, dict):
                    raise ValueError("el registro no es un objeto JSON")
                usuarios.append(Usuario.desde_dict(registro))
            except (KeyError, TypeError, ValueError) as error:
                print(
                    f"Advertencia: se omitió el registro {numero_registro} en usuarios.json: {error}"
                )
        return usuarios
