# Restaurante App - Semana 8

## Estudiante
Cristhian Tenesaca

## Descripción
Este proyecto implementa un sistema básico de restaurante en Python utilizando Programación Orientada a Objetos. El sistema permite registrar productos, bebidas y clientes, además de listarlos desde un menú interactivo en consola.

## Estructura del proyecto
```text
restaurante_app/
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── bebida.py
│   └── cliente.py
├── servicios/
│   ├── __init__.py
│   └── restaurante.py
└── main.py
```

## Responsabilidad de cada clase
- Producto: representa los datos comunes de un producto y define el método mostrar_informacion().
- Bebida: hereda de Producto y agrega atributos específicos como tamaño y tipo de envase.
- Cliente: representa la información de un cliente registrado.
- Restaurante: administra las colecciones de productos y clientes, así como sus validaciones.
- main.py: coordina la interacción con el usuario mediante un menú en consola.

## Relación entre Producto y Bebida
Bebida hereda de Producto, lo que permite tratar a una bebida como un producto más dentro del sistema sin alterar la lógica general del servicio.

## Principios SOLID aplicados
- SRP (Responsabilidad única): cada clase tiene una responsabilidad concreta.
- OCP (Abierto/Cerrado): la clase Bebida amplía el comportamiento de Producto sin modificar la lógica del servicio.
- LSP (Sustitución de Liskov): una Bebida puede utilizarse donde se espera un Producto sin romper el comportamiento del sistema.

## Instrucciones de ejecución
1. Abra una terminal en la carpeta del proyecto.
2. Ejecute el siguiente comando:
   ```bash
   python main.py
   ```
3. Use el menú para registrar productos, bebidas y clientes.

## Reflexión
Diseñar un proyecto con clases bien separadas facilita su mantenimiento, evita errores y permite crecer el sistema sin reescribir todo el código.
