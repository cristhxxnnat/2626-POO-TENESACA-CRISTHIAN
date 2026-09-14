# Semana 13 - Restaurante App con Tkinter

Esta carpeta contiene una base gráfica del proyecto `restaurante_app` adaptada a la Semana 13 de Programación Orientada a Objetos.

## Objetivo

Desarrollar una primera versión de la aplicación con interfaz gráfica utilizando `Tkinter`, manteniendo la organización por capas:

- `modelos/` para las entidades del dominio (`Producto`, `Usuario`)
- `servicios/` para la lectura de archivos JSON y la lógica del restaurante
- `ui/` para las vistas `LoginView` y `MainView`
- `main.py` como punto de entrada único de la aplicación

## Estructura

```text
restaurante_app/
├── datos/
│   ├── productos.json
│   └── usuarios.json
├── modelos/
│   ├── __init__.py
│   ├── producto.py
│   └── usuario.py
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py
│   └── restaurante_servicio.py
├── ui/
│   ├── __init__.py
│   ├── login_view.py
│   └── main_view.py
├── main.py
├── README.md
└── __init__.py
```

## Flujo de la aplicación

1. Se inicia `main.py`.
2. Se muestra la pantalla de acceso (`LoginView`).
3. El usuario ingresa su identificación y contraseña.
4. `RestauranteServicio` valida las credenciales con los usuarios cargados desde `usuarios.json`.
5. Si la validación es correcta, aparece la interfaz principal (`MainView`).
6. Desde la vista principal se pueden consultar los productos y usuarios registrados.
7. La opción de ventas queda marcada como pendiente para próximas semanas.

## Ejecución

Desde la carpeta `SEMANA 13`, ejecute:

```bash
python restaurante_app/main.py
```

## Verificación mínima

- La aplicación inicia sin errores.
- Se muestra primero la vista de inicio de sesión.
- Las credenciales válidas permiten acceder a la vista principal.
- Las opciones `Productos` y `Usuarios` consultan la información desde el servicio, no desde archivos JSON directamente.
- La opción `Cerrar sesión` regresa a la pantalla de login dentro de la misma ventana principal.

## Credenciales de ejemplo

- Usuario: `admin`
- Contraseña: `1234`
