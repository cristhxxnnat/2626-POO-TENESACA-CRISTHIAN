from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.modelos.venta import Venta


class ArchivoServicio:
    """Lee y escribe productos, usuarios y ventas en JSON."""

    def __init__(self, ruta_productos: Path, ruta_usuarios: Path, ruta_ventas: Path) -> None:
        self.ruta_productos: Path = ruta_productos
        self.ruta_usuarios: Path = ruta_usuarios
        self.ruta_ventas: Path = ruta_ventas
        self.ruta_productos.parent.mkdir(parents=True, exist_ok=True)

    def cargar_productos(self) -> list[Producto]:
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
                print(f"Advertencia: se omitió el registro {numero_registro} en productos.json: {error}")
        return productos

    def guardar_productos(self, productos: list[Producto]) -> bool:
        try:
            with open(self.ruta_productos, "w", encoding="utf-8") as archivo:
                json.dump([producto.a_dict() for producto in productos], archivo, ensure_ascii=False, indent=2)
            return True
        except OSError as error:
            print(f"No se pudo guardar productos.json: {error}")
            return False

    def cargar_usuarios(self) -> list[Usuario]:
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
                print(f"Advertencia: se omitió el registro {numero_registro} en usuarios.json: {error}")
        return usuarios

    def guardar_usuarios(self, usuarios: list[Usuario]) -> bool:
        try:
            with open(self.ruta_usuarios, "w", encoding="utf-8") as archivo:
                json.dump([usuario.a_dict() for usuario in usuarios], archivo, ensure_ascii=False, indent=2)
            return True
        except OSError as error:
            print(f"No se pudo guardar usuarios.json: {error}")
            return False

    def cargar_ventas(self) -> list[Venta]:
        try:
            with open(self.ruta_ventas, "r", encoding="utf-8") as archivo:
                datos: Any = json.load(archivo)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError as error:
            print(f"Advertencia: ventas.json no contiene JSON válido: {error}")
            return []
        except PermissionError:
            print("Advertencia: no hay permisos para leer ventas.json.")
            return []

        if not isinstance(datos, list):
            print("Advertencia: ventas.json debe contener una lista de ventas.")
            return []

        ventas: list[Venta] = []
        for numero_registro, registro in enumerate(datos, start=1):
            try:
                if not isinstance(registro, dict):
                    raise ValueError("el registro no es un objeto JSON")
                ventas.append(Venta.desde_dict(registro))
            except (KeyError, TypeError, ValueError) as error:
                print(f"Advertencia: se omitió el registro {numero_registro} en ventas.json: {error}")
        return ventas

    def guardar_ventas(self, ventas: list[Venta]) -> bool:
        try:
            with open(self.ruta_ventas, "w", encoding="utf-8") as archivo:
                json.dump([venta.a_dict() for venta in ventas], archivo, ensure_ascii=False, indent=2)
            return True
        except OSError as error:
            print(f"No se pudo guardar ventas.json: {error}")
            return False
