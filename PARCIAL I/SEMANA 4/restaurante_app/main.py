# Archivo: main.py
# Descripción: Punto de entrada del sistema de gestión de restaurante
# Este archivo demuestra la funcionalidad del sistema

# Importaciones desde los módulos del proyecto
from modelos import Producto, Cliente
from servicios import Restaurante


def main():
    """
    Función principal que demuestra el funcionamiento del sistema.
    Crea instancias de las clases y ejecuta las operaciones principales.
    """
    
    # 1. CREACIÓN DEL RESTAURANTE
    print("\n" + "="*60)
    print("SISTEMA DE GESTIÓN DE RESTAURANTE".center(60))
    print("="*60)
    
    restaurante = Restaurante("La Buena Mesa", "Centro de la Ciudad")
    print(f"\n{restaurante}")
    
    
    # 2. CREACIÓN Y ADICIÓN DE PRODUCTOS
    print("\n--- AGREGANDO PRODUCTOS ---\n")
    
    # Crear productos de tipo "Plato"
    producto1 = Producto(1, "Arroz con Pollo", "Arroz con pollo jugoso y vegetales frescos", 12.50, "Plato")
    producto2 = Producto(2, "Lomo Saltado", "Trozos de lomo salteados con papas y cebolla", 18.00, "Plato")
    producto3 = Producto(3, "Ceviche", "Pescado fresco marinado en limón y especias", 16.99, "Plato")
    
    # Crear productos de tipo "Bebida"
    producto4 = Producto(4, "Jugo de Naranja", "Jugo natural de naranja recién exprimido", 3.50, "Bebida")
    producto5 = Producto(5, "Limonada", "Limonada fría con hielo y limón", 2.99, "Bebida")
    
    # Crear productos de tipo "Postre"
    producto6 = Producto(6, "Flan", "Postre tradicional de flan casero", 4.99, "Postre")
    
    # Agregar los productos al restaurante
    restaurante.agregar_producto(producto1)
    restaurante.agregar_producto(producto2)
    restaurante.agregar_producto(producto3)
    restaurante.agregar_producto(producto4)
    restaurante.agregar_producto(producto5)
    restaurante.agregar_producto(producto6)
    
    # Intentar agregar un producto duplicado (prueba de validación)
    producto_duplicado = Producto(1, "Duplicate", "No debería agregarse", 10.00, "Plato")
    restaurante.agregar_producto(producto_duplicado)
    
    
    # 3. MOSTRAR LISTADO DE PRODUCTOS
    restaurante.mostrar_productos()
    
    
    # 4. MOSTRAR INFORMACIÓN DETALLADA DE PRODUCTOS
    restaurante.mostrar_detalle_productos()
    
    
    # 5. CREACIÓN Y ADICIÓN DE CLIENTES
    print("\n--- AGREGANDO CLIENTES ---\n")
    
    cliente1 = Cliente(101, "Juan Pérez García", "555-1234", "juan.perez@email.com")
    cliente2 = Cliente(102, "María López Martínez", "555-5678", "maria.lopez@email.com")
    cliente3 = Cliente(103, "Carlos Rodríguez Sanchez", "555-9101", "carlos.rod@email.com")
    
    restaurante.agregar_cliente(cliente1)
    restaurante.agregar_cliente(cliente2)
    restaurante.agregar_cliente(cliente3)
    
    # Intentar agregar un cliente duplicado (prueba de validación)
    cliente_duplicado = Cliente(101, "Duplicate", "555-0000", "dup@email.com")
    restaurante.agregar_cliente(cliente_duplicado)
    
    
    # 6. MOSTRAR LISTADO DE CLIENTES
    restaurante.mostrar_clientes()
    
    
    # 7. MOSTRAR INFORMACIÓN DETALLADA DE CLIENTES
    restaurante.mostrar_detalle_clientes()
    
    
    # 8. OPERACIONES DE BÚSQUEDA
    print("\n--- BÚSQUEDAS EN EL SISTEMA ---\n")
    
    # Buscar un producto específico
    producto_buscado = restaurante.buscar_producto(2)
    if producto_buscado:
        print(f"Producto encontrado: {producto_buscado}")
    
    # Buscar un cliente específico
    cliente_buscado = restaurante.buscar_cliente(102)
    if cliente_buscado:
        print(f"Cliente encontrado: {cliente_buscado}")
    
    print()
    
    
    # 9. OPERACIONES ESPECIALES CON PRODUCTOS
    print("\n--- OPERACIONES CON PRODUCTOS ---\n")
    
    # Aplicar descuento a un producto
    producto_desc = restaurante.buscar_producto(1)
    if producto_desc:
        precio_con_descuento = producto_desc.aplicar_descuento(10)
        print(f"Precio del '{producto_desc.nombre}' con 10% de descuento: ${precio_con_descuento}\n")
    
    # Filtrar productos por tipo
    platosmenu = restaurante.obtener_productos_por_tipo("Plato")
    print(f"Cantidad de Platos disponibles: {len(platosmenu)}")
    for plato in platosmenu:
        print(f"  - {plato}")
    print()
    
    # Calcular valor del inventario
    valor_inventario = restaurante.calcular_valor_inventario()
    print(f"Valor total del inventario: ${valor_inventario}\n")
    
    
    # 10. OPERACIONES CON CLIENTES
    print("--- OPERACIONES CON CLIENTES ---\n")
    
    # Actualizar contacto de un cliente
    cliente_actualizar = restaurante.buscar_cliente(101)
    if cliente_actualizar:
        cliente_actualizar.actualizar_contacto(
            nuevo_telefono="555-9999",
            nuevo_email="juan.perez.nuevo@email.com"
        )
    
    print()
    
    
    # 11. RESUMEN FINAL
    print("\n" + "="*60)
    print("RESUMEN DEL SISTEMA".center(60))
    print("="*60)
    print(f"\nRestaurante: {restaurante.nombre}")
    print(f"Total de Productos: {len(restaurante.productos)}")
    print(f"Total de Clientes: {len(restaurante.clientes)}")
    print(f"Valor del Inventario: ${restaurante.calcular_valor_inventario()}")
    print("\n" + "="*60 + "\n")


# Punto de entrada del programa
if __name__ == "__main__":
    main()
