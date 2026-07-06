class Restaurante:
    """Administra los productos registrados en el restaurante."""

    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un producto a la lista del restaurante."""
        self.productos.append(producto)

    def mostrar_productos(self):
        """Muestra el menú registrado de forma organizada."""
        print(f"\nMenú del restaurante: {self.nombre}")
        print("-" * 70)

        if not self.productos:
            print("No hay productos registrados.")
            return

        for producto in self.productos:
            print(producto.mostrar_informacion())
            print("-" * 70)
