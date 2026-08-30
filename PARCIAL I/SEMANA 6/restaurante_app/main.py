from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def main():
    """Punto de entrada del sistema de restaurante."""
    restaurante = Restaurante("El Buen Sabor")

    # Crear platillos
    platillo_1 = Platillo("Lomo saltado", 18.50, 650, "Plato principal", 25, True)
    platillo_2 = Platillo("Aji de gallina", 16.00, 590, "Plato principal", 20, True)

    # Crear bebidas
    bebida_1 = Bebida("Jugo de naranja", 4.50, 350, "Natural", True)
    bebida_2 = Bebida("Gaseosa personal", 3.50, 500, "Refrescante", True)

    # Agregar productos al restaurante
    restaurante.agregar_producto(platillo_1)
    restaurante.agregar_producto(platillo_2)
    restaurante.agregar_producto(bebida_1)
    restaurante.agregar_producto(bebida_2)

    # Mostrar información registrada
    restaurante.mostrar_productos()

    # Demostrar validación del precio
    print("\nValidación de precio:")
    try:
        platillo_1.cambiar_precio(0)
    except ValueError as error:
        print(f"Error: {error}")

    print(f"Precio actual de {platillo_1.nombre}: ${platillo_1.obtener_precio():.2f}")

    # Demostrar polimorfismo
    print("\nPolimorfismo en acción:")
    for producto in restaurante.productos:
        print(producto.mostrar_informacion())


if __name__ == "__main__":
    main()
