from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from restaurante_app.modelos.producto import Producto


class ArchivoServicio:
    """Centraliza la lectura y escritura de productos en formato JSON."""

    def __init__(self, ruta_productos: Path) -> None:
        self.ruta_productos: Path = ruta_productos
        self.ruta_productos.parent.mkdir(parents=True, exist_ok=True)

    def cargar_productos(self) -> list[Producto]:
        """Carga registros válidos y descarta los defectuosos sin detener el sistema."""
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
                print(f"Advertencia: se omitió el registro {numero_registro}: {error}")
        return productos

    def guardar_productos(self, productos: list[Producto]) -> bool:
        """Guarda objetos Producto como una lista de diccionarios JSON."""
        datos: list[dict[str, object]] = [producto.a_dict() for producto in productos]
        try:
            with open(self.ruta_productos, "w", encoding="utf-8") as archivo:
                json.dump(datos, archivo, ensure_ascii=False, indent=2)
        except PermissionError:
            print("Error: no hay permisos para escribir productos.json.")
            return False
        return True
