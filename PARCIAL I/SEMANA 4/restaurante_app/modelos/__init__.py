# Módulo: __init__.py para la carpeta modelos
# Este archivo permite importar las clases desde el paquete modelos

from .producto import Producto
from .cliente import Cliente

__all__ = ['Producto', 'Cliente']
