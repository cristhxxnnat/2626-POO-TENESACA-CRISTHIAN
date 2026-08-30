from restaurante_app.modelos.producto import Producto


class Bebida(Producto):
    """Representa una bebida del restaurante."""

    def __init__(self, codigo: str, nombre: str, categoria: str, precio: float, tamaño: str, tipo_envase: str) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self.tamaño: str = tamaño
        self.tipo_envase: str = tipo_envase

    @property
    def tamaño(self) -> str:
        return self._tamaño

    @tamaño.setter
    def tamaño(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El tamaño de la bebida no puede estar vacío.")
        self._tamaño = valor.strip()

    @property
    def tipo_envase(self) -> str:
        return self._tipo_envase

    @tipo_envase.setter
    def tipo_envase(self, valor: str) -> None:
        if not valor or not valor.strip():
            raise ValueError("El tipo de envase no puede estar vacío.")
        self._tipo_envase = valor.strip()

    def __str__(self) -> str:
        return (
            f"Bebida(codigo={self.codigo}, nombre={self.nombre}, "
            f"categoria={self.categoria}, precio=${self.precio:.2f}, "
            f"tamaño={self.tamaño}, tipo_envase={self.tipo_envase})"
        )
