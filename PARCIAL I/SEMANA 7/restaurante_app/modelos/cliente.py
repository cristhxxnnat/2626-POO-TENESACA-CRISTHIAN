from dataclasses import dataclass


@dataclass
class Cliente:
    """Representa un cliente registrado en el restaurante."""

    nombre: str
    correo: str
    id_cliente: int
