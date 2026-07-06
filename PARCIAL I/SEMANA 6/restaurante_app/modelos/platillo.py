from modelos.producto import Producto


class Platillo(Producto):
    """Representa un platillo del restaurante."""

    def __init__(self, nombre, precio, calorias, tipo_platillo, tiempo_preparacion, disponible=True):
        super().__init__(nombre, precio, disponible)
        self.calorias = calorias
        self.tipo_platillo = tipo_platillo
        self.tiempo_preparacion = tiempo_preparacion

    def mostrar_informacion(self):
        """Muestra información específica del platillo."""
        informacion_base = super().mostrar_informacion()
        return (
            f"{informacion_base} | Tipo: {self.tipo_platillo} | "
            f"Calorías: {self.calorias} kcal | Tiempo de preparación: {self.tiempo_preparacion} min"
        )
