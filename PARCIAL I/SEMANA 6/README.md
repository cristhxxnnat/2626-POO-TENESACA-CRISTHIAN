# Sistema de Restaurante en Python

Estudiante: Cristian Tenesaca

## Descripción
Este proyecto implementa un sistema de restaurante utilizando Programación Orientada a Objetos en Python. Se modelan productos del restaurante mediante una jerarquía de herencia con las clases Producto, Platillo y Bebida.

## Estructura del proyecto
- modelos/: contiene las clases del dominio del sistema.
- servicios/: contiene la clase Restaurante para administrar los productos.
- main.py: punto de entrada del programa.

## Herencia aplicada
La clase Producto es la clase base, mientras que Platillo y Bebida heredan de ella. Esto permite reutilizar atributos y métodos comunes, además de personalizar el comportamiento en cada clase hija.

## Atributo encapsulado
El atributo precio de la clase Producto está encapsulado mediante doble guion bajo y se accede mediante los métodos obtener_precio() y cambiar_precio().

## Polimorfismo
Se demuestra el polimorfismo al recorrer una lista de productos y ejecutar el método mostrar_informacion() en cada objeto, obteniendo resultados diferentes según si el objeto es un Platillo o una Bebida.

## Reflexión
Aplicar principios de POO en proyectos modulares facilita la organización del código, mejora la reutilización y permite construir sistemas más mantenibles y escalables.
