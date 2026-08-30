import json
from pathlib import Path
from typing import Optional

from restaurante_app.modelos.cliente import Cliente
from restaurante_app.modelos.producto import Producto


class Restaurante:
    """Administra productos y clientes del restaurante."""

    def __init__(self, nombre_restaurante: str = "La Mesa de Cristi") -> None:
        self.nombre_restaurante: str = nombre_restaurante
        self.productos: list[Producto] = []
        self.clientes: list[Cliente] = []

        self.base_dir: Path = Path(__file__).resolve().parent.parent
        self.data_dir: Path = self.base_dir / "data"
        self.data_dir.mkdir(parents=True, exist_ok=True)

        self.productos_path: Path = self.data_dir / "productos.json"
        self.clientes_path: Path = self.data_dir / "clientes.json"

        self._crear_archivos_json_si_no_existen()
        self._cargar_productos_json()
        self._cargar_clientes_json()

    def _crear_archivos_json_si_no_existen(self) -> None:
        if not self.productos_path.exists():
            self.productos_path.write_text("{}", encoding="utf-8")
        if not self.clientes_path.exists():
            self.clientes_path.write_text("{}", encoding="utf-8")

    def _producto_a_dict(self, producto: Producto) -> dict[str, object]:
        return {
            "codigo": producto.codigo,
            "nombre": producto.nombre,
            "categoria": producto.categoria,
            "precio": producto.precio,
        }

    def _cliente_a_dict(self, cliente: Cliente) -> dict[str, str]:
        return {
            "identificacion": cliente.identificacion,
            "nombre": cliente.nombre,
            "correo": cliente.correo,
        }

    def _guardar_productos_json(self) -> None:
        datos: dict[str, dict[str, object]] = {}
        for producto in self.productos:
            datos[producto.codigo] = self._producto_a_dict(producto)

        with self.productos_path.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)

    def _guardar_clientes_json(self) -> None:
        datos: dict[str, dict[str, str]] = {}
        for cliente in self.clientes:
            datos[cliente.identificacion] = self._cliente_a_dict(cliente)

        with self.clientes_path.open("w", encoding="utf-8") as archivo:
            json.dump(datos, archivo, ensure_ascii=False, indent=2)

    def _cargar_productos_json(self) -> None:
        try:
            with self.productos_path.open("r", encoding="utf-8") as archivo:
                datos: dict[str, dict[str, object]] = json.load(archivo)

            self.productos = []
            for clave, valor in datos.items():
                if isinstance(valor, dict):
                    producto = Producto(
                        codigo=str(valor.get("codigo", clave)),
                        nombre=str(valor.get("nombre", "")),
                        categoria=str(valor.get("categoria", "")),
                        precio=float(valor.get("precio", 0.0)),
                    )
                    self.productos.append(producto)
        except (FileNotFoundError, json.JSONDecodeError, ValueError, TypeError):
            self.productos = []

    def _cargar_clientes_json(self) -> None:
        try:
            with self.clientes_path.open("r", encoding="utf-8") as archivo:
                datos: dict[str, dict[str, str]] = json.load(archivo)

            self.clientes = []
            for clave, valor in datos.items():
                if isinstance(valor, dict):
                    cliente = Cliente(
                        identificacion=str(valor.get("identificacion", clave)),
                        nombre=str(valor.get("nombre", "")),
                        correo=str(valor.get("correo", "")),
                    )
                    self.clientes.append(cliente)
        except (FileNotFoundError, json.JSONDecodeError, ValueError, TypeError):
            self.clientes = []

    def registrar_producto(self, producto: Producto) -> bool:
        if self._existe_codigo_producto(producto.codigo):
            raise ValueError(f"El código del producto '{producto.codigo}' ya está registrado.")

        self.productos.append(producto)
        self._guardar_productos_json()
        return True

    def buscar_producto(self, codigo: str) -> Optional[Producto]:
        for producto in self.productos:
            if producto.codigo.lower() == codigo.lower():
                return producto
        return None

    def actualizar_producto(
        self,
        codigo: str,
        nuevo_nombre: str,
        nueva_categoria: str,
        nuevo_precio: float,
    ) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError(f"No existe un producto con el código '{codigo}'.")

        producto.nombre = nuevo_nombre
        producto.categoria = nueva_categoria
        producto.precio = nuevo_precio
        self._guardar_productos_json()
        return True

    def eliminar_producto(self, codigo: str) -> bool:
        producto = self.buscar_producto(codigo)
        if producto is None:
            raise ValueError(f"No existe un producto con el código '{codigo}'.")

        self.productos = [item for item in self.productos if item.codigo.lower() != codigo.lower()]
        self._guardar_productos_json()
        return True

    def listar_productos(self) -> list[Producto]:
        return self.productos

    def registrar_cliente(self, cliente: Cliente) -> bool:
        if self._existe_identificacion_cliente(cliente.identificacion):
            raise ValueError(f"La identificación del cliente '{cliente.identificacion}' ya está registrada.")

        self.clientes.append(cliente)
        self._guardar_clientes_json()
        return True

    def listar_clientes(self) -> list[Cliente]:
        return self.clientes

    def obtener_categorias(self) -> set[str]:
        categorias: set[str] = set()
        for producto in self.productos:
            categorias.add(producto.categoria)
        return categorias

    def _existe_codigo_producto(self, codigo: str) -> bool:
        return any(producto.codigo.lower() == codigo.lower() for producto in self.productos)

    def _existe_identificacion_cliente(self, identificacion: str) -> bool:
        return any(cliente.identificacion.lower() == identificacion.lower() for cliente in self.clientes)
