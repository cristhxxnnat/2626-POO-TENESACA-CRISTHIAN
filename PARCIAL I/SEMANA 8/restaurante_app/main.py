from restaurante_app.modelos.bebida import Bebida
from restaurante_app.modelos.cliente import Cliente
from restaurante_app.modelos.producto import Producto
from restaurante_app.servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    print("=" * 40)
    print("\tSISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("4. Listar productos")
    print("5. Listar clientes")
    print("6. Salir")
    print("-" * 40)


def main() -> None:
    restaurante = Restaurante("La Mesa de Cristi")

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            try:
                codigo = input("Código del producto: ").strip()
                nombre = input("Nombre del producto: ").strip()
                categoria = input("Categoría: ").strip()
                precio = float(input("Precio: ").strip())
                producto = Producto(codigo, nombre, categoria, precio)
                restaurante.registrar_producto(producto)
                print("Producto registrado correctamente.")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "2":
            try:
                codigo = input("Código de la bebida: ").strip()
                nombre = input("Nombre de la bebida: ").strip()
                categoria = input("Categoría: ").strip()
                precio = float(input("Precio: ").strip())
                tamaño = input("Tamaño: ").strip()
                tipo_envase = input("Tipo de envase: ").strip()
                bebida = Bebida(codigo, nombre, categoria, precio, tamaño, tipo_envase)
                restaurante.registrar_producto(bebida)
                print("Bebida registrada correctamente.")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "3":
            try:
                identificacion = input("Identificación del cliente: ").strip()
                nombre = input("Nombre del cliente: ").strip()
                correo = input("Correo del cliente: ").strip()
                cliente = Cliente(identificacion, nombre, correo)
                restaurante.registrar_cliente(cliente)
                print("Cliente registrado correctamente.")
            except ValueError as error:
                print(f"Error: {error}")

        elif opcion == "4":
            restaurante.listar_productos()

        elif opcion == "5":
            restaurante.listar_clientes()

        elif opcion == "6":
            print("Gracias por usar el sistema.")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

        input("\nPresione Enter para continuar...")


if __name__ == "__main__":
    main()
