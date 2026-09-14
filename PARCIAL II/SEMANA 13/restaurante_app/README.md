# restaurante_app

Aplicación base del restaurante con interfaz gráfica en Tkinter.

## Propósito

Esta versión inicial del proyecto separa las responsabilidades en capas para facilitar la transición desde la consola a una aplicación de escritorio con ventanas. La lógica de negocio se mantiene en `servicios/`, las entidades en `modelos/`, la interfaz gráfica en `ui/`, y `main.py` prepara y conecta los elementos de la aplicación.

## Componentes principales

- `datos/productos.json`: productos cargados al iniciar la aplicación.
- `datos/usuarios.json`: usuarios disponibles para una simulación de acceso.
- `modelos/producto.py`: representación del producto del restaurante.
- `modelos/usuario.py`: representación del usuario con credenciales simuladas.
- `servicios/archivo_servicio.py`: lectura y validación de archivos JSON.
- `servicios/restaurante_servicio.py`: acceso a datos, validación y consultas del restaurante.
- `ui/login_view.py`: pantalla de acceso.
- `ui/main_view.py`: vista principal con opciones de consulta.

## Ejecución

```bash
python restaurante_app/main.py
```

## Credenciales de ejemplo

- Identificación: `admin`
- Contraseña: `1234`
