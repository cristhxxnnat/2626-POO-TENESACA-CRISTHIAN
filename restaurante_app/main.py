from __future__ import annotations

from pathlib import Path
import sys
from typing import Callable

# Permite ejecutar este archivo directamente desde el botón de VS Code.
if __package__ is None or __package__ == "":
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.archivo_servicio import ArchivoServicio
from restaurante_app.servicios.restaurante import Restaurante


# Configuración de rutas
RUTA_DATOS: Path = Path(__file__).resolve().parent / "datos"
RUTA_PRODUCTOS: Path = RUTA_DATOS / "productos.json"
RUTA_USUARIOS: Path = RUTA_DATOS / "usuarios.json"
RUTA_VENTAS: Path = RUTA_DATOS / "ventas.json"

# Inicialización de servicios
restaurante = Restaurante()
archivo_servicio = ArchivoServicio(RUTA_PRODUCTOS, RUTA_USUARIOS, RUTA_VENTAS)

# Cargar datos al iniciar
restaurante.cargar_productos(archivo_servicio.cargar_productos())
restaurante.cargar_usuarios(archivo_servicio.cargar_usuarios())
restaurante.cargar_ventas(archivo_servicio.cargar_ventas())

OPCIONES_MENU: tuple[str, ...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Vender producto",
    "9. Consultar ventas de un usuario",
    "10. Mostrar categorías",
    "11. Salir",
)


# ==================== FUNCIONES DE PERSISTENCIA ====================

def guardar_productos() -> None:
    """Guarda los productos en el archivo JSON."""
    if archivo_servicio.guardar_productos(restaurante.listar_productos()):
        print("Archivo de productos actualizado.")


def guardar_usuarios() -> None:
    """Guarda los usuarios en el archivo JSON."""
    if archivo_servicio.guardar_usuarios(restaurante.listar_usuarios()):
        print("Archivo de usuarios actualizado.")


def guardar_ventas() -> None:
    """Guarda las ventas en el archivo JSON."""
    if archivo_servicio.guardar_ventas(restaurante.listar_ventas()):
        print("Archivo de ventas actualizado.")


# ==================== PRODUCTOS ====================

def registrar_producto_desde_consola() -> None:
    """Solicita datos para registrar un nuevo producto."""
    try:
        producto = Producto(
            codigo=input("Ingrese el código del producto: ").strip(),
            nombre=input("Ingrese el nombre del producto: ").strip(),
            categoria=input("Ingrese la categoría del producto: ").strip(),
            precio=float(input("Ingrese el precio del producto: ").strip()),
            stock=int(input("Ingrese el stock disponible del producto: ").strip()),
        )
        restaurante.registrar_producto(producto)
        guardar_productos()
        print("Producto registrado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def buscar_producto_desde_consola() -> None:
    """Solicita el código y busca un producto."""
    codigo = input("Ingrese el código del producto a buscar: ").strip()
    producto = restaurante.buscar_producto(codigo)
    print(producto if producto is not None else "Producto no encontrado.")


def actualizar_producto_desde_consola() -> None:
    """Solicita datos para actualizar un producto."""
    try:
        codigo = input("Ingrese el código del producto a actualizar: ").strip()
        restaurante.actualizar_producto(
            codigo=codigo,
            nuevo_nombre=input("Ingrese el nuevo nombre: ").strip(),
            nueva_categoria=input("Ingrese la nueva categoría: ").strip(),
            nuevo_precio=float(input("Ingrese el nuevo precio: ").strip()),
            nuevo_stock=int(input("Ingrese el nuevo stock: ").strip()),
        )
        guardar_productos()
        print("Producto actualizado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto_desde_consola() -> None:
    """Solicita el código y elimina un producto."""
    try:
        codigo = input("Ingrese el código del producto a eliminar: ").strip()
        restaurante.eliminar_producto(codigo)
        guardar_productos()
        print("Producto eliminado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def listar_productos_desde_consola() -> None:
    """Lista todos los productos registrados."""
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        print(producto)


# ==================== USUARIOS ====================

def registrar_usuario_desde_consola() -> None:
    """Solicita datos para registrar un nuevo usuario."""
    try:
        usuario = Usuario(
            identificacion=input("Ingrese la identificación del usuario: ").strip(),
            nombre=input("Ingrese el nombre del usuario: ").strip(),
            correo=input("Ingrese el correo del usuario: ").strip(),
        )
        restaurante.registrar_usuario(usuario)
        guardar_usuarios()
        print("Usuario registrado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios_desde_consola() -> None:
    """Lista todos los usuarios registrados."""
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for usuario in usuarios:
        print(usuario)


# ==================== VENTAS ====================

def vender_producto_desde_consola() -> None:
    """Solicita datos para realizar una venta."""
    try:
        identificacion = input("Ingrese la identificación del usuario: ").strip()
        codigo_producto = input("Ingrese el código del producto: ").strip()
        cantidad = int(input("Ingrese la cantidad a vender: ").strip())

        # Validar usuario y producto antes de vender
        usuario = restaurante.buscar_usuario(identificacion)
        producto = restaurante.buscar_producto(codigo_producto)

        if usuario is None:
            print("Error: usuario no encontrado.")
            return

        if producto is None:
            print("Error: producto no encontrado.")
            return

        # Intentar venta
        if restaurante.vender_producto(codigo_producto, identificacion, cantidad):
            guardar_ventas()
            guardar_productos()
            print(
                f"Venta realizada correctamente. "
                f"Stock actual de '{producto.nombre}': {producto.stock}"
            )
        else:
            if cantidad <= 0:
                print("Error: la cantidad debe ser mayor que cero.")
            elif producto.stock < cantidad:
                print(
                    f"Error: stock insuficiente. "
                    f"Disponible: {producto.stock}, Solicitado: {cantidad}"
                )
            else:
                print("Error: no se pudo realizar la venta.")

    except ValueError as error:
        print(f"Error: {error}")


def consultar_ventas_usuario_desde_consola() -> None:
    """Consulta todas las ventas de un usuario."""
    try:
        identificacion = input("Ingrese la identificación del usuario: ").strip()

        usuario = restaurante.buscar_usuario(identificacion)
        if usuario is None:
            print("Error: usuario no encontrado.")
            return

        ventas = restaurante.consultar_ventas_usuario(identificacion)
        if not ventas:
            print(f"El usuario '{usuario.nombre}' no tiene ventas registradas.")
            return

        print(f"\nVentas de {usuario.nombre} ({usuario.identificacion}):")
        for venta in ventas:
            producto = restaurante.buscar_producto(venta.producto_codigo)
            nombre_producto = producto.nombre if producto else "Producto eliminado"
            print(
                f"  - {nombre_producto} (Código: {venta.producto_codigo}), "
                f"Cantidad: {venta.cantidad}"
            )

    except ValueError as error:
        print(f"Error: {error}")


# ==================== OTRAS OPERACIONES ====================

def mostrar_categorias() -> None:
    """Muestra todas las categorías de productos disponibles."""
    categorias = restaurante.obtener_categorias()
    if not categorias:
        print("No hay categorías disponibles.")
        return
    print("Categorías disponibles:")
    for categoria in sorted(categorias):
        print(f"  - {categoria}")


# ==================== MENÚ PRINCIPAL ====================

ACCIONES: dict[str, Callable[[], None]] = {
    "1": registrar_producto_desde_consola,
    "2": buscar_producto_desde_consola,
    "3": actualizar_producto_desde_consola,
    "4": eliminar_producto_desde_consola,
    "5": listar_productos_desde_consola,
    "6": registrar_usuario_desde_consola,
    "7": listar_usuarios_desde_consola,
    "8": vender_producto_desde_consola,
    "9": consultar_ventas_usuario_desde_consola,
    "10": mostrar_categorias,
}


def mostrar_menu() -> None:
    """Muestra el menú principal."""
    print(f"\n{'=' * 50}")
    print(f"Bienvenido a {restaurante.nombre_restaurante}")
    print(f"{'=' * 50}")
    for opcion in OPCIONES_MENU:
        print(opcion)
    print()


def main() -> None:
    """Loop principal de la aplicación."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "11":
            print("¡Gracias por usar el restaurante!")
            break

        accion = ACCIONES.get(opcion)
        if accion:
            print()
            accion()
        else:
            print("Error: opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
