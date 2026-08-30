from typing import List

from restaurante_app.modelos.cliente import Cliente
from restaurante_app.modelos.producto import Producto


class Restaurante:
    """Administra productos y clientes del restaurante."""

    def __init__(self, nombre_restaurante: str) -> None:
        self.nombre_restaurante = nombre_restaurante
        self.productos: List[Producto] = []
        self.clientes: List[Cliente] = []

    def registrar_producto(self, producto: Producto) -> None:
        if self._existe_codigo_producto(producto.codigo):
            raise ValueError("El código del producto ya está registrado.")
        self.productos.append(producto)

    def listar_productos(self) -> None:
        if not self.productos:
            print("No hay productos registrados.")
            return

        print(f"\nProductos en {self.nombre_restaurante}:")
        for producto in self.productos:
            producto.mostrar_informacion()

    def registrar_cliente(self, cliente: Cliente) -> None:
        if self._existe_identificacion_cliente(cliente.identificacion):
            raise ValueError("La identificación del cliente ya está registrada.")
        self.clientes.append(cliente)

    def listar_clientes(self) -> None:
        if not self.clientes:
            print("No hay clientes registrados.")
            return

        print(f"\nClientes en {self.nombre_restaurante}:")
        for cliente in self.clientes:
            cliente.mostrar_informacion()

    def _existe_codigo_producto(self, codigo: str) -> bool:
        return any(producto.codigo.lower() == codigo.lower() for producto in self.productos)

    def _existe_identificacion_cliente(self, identificacion: str) -> bool:
        return any(cliente.identificacion.lower() == identificacion.lower() for cliente in self.clientes)
