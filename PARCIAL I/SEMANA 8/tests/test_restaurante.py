import unittest

from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.bebida import Bebida
from restaurante_app.modelos.cliente import Cliente
from restaurante_app.servicios.restaurante import Restaurante


class RestauranteTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.restaurante = Restaurante("La Mesa de Cristi")

    def test_registrar_y_listar_productos_con_polimorfismo(self) -> None:
        producto = Producto("P001", "Pizza", "Comida", 12000.0)
        bebida = Bebida("B001", "Coca Cola", "Bebidas", 4000.0, "500 ml", "Botella")

        self.restaurante.registrar_producto(producto)
        self.restaurante.registrar_producto(bebida)

        self.assertEqual(len(self.restaurante.productos), 2)
        self.assertEqual(self.restaurante.productos[1].codigo, "B001")

    def test_registrar_clientes_con_identificacion_unica(self) -> None:
        cliente = Cliente("C001", "Ana", "ana@email.com")
        self.restaurante.registrar_cliente(cliente)

        self.assertEqual(len(self.restaurante.clientes), 1)

        with self.assertRaises(ValueError):
            self.restaurante.registrar_cliente(Cliente("C001", "Luis", "luis@email.com"))


if __name__ == "__main__":
    unittest.main()
