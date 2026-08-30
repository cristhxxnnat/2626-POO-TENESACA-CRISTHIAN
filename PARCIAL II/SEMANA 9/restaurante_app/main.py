from typing import Callable

from restaurante_app.modelos.cliente import Cliente
from restaurante_app.modelos.producto import Producto
from restaurante_app.servicios.restaurante import Restaurante

restaurante = Restaurante("La Mesa de Cristi")

OPCIONES_MENU: tuple[str, ...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar cliente",
    "7. Listar clientes",
    "8. Mostrar categorías",
    "9. Salir",
)


def registrar_producto_desde_consola() -> None:
    try:
        codigo = input("Ingrese el código del producto: ").strip()
        nombre = input("Ingrese el nombre del producto: ").strip()
        categoria = input("Ingrese la categoría del producto: ").strip()
        precio = float(input("Ingrese el precio del producto: ").strip())

        producto = Producto(codigo=codigo, nombre=nombre, categoria=categoria, precio=precio)
        restaurante.registrar_producto(producto)
        print("Producto registrado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def buscar_producto_desde_consola() -> None:
    try:
        codigo = input("Ingrese el código del producto a buscar: ").strip()
        producto = restaurante.buscar_producto(codigo)
        if producto is None:
            print("Producto no encontrado.")
        else:
            print(producto)
    except ValueError as error:
        print(f"Error: {error}")


def actualizar_producto_desde_consola() -> None:
    try:
        codigo = input("Ingrese el código del producto a actualizar: ").strip()
        nombre = input("Ingrese el nuevo nombre: ").strip()
        categoria = input("Ingrese la nueva categoría: ").strip()
        precio = float(input("Ingrese el nuevo precio: ").strip())

        restaurante.actualizar_producto(codigo, nombre, categoria, precio)
        print("Producto actualizado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def eliminar_producto_desde_consola() -> None:
    try:
        codigo = input("Ingrese el código del producto a eliminar: ").strip()
        restaurante.eliminar_producto(codigo)
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


def registrar_cliente_desde_consola() -> None:
    try:
        identificacion = input("Ingrese la identificación del cliente: ").strip()
        nombre = input("Ingrese el nombre del cliente: ").strip()
        correo = input("Ingrese el correo del cliente: ").strip()

        cliente = Cliente(identificacion=identificacion, nombre=nombre, correo=correo)
        restaurante.registrar_cliente(cliente)
        print("Cliente registrado correctamente.")
    except ValueError as error:
        print(f"Error: {error}")


def listar_clientes_desde_consola() -> None:
    clientes = restaurante.listar_clientes()
    if not clientes:
        print("No hay clientes registrados.")
        return

    for cliente in clientes:
        print(cliente)


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
    6: registrar_cliente_desde_consola,
    7: listar_clientes_desde_consola,
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
