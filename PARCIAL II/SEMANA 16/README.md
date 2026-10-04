# Semana 16: Restaurante App

La aplicación continúa el proyecto de semanas anteriores. Conserva el inicio de sesión, navegación, gestión de productos y ventas, y amplía la sección de usuarios para practicar eventos de Tkinter con un formulario y una tabla `ttk.Treeview`.

## Evolución y arquitectura

La capa visual coordina los eventos y muestra respuestas. `RestauranteServicio` valida permisos y reglas del CRUD; `ArchivoServicio` guarda y carga los datos JSON.

```text
restaurante_app/
├── assets/                 # Logo e icono
├── datos/                  # productos.json, usuarios.json, ventas.json
├── modelos/                # Producto, Usuario y Venta
├── servicios/              # Reglas del restaurante y archivos JSON
├── ui/                     # LoginView y MainView
└── main.py
tests/
```

## Gestión de usuarios

El administrador puede registrar, consultar, actualizar y eliminar cuentas de tipo `Empleado` y `Cliente`. La pestaña administrativa no está disponible para Empleados ni Clientes. El servicio vuelve a validar el rol antes de cada operación y protege la cuenta Administrador autenticada contra eliminación. Al actualizar, una contraseña vacía conserva la existente.

El Treeview muestra identificador, nombre, correo/usuario y rol; nunca incluye la contraseña. `<<TreeviewSelect>>` obtiene el identificador de la fila y un callback consulta el objeto mediante `RestauranteServicio` para cargarlo en el formulario. El selector de rol responde a `<<ComboboxSelected>>`. `Return` reutiliza el callback de registro y `Escape` limpia el formulario y la selección.

Los botones de acción utilizan `command=`. Los eventos de selección, teclado y cambio de rol utilizan `bind()` porque reciben un evento de Tkinter. En ambos casos, los callbacks delegan las reglas y la persistencia al servicio.

## Persistencia

Los usuarios se guardan en `restaurante_app/datos/usuarios.json`, incluyendo su rol. Los registros anteriores sin rol siguen siendo legibles: el identificador `admin` se interpreta como `Administrador` y los demás como `Cliente`. Los archivos de productos y ventas mantienen el formato de la versión anterior.

## Ejecución

Requisitos: Python 3.10 o posterior con Tkinter disponible.

Desde la carpeta `PARCIAL II/SEMANA 16`:

```bash
python restaurante_app/main.py
```

Cuenta inicial de demostración: usuario `admin`, contraseña `1234`. También está disponible `empleado1` con contraseña `5678` para comprobar que no ve la pestaña Usuarios.

Para ejecutar las pruebas, con `pytest` instalado:

```bash
python -m pytest tests -q
```
