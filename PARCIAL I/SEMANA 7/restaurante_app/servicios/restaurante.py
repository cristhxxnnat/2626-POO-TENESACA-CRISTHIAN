from modelos.cliente import Cliente
from modelos.producto import Producto


class Restaurante:
    """Administra productos y clientes del restaurante."""

    def __init__(self, nombre_restaurante: str):
        self.nombre_restaurante = nombre_restaurante
        self.productos = []
        self.clientes = []

    def registrar_producto(self, producto: Producto) -> None:
        self.productos.append(producto)

    def listar_productos(self) -> None:
        if not self.productos:
            print("No hay productos registrados.")
            return

        print(f"\nProductos en {self.nombre_restaurante}:")
        for producto in self.productos:
            producto.mostrar_informacion()

    def buscar_producto(self, nombre: str) -> Producto | None:
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto
        return None

    def registrar_cliente(self, cliente: Cliente) -> None:
        self.clientes.append(cliente)

    def listar_clientes(self) -> None:
        if not self.clientes:
            print("No hay clientes registrados.")
            return

        print(f"\nClientes en {self.nombre_restaurante}:")
        for cliente in self.clientes:
            print(f"ID: {cliente.id_cliente} | Nombre: {cliente.nombre} | Correo: {cliente.correo}")

    def buscar_cliente(self, nombre: str) -> Cliente | None:
        for cliente in self.clientes:
            if cliente.nombre.lower() == nombre.lower():
                return cliente
        return None
