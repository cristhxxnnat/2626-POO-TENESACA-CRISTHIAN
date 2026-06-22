# Módulo: restaurante.py
# Descripción: Define la clase Restaurante que gestiona productos y clientes

class Restaurante:
    """
    Clase que administra las operaciones principales del restaurante.
    Gestiona el registro de productos y clientes, y proporciona métodos
    para buscar y mostrar información.
    
    Atributos:
        nombre (str): Nombre del restaurante
        ubicacion (str): Ubicación del restaurante
        productos (list): Lista de productos disponibles
        clientes (list): Lista de clientes registrados
    """
    
    def __init__(self, nombre, ubicacion):
        """
        Constructor de la clase Restaurante.
        
        Args:
            nombre (str): Nombre del restaurante
            ubicacion (str): Ubicación del restaurante
        """
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.productos = []  # Lista para almacenar productos
        self.clientes = []   # Lista para almacenar clientes
    
    def __str__(self):
        """
        Representación en texto del objeto Restaurante.
        
        Returns:
            str: Información formateada del restaurante
        """
        return (f"Restaurante: {self.nombre}\n"
                f"Ubicación: {self.ubicacion}\n"
                f"Productos registrados: {len(self.productos)}\n"
                f"Clientes registrados: {len(self.clientes)}")
    
    def agregar_producto(self, producto):
        """
        Agrega un nuevo producto al registro del restaurante.
        
        Args:
            producto (Producto): Objeto Producto a agregar
        
        Returns:
            bool: True si se agregó exitosamente, False si ya existe
        """
        # Verifica que el producto no esté duplicado por ID
        if self._producto_existe(producto.id):
            print(f"Error: El producto con ID {producto.id} ya existe.")
            return False
        
        self.productos.append(producto)
        print(f"Producto '{producto.nombre}' agregado exitosamente.")
        return True
    
    def agregar_cliente(self, cliente):
        """
        Agrega un nuevo cliente al registro del restaurante.
        
        Args:
            cliente (Cliente): Objeto Cliente a agregar
        
        Returns:
            bool: True si se agregó exitosamente, False si ya existe
        """
        # Verifica que el cliente no esté duplicado por ID
        if self._cliente_existe(cliente.id):
            print(f"Error: El cliente con ID {cliente.id} ya existe.")
            return False
        
        self.clientes.append(cliente)
        print(f"Cliente '{cliente.nombre}' agregado exitosamente.")
        return True
    
    def buscar_producto(self, id_producto):
        """
        Busca un producto por su ID.
        
        Args:
            id_producto (int): ID del producto a buscar
        
        Returns:
            Producto: El objeto Producto encontrado, o None si no existe
        """
        for producto in self.productos:
            if producto.id == id_producto:
                return producto
        return None
    
    def buscar_cliente(self, id_cliente):
        """
        Busca un cliente por su ID.
        
        Args:
            id_cliente (int): ID del cliente a buscar
        
        Returns:
            Cliente: El objeto Cliente encontrado, o None si no existe
        """
        for cliente in self.clientes:
            if cliente.id == id_cliente:
                return cliente
        return None
    
    def _producto_existe(self, id_producto):
        """
        Método privado para verificar si un producto existe.
        
        Args:
            id_producto (int): ID del producto a verificar
        
        Returns:
            bool: True si existe, False en caso contrario
        """
        return self.buscar_producto(id_producto) is not None
    
    def _cliente_existe(self, id_cliente):
        """
        Método privado para verificar si un cliente existe.
        
        Args:
            id_cliente (int): ID del cliente a verificar
        
        Returns:
            bool: True si existe, False en caso contrario
        """
        return self.buscar_cliente(id_cliente) is not None
    
    def mostrar_productos(self):
        """
        Muestra todos los productos registrados en el restaurante.
        """
        if not self.productos:
            print("\n*** No hay productos registrados ***\n")
            return
        
        print("\n" + "="*60)
        print("PRODUCTOS DEL RESTAURANTE".center(60))
        print("="*60)
        
        for producto in self.productos:
            print(f"  {producto}")
        
        print("="*60 + "\n")
    
    def mostrar_clientes(self):
        """
        Muestra todos los clientes registrados en el restaurante.
        """
        if not self.clientes:
            print("\n*** No hay clientes registrados ***\n")
            return
        
        print("\n" + "="*60)
        print("CLIENTES DEL RESTAURANTE".center(60))
        print("="*60)
        
        for cliente in self.clientes:
            print(f"  {cliente}")
        
        print("="*60 + "\n")
    
    def mostrar_detalle_productos(self):
        """
        Muestra la información detallada de todos los productos.
        """
        if not self.productos:
            print("\n*** No hay productos registrados ***\n")
            return
        
        print("\n" + "="*60)
        print("DETALLE DE PRODUCTOS".center(60))
        print("="*60)
        
        for producto in self.productos:
            print(f"\n{producto.obtener_info_detallada()}")
        
        print("\n" + "="*60 + "\n")
    
    def mostrar_detalle_clientes(self):
        """
        Muestra la información detallada de todos los clientes.
        """
        if not self.clientes:
            print("\n*** No hay clientes registrados ***\n")
            return
        
        print("\n" + "="*60)
        print("DETALLE DE CLIENTES".center(60))
        print("="*60)
        
        for cliente in self.clientes:
            print(f"\n{cliente.obtener_info_completa()}")
        
        print("\n" + "="*60 + "\n")
    
    def obtener_productos_por_tipo(self, tipo):
        """
        Obtiene todos los productos de un tipo específico.
        
        Args:
            tipo (str): Tipo de producto a filtrar (ej: 'plato', 'bebida')
        
        Returns:
            list: Lista de productos del tipo especificado
        """
        return [p for p in self.productos if p.tipo.lower() == tipo.lower()]
    
    def calcular_valor_inventario(self):
        """
        Calcula el valor total del inventario de productos.
        
        Returns:
            float: Valor total del inventario
        """
        total = sum(p.precio for p in self.productos)
        return round(total, 2)
