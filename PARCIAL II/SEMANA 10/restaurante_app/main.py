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


RUTA_PRODUCTOS: Path = Path(__file__).resolve().parent / "datos" / "productos.json"
restaurante = Restaurante()
archivo_servicio = ArchivoServicio(RUTA_PRODUCTOS)
restaurante.cargar_productos(archivo_servicio.cargar_productos())

OPCIONES_MENU: tuple[str, ...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías",
    "9. Salir",
)


def guardar_productos() -> None:
    if archivo_servicio.guardar_productos(restaurante.listar_productos()):
        print("Archivo de productos actualizado.")


def registrar_producto_desde_consola() -> None:
    try:
        producto = Producto(
            codigo=input("Ingrese el código del producto: ").strip(),
            nombre=input("Ingrese el nombre del producto: ").strip(),
            categoria=input("Ingrese la categoría del producto: ").strip(),
            precio=float(input("Ingrese el precio del producto: ").strip()),
        )
        restaurante.registrar_producto(producto)
        guardar_productos()
        print("Producto registrado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def buscar_producto_desde_consola() -> None:
    codigo = input("Ingrese el código del producto a buscar: ").strip()
    producto = restaurante.buscar_producto(codigo)
    print(producto if producto is not None else "Producto no encontrado.")


def actualizar_producto_desde_consola() -> None:
    try:
        codigo = input("Ingrese el código del producto a actualizar: ").strip()
        restaurante.actualizar_producto(
            codigo=codigo,
            nuevo_nombre=input("Ingrese el nuevo nombre: ").strip(),
            nueva_categoria=input("Ingrese la nueva categoría: ").strip(),
            nuevo_precio=float(input("Ingrese el nuevo precio: ").strip()),
        )
        guardar_productos()
        print("Producto actualizado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto_desde_consola() -> None:
    try:
        codigo = input("Ingrese el código del producto a eliminar: ").strip()
        restaurante.eliminar_producto(codigo)
        guardar_productos()
        print("Producto eliminado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def listar_productos_desde_consola() -> None:
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for producto in productos:
        print(producto)


def registrar_usuario_desde_consola() -> None:
    try:
        usuario = Usuario(
            identificacion=input("Ingrese la identificación del usuario: ").strip(),
            nombre=input("Ingrese el nombre del usuario: ").strip(),
            correo=input("Ingrese el correo del usuario: ").strip(),
        )
        restaurante.registrar_usuario(usuario)
        print("Usuario registrado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def listar_usuarios_desde_consola() -> None:
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for usuario in usuarios:
        print(usuario)


def mostrar_categorias_desde_consola() -> None:
    categorias = restaurante.obtener_categorias()
    if not categorias:
        print("No hay categorías registradas.")
        return
    print("Categorías únicas:")
    for categoria in sorted(categorias):
        print(f"- {categoria}")


FUNCIONES_MENU: dict[int, Callable[[], None]] = {
    1: registrar_producto_desde_consola,
    2: buscar_producto_desde_consola,
    3: actualizar_producto_desde_consola,
    4: eliminar_producto_desde_consola,
    5: listar_productos_desde_consola,
    6: registrar_usuario_desde_consola,
    7: listar_usuarios_desde_consola,
    8: mostrar_categorias_desde_consola,
}


def mostrar_menu() -> None:
    print("=" * 40)
    print("\tSISTEMA DE RESTAURANTE")
    print("=" * 40)
    for opcion in OPCIONES_MENU:
        print(opcion)
    print("-" * 40)


def main() -> None:
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: ").strip())
        except ValueError:
            print("Debe ingresar un número válido.")
            continue

        if opcion == 9:
            print("Gracias por usar el sistema.")
            break
        funcion = FUNCIONES_MENU.get(opcion)
        if funcion is None:
            print("Opción no válida. Intente nuevamente.")
            continue
        funcion()
        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
