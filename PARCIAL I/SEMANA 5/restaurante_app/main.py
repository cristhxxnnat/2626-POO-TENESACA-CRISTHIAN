# Punto de entrada del sistema de gestión de restaurante
# Crea objetos y demuestra la funcionalidad del sistema

from modelos.producto import Producto
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


# Crear instancia del restaurante
restaurante = Restaurante("El Buen Sabor")

# ============================================================================
# CREAR PRODUCTOS
# ============================================================================

# Crear productos de diferentes categorías
producto_1 = Producto(
    id_producto=1,
    nombre="Arroz con Pollo",
    precio=12.50,
    categoria="Plato Principal",
    disponible=True
)

producto_2 = Producto(
    id_producto=2,
    nombre="Ceviche",
    precio=15.00,
    categoria="Entrada",
    disponible=True
)

producto_3 = Producto(
    id_producto=3,
    nombre="Jugo de Naranja",
    precio=3.50,
    categoria="Bebida",
    disponible=False
)

producto_4 = Producto(
    id_producto=4,
    nombre="Tiramisu",
    precio=8.00,
    categoria="Postre",
    disponible=True
)

# Agregar productos al restaurante
restaurante.agregar_producto(producto_1)
restaurante.agregar_producto(producto_2)
restaurante.agregar_producto(producto_3)
restaurante.agregar_producto(producto_4)

# ============================================================================
# CREAR CLIENTES
# ============================================================================

# Crear clientes con diferentes estados
cliente_1 = Cliente(
    id_cliente=101,
    nombre="María García López",
    email="maria.garcia@email.com",
    telefono="555-1234",
    es_cliente_frecuente=True
)

cliente_2 = Cliente(
    id_cliente=102,
    nombre="Juan Rodríguez Martínez",
    email="juan.rodriguez@email.com",
    telefono="555-5678",
    es_cliente_frecuente=False
)

cliente_3 = Cliente(
    id_cliente=103,
    nombre="Ana López Sánchez",
    email="ana.lopez@email.com",
    telefono="555-9012",
    es_cliente_frecuente=True
)

# Agregar clientes al restaurante
restaurante.agregar_cliente(cliente_1)
restaurante.agregar_cliente(cliente_2)
restaurante.agregar_cliente(cliente_3)

# ============================================================================
# MOSTRAR INFORMACIÓN DEL SISTEMA
# ============================================================================

# Mostrar todos los productos
restaurante.mostrar_todos_los_productos()

# Mostrar todos los clientes
restaurante.mostrar_todos_los_clientes()

# Mostrar estadísticas
restaurante.obtener_resumen_estadisticas()

# ============================================================================
# DEMOSTRACIONES ADICIONALES
# ============================================================================

# Buscar un producto específico
print("\nBÚSQUEDA DE PRODUCTO:")
print("-" * 80)
producto_buscado = restaurante.obtener_producto_por_id(2)
if producto_buscado:
    print(f"Producto encontrado: {producto_buscado}")
else:
    print("Producto no encontrado.")

# Buscar un cliente específico
print("\nBÚSQUEDA DE CLIENTE:")
print("-" * 80)
cliente_buscado = restaurante.obtener_cliente_por_id(101)
if cliente_buscado:
    print(f"Cliente encontrado: {cliente_buscado}")
else:
    print("Cliente no encontrado.")

# Cambiar disponibilidad de un producto
print("\nCAMBIO DE DISPONIBILIDAD:")
print("-" * 80)
print(f"Antes: {producto_3}")
producto_3.cambiar_disponibilidad()
print(f"Después: {producto_3}")

# Calcular precio con descuento
print("\nCÁLCULO DE DESCUENTO:")
print("-" * 80)
precio_original = producto_1.precio
precio_con_descuento = producto_1.obtener_precio_con_descuento(10)
print(f"Producto: {producto_1.nombre}")
print(f"Precio original: ${precio_original:.2f}")
print(f"Precio con 10% de descuento: ${precio_con_descuento:.2f}")

# Registrar cliente frecuente
print("\nREGISTRO DE CLIENTE FRECUENTE:")
print("-" * 80)
print(f"Antes: {cliente_2}")
cliente_2.registrar_cliente_frecuente()
print(f"Después: {cliente_2}")

# Actualizar teléfono de cliente
print("\nACTUALIZACIÓN DE TELÉFONO:")
print("-" * 80)
print(f"Teléfono anterior de {cliente_3.nombre}: {cliente_3.telefono}")
cliente_3.actualizar_telefono("555-3333")
print(f"Nuevo teléfono: {cliente_3.telefono}")

print("\n" + "="*80)
print("FIN DE LA DEMOSTRACIÓN DEL SISTEMA")
print("="*80 + "\n")
