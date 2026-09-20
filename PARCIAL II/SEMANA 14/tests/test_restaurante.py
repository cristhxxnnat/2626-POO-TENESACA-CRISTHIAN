from __future__ import annotations

from restaurante_app.modelos.producto import Producto
from restaurante_app.servicios.restaurante_servicio import RestauranteServicio


def test_registrar_y_buscar_producto() -> None:
    servicio = RestauranteServicio("La Mesa de Cristi")

    producto = Producto("P001", "Café", "Bebidas", 5000, 10)
    servicio.registrar_producto(producto)

    encontrado = servicio.buscar_producto("p001")
    assert encontrado is not None
    assert encontrado.nombre == "Café"
    assert servicio.obtener_total_productos() == 1


def test_actualizar_y_eliminar_producto() -> None:
    servicio = RestauranteServicio("La Mesa de Cristi")
    servicio.registrar_producto(Producto("P002", "Sopa", "Platos", 12000, 5))

    actualizado = servicio.actualizar_producto("P002", nombre="Sopa especial", precio=14000, stock=7)
    assert actualizado is not None
    assert actualizado.nombre == "Sopa especial"
    assert actualizado.precio == 14000
    assert actualizado.stock == 7

    eliminado = servicio.eliminar_producto("P002")
    assert eliminado is not None
    assert servicio.obtener_total_productos() == 0


def test_validar_acceso_usuario() -> None:
    servicio = RestauranteServicio("La Mesa de Cristi")
    servicio.cargar_usuarios([
        __import__("restaurante_app.modelos.usuario", fromlist=["Usuario"]).Usuario("admin", "Administrador", "admin@restaurante.com", "1234")
    ])

    assert servicio.validar_acceso("admin", "1234") is True
    assert servicio.validar_acceso("admin", "0000") is False
