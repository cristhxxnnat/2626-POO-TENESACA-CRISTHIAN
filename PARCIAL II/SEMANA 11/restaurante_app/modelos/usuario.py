from __future__ import annotations

from typing import Any


class Usuario:
    """Representa un usuario registrado en el restaurante con persistencia JSON."""

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self.identificacion: str = identificacion
        self.nombre: str = nombre
        self.correo: str = correo

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @identificacion.setter
    def identificacion(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("La identificación del usuario no puede estar vacía.")
        self._identificacion = valor.strip()

    @property
    def nombre(self) -> str:
        return self._nombre

    @nombre.setter
    def nombre(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El nombre del usuario no puede estar vacío.")
        self._nombre = valor.strip()

    @property
    def correo(self) -> str:
        return self._correo

    @correo.setter
    def correo(self, valor: str) -> None:
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El correo del usuario no puede estar vacío.")
        self._correo = valor.strip()

    def a_dict(self) -> dict[str, object]:
        """Convierte el objeto a una estructura compatible con JSON."""
        return {
            "identificacion": self.identificacion,
            "nombre": self.nombre,
            "correo": self.correo,
        }

    @classmethod
    def desde_dict(cls, datos: dict[str, Any]) -> Usuario:
        """Reconstruye un Usuario y deja que sus validaciones actúen."""
        try:
            return cls(
                identificacion=datos["identificacion"],
                nombre=datos["nombre"],
                correo=datos["correo"],
            )
        except KeyError as error:
            raise KeyError(f"Falta la clave requerida en el registro: {error}") from error

    def __str__(self) -> str:
        return (
            f"Usuario(identificacion={self.identificacion}, nombre={self.nombre}, "
            f"correo={self.correo})"
        )

    def __repr__(self) -> str:
        return self.__str__()
