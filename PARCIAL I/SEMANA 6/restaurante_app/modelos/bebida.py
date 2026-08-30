from modelos.producto import Producto


class Bebida(Producto):
    """Representa una bebida disponible en el restaurante."""

    def __init__(self, nombre, precio, volumen_ml, tipo_bebida, disponible=True):
        super().__init__(nombre, precio, disponible)
        self.volumen_ml = volumen_ml
        self.tipo_bebida = tipo_bebida

    def mostrar_informacion(self):
        """Muestra información específica de la bebida."""
        informacion_base = super().mostrar_informacion()
        return f"{informacion_base} | Tipo: {self.tipo_bebida} | Volumen: {self.volumen_ml} ml"
