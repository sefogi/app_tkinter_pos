# 🛒 Sistema de Punto de Venta (POS) - Cremería "Rimbero"

Este es un sistema de punto de venta (POS) básico desarrollado en Python utilizando la librería **Tkinter** y el módulo **ttk** para una interfaz de usuario moderna. Utiliza la librería **Pillow (PIL)** para la gestión de imágenes.

## 📋 Requisitos

* Python 3.x
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
| **`Accent.TButton`** | `TButton` | **Botón Primario**. Fondo `COLOR_SECONDARY` (Azul Brillante), texto `COLOR_CARD` (Blanco). Se usa para acciones principales (e.g., *IMPRIMIR / FINALIZAR*). |
| **`Secondary.TButton`**| `TButton` | **Botón Secundario**. Fondo **`COLOR_CARD` (Blanco)**, texto `COLOR_PRIMARY` (Azul Oscuro). Se usa para acciones secundarias (e.g., *Volver al Menú*). **Asegura la integración visual en los contenedores `Card.TFrame`.** |
| `Treeview.Heading`| `Treeview` | Fondo **`COLOR_PRIMARY`** (Azul Oscuro) y texto blanco para los encabezados de las tablas. |
| `Treeview` | `Treeview` | Fondo `COLOR_CARD` (Blanco) y texto `COLOR_TEXT`. La selección utiliza `COLOR_SECONDARY` (Azul Brillante). |

---

## 🗃️ Estructura y Funcionalidad del Código

El código se organiza en la clase principal `CremeriaApp` y funciones auxiliares para el formato de moneda y la navegación entre pantallas.

### Funciones Auxiliares

| Función | Descripción |
| :--- | :--- |
| `money(v)` | **Formateo de Moneda**. Recibe un valor numérico (`v`), lo convierte a `Decimal`, lo redondea a dos decimales (`0.01`) y devuelve el formato de cadena `"$0.00"`. |

### Clase `CremeriaApp(tk.Tk)`

#### Métodos de Inicialización y Control de Pantalla

| Método | Descripción |
| :--- | :--- |
| `__init__(self)` | **Constructor**. Configura la ventana principal (`tk.Tk`), carga la configuración de estilos TTK (`self.style`), inicializa las variables de estado (`self.cart`, `self.descuento_adulto_mayor`, `self.metodo_pago`) y muestra la pantalla de inicio de sesión (`show_login`). |
| `clear_screen(self)` | Limpia la pantalla eliminando todos los widgets contenidos en `self.main_container`. Se llama antes de mostrar una nueva vista. |

#### Métodos de Vistas (Screens)

| Método | Descripción | Estilos Aplicados |
| :--- | :--- | :--- |
| `show_login(self)` | Muestra la pantalla de inicio de sesión. | `Card.TFrame`, `Header.TLabel`, `SubHeader.TLabel`, `Accent.TButton`, `Secondary.TButton`. |
| `try_login(self)` | Verifica la clave ingresada. Si es correcta (`self.key_correct`), llama a `show_main_menu()`. | N/A (usa `messagebox` para errores). |
| `show_main_menu(self)` | Muestra la pantalla principal con botones de navegación. | `Card.TFrame`, `Header.TLabel`, `SubHeader.TLabel`, **`Accent.TButton`** (para acciones importantes) y **`Secondary.TButton`** (para navegación). |
| `show_equipo(self)` / `show_objetivo(self)` | Muestran información estática del equipo o el objetivo. | `Card.TFrame`, `Header.TLabel`, `SubHeader.TLabel`, `Secondary.TButton` (para volver). |
| `show_inventario(self)` | Muestra una tabla (`Treeview`) con la lista completa de productos (`PRODUCTS`). | `Card.TFrame`, `Header.TLabel`, `Treeview.Heading`, `Treeview`, `Secondary.TButton`. |
| `show_productos(self)` | Muestra la interfaz para seleccionar productos y agregarlos al carrito (`self.cart`). | `Card.TFrame`, `Header.TLabel`, `Treeview`, `Accent.TButton` (Agregar), `Secondary.TButton` (Ver Carrito/Volver). |
| `show_cart(self)` | Muestra una ventana emergente (`Toplevel`) con el resumen actual del carrito. | `Card.TFrame`, `Body.TLabel`, `Secondary.TButton`. |

#### Métodos de Lógica del Carrito y Venta

| Método | Descripción | Estilos Aplicados |
| :--- | :--- | :--- |
| `add_product(self)` | Añade el producto seleccionado en `self.product_tree` a `self.cart`. Si el producto ya existe, incrementa la cantidad (`qty`). | N/A (usa `messagebox`). |
| `show_ticket(self)` | Muestra la pantalla final para revisar el pedido, aplicar descuentos y finalizar la venta. | **Contenedores usan `Card.TFrame` (fondo blanco)**. Botones usan `Accent.TButton` y `Secondary.TButton`. Totales usan `Header.TLabel` y `Body.TLabel`. |
| `toggle_descuento(self)` | Maneja el checkbox de "Adulto Mayor" y llama a `refresh_ticket()` para recalcular. | N/A. |
| `cambiar_metodo_pago(self)` | Actualiza la variable `self.metodo_pago` y el Label correspondiente en la pantalla de ticket. | N/A. |
| **`refresh_ticket(self)`** | **Lógica Central de Cálculo.** Recalcula el subtotal, aplica el descuento del 10% si `self.descuento_adulto_mayor` es True, calcula el total final y actualiza todos los `ttk.Label` de resumen (`ticket_subtotal`, `ticket_descuento`, `ticket_total`). | `COLOR_ERROR` (Rojo) para el descuento aplicado; `COLOR_SUCCESS` (Verde) si no hay descuento. |
| `print_ticket(self)` | Simula la impresión: genera el contenido del ticket en formato texto y lo muestra en una nueva ventana (`Toplevel`) usando un widget `tk.Text`. **Esta acción también se considera la finalización de la venta.** | El ticket se muestra con una fuente monoespaciada (`Courier New`) para simular un recibo impreso. |