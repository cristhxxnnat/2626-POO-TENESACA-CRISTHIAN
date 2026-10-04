from restaurante_app.modelos.producto import Producto
from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.restaurante_servicio import RestauranteServicio


def test_registrar_venta_actualiza_stock_y_listado() -> None:
    servicio = RestauranteServicio("La Mesa de Cristi")
    usuario = Usuario("u001", "Ana García", "ana@restaurante.com", "1234")
    producto = Producto("P001", "Pizza Margarita", "Pizzas", 12000, 5)

    servicio.cargar_usuarios([usuario])
    servicio.cargar_productos([producto])

    venta = servicio.registrar_venta("u001", "P001", cantidad=2)

    assert len(servicio.listar_ventas()) == 1
    assert venta.usuario_id == "u001"
    assert venta.producto_codigo == "P001"
    assert producto.stock == 3
    assert servicio.consultar_ventas_usuario("u001")[0].usuario_id == "u001"
