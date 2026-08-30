class Producto:
    """Representa un producto disponible en el restaurante."""

    def __init__(self, nombre: str, categoria: str, precio: float, disponible: bool = True):
        self._nombre = ""
        self._categoria = ""
        self._precio = 0.0
        self._disponible = True

        self.nombre = nombre
        self.categoria = categoria
        self.precio = precio
        self.disponible = disponible

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str):
        if not valor.strip():
            raise ValueError("El nombre del producto no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def categoria(self) -> str:
        return self._categoria

    @categoria.setter
    def categoria(self, valor: str):
        if not valor.strip():
            raise ValueError("La categoría del producto no puede estar vacía.")
        self._categoria = valor.strip()

    @property
    def precio(self) -> float:
        return self._precio

    @precio.setter
    def precio(self, valor: float):
        if valor <= 0:
            raise ValueError("El precio debe ser mayor que cero.")
        self._precio = float(valor)

    @property
    def disponible(self) -> bool:
        return self._disponible

    @disponible.setter
    def disponible(self, valor: bool):
        self._disponible = bool(valor)

    def mostrar_informacion(self) -> None:
        estado = "Disponible" if self.disponible else "No disponible"
        print(f"Producto: {self.nombre} | Categoría: {self.categoria} | Precio: ${self.precio:.2f} | Estado: {estado}")
