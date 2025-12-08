import tkinter as tk
from tkinter import ttk, messagebox
from decimal import Decimal, ROUND_HALF_UP
from datetime import datetime
from PIL import Image, ImageTk

print("version 1.0")

# -------------------
# Configuración visual
# -------------------
# Paleta de colores más (Estilo Flat/Minimalista)
COLOR_PRIMARY = "#2C3E50"  # Azul oscuro/Gris (Acero/Principal)
COLOR_SECONDARY = "#3498DB"  # Azul brillante (Acento)
COLOR_BG = "#ECF0F1"  # Fondo gris muy claro (Plata/Claro)
COLOR_CARD = "#FFFFFF"  # Tarjetas/Contenedores (Blanco puro)
COLOR_TEXT = "#2C3E50"  # Texto principal

# Colores para estados (éxito, error, acento en totales)
COLOR_SUCCESS = "#27AE60"  # Verde para totales y descuentos positivos
COLOR_ERROR = "#E74C3C"  # Rojo para descuentos aplicados

# -------------------
# Datos iniciales
# -------------------
CREMERIA_INFO = {
    "institucion": "Centro de Estudios Científicos y Tecnológicos del Estado de México",
    "programa": "Técnico en Programación",
    "modulo": "Módulo: Emplea metodologías ágiles para el desarrollo de software",
    "nombre": "Cremería \"Rimbero\"",
    "eslogan": "Frescura y sabor en cada bocado"
}

EQUIPO = "Integrantes: Paola García"
OBJETIVO = "Objetivo: Ofrecer productos lácteos y helados artesanales con calidad y atención amable."

PRODUCTS = [
    {"codigo": "P001", "nombre": "leche entera", "marca": "Rimbero", "costo": 15.00},
    {"codigo": "P002", "nombre": "leche deslactosada", "marca": "Rimbero", "costo": 25.00},
    {"codigo": "P003", "nombre": "nata artesanal", "marca": "Rimbero", "costo": 18.00},
    {"codigo": "P004", "nombre": "crema", "marca": "Rimbero", "costo": 35.00},
    {"codigo": "P005", "nombre": "yogurt natural", "marca": "Rimbero", "costo": 120.00},
    {"codigo": "P006", "nombre": "yogurt fresa", "marca": "Rimbero", "costo": 125.00},
    {"codigo": "P007", "nombre": "yogurt griego", "marca": "Rimbero", "costo": 150.00},
    {"codigo": "P008", "nombre": "Leche vaporizada", "marca": "Rimbero", "costo": 16.00},
    {"codigo": "P009", "nombre": "Helado de horchata", "marca": "Rimbero", "costo": 10.00},
    {"codigo": "P010", "nombre": "helado de fresa", "marca": "Rimbero", "costo": 10.00},
]


# -------------------
# Helper
# -------------------
def money(v):
    """Formatea un valor numérico a moneda ($0.00)"""
    d = Decimal(v).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    return f"${d}"


# -------------------
# App Principal
# -------------------
class CremeriaApp(tk.Tk):
    def __init__(self):
        super().__init__()
        print("Inicializando ventana principal...")

        self.title("Cremería - " + CREMERIA_INFO["nombre"])
        self.geometry("1000x700")

        try:
            self.state('zoomed')
        except:
            pass

        self.configure(bg=COLOR_BG)

        # Configuración de estilo (TTK)
        self.style = ttk.Style(self)
        self.style.theme_use('clam')

        # Estilos generales
        self.style.configure('Custom.TFrame', background=COLOR_BG)
        self.style.configure('Card.TFrame', background=COLOR_CARD)

        # Estilos de etiquetas
        self.style.configure('Header.TLabel', font=('Helvetica', 22, 'bold'), foreground=COLOR_PRIMARY,
                             background=COLOR_CARD)
        self.style.configure('SubHeader.TLabel', font=('Helvetica', 14, 'bold'), foreground=COLOR_PRIMARY,
                             background=COLOR_CARD)
        self.style.configure('Body.TLabel', font=('Helvetica', 11), foreground=COLOR_TEXT, background=COLOR_CARD)

        # Estilos de botones
        self.style.configure('Accent.TButton', font=('Helvetica', 12, 'bold'),
                             foreground=COLOR_CARD, background=COLOR_SECONDARY,
                             padding=[10, 8])
        self.style.map('Accent.TButton',
                       background=[('active', COLOR_PRIMARY)])


        self.style.configure('Secondary.TButton', font=('Helvetica', 12),
                             foreground=COLOR_PRIMARY, background=COLOR_CARD,  # CORREGIDO: Sin doble asterisco
                             padding=[10, 8])
        self.style.map('Secondary.TButton',
                       background=[('active', COLOR_PRIMARY)],
                       foreground=[('active', 'white')])

        # Estilo para (Tabla)
        self.style.configure("Treeview.Heading", font=('Helvetica', 11, 'bold'),
                             background=COLOR_PRIMARY, foreground="white")
        self.style.configure("Treeview", font=('Helvetica', 11), rowheight=25,
                             background=COLOR_CARD, fieldbackground=COLOR_CARD, foreground=COLOR_TEXT)
        self.style.map("Treeview", background=[('selected', COLOR_SECONDARY)])

        # Estado
        self.key_correct = "1234"
        self.cart = []
        self.current_screen = None
        self.descuento_adulto_mayor = False
        self.metodo_pago = "Efectivo"

        # Contenedor principal
        self.main_container = ttk.Frame(self, style='Custom.TFrame', padding="15 15 15 15")
        self.main_container.pack(fill="both", expand=True)

        print("Mostrando pantalla de login...")
        self.show_login()

    def clear_screen(self):
        for widget in self.main_container.winfo_children():
            widget.destroy()

    # ======================================================================
    # PANTALLA DE LOGIN
    # ======================================================================
    def show_login(self):
        self.clear_screen()

        frame = ttk.Frame(self.main_container, padding="40 40 40 40", style='Card.TFrame')
        frame.place(relx=0.5, rely=0.5, anchor="center")

        try:
            img = Image.open("logo.png")
            img = img.resize((120, 120), Image.LANCZOS)
            self.logo_login = ImageTk.PhotoImage(img)

            ttk.Label(frame, image=self.logo_login, background=COLOR_CARD).pack(pady=10)
        except (FileNotFoundError, Exception):
            ttk.Label(frame, text=CREMERIA_INFO["nombre"], style='Header.TLabel').pack(pady=10)
            print("Advertencia: No se encontró logo.png, usando nombre como alternativa")

        ttk.Label(frame, text="Acceso al Sistema", style='SubHeader.TLabel').pack(pady=(10, 5))
        ttk.Label(frame, text="Ingresa la clave correcta para acceder.", style='Body.TLabel').pack(pady=5)

        self.entry_password = ttk.Entry(frame, font=("Helvetica", 14), width=20, justify="center", show="*")
        self.entry_password.pack(pady=10)
        self.entry_password.focus()
        self.entry_password.bind("<Return>", lambda e: self.try_login())

        ttk.Button(frame, text="🔑 Ingresar", style='Accent.TButton',
                   command=self.try_login).pack(pady=5, ipadx=10)
        ttk.Button(frame, text="❌ Salir", style='Secondary.TButton',
                   command=self.destroy).pack(pady=5, ipadx=10)

    def try_login(self):
        if self.entry_password.get() == self.key_correct:
            print("Login exitoso")
            self.show_main_menu()
        else:
            messagebox.showerror("Error", "Clave incorrecta.")

    # ======================================================================
    # PANTALLA MENÚ PRINCIPAL
    # ======================================================================
    def show_main_menu(self):
        self.clear_screen()

        frame = ttk.Frame(self.main_container, padding="30 30 30 30", style='Card.TFrame')
        frame.place(relx=0.5, rely=0.5, anchor="center")

        ttk.Label(frame, text=CREMERIA_INFO["institucion"],
                  font=('Helvetica', 14, 'bold'), foreground=COLOR_PRIMARY, background=COLOR_CARD, wraplength=800).pack(
            pady=5)

        ttk.Label(frame, text=f"{CREMERIA_INFO['programa']} | {CREMERIA_INFO['modulo']}",
                  style='Body.TLabel', wraplength=800).pack(pady=5)

        ttk.Separator(frame, orient='horizontal').pack(fill='x', pady=10)

        ttk.Label(frame, text=CREMERIA_INFO["nombre"],
                  style='Header.TLabel', foreground=COLOR_SECONDARY).pack(pady=(10, 5))

        ttk.Label(frame, text="Eslogan: " + CREMERIA_INFO["eslogan"],
                  style='SubHeader.TLabel', font=('Helvetica', 12, 'italic')).pack(pady=5)

        btn_frame = ttk.Frame(frame, style='Card.TFrame')
        btn_frame.pack(pady=20)

        buttons = [
            ("🧑‍💻 Equipo", self.show_equipo),
            ("🎯 Objetivo", self.show_objetivo),
            ("🛒 Productos", self.show_productos),
            ("📦 Inventario", self.show_inventario),
            ("🧾 Generar ticket", self.show_ticket),
            ("🚪 Cerrar sesión", self.show_login)
        ]

        for i, (text, cmd) in enumerate(buttons):
            style_name = 'Accent.TButton' if "Productos" in text or "ticket" in text else 'Secondary.TButton'
            row = i // 3
            col = i % 3
            ttk.Button(btn_frame, text=text, style=style_name,
                       command=cmd, width=18).grid(row=row, column=col, padx=8, pady=8)

    # ======================================================================
    # PANTALLA EQUIPO / OBJETIVO / INVENTARIO
    # ======================================================================
    def show_equipo(self):
        self.clear_screen()
        frame = ttk.Frame(self.main_container, padding="40 40 40 40", style='Card.TFrame')
        frame.place(relx=0.5, rely=0.5, anchor="center")
        ttk.Label(frame, text="Equipo e integrantes", style='Header.TLabel').pack(pady=10)
        ttk.Label(frame, text=EQUIPO, style='SubHeader.TLabel').pack(pady=20)
        ttk.Button(frame, text="◀️ Volver al Menú", style='Secondary.TButton',
                   command=self.show_main_menu).pack(pady=10)

    def show_objetivo(self):
        self.clear_screen()
        frame = ttk.Frame(self.main_container, padding="40 40 40 40", style='Card.TFrame')
        frame.place(relx=0.5, rely=0.5, anchor="center")
        ttk.Label(frame, text="Objetivo", style='Header.TLabel').pack(pady=10)
        ttk.Label(frame, text=OBJETIVO, style='SubHeader.TLabel', wraplength=700).pack(pady=20)
        ttk.Button(frame, text="◀️ Volver al Menú", style='Secondary.TButton',
                   command=self.show_main_menu).pack(pady=10)

    def show_inventario(self):
        self.clear_screen()
        frame = ttk.Frame(self.main_container, padding="30 30 30 30", style='Card.TFrame')
        frame.pack(fill='both', expand=True, padx=50, pady=50)
        ttk.Label(frame, text="📦 Inventario / Concentrado", style='Header.TLabel').pack(pady=10)
        tree_frame = ttk.Frame(frame, padding="10 10 10 10", style='Card.TFrame')
        tree_frame.pack(pady=10, fill='both', expand=True)

        cols = ("codigo", "nombre", "marca", "costo")
        tree = ttk.Treeview(tree_frame, columns=cols, show="headings", height=10)
        for c in cols:
            tree.heading(c, text=c.capitalize())
            tree.column(c, anchor="center", width=150)
        tree.pack(side="left", fill='both', expand=True)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

        for p in PRODUCTS:
            tree.insert("", "end", values=(p["codigo"], p["nombre"], p["marca"], money(p["costo"])))

        ttk.Button(frame, text="◀️ Volver al Menú", style='Secondary.TButton',
                   command=self.show_main_menu).pack(pady=15)

    # ======================================================================
    # PANTALLA SELECCIONAR PRODUCTOS
    # ======================================================================
    def show_productos(self):
        self.clear_screen()

        frame = ttk.Frame(self.main_container, padding="30 30 30 30", style='Card.TFrame')
        frame.pack(fill='both', expand=True, padx=50, pady=50)

        ttk.Label(frame, text="🛒 Selección de Productos", style='Header.TLabel').pack(pady=10)

        tree_frame = ttk.Frame(frame, padding="10 10 10 10", style='Card.TFrame')
        tree_frame.pack(pady=10, fill='both', expand=True)

        cols = ("codigo", "nombre", "marca", "costo")
        self.product_tree = ttk.Treeview(tree_frame, columns=cols, show="headings", height=15)

        for c in cols:
            self.product_tree.heading(c, text=c.capitalize())
            self.product_tree.column(c, anchor="center", width=150)

        self.product_tree.pack(side="left", fill='both', expand=True)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.product_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.product_tree.configure(yscrollcommand=scrollbar.set)

        for p in PRODUCTS:
            self.product_tree.insert("", "end",
                                     values=(p["codigo"], p["nombre"], p["marca"], money(p["costo"])))

        # Controles
        controls = ttk.Frame(frame, style='Card.TFrame')
        controls.pack(pady=15)

        ttk.Label(controls, text="Cantidad:", style='Body.TLabel').pack(side="left", padx=5)

        self.qty_var = tk.IntVar(value=1)
        ttk.Spinbox(controls, from_=1, to=99, textvariable=self.qty_var,
                    width=5, font=("Helvetica", 11)).pack(side="left", padx=10)

        ttk.Button(controls, text="➕ Agregar al carrito", style='Accent.TButton',
                   command=self.add_product).pack(side="left", padx=10)
        ttk.Button(controls, text="👀 Ver carrito", style='Secondary.TButton',
                   command=self.show_cart).pack(side="left", padx=10)
        ttk.Button(controls, text="◀️ Volver", style='Secondary.TButton',
                   command=self.show_main_menu).pack(side="left", padx=10)

    def add_product(self):
        sel = self.product_tree.selection()
        if not sel:
            messagebox.showwarning("Atención", "Selecciona un producto.")
            return

        vals = self.product_tree.item(sel[0], "values")
        codigo = vals[0]

        p = next((x for x in PRODUCTS if x["codigo"] == codigo), None)
        if p:
            qty = self.qty_var.get()
            found = False
            for item in self.cart:
                if item["codigo"] == p["codigo"]:
                    item["qty"] += qty
                    found = True
                    break

            if not found:
                new_item = p.copy()
                new_item["qty"] = qty
                self.cart.append(new_item)

            messagebox.showinfo("Agregado", f"Agregado {qty} x {p['nombre']}")

    def show_cart(self):
        if not self.cart:
            messagebox.showinfo("Vacío", "Aún no hay productos en el carrito.")
            return

        win = tk.Toplevel(self)
        win.title("🛒 Carrito de compras")
        win.geometry("700x450")
        win.configure(bg=COLOR_BG)

        ttk.Label(win, text="Carrito de compras", font=("Helvetica", 18, "bold"),
                  background=COLOR_BG, foreground=COLOR_PRIMARY).pack(pady=10)

        tree_frame = ttk.Frame(win, padding="10 10 10 10", style='Card.TFrame')
        tree_frame.pack(padx=10, pady=10, fill='both', expand=True)

        cols = ("nombre", "qty", "precio", "subtotal")
        tree = ttk.Treeview(tree_frame, columns=cols, show="headings", height=12)

        for h in cols:
            tree.heading(h, text=h.capitalize())
            tree.column(h, anchor="center", width=150)

        tree.pack(side="left", fill='both', expand=True)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side="right", fill="y")
        tree.configure(yscrollcommand=scrollbar.set)

        total = 0
        for item in self.cart:
            subtotal = item["costo"] * item["qty"]
            total += subtotal
            tree.insert("", "end",
                        values=(item["nombre"], item["qty"], money(item["costo"]), money(subtotal)))

        ttk.Label(win, text=f"Total: {money(total)}", font=("Helvetica", 16, "bold"),
                  background=COLOR_BG, foreground=COLOR_SUCCESS).pack(pady=10)

        ttk.Button(win, text="C¿errar", style='Secondary.TButton',
                   command=win.destroy).pack(pady=5)

    # ======================================================================
    # PANTALLA GENERAR TICKET
    # ======================================================================
    def show_ticket(self):
        self.clear_screen()

        main_frame = ttk.Frame(self.main_container, padding="30 30 30 30", style='Card.TFrame')
        main_frame.pack(fill='both', expand=True, padx=30, pady=30)

        # -------------------
        # Título y Opciones
        # -------------------
        ttk.Label(main_frame, text="🧾 Generar Ticket de Venta",
                  style='Header.TLabel').pack(pady=10, anchor='center')

        # Contenedor para opciones
        opciones_frame = ttk.Frame(main_frame, style='Card.TFrame')
        opciones_frame.pack(pady=0, fill='x', padx=0)

        # Checkbox para adulto mayor
        self.adulto_mayor_var = tk.BooleanVar(value=self.descuento_adulto_mayor)
        ttk.Checkbutton(opciones_frame, text="👵 Aplicar descuento del 10% (Adulto Mayor)",
                        variable=self.adulto_mayor_var, style='Body.TLabel',
                        command=self.toggle_descuento).pack(side='left', padx=10)

        # Método de pago
        pago_frame = ttk.Frame(opciones_frame, style='Card.TFrame')
        pago_frame.pack(side='right', padx=10)

        ttk.Label(pago_frame, text="Método de pago:", style='SubHeader.TLabel').pack(side="left", padx=(0, 10))
        self.metodo_pago_var = tk.StringVar(value=self.metodo_pago)

        ttk.Radiobutton(pago_frame, text="💵 Efectivo", variable=self.metodo_pago_var,
                        value="Efectivo", style='Body.TLabel',
                        command=self.cambiar_metodo_pago).pack(side="left", padx=5)

        ttk.Radiobutton(pago_frame, text="💳 Tarjeta", variable=self.metodo_pago_var,
                        value="Tarjeta", style='Body.TLabel',
                        command=self.cambiar_metodo_pago).pack(side="left", padx=5)

        ttk.Separator(main_frame, orient='horizontal').pack(fill='x', pady=10)

        # -------------------
        # Tabla del ticket
        # -------------------
        tree_frame = ttk.Frame(main_frame, padding="5", style='Card.TFrame')
        tree_frame.pack(pady=10, fill='both', expand=True)

        cols = ("nombre", "qty", "precio", "subtotal")
        self.ticket_tree = ttk.Treeview(tree_frame, columns=cols, show="headings")

        widths = {"nombre": 350, "qty": 80, "precio": 120, "subtotal": 120}
        for c in cols:
            self.ticket_tree.heading(c, text=c.capitalize())
            self.ticket_tree.column(c, anchor="center" if c != "nombre" else "w", width=widths.get(c, 100))

        self.ticket_tree.pack(fill='both', expand=True)

        # -------------------
        # Totales y Resumen
        # -------------------
        totals_frame = ttk.Frame(main_frame, style='Card.TFrame')
        totals_frame.pack(pady=10, fill='x')

        inner_totals = ttk.Frame(totals_frame, style='Card.TFrame')
        inner_totals.pack(side='right', anchor='ne')

        self.ticket_subtotal = ttk.Label(inner_totals, text="Subtotal: $0.00",
                                         font=("Helvetica", 13), foreground=COLOR_TEXT, background=COLOR_CARD)
        self.ticket_subtotal.pack(anchor='e')

        self.ticket_descuento = ttk.Label(inner_totals, text="Descuento (10%): $0.00",
                                          font=("Helvetica", 13), foreground=COLOR_SUCCESS, background=COLOR_CARD)
        self.ticket_descuento.pack(anchor='e')

        self.ticket_total = ttk.Label(inner_totals, text="TOTAL: $0.00",
                                      font=("Helvetica", 18, "bold"), foreground=COLOR_PRIMARY, background=COLOR_CARD)
        self.ticket_total.pack(anchor='e', pady=(5, 0))

        self.ticket_metodo = ttk.Label(inner_totals, text="Método de pago: Efectivo",
                                       font=("Helvetica", 11, "italic"), foreground="#7F8C8D", background=COLOR_CARD)
        self.ticket_metodo.pack(anchor='e', pady=(5, 0))

        # -------------------
        # Botones de Acción
        # -------------------
        btn_container = ttk.Frame(main_frame, style='Card.TFrame')
        btn_container.pack(pady=15, fill='x')

        btn_frame = ttk.Frame(btn_container, style='Card.TFrame')
        btn_frame.pack(fill='none', anchor='center')

        # Botón Volver (Columna 0)
        ttk.Button(btn_frame, text="◀️ Volver al Menú", style='Secondary.TButton',
                   command=self.show_main_menu).grid(row=0, column=0, padx=10)

        # Botón Actualizar (Columna 1)
        ttk.Button(btn_frame, text="🔄 Actualizar totales", style='Secondary.TButton',
                   command=self.refresh_ticket).grid(row=0, column=1, padx=10)

        # Botón Imprimir/Finalizar (Columna 2, Estilo Primario)
        ttk.Button(btn_frame, text="🖨️ IMPRIMIR / FINALIZAR", style='Accent.TButton',
                   command=self.print_ticket).grid(row=0, column=2, padx=10, ipadx=20)

        self.refresh_ticket()
        self.cambiar_metodo_pago()

    def toggle_descuento(self):
        """Actualiza el estado del descuento y refresca el ticket"""
        self.descuento_adulto_mayor = self.adulto_mayor_var.get()
        self.refresh_ticket()

    def cambiar_metodo_pago(self):
        """Actualiza el método de pago"""
        self.metodo_pago = self.metodo_pago_var.get()
        self.ticket_metodo.config(text=f"Método de pago: {self.metodo_pago}")

    def refresh_ticket(self):
        # Limpiar tabla
        for item in self.ticket_tree.get_children():
            self.ticket_tree.delete(item)

        if not self.cart:
            self.ticket_subtotal.config(text="Subtotal: $0.00")
            self.ticket_descuento.config(text="Descuento (10%): $0.00", foreground=COLOR_SUCCESS)
            self.ticket_total.config(text="TOTAL: $0.00")
            return

        subtotal = 0
        for item in self.cart:
            item_subtotal = item["costo"] * item["qty"]
            subtotal += item_subtotal
            self.ticket_tree.insert("", "end",
                                    values=(item["nombre"], item["qty"],
                                            money(item["costo"]), money(item_subtotal)))

        # Calcular descuento si aplica
        descuento = 0
        if self.descuento_adulto_mayor:
            descuento = subtotal * 0.10

        total = subtotal - descuento

        # Actualizar labels
        self.ticket_subtotal.config(text=f"Subtotal: {money(subtotal)}")

        if self.descuento_adulto_mayor:
            self.ticket_descuento.config(text=f"Descuento (10%): -{money(descuento)}", foreground=COLOR_ERROR)
        else:
            self.ticket_descuento.config(text="Descuento (10%): $0.00", foreground=COLOR_SUCCESS)

        self.ticket_total.config(text=f"TOTAL: {money(total)}")

    def print_ticket(self):
        if not self.cart:
            messagebox.showinfo("Vacío", "No hay productos para generar ticket.")
            return

        now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        txt = f"{'=' * 50}\n"
        txt += f"           TICKET DE COMPRA\n"
        txt += f"     {CREMERIA_INFO['nombre']}\n"
        txt += f"{'=' * 50}\n"
        txt += f"Fecha: {now}\n"
        txt += f"Método de pago: {self.metodo_pago}\n"
        txt += f"{'-' * 50}\n\n"

        subtotal = 0
        for item in self.cart:
            item_subtotal = item["costo"] * item["qty"]
            subtotal += item_subtotal
            txt += f"{item['qty']} x {item['nombre']}\n"
            txt += f"    {money(item['costo'])} c/u = {money(item_subtotal)}\n\n"

        txt += f"{'-' * 50}\n"
        txt += f"Subtotal: {money(subtotal)}\n"

        if self.descuento_adulto_mayor:
            descuento = subtotal * 0.10
            total = subtotal - descuento
            txt += f"Descuento Adulto Mayor (10%): -{money(descuento)}\n"
            txt += f"{'-' * 50}\n"
            txt += f"TOTAL A PAGAR: {money(total)}\n"
        else:
            txt += f"{'-' * 50}\n"
            txt += f"TOTAL: {money(subtotal)}\n"

        txt += f"{'=' * 50}\n"
        txt += f"\n¡Gracias por su compra!\n"
        txt += f"{CREMERIA_INFO['eslogan']}\n"

        if self.descuento_adulto_mayor:
            txt += f"\n* Descuento para adulto mayor aplicado\n"

        txt += f"* Pagado con: {self.metodo_pago}\n"

        # Ventana del ticket
        win = tk.Toplevel(self)
        win.title("Ticket impreso")
        win.geometry("550x600")
        win.configure(bg=COLOR_CARD)

        text_widget = tk.Text(win, font=("Courier New", 11), bg=COLOR_CARD,
                              wrap="word", padx=20, pady=20, foreground=COLOR_TEXT)
        text_widget.pack(expand=True, fill="both")
        text_widget.insert("1.0", txt)
        text_widget.configure(state="disabled")

        ttk.Button(win, text="Cerrar", style='Secondary.TButton',
                   command=win.destroy).pack(pady=10)


# -------------------
# Ejecutar aplicación
# -------------------
if __name__ == "__main__":
    try:
        print("Creando aplicación...")
        app = CremeriaApp()
        print("Iniciando interfaz gráfica...")
        app.mainloop()
        print("Aplicación cerrada correctamente")
    except Exception as e:
        print(f"\n{'=' * 50}")
        print(f"ERROR CRÍTICO:")
        print(f"{'=' * 50}")
        print(f"{e}")
        import traceback

        traceback.print_exc()
        print(f"{'=' * 50}")
        input("\nPresiona ENTER para cerrar...")