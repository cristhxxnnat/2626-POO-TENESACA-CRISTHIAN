1
# Sistema de Restaurante con POO en Python

Estudiante: Cristian Tenesaca

## Descripción del sistema
Este proyecto implementa un sistema básico de gestión de restaurante usando Programación Orientada a Objetos en Python. Permite registrar, listar y buscar productos y clientes desde un menú interactivo ejecutado en consola.

## Estructura del proyecto
- modelos/producto.py: contiene la clase Producto, implementada con constructor tradicional y propiedades para controlar el acceso a sus atributos.
- modelos/cliente.py: contiene la clase Cliente, implementada con el decorador @dataclass.
- servicios/restaurante.py: contiene la clase Restaurante, encargada de administrar las listas de productos y clientes.
- main.py: punto de entrada del programa y menú interactivo.

## Uso de constructores y decoradores
- La clase Producto usa el constructor __init__ para crear objetos desde datos ingresados por consola.
- Se utilizan @property y @setter para validar y controlar los atributos nombre, categoría y precio.
- La clase Cliente usa @dataclass para definir de forma simple sus atributos.

## Menú interactivo
El programa muestra un menú con opciones para:
1. Registrar producto
2. Listar productos
3. Buscar producto
4. Registrar cliente
5. Listar clientes
6. Buscar cliente
7. Salir

## Reflexión
Crear objetos a partir de datos ingresados por el usuario permite organizar mejor la información y representar entidades del mundo real de forma clara dentro de un sistema orientado a objetos.
