# Restaurante App - Semana 10

**Estudiante:** Cristhian Tenesaca

## Descripción

Esta versión continúa el proyecto de restaurante de las semanas anteriores. Permite registrar, buscar, actualizar, eliminar y listar productos. La mejora de la Semana 10 es la persistencia de productos mediante `productos.json`: los objetos `Producto` se convierten a diccionarios solo al guardar y se reconstruyen como objetos al iniciar.

Los usuarios se administran únicamente en memoria, porque la persistencia de usuarios no forma parte de esta actividad.

## Estructura

```text
SEMANA 10/
├── README.md
├── iniciar.bat
└── restaurante_app/
    ├── __init__.py
    ├── main.py
    ├── datos/
    │   └── productos.json
    ├── modelos/
    │   ├── __init__.py
    │   ├── producto.py
    │   └── usuario.py
    └── servicios/
        ├── __init__.py
        ├── archivo_servicio.py
        └── restaurante.py
```

## Responsabilidades

- `modelos/producto.py`: contiene `Producto`, sus validaciones, `a_dict()` y `desde_dict()`.
- `modelos/usuario.py`: contiene `Usuario` y sus validaciones; no se guarda en disco.
- `servicios/restaurante.py`: administra las colecciones y las operaciones del restaurante.
- `servicios/archivo_servicio.py`: lee y escribe exclusivamente `datos/productos.json` usando `with open()`, `json.load()` y `json.dump()`.
- `main.py`: crea los servicios, carga los productos al iniciar, coordina el menú y solicita el guardado después de registrar, actualizar o eliminar.
- `datos/productos.json`: contiene una lista de diccionarios con los datos persistidos.

## Flujo de persistencia

Al iniciar, `main.py` crea `ArchivoServicio`, lee el JSON y valida cada registro. Cada registro correcto se transforma en un objeto `Producto` mediante `Producto.desde_dict()` y se entrega a `Restaurante`.

Cuando una operación modifica la colección, `main.py` solicita a `ArchivoServicio` guardar la lista de objetos. El archivo se sobrescribe con `json.dump()` usando UTF-8 e indentación legible.

## Excepciones controladas

- `FileNotFoundError`: el primer inicio continúa con una lista vacía.
- `json.JSONDecodeError`: un archivo con formato inválido produce una advertencia y una lista vacía.
- `PermissionError`: se informa el problema de lectura o escritura sin cerrar abruptamente el menú.
- `KeyError`, `TypeError` y `ValueError`: un registro incompleto o inválido se omite y los demás registros continúan cargándose.
- `ValueError`: también controla datos inválidos ingresados por consola y las validaciones de `Producto`.

No se utiliza `except: pass` ni capturas genéricas para ocultar errores.

## Ejecución

Desde la carpeta `SEMANA 10`:

```bash
python -m restaurante_app.main
```

También puede ejecutarse `iniciar.bat` en Windows.

## Comprobación de persistencia

1. Se inició `main.py` y se registró un producto desde el menú.
2. Se verificó que `datos/productos.json` contuviera una lista con sus datos.
3. Se cerró el programa y se ejecutó nuevamente.
4. La opción de listar mostró el producto recuperado como objeto `Producto`.
5. Se actualizó y se eliminó el producto desde el menú, verificando en cada caso el contenido del JSON.
6. Tras reiniciar nuevamente, el cambio permaneció guardado.
