from modelos.cliente import Cliente
from modelos.producto import Producto
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("=" * 40)
    print("SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Listar productos")
    print("3. Buscar producto")
    print("4. Registrar cliente")
    print("5. Listar clientes")
    print("6. Buscar cliente")
    print("7. Salir")
    print("-" * 40)


def main() -> None:
    restaurante = Restaurante("El Buen Sabor")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                nombre = input("Nombre del producto: ")
                categoria = input("Categoría del producto: ")
                precio = float(input("Precio del producto: "))
                disponible = input("¿Está disponible? (s/n): ").strip().lower() == "s"

                producto = Producto(nombre=nombre, categoria=categoria, precio=precio, disponible=disponible)
                restaurante.registrar_producto(producto)
                print("Producto registrado correctamente.")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "2":
            restaurante.listar_productos()

        elif opcion == "3":
            nombre_buscar = input("Ingrese el nombre del producto a buscar: ")
            producto_encontrado = restaurante.buscar_producto(nombre_buscar)
            if producto_encontrado:
                producto_encontrado.mostrar_informacion()
            else:
                print("Producto no encontrado.")

        elif opcion == "4":
            try:
                nombre = input("Nombre del cliente: ")
                correo = input("Correo del cliente: ")
                id_cliente = int(input("ID del cliente: "))

                cliente = Cliente(nombre=nombre, correo=correo, id_cliente=id_cliente)
                restaurante.registrar_cliente(cliente)
                print("Cliente registrado correctamente.")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "5":
            restaurante.listar_clientes()

        elif opcion == "6":
            nombre_buscar = input("Ingrese el nombre del cliente a buscar: ")
            cliente_encontrado = restaurante.buscar_cliente(nombre_buscar)
            if cliente_encontrado:
                print(f"ID: {cliente_encontrado.id_cliente} | Nombre: {cliente_encontrado.nombre} | Correo: {cliente_encontrado.correo}")
            else:
                print("Cliente no encontrado.")

        elif opcion == "7":
            print("Gracias por usar el sistema de restaurante.")
            break

        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()
