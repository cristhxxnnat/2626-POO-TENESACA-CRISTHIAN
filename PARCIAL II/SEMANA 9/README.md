# Restaurante App - Semana 9

Estudiante: Cristhian Tenesaca

## Descripción del sistema
Este proyecto representa la evolución del sistema de restaurante desarrollado en semanas anteriores. El programa permite registrar, buscar, actualizar, eliminar y listar productos y clientes, utilizando colecciones y persistencia en archivos JSON para mantener la información en memoria y en disco.

## Estructura del proyecto

```text
PARCIAL II/
└── SEMANA 9/
    ├── .vscode/
    │   └── launch.json
    ├── iniciar.bat
    ├── README.md
    └── restaurante_app/
        ├── __init__.py
        ├── main.py
        ├── data/
        │   ├── productos.json
        │   └── clientes.json
        ├── modelos/
        │   ├── __init__.py
        │   ├── producto.py
        │   ├── bebida.py
        │   └── cliente.py
        └── servicios/
            ├── __init__.py
            └── restaurante.py
```

## Responsabilidad de cada archivo

- `restaurante_app/__init__.py`: marca el paquete principal del proyecto.
- `restaurante_app/main.py`: punto de entrada del sistema. Muestra el menú, solicita información por consola y delega las operaciones al servicio `Restaurante`.
- `restaurante_app/modelos/producto.py`: define la clase `Producto` con código, nombre, categoría y precio.
- `restaurante_app/modelos/bebida.py`: define la clase `Bebida`, hija de `Producto`, agregando tamaño y tipo de envase.
- `restaurante_app/modelos/cliente.py`: define la clase `Cliente` con identificación, nombre y correo.
- `restaurante_app/servicios/restaurante.py`: administra las listas de productos y clientes, valida duplicados, realiza búsquedas y persiste los datos en JSON.
- `restaurante_app/data/productos.json`: almacena los productos en un diccionario indexado por código.
- `restaurante_app/data/clientes.json`: almacena los clientes en un diccionario indexado por identificación.
- `iniciar.bat`: ejecuta el programa con un doble clic desde Windows.
- `.vscode/launch.json`: permite ejecutar el proyecto desde VS Code con Run and Debug.

## Uso de estructuras de datos

### list
La clase `Restaurante` usa listas para guardar los productos y clientes del sistema. Esto permite registrar, buscar, actualizar, eliminar y listar colecciones dinámicas.

Ejemplo concreto:

```python
self.productos: list[Producto] = []
self.clientes: list[Cliente] = []
```

### tuple
En `main.py` se define una tupla constante con las opciones del menú:

```python
OPCIONES_MENU: tuple[str, ...] = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar cliente",
    "7. Listar clientes",
    "8. Mostrar categorías",
    "9. Salir",
)
```

Esto mantiene el texto del menú fijo durante la ejecución.

### dict
Se usa un diccionario para:

1. mapear cada número del menú con la función que debe ejecutarse.
2. guardar la información persistida en JSON como un diccionario indexado por clave.

Ejemplo:

```python
FUNCIONES_MENU: dict[int, Callable[[], None]] = {
    1: registrar_producto_desde_consola,
    2: buscar_producto_desde_consola,
    3: actualizar_producto_desde_consola,
}
```

Y en el archivo JSON:

```json
{
  "P001": {
    "codigo": "P001",
    "nombre": "Pizza Margarita",
    "categoria": "Plato fuerte",
    "precio": 14.5
  }
}
```

### set
Se usa un conjunto para mostrar categorías únicas sin duplicados:

```python
categorias: set[str] = set()
for producto in self.productos:
    categorias.add(producto.categoria)
```

Esto permite obtener solo una vez cada categoría registrada.

## Cómo ejecutar el programa

### Opción 1: doble clic
Desde la raíz `PARCIAL II/SEMANA 9`, haga doble clic en `iniciar.bat`.

### Opción 2: desde la terminal
Desde la raíz `PARCIAL II/SEMANA 9`, ejecute:

```bash
python -m restaurante_app.main
```

## Reflexión
La elección adecuada de la estructura de datos es un factor clave para construir software claro y mantenible. Una lista permite manejar colecciones dinámicas, una tupla fija valores estables, un diccionario organiza información clave-valor y un conjunto elimina duplicados. Cuando estas estructuras se usan con una intención concreta, el programa resulta más eficiente, legible y fácil de extender.
