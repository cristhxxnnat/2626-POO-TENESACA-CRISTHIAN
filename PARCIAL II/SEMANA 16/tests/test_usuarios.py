import json

import pytest

from restaurante_app.modelos.usuario import Usuario
from restaurante_app.servicios.archivo_servicio import ArchivoServicio
from restaurante_app.servicios.restaurante_servicio import RestauranteServicio


def crear_servicio(tmp_path):
    archivos = ArchivoServicio(
        tmp_path / "productos.json",
        tmp_path / "usuarios.json",
        tmp_path / "ventas.json",
    )
    servicio = RestauranteServicio(guardar_usuarios=archivos.guardar_usuarios)
    servicio.cargar_usuarios(
        [
            Usuario("admin", "Administradora", "admin@restaurante.com", "1234", "Administrador"),
            Usuario("empleado1", "Ana García", "ana@restaurante.com", "5678", "Empleado"),
        ]
    )
    return servicio, archivos


def test_crud_usuarios_persiste_roles_y_conserva_password(tmp_path):
    servicio, archivos = crear_servicio(tmp_path)

    cliente = Usuario("cliente1", "Luis Pérez", "luis@restaurante.com", "clave", "Cliente")
    servicio.registrar_usuario(cliente, "admin")
    usuario_actualizado = servicio.actualizar_usuario(
        "cliente1", "admin", "Luis P.", "luis@restaurante.com", "", "Empleado"
    )

    assert usuario_actualizado is not None
    assert usuario_actualizado.nombre == "Luis P."
    assert usuario_actualizado.password == "clave"
    assert usuario_actualizado.rol == "Empleado"
    assert servicio.eliminar_usuario("cliente1", "admin") is usuario_actualizado

    datos = json.loads(archivos.ruta_usuarios.read_text(encoding="utf-8"))
    assert all(registro["identificacion"] != "cliente1" for registro in datos)
    assert next(registro for registro in datos if registro["identificacion"] == "admin")["rol"] == "Administrador"


def test_solo_admin_gestiona_usuarios_y_no_puede_eliminarse(tmp_path):
    servicio, _ = crear_servicio(tmp_path)

    with pytest.raises(ValueError, match="Solo un Administrador"):
        servicio.registrar_usuario(
            Usuario("cliente1", "Luis Pérez", "luis@restaurante.com", "clave", "Cliente"),
            "empleado1",
        )
    with pytest.raises(ValueError, match="No puede eliminar la cuenta Administrador"):
        servicio.eliminar_usuario("admin", "admin")
    with pytest.raises(ValueError, match="solo permite asignar Empleado o Cliente"):
        servicio.actualizar_usuario("empleado1", "admin", "Ana", "ana@restaurante.com", "", "Administrador")


def test_json_legacy_asigna_roles_compatibles():
    administrador = Usuario.desde_dict(
        {"identificacion": "admin", "nombre": "Admin", "correo": "admin@example.com", "password": "1234"}
    )
    usuario_legacy = Usuario.desde_dict(
        {"identificacion": "u001", "nombre": "Cliente", "correo": "u@example.com", "password": "1234"}
    )

    assert administrador.rol == "Administrador"
    assert usuario_legacy.rol == "Cliente"
