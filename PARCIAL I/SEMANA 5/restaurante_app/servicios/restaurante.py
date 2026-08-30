# Servicio de Restaurante
# Gestiona listas de productos y clientes registrados en el sistema

from modelos.producto import Producto
from modelos.cliente import Cliente


class Restaurante:
    """
    Clase que administra los productos y clientes del restaurante.
    Proporciona métodos para agregar, consultar y mostrar información.
    """
    
    def __init__(self, nombre_restaurante: str):
        """
        Constructor de la clase Restaurante.
        
        Args:
            nombre_restaurante: Nombre del restaurante
        """
        self.nombre_restaurante: str = nombre_restaurante
        self.lista_productos: list[Producto] = []
        self.lista_clientes: list[Cliente] = []
    
    def agregar_producto(self, producto: Producto) -> None:
        """
        Agrega un nuevo producto a la lista del restaurante.
        
        Args:
            producto: Objeto de tipo Producto a agregar
        """
        self.lista_productos.append(producto)
    
    def agregar_cliente(self, cliente: Cliente) -> None:
        """
        Agrega un nuevo cliente a la lista del restaurante.
        
        Args:
            cliente: Objeto de tipo Cliente a agregar
        """
        self.lista_clientes.append(cliente)
    
    def obtener_producto_por_id(self, id_producto: int) -> Producto | None:
        """
        Busca un producto por su identificador.
        
        Args:
            id_producto: ID del producto a buscar
            
        Returns:
            Objeto Producto si existe, None si no se encuentra
        """
        for producto in self.lista_productos:
            if producto.id_producto == id_producto:
                return producto
        return None
    
    def obtener_cliente_por_id(self, id_cliente: int) -> Cliente | None:
        """
        Busca un cliente por su identificador.
        
        Args:
            id_cliente: ID del cliente a buscar
            
        Returns:
            Objeto Cliente si existe, None si no se encuentra
        """
        for cliente in self.lista_clientes:
            if cliente.id_cliente == id_cliente:
                return cliente
        return None
    
    def mostrar_todos_los_productos(self) -> None:
        """Muestra todos los productos registrados en el restaurante."""
        print(f"\n{'='*80}")
        print(f"PRODUCTOS DEL RESTAURANTE: {self.nombre_restaurante}")
        print(f"{'='*80}")
        
        if not self.lista_productos:
            print("No hay productos registrados.")
        else:
            for producto in self.lista_productos:
                print(producto)
    
    def mostrar_todos_los_clientes(self) -> None:
        """Muestra todos los clientes registrados en el restaurante."""
        print(f"\n{'='*80}")
        print(f"CLIENTES DEL RESTAURANTE: {self.nombre_restaurante}")
        print(f"{'='*80}")
        
        if not self.lista_clientes:
            print("No hay clientes registrados.")
        else:
            for cliente in self.lista_clientes:
                print(cliente)
    
    def contar_productos_disponibles(self) -> int:
        """
        Cuenta cuántos productos están disponibles.
        
        Returns:
            Número de productos disponibles
        """
        cantidad = 0
        for producto in self.lista_productos:
            if producto.disponible:
                cantidad += 1
        return cantidad
    
    def contar_clientes_frecuentes(self) -> int:
        """
        Cuenta cuántos clientes son frecuentes.
        
        Returns:
            Número de clientes frecuentes
        """
        cantidad = 0
        for cliente in self.lista_clientes:
            if cliente.es_cliente_frecuente:
                cantidad += 1
        return cantidad
    
    def obtener_resumen_estadisticas(self) -> None:
        """Muestra un resumen de estadísticas del restaurante."""
        print(f"\n{'='*80}")
        print(f"ESTADÍSTICAS DEL RESTAURANTE: {self.nombre_restaurante}")
        print(f"{'='*80}")
        print(f"Total de productos: {len(self.lista_productos)}")
        print(f"Productos disponibles: {self.contar_productos_disponibles()}")
        print(f"Total de clientes: {len(self.lista_clientes)}")
        print(f"Clientes frecuentes: {self.contar_clientes_frecuentes()}")
        print(f"{'='*80}\n")
