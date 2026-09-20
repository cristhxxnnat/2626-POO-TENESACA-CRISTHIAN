# Semana 14 - Componentes y contenedores con Tkinter

## Objetivo

En esta semana se evoluciona la aplicación `restaurante_app` incorporando una interfaz gráfica más organizada mediante componentes y contenedores de `Tkinter`, manteniendo la arquitectura modular y la persistencia en JSON.

## Estructura del proyecto

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
├── __init__.py
├── main.py
└── README.md
```

## Mejoras realizadas

- Se conserva el flujo de acceso con `LoginView`.
- La vista principal se organiza en contenedores para diferenciar visualmente la navegación, los formularios y la consulta de datos.
- Se incorpora un formulario estructurado para registrar, buscar, actualizar y eliminar productos.
- La información de usuarios sigue consultándose desde la capa de servicio.
- Las validaciones y reglas del negocio permanecen en `RestauranteServicio` y no se resuelven directamente desde botones.
- Los cambios en productos se persisten en `productos.json` mediante el servicio de archivos.

## Componentes y contenedores utilizados

- `tk.Frame` para estructurar la interfaz en áreas.
- `ttk.Notebook` para separar las secciones de `Productos` y `Usuarios`.
- `LabelFrame` para agrupar formularios y tablas.
- `Entry` para capturar datos del producto.
- `Button` para las acciones de registrar, buscar, actualizar y eliminar.
- `Treeview` para mostrar productos y usuarios en formato tabular.

## Operaciones sobre productos

La vista principal permite:

1. Registrar un producto nuevo.
2. Buscar un producto por su código.
3. Actualizar la información del producto.
4. Eliminar un producto registrado.

Todas las operaciones se delegan a `RestauranteServicio`, y al finalizar se actualiza la vista para reflejar el resultado.

## Persistencia

La persistencia se mantiene en archivos JSON usando `ArchivoServicio`:

- `datos/productos.json`
- `datos/usuarios.json`

## Ejecución

Desde la carpeta `SEMANA 14` ejecute:

```bash
python restaurante_app/main.py
```

## Credenciales de ejemplo

- Usuario: `admin`
- Contraseña: `1234`

## Verificación propuesta

- La aplicación inicia sin errores.
- El acceso con credenciales válidas continua funcionando.
- La vista principal muestra la información de productos y usuarios.
- El CRUD de productos funciona en la interfaz gráfica y persiste en el archivo JSON.
