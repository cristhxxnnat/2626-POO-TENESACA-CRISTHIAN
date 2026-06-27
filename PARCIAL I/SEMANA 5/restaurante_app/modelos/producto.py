# Modelo de Producto
# Representa un plato, bebida o producto disponible en el restaurante

class Producto:
    """
    Clase que representa un producto del restaurante.
    Almacena información sobre platos, bebidas y otros productos.
    """
    
    def __init__(
        self,
        id_producto: int,
        nombre: str,
        precio: float,
        categoria: str,
        disponible: bool = True
    ):
        """
        Constructor de la clase Producto.
        
        Args:
            id_producto: Identificador único del producto
            nombre: Nombre descriptivo del producto
            precio: Precio del producto en unidades monetarias
            categoria: Categoría del producto (plato, bebida, postre, etc.)
            disponible: Indica si el producto está disponible (True por defecto)
        """
        self.id_producto: int = id_producto
        self.nombre: str = nombre
        self.precio: float = precio
        self.categoria: str = categoria
        self.disponible: bool = disponible
    
    def cambiar_disponibilidad(self) -> None:
        """Cambia el estado de disponibilidad del producto."""
        self.disponible = not self.disponible
    
    def obtener_precio_con_descuento(self, porcentaje_descuento: float) -> float:
        """
        Calcula el precio del producto con descuento.
        
        Args:
            porcentaje_descuento: Porcentaje de descuento a aplicar
            
        Returns:
            Precio final con descuento aplicado
        """
        descuento = self.precio * (porcentaje_descuento / 100)
        return self.precio - descuento
    
    def __str__(self) -> str:
        """Representación en texto del producto."""
        estado = "Disponible" if self.disponible else "No disponible"
        return (
            f"ID: {self.id_producto} | Nombre: {self.nombre} | "
            f"Precio: ${self.precio:.2f} | Categoría: {self.categoria} | "
            f"Estado: {estado}"
        )
