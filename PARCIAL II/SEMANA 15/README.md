# Semana 15 - Restaurante App

Esta versión de la aplicación continúa el desarrollo del proyecto de restaurante y agrega la nueva funcionalidad de ventas siguiendo el enfoque de manejo de eventos en Tkinter.

## Objetivo de la semana

Se conserva la arquitectura modular del proyecto sin reconstruir todo desde cero. La intención es mostrar cómo una acción del usuario, a través de un `command=` y un callback, dispara una operación coordinada que delega la lógica al servicio y luego actualiza la interfaz con la respuesta del sistema.

## Evolución sobre la versión anterior

Se mantiene el flujo base de:

- inicio de sesión
- navegación por pestañas
- gestión de productos
- consulta de usuarios
- persistencia en JSON

Además, se incorpora la nueva sección de ventas que conecta un usuario y un producto para registrar una venta con validaciones en el servicio.

## Arquitectura

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   ├── usuarios.json
│   └── ventas.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   ├── usuario.py
│   └── venta.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── assets/
├── main.py
├── README.md
└── __init__.py
```

## Nueva funcionalidad de ventas

La sección de ventas permite:

- seleccionar un usuario registrado
- seleccionar un producto registrado
- definir la cantidad
- presionar el botón "Registrar venta"
- ejecutar el callback desde `command=`
- delegar la validación y la lógica del negocio a `RestauranteServicio`
- guardar la venta en `ventas.json`
- actualizar la tabla visual con la nueva información

## Flujo funcional

```text
Usuario
  ↓
Botón / componente
  ↓
command= callback
  ↓
RestauranteServicio
  ↓
Persistencia en ventas.json
  ↓
Actualización de la vista
```

## Ejecución

Desde la carpeta de la semana 15:

```bash
python restaurante_app/main.py
```

## Notas

- La lógica de validación y reglas de negocio queda en el servicio.
- La interfaz no escribe directamente los archivos JSON.
- El modelo `Venta` representa la relación entre usuario, producto y fecha.
- La carpeta `assets/` queda preparada para incorporar logotipo e íconos de la aplicación.
