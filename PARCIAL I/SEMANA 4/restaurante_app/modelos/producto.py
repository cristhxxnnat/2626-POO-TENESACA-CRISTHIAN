# Módulo: producto.py
# Descripción: Define la clase Producto que representa los items del restaurante

class Producto:
    """
    Clase que representa un producto (plato, bebida, etc.) disponible en el restaurante.
    
    Atributos:
        id (int): Identificador único del producto
        nombre (str): Nombre del producto
        descripcion (str): Descripción breve del producto
        precio (float): Precio unitario en dólares
        tipo (str): Tipo de producto (plato, bebida, postre, etc.)
    """
    
    def __init__(self, id, nombre, descripcion, precio, tipo):
        """
        Constructor de la clase Producto.
        
        Args:
            id (int): Identificador único
            nombre (str): Nombre del producto
            descripcion (str): Descripción del producto
            precio (float): Precio del producto
            tipo (str): Tipo de producto
        """
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.tipo = tipo
    
    def __str__(self):
        """
        Representación en texto del objeto Producto.
        
        Returns:
            str: Información formateada del producto
        """
        return f"[{self.id}] {self.nombre} ({self.tipo}) - ${self.precio:.2f}"
    
    def obtener_info_detallada(self):
        """
        Obtiene la información detallada del producto.
        
        Returns:
            str: Información completa incluyendo descripción
        """
        return (f"Producto: {self.nombre}\n"
                f"  Tipo: {self.tipo}\n"
                f"  Descripción: {self.descripcion}\n"
                f"  Precio: ${self.precio:.2f}")
    
    def actualizar_precio(self, nuevo_precio):
        """
        Actualiza el precio del producto.
        
        Args:
            nuevo_precio (float): Nuevo precio del producto
        """
        if nuevo_precio > 0:
            self.precio = nuevo_precio
            print(f"Precio de '{self.nombre}' actualizado a ${nuevo_precio:.2f}")
        else:
            print("El precio debe ser mayor a 0")
    
    def aplicar_descuento(self, porcentaje):
        """
        Aplica un descuento al precio del producto.
        
        Args:
            porcentaje (float): Porcentaje de descuento (0-100)
        
        Returns:
            float: Nuevo precio con descuento aplicado
        """
        if 0 <= porcentaje <= 100:
            descuento = self.precio * (porcentaje / 100)
            precio_descuento = self.precio - descuento
            return round(precio_descuento, 2)
        else:
            print("El porcentaje debe estar entre 0 y 100")
            return self.precio
