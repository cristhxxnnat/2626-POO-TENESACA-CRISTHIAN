# Restaurante App - Semana 11

## Estudiante
**Cristhian Tenesaca**

## Descripción del Sistema

La presente aplicación corresponde a la **Semana 11** de la asignatura Programación Orientada a Objetos. Es una evolución del proyecto `restaurante_app` que incorpora un sistema de ventas relacional entre usuarios y productos, con persistencia JSON de todas las colecciones principales.

El sistema permite:
- Registrar y gestionar productos con control de stock
- Registrar usuarios del restaurante
- Realizar ventas relacionando usuarios con productos
- Consultar el historial de ventas por usuario
- Persistir datos en archivos JSON (productos, usuarios, ventas)
- Recuperar automáticamente la información al reiniciar la aplicación

## Estructura del Proyecto

```
restaurante_app/
├── datos/
│   ├── productos.json        # Persistencia de productos con stock
│   ├── usuarios.json         # Persistencia de usuarios registrados
│   └── ventas.json           # Persistencia de relaciones usuario-producto
├── modelos/
│   ├── __init__.py
│   ├── producto.py           # Clase Producto con stock y validaciones
│   ├── usuario.py            # Clase Usuario con persistencia JSON
│   └── venta.py              # Clase Venta (relación usuario-producto)
├── servicios/
│   ├── __init__.py
│   ├── archivo_servicio.py   # Lectura/escritura de productos, usuarios, ventas
│   └── restaurante.py        # Lógica de negocio y administración de colecciones
├── main.py                   # Punto de entrada con menú interactivo
└── README.md                 # Este archivo
```

## Responsabilidad de Cada Componente

### `modelos/producto.py`
- Representa un producto del restaurante
- Atributos: código, nombre, categoría, precio, stock
- Métodos: `vender(cantidad)`, `a_dict()`, `desde_dict(datos)` (JSON)
- Validaciones: código y nombre no vacíos, precio > 0, stock ≥ 0, stock nunca negativo

### `modelos/usuario.py`
- Representa un usuario registrado
- Atributos: identificación, nombre, correo
- Métodos: `a_dict()`, `desde_dict(datos)` (JSON)
- Validaciones: identificación, nombre y correo no vacíos
- Permite persistencia en usuarios.json

### `modelos/venta.py`
- Representa una relación entre usuario y producto vendido
- Atributos: usuario_id, producto_codigo, cantidad
- Métodos: `a_dict()`, `desde_dict(datos)` (JSON)
- Registra cada transacción de compra
- Validaciones: IDs no vacíos, cantidad > 0

### `servicios/archivo_servicio.py`
- Centraliza la lectura y escritura de archivos JSON
- Métodos: `cargar_productos()`, `guardar_productos()`
- Métodos: `cargar_usuarios()`, `guardar_usuarios()`
- Métodos: `cargar_ventas()`, `guardar_ventas()`
- Manejo de excepciones:
  - `FileNotFoundError`: Inicia con colecciones vacías
  - `json.JSONDecodeError`: Advierte sobre JSON inválido
  - `PermissionError`: Notifica falta de permisos

### `servicios/restaurante.py`
- Administra las colecciones de productos, usuarios y ventas
- Métodos de gestión de productos (registrar, buscar, actualizar, eliminar, listar)
- Métodos de gestión de usuarios (registrar, buscar, listar)
- **Nueva operación**: `vender_producto(codigo_producto, identificacion_usuario, cantidad)`
- **Nueva consulta**: `consultar_ventas_usuario(identificacion_usuario)`
- Lógica de validación centralizada

### `main.py`
- Punto de entrada de la aplicación
- Menú interactivo con 11 opciones
- Carga automática de datos al iniciar
- Gestiona la persistencia llamando al `ArchivoServicio` después de cada operación
- No modifica directamente las colecciones internas del servicio

## Funcionamiento del Stock

Cada producto mantiene una cantidad disponible (`stock`). La venta solo se realiza cuando:
1. El usuario existe
2. El producto existe
3. La cantidad solicitada > 0
4. Stock disponible ≥ cantidad solicitada

**Después de una venta válida:**
- Se crea un objeto `Venta` con los datos de la transacción
- La `Venta` se agrega a la colección `_ventas` del restaurante
- El stock del producto se reduce automáticamente mediante `producto.vender(cantidad)`
- Se guardan `productos.json` y `ventas.json`

**Ejemplo:**
```
Antes de vender:
  Producto: Hamburguesa, Stock: 10
  Usuario solicita: 3 unidades

Después de vender:
  Producto: Hamburguesa, Stock: 7
  Venta registrada: Venta(usuario_id=001, producto_codigo=HAM, cantidad=3)
```

## Relación Usuario – Producto mediante Venta

La operación principal de la semana es la **venta de productos**, que establece una relación entre un usuario y un producto.

**Flujo de venta:**
```
Usuario selecciona la opción vender
        ↓
main.py solicita identificación, código de producto y cantidad
        ↓
Restaurante busca usuario y producto
        ↓
Se valida cantidad > 0 y stock disponible
        ↓
Se crea Venta(usuario.identificacion, producto.codigo, cantidad)
        ↓
La Venta se agrega a self._ventas
        ↓
Producto disminuye su stock mediante vender(cantidad)
        ↓
Se guardan ventas.json y productos.json
        ↓
El sistema muestra el resultado
```

**Método clave: `vender_producto(codigo_producto, identificacion_usuario, cantidad)`**
```python
usuario = self.buscar_usuario(identificacion_usuario)
producto = self.buscar_producto(codigo_producto)

if usuario is None or producto is None:
    return False

if cantidad <= 0 or producto.stock < cantidad:
    return False

venta = Venta(usuario.identificacion, producto.codigo, cantidad)
self._ventas.append(venta)
producto.vender(cantidad)
return True
```

## Persistencia: Productos, Usuarios y Ventas

### Estructura de Datos en JSON

**productos.json:**
```json
[
  {
    "codigo": "HAM001",
    "nombre": "Hamburguesa Simple",
    "categoria": "Platos",
    "precio": 8.50,
    "stock": 15
  }
]
```

**usuarios.json:**
```json
[
  {
    "identificacion": "0912345678",
    "nombre": "Juan Pérez",
    "correo": "juan@example.com"
  }
]
```

**ventas.json:**
```json
[
  {
    "usuario_id": "0912345678",
    "producto_codigo": "HAM001",
    "cantidad": 2
  }
]
```

### Ciclo de Persistencia

1. **Al iniciar la aplicación:**
   - `main.py` crea el `ArchivoServicio`
   - Carga productos, usuarios y ventas desde JSON
   - Si un archivo no existe, comienza con colección vacía

2. **Durante operaciones:**
   - Cada acción que modifique datos llama a guardar automáticamente
   - Registrar producto → guardar `productos.json`
   - Registrar usuario → guardar `usuarios.json`
   - Realizar venta → guardar `ventas.json` y `productos.json`

3. **Reconstrucción de objetos:**
   - JSON → `json.load()` → diccionarios → `desde_dict()` → objetos

**Métodos clave de persistencia:**
- `Producto.a_dict()`: Convierte Producto a diccionario
- `Producto.desde_dict(datos)`: Reconstruye Producto desde diccionario
- `Usuario.a_dict()`: Convierte Usuario a diccionario
- `Usuario.desde_dict(datos)`: Reconstruye Usuario desde diccionario
- `Venta.a_dict()`: Convierte Venta a diccionario
- `Venta.desde_dict(datos)`: Reconstruye Venta desde diccionario

## Excepciones Controladas

| Excepción | Situación | Acción |
|-----------|-----------|--------|
| `FileNotFoundError` | Archivo JSON no existe | Inicia con colección vacía |
| `json.JSONDecodeError` | Contenido JSON inválido | Advierte y retorna lista vacía |
| `PermissionError` | Falta permisos de lectura/escritura | Notifica y retorna lista vacía |
| `KeyError` | Falta clave en registro JSON | Omite el registro con advertencia |
| `ValueError` | Validación de Producto, Usuario o Venta | Lanza excepción con mensaje descriptivo |

## Ejecución del Programa

### Requisitos
- Python 3.7 o superior
- Módulos estándar: `json`, `pathlib`

### Instrucciones
1. Abrir terminal en el directorio del proyecto
2. Ejecutar el programa:
   ```bash
   python restaurante_app/main.py
   ```
   O, si se ejecuta desde VS Code, hacer clic en el botón de ejecutar.

3. El programa cargará automáticamente datos previos y mostrará un menú interactivo

4. Seleccionar opciones del 1 al 10 para realizar operaciones
5. Seleccionar opción 11 para salir (los datos se guardan automáticamente)

### Menú Disponible
```
1. Registrar producto
2. Buscar producto
3. Actualizar producto
4. Eliminar producto
5. Listar productos
6. Registrar usuario
7. Listar usuarios
8. Vender producto              ← NUEVA OPERACIÓN
9. Consultar ventas de un usuario ← NUEVA OPERACIÓN
10. Mostrar categorías
11. Salir
```

## Pruebas Realizadas

### Prueba 1: Persistencia de Productos
- ✓ Se registran productos con stock inicial
- ✓ `productos.json` se actualiza correctamente
- ✓ Al reiniciar, los productos se cargan correctamente

### Prueba 2: Persistencia de Usuarios
- ✓ Se registran usuarios
- ✓ `usuarios.json` se actualiza correctamente
- ✓ Al reiniciar, los usuarios se cargan correctamente

### Prueba 3: Venta con Stock Suficiente
- ✓ Usuario registrado puede comprar producto
- ✓ Stock disminuye correctamente
- ✓ Venta se registra en `ventas.json`
- ✓ `productos.json` refleja el nuevo stock

### Prueba 4: Venta con Stock Insuficiente
- ✓ Sistema rechaza venta si stock < cantidad solicitada
- ✓ Datos no se modifican
- ✓ Se muestra mensaje de error claro

### Prueba 5: Consulta de Ventas por Usuario
- ✓ Se filtran correctamente las ventas de un usuario específico
- ✓ Se muestran producto, código y cantidad de cada venta
- ✓ Manejo correcto cuando el usuario no tiene ventas

### Prueba 6: Recuperación de Datos
- ✓ Se cierra y reabre la aplicación
- ✓ Productos, usuarios y ventas se recuperan correctamente
- ✓ Stock reflejado es el actual (después de ventas)

### Prueba 7: Validaciones
- ✓ No permite productos con código duplicado
- ✓ No permite usuarios con identificación duplicada
- ✓ Rechaza ventas con cantidad ≤ 0
- ✓ Rechaza ventas de productos no existentes
- ✓ Rechaza ventas de usuarios no existentes

### Prueba 8: Manejo de Excepciones
- ✓ Aplicación funciona incluso si archivos JSON no existen
- ✓ Advierte sobre JSON inválido sin bloquear
- ✓ Notifica sobre problemas de permisos

## Notas de Implementación

1. **Colecciones vs Diccionarios**: Se utilizan objetos `Producto`, `Usuario` y `Venta` en lugar de diccionarios. Los diccionarios solo se usan en el paso JSON intermedio.

2. **Métodos de Negocio Centralizados**: Toda la lógica de validación y operaciones se encuentra en `Restaurante`, no en `main.py`.

3. **Copias de Listas**: Los métodos `listar_*()` retornan copias para evitar modificaciones accidentales externas.

4. **Case-Insensitive**: Las búsquedas de códigos de producto e identificaciones de usuario son case-insensitive.

5. **Validación de Stock Nunca Negativo**: El método `vender()` de `Producto` valida que el stock nunca sea negativo.

## Mejoras de la Semana 11 vs. Semana 10

| Aspecto | Semana 10 | Semana 11 |
|--------|-----------|----------|
| Stock en Productos | No | **Sí** |
| Persistencia de Usuarios | No | **Sí** |
| Persistencia de Ventas | No | **Sí** |
| Clase Venta | No | **Sí** |
| Operación vender_producto() | No | **Sí** |
| Consulta de ventas por usuario | No | **Sí** |
| Métodos a_dict/desde_dict en Usuario | No | **Sí** |
| Validación de cantidad y stock | No | **Sí** |
| Relación Usuario-Producto | No | **Sí** |

## Autor
Cristhian Tenesaca - POO Semana 11
