class Producto:
    """Representa un producto general del restaurante."""

    def __init__(self, nombre, precio, disponible=True):
        self.nombre = nombre
        self.disponible = disponible
        self.__precio = 0.0
        self.cambiar_precio(precio)

    def obtener_precio(self):
        """Devuelve el precio del producto."""
        return self.__precio

    def cambiar_precio(self, nuevo_precio):
        """Cambia el precio si el nuevo valor es válido."""
        if nuevo_precio <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self.__precio = nuevo_precio

    def mostrar_informacion(self):
        """Muestra los datos básicos del producto."""
        estado = "Disponible" if self.disponible else "No disponible"
        return f"Producto: {self.nombre} | Precio: ${self.obtener_precio():.2f} | Estado: {estado}"
