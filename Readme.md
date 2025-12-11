# 🛒 Sistema de Punto de Venta (POS) - Cremería "Rimbero"

Este es un sistema de punto de venta (POS) desarrollado en Python utilizando la librería **Tkinter** y el módulo **ttk** para una interfaz de usuario moderna y profesional. Utiliza la librería **Pillow (PIL)** para la gestión de imágenes de productos.

---

## 📋 Requisitos

* Python 3.8 o superior
* Librería Tkinter (incluida en la instalación estándar de Python)
* Librería Pillow (`PIL`) para la gestión de imágenes:
    ```bash
    pip install Pillow
    ```

---

## 🎨 Estilos y Paleta de Colores

La aplicación utiliza una paleta de colores moderna y flat definida al inicio para aplicar consistencia a través de los estilos de `ttk.Style`.

### Paleta de Colores

| Constante | Valor | Descripción | Uso Principal |
| :--- | :--- | :--- | :--- |
| `COLOR_PRIMARY` | `#2C3E50` | Azul oscuro/Gris (Acero) | Texto principal, fondos de botones activos, encabezados de tabla. |
| `COLOR_SECONDARY` | `#3498DB` | Azul brillante | Fondo de botones de acento (`Accent.TButton`). |
| `COLOR_BG` | `#ECF0F1` | Gris muy claro (Plata) | Fondo principal de la ventana. |
| `COLOR_CARD` | `#FFFFFF` | Blanco puro | Fondo de contenedores principales (cards), campos de texto, botones secundarios. |
| `COLOR_TEXT` | `#2C3E50` | Azul oscuro/Gris | Color del texto general en la aplicación. |
| `COLOR_SUCCESS` | `#27AE60` | Verde | Textos de totales positivos o sin descuento. |
| `COLOR_ERROR` | `#E74C3C` | Rojo | Indicador de descuento aplicado. |

### Estilos TTK Definidos

Los estilos se configuran en `CremeriaApp.__init__` para dar una apariencia moderna a los widgets estándar.

| Nombre del Estilo | Widget Base | Uso y Colores Aplicados |
| :--- | :--- | :--- |
| `Custom.TFrame` | `TFrame` | Utiliza `COLOR_BG` (gris claro) como fondo para el contenedor principal. |
| **`Card.TFrame`** | `TFrame` | Utiliza **`COLOR_CARD` (blanco)** como fondo. Se aplica a todos los **contenedores de pantalla** (`frame` en `show_login`, `main_frame` en `show_ticket`, etc.) para crear un efecto de "tarjeta" flotante. |
| `Header.TLabel` | `TLabel` | Fuente **negrita 22pt**, `COLOR_PRIMARY` (Azul Oscuro). Para títulos de pantalla. |
| `SubHeader.TLabel`| `TLabel` | Fuente **negrita 14pt**, `COLOR_PRIMARY` (Azul Oscuro). Para subtítulos. |
| `Body.TLabel` | `TLabel` | Fuente 11pt, `COLOR_TEXT`. Para texto general y opciones. |
| **`Accent.TButton`** | `TButton` | **Botón Primario**. Fondo `COLOR_SECONDARY` (Azul Brillante), texto `COLOR_CARD` (Blanco). Se usa para acciones principales (e.g., *IMPRIMIR / FINALIZAR*, *Agregar al carrito*). |
| **`Secondary.TButton`**| `TButton` | **Botón Secundario**. Fondo **`COLOR_CARD` (Blanco)**, texto `COLOR_PRIMARY` (Azul Oscuro). Se usa para acciones secundarias (e.g., *Volver al Menú*, *Cerrar*). **Asegura la integración visual en los contenedores `Card.TFrame`.** |
| `Treeview.Heading`| `Treeview` | Fondo **`COLOR_PRIMARY`** (Azul Oscuro) y texto blanco para los encabezados de las tablas. |
| `Treeview` | `Treeview` | Fondo `COLOR_CARD` (Blanco) y texto `COLOR_TEXT`. La selección utiliza `COLOR_SECONDARY` (Azul Brillante). |

---

## 🗃️ Estructura y Funcionalidad del Código

El código se organiza en la clase principal `CremeriaApp` y funciones auxiliares para el formato de moneda, gestión de imágenes y la navegación entre pantallas.

### Datos del Sistema

#### Información Institucional
```python
CREMERIA_INFO = {
    "institucion": "Centro de Estudios Científicos y Tecnológicos del Estado de México",
    "programa": "Técnico en Programación",
    "modulo": "Módulo: Emplea metodologías ágiles para el desarrollo de software",
    "nombre": "Cremería \"Rimbero\"",
    "eslogan": "Frescura y sabor en cada bocado"
}
```

#### Catálogo de Productos
El sistema incluye **10 productos** con su información completa:

| Código | Nombre | Precio | Imagen |
| :--- | :--- | ---: | :--- |
| P001 | Leche entera | $15.00 | `leche_entera.webp` |
| P002 | Leche deslactosada | $25.00 | `leche_deslactosada.webp` |
| P003 | Nata artesanal | $18.00 | `nata_artesanal.webp` |
| P004 | Crema | $35.00 | `crema.webp` |
| P005 | Yogurt natural | $120.00 | `yogurt_natural.webp` |
| P006 | Yogurt fresa | $125.00 | `yogurt_fresa.webp` |
| P007 | Yogurt griego | $150.00 | `yogurt_griego.webp` |
| P008 | Leche vaporizada | $16.00 | `leche_vaporizada.webp` |
| P009 | Helado de horchata | $10.00 | `Helado_Horchata.webp` |
| P010 | Helado de fresa | $10.00 | `helado_fresa.webp` |

### Funciones Auxiliares

| Función | Descripción |
| :--- | :--- |
| `money(v)` | **Formateo de Moneda**. Recibe un valor numérico (`v`), lo convierte a `Decimal`, lo redondea a dos decimales (`0.01`) y devuelve el formato de cadena `"$0.00"`. Utiliza `ROUND_HALF_UP` para redondeo comercial. |

### Clase `CremeriaApp(tk.Tk)`

#### Métodos de Inicialización y Control de Pantalla

| Método | Descripción |
| :--- | :--- |
| `__init__(self)` | **Constructor**. Configura la ventana principal (`tk.Tk`), carga la configuración de estilos TTK (`self.style`), inicializa las variables de estado (`self.cart`, `self.descuento_adulto_mayor`, `self.metodo_pago`), inicializa diccionarios para caché de imágenes (`self.product_images`, `self.cart_images`), carga la imagen por defecto y muestra la pantalla de inicio de sesión (`show_login`). |
| `clear_screen(self)` | Limpia la pantalla eliminando todos los widgets contenidos en `self.main_container`. Se llama antes de mostrar una nueva vista. |
| **`_load_image(self, path, size)`** | **Nuevo: Gestión de Imágenes**. Carga una imagen desde `path`, la convierte a formato RGBA, la redimensiona a `size` usando `Image.LANCZOS` y retorna un objeto `ImageTk.PhotoImage`. Si falla, retorna una imagen placeholder gris. Utiliza rutas absolutas para mayor compatibilidad. |

#### Variables de Estado

| Variable | Tipo | Descripción |
| :--- | :--- | :--- |
| `self.key_correct` | `str` | Clave de acceso al sistema (por defecto: `"1234"`). |
| `self.cart` | `list` | Lista de productos agregados al carrito con sus cantidades. |
| `self.descuento_adulto_mayor` | `bool` | Indica si se aplica descuento del 10%. |
| `self.metodo_pago` | `str` | Método de pago seleccionado (`"Efectivo"` o `"Tarjeta"`). |
| `self.product_images` | `dict` | Caché de imágenes de productos cargadas. |
| `self.cart_images` | `dict` | Caché de imágenes para vista previa en carrito. |
| `self.default_image` | `ImageTk.PhotoImage` | Imagen por defecto cuando falla la carga. |

#### Métodos de Vistas (Screens)

| Método | Descripción | Estilos Aplicados | Nuevas Características |
| :--- | :--- | :--- | :--- |
| `show_login(self)` | Muestra la pantalla de inicio de sesión. Intenta cargar `logo.png` (120x120px). Si no existe, muestra el nombre de la cremería. | `Card.TFrame`, `Header.TLabel`, `SubHeader.TLabel`, `Accent.TButton`, `Secondary.TButton`. | **Logo personalizable** con fallback a texto. Soporte para Enter para login rápido. |
| `try_login(self)` | Verifica la clave ingresada. Si es correcta (`self.key_correct`), llama a `show_main_menu()`. | N/A (usa `messagebox` para errores). | Sin cambios. |
| `show_main_menu(self)` | Muestra la pantalla principal con **6 botones de navegación** organizados en grid 2x3. Incluye separador horizontal para mejor organización visual. | `Card.TFrame`, `Header.TLabel`, `SubHeader.TLabel`, `Separator`, **`Accent.TButton`** (Productos/Ticket), **`Secondary.TButton`** (resto). | **Iconos emoji** en botones: 🧑‍💻 Equipo, 🎯 Objetivo, 🛒 Productos, 📦 Inventario, 🧾 Ticket, 🚪 Cerrar sesión. |
| `show_equipo(self)` / `show_objetivo(self)` | Muestran información estática del equipo o el objetivo. | `Card.TFrame`, `Header.TLabel`, `SubHeader.TLabel`, `Secondary.TButton`. | **Iconos** en títulos y botón de retorno con ◀️. |
| `show_inventario(self)` | Muestra una tabla (`Treeview`) con la lista completa de **10 productos** (`PRODUCTS`). Incluye scrollbar vertical. | `Card.TFrame`, `Header.TLabel`, `Treeview.Heading`, `Treeview`, `Secondary.TButton`. | **Icono 📦** en título. Tabla expandible con scroll. |
| **`show_productos(self)`** | **Mejorado**: Muestra la interfaz para seleccionar productos con **vista previa de imagen** en panel derecho. Layout de dos columnas: tabla de productos (izq.) y preview (der.). | `Card.TFrame`, `Header.TLabel`, `Treeview`, `Accent.TButton` (Agregar), `Secondary.TButton` (Ver Carrito/Volver). | **NUEVO: Panel de vista previa** con imagen del producto (180x180px), nombre y precio. Actualización dinámica al seleccionar. **Iconos**: 🛒, ➕, 👀, ◀️. |
| **`on_product_select(self, event)`** | **Nuevo**: Event handler para selección en `product_tree`. Carga y muestra la imagen del producto seleccionado en el panel de vista previa. Actualiza labels de nombre y precio. | N/A | Sistema de **caché de imágenes** para optimización. |
| **`show_cart(self)`** | **Mejorado**: Ventana emergente (`Toplevel`) de 900x500px con **dos paneles**: tabla de productos (izq.) y vista previa de imagen (der.). Incluye evento de selección para preview. | `Card.TFrame`, `Body.TLabel`, `Secondary.TButton`. | **NUEVO: Vista previa de productos** en carrito (200x200px). Botón con **icono personalizable** (`icono_pagar.png`). Layout mejorado con scrollbar. |

#### Métodos de Lógica del Carrito y Venta

| Método | Descripción | Estilos Aplicados | Características |
| :--- | :--- | :--- | :--- |
| `add_product(self)` | Añade el producto seleccionado en `self.product_tree` a `self.cart`. Si el producto ya existe, incrementa la cantidad (`qty`). | N/A (usa `messagebox`). | Validación de selección. Acumulación inteligente de cantidades. |
| **`show_ticket(self)`** | **Mejorado**: Pantalla final de venta con **3 secciones**: (1) Opciones de descuento y pago, (2) Tabla de productos, (3) Totales y botones. Separador visual entre secciones. | **Contenedores: `Card.TFrame`**. Botones: `Accent.TButton` (FINALIZAR), `Secondary.TButton` (Volver/Actualizar). Separadores: `ttk.Separator`. | **NUEVO: Selector de método de pago** (💵 Efectivo / 💳 Tarjeta) con RadioButtons. Checkbox 👵 para descuento. Layout con **3 botones centrados** en fila. Iconos: 🧾, ◀️, 🔄, 🖨️. |
| `toggle_descuento(self)` | Maneja el checkbox de "Adulto Mayor" y llama a `refresh_ticket()` para recalcular totales en tiempo real. | N/A. | Actualización instantánea de totales. |
| **`cambiar_metodo_pago(self)`** | **Nuevo**: Actualiza la variable `self.metodo_pago` ("Efectivo" o "Tarjeta") y el Label correspondiente en la pantalla de ticket. | N/A. | Sincronización inmediata de UI. |
| **`refresh_ticket(self)`** | **Lógica Central de Cálculo.** Recalcula el subtotal, aplica el descuento del 10% si `self.descuento_adulto_mayor` es True, calcula el total final y actualiza todos los `ttk.Label` de resumen (`ticket_subtotal`, `ticket_descuento`, `ticket_total`, **`ticket_metodo`**). | `COLOR_ERROR` (Rojo) para el descuento aplicado; `COLOR_SUCCESS` (Verde) si no hay descuento. Total en **negrita 18pt**. | **Nuevo label**: `ticket_metodo` muestra el método de pago seleccionado en formato itálico gris. Cambio dinámico de color del descuento. |
| **`print_ticket(self)`** | **Mejorado**: Simula la impresión generando el contenido del ticket en formato texto con **ancho de 35 caracteres**. Incluye fecha/hora, **método de pago**, productos con cantidades, subtotal, descuento (si aplica), total y notas finales. Muestra en ventana `Toplevel` (550x600px) con fuente `Courier New`. **Esta acción finaliza la venta.** | Ticket con fuente monoespaciada. Ventana con fondo `COLOR_CARD`. Botón `Secondary.TButton`. | **NUEVO: Incluye método de pago** en encabezado y pie del ticket. Nota adicional: `* Pagado con: [Método]`. Validación de carrito vacío. Formato de recibo profesional. |

---

## 📁 Estructura de Archivos Requerida

```
cremeria-rimbero/
├── rimberio.py                    # Archivo principal de la aplicación
├── logo.png                       # Logo de la cremería (opcional, 120x120px recomendado)
├── README.md                      # Este archivo
└── images/                        # Carpeta de recursos gráficos
    ├── leche_entera.webp
    ├── leche_deslactosada.webp
    ├── nata_artesanal.webp
    ├── crema.webp
    ├── yogurt_natural.webp
    ├── yogurt_fresa.webp
    ├── yogurt_griego.webp
    ├── leche_vaporizada.webp
    ├── Helado_Horchata.webp
    ├── helado_fresa.webp
    ├── no_image.png               # Imagen placeholder (180x180px recomendado)
    └── icono_pagar.png            # Icono para botones (28x28px, opcional)
```

### Notas sobre Imágenes:
- **Formato recomendado**: WebP o PNG para productos
- **Tamaños sugeridos**: 
  - Productos: 400x400px (se redimensionan automáticamente)
  - Logo: 500x500px (se redimensiona a 120x120px)
  - Iconos: 28x28px
- Las imágenes faltantes mostrarán un placeholder gris automáticamente
- El sistema utiliza `Image.LANCZOS` para redimensionamiento de alta calidad

---

## ✨ Nuevas Características v2.0

### 🖼️ Sistema de Visualización de Productos
- **Vista previa en tiempo real** al seleccionar productos
- **Panel dedicado** con imagen de 180x180px
- **Caché de imágenes** para mejor rendimiento
- **Imágenes placeholder** automáticas si falta el archivo

### 💳 Métodos de Pago
- Selector entre **Efectivo** y **Tarjeta**
- Integración en el ticket impreso
- Indicador visual en pantalla de venta

### 👵 Descuento para Adultos Mayores
- **10% de descuento** aplicable mediante checkbox
- Cálculo automático en tiempo real
- Desglose detallado en ticket:
  - Subtotal
  - Descuento (si aplica)
  - Total final

### 🎨 Mejoras Visuales
- **Iconos emoji** en todos los botones y títulos
- **Separadores horizontales** para mejor organización
- **Layout mejorado** con paneles de dos columnas
- **Colores semánticos**: Verde para totales, Rojo para descuentos
- **Botones con estilos diferenciados**: Primario (Accent) y Secundario

### 📊 Carrito de Compras Mejorado
- **Vista previa** de productos en el carrito
- **Tabla expandible** con scrollbar
- **Layout de dos paneles** para mejor UX
- **Totales destacados** con fuente grande

---

## 🚀 Instalación y Ejecución

### 1. Clonar o Descargar
```bash
git clone [URL_DEL_REPOSITORIO]
cd cremeria-rimbero
```

### 2. Instalar Dependencias
```bash
pip install Pillow
```

### 3. Verificar Estructura de Carpetas
Asegúrate de tener la carpeta `images/` con las imágenes de productos.

### 4. Ejecutar
```bash
python rimberio.py
```

### 5. Iniciar Sesión
- **Clave por defecto**: `1234`

---

## 🎯 Flujo de Uso del Sistema

### Inicio de Sesión → Menú Principal → Selección de Productos → Carrito → Ticket → Finalizar Venta

1. **Login**: Ingresa la clave `1234`
2. **Menú Principal**: Navega a "🛒 Productos"
3. **Seleccionar Productos**: 
   - Haz clic en un producto para ver su imagen
   - Ajusta la cantidad con el spinner
   - Presiona "➕ Agregar al carrito"
4. **Revisar Carrito**: Presiona "👀 Ver carrito"
5. **Generar Ticket**:
   - Selecciona método de pago (💵/💳)
   - Marca descuento si aplica (👵)
   - Presiona "🖨️ IMPRIMIR / FINALIZAR"
6. **Ticket Impreso**: Se genera el recibo con todos los detalles

---

## 🔧 Personalización

### Cambiar Clave de Acceso
Edita la línea 135:
```python
self.key_correct = "TU_CLAVE_AQUI"
```

### Agregar Nuevos Productos
Edita la lista `PRODUCTS` (línea 36):
```python
{"codigo": "P011", "nombre": "Nuevo Producto", "marca": "Rimbero", 
 "costo": 50.00, "imagen": "images/nuevo_producto.webp"}
```

### Modificar Paleta de Colores
Edita las constantes (líneas 13-18):
```python
COLOR_PRIMARY = "#TU_COLOR"
COLOR_SECONDARY = "#TU_COLOR"
# etc.
```

### Cambiar Porcentaje de Descuento
En `refresh_ticket()` y `print_ticket()`, busca:
```python
descuento = subtotal * 0.10  # Cambia 0.10 por tu porcentaje
```

---

## 🐛 Solución de Problemas

### No se muestran las imágenes
- Verifica que la carpeta `images/` existe
- Confirma que los nombres de archivo coinciden exactamente
- Revisa que las extensiones sean `.webp` o `.png`

### Error al cargar Pillow
```bash
pip uninstall Pillow
pip install Pillow
```

### Ventana no se maximiza
La línea `self.state('zoomed')` solo funciona en Windows. En Linux/Mac, la ventana tendrá tamaño fijo de 1000x700px.

---

## 📊 Información Técnica

### Tecnologías Utilizadas
- **Python 3.8+**
- **Tkinter** (GUI)
- **ttk** (Widgets temáticos)
- **Pillow** (Procesamiento de imágenes)
- **Decimal** (Cálculos precisos monetarios)
- **datetime** (Timestamps)

### Arquitectura
- **Patrón**: Orientado a Objetos (OOP)
- **Clase principal**: `CremeriaApp(tk.Tk)`
- **Gestión de estado**: Variables de instancia
- **Navegación**: Sistema de pantallas con `clear_screen()`

### Características Técnicas
- **Redondeo comercial** con `Decimal.ROUND_HALF_UP`
- **Caché de imágenes** para optimización de memoria
- **Rutas absolutas** para compatibilidad multiplataforma
- **Manejo de excepciones** en carga de recursos
- **Layout responsivo** con `pack()` y `grid()`

---

## 👥 Créditos

**Desarrollador**:Paola García  
**Institución**: Centro de Estudios Científicos y Tecnológicos del Estado de México  
**Programa**: Técnico en Programación  
**Módulo**: Emplea metodologías ágiles para el desarrollo de software

---

## 📄 Licencia

Proyecto educativo desarrollado para fines académicos.

---

**Cremería "Rimbero"** - *Frescura y sabor en cada bocado* 🥛✨
