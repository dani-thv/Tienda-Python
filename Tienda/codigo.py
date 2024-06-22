import tkinter as tk
from tkinter import Image, PhotoImage, font
from tkinter import messagebox
from PIL import ImageTk, Image

#Clases
class Cliente:
    def __init__(self, nombre, apellido, id_cliente):
        self.nombre = nombre
        self.apellido = apellido
        self.id_cliente = id_cliente

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Apellido: {self.apellido}, ID Cliente: {self.id_cliente}"

    # Getters
    def get_nombre(self):
        return self.nombre

    def get_apellido(self):
        return self.apellido

    def get_id_cliente(self):
        return self.id_cliente

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_apellido(self, apellido):
        self.apellido = apellido

    def set_id_cliente(self, id_cliente):
        self.id_cliente = id_cliente

class Categoria:
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar_info(self):
        return f"Nombre: {self.nombre}"

    # Getters
    def get_nombre(self):
        return self.nombre

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def mostrar_info(self):
        return f"Nombre: {self.nombre}, Precio: {self.precio}, Categoria: {self.categoria}"

    # Getters
    def get_nombre(self):
        return self.nombre

    def get_precio(self):
        return self.precio

    def get_categoria(self):
        return self.categoria

    # Setters
    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_precio(self, precio):
        self.precio = precio

    def set_categoria(self, categoria):
        self.categoria = categoria

class Itemorden:
    def __init__(self, producto, cantidad):
        self.producto = producto
        self.cantidad = cantidad
        self.items = []  # lista de items vacía al inicio
        self.total = 0

    def get_producto(self):
        return self.producto

    def get_cantidad(self):
        return self.cantidad

    # Método para calcular el subtotal
    def calcular_subtotal(self):
        return self.producto.get_precio() * self.cantidad

    def __str__(self):
        return f"Producto: {self.producto.get_nombre()}, Cantidad: {self.cantidad}"

    def calcular_total(self):
        self.total = 0
        for item in self.items:
            self.total += item.calcular_subtotal()
        return self.total

class Tienda:
    def __init__(self):
        self.productos = []
        self.clientes = []
        self.items = []
        self.categorias = []

    # Método para registrar un producto
    def registrar_producto(self, producto):
        self.productos.append(producto)

    # Método para registrar un cliente
    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)

    # Método para mostrar productos
    def mostrar_productos(self):
        info_productos = []
        for producto in self.productos:
            info_productos.append(producto.mostrar_info())
        return info_productos

#Interfaz
class Interfaz(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Login")
        self.geometry("520x550")

        self.boton = tk.Button(self, text="SALIR", bg="red", fg="white", font=("Segoe UI Black", 14), command=self.salir)
        self.boton.place(x=430, y=0, width=90, height=40)

        self.icono = tk.Label(self)
        self.icono.img = tk.PhotoImage(file=r"C:\Users\Carla Daniela\Documents\UML\Tiendam\Imagenes\usuario.png")  # Ajusta la ruta de la imagen según tu ubicación
        self.icono.config(image=self.icono.img)
        self.icono.place(x=130, y=40)

        self.id_label = tk.Label(self, text="ID:", font=("Segoe UI Black", 18))
        self.id_label.place(x=240, y=410)

        self.campoid_user = tk.Entry(self)
        self.campoid_user.place(x=150, y=440, width=220, height=30)

        self.jlabeln = tk.Label(self, text="NOMBRE:", font=("Segoe UI Black", 18))
        self.jlabeln.place(x=205, y=340)

        self.camponombre = tk.Entry(self)
        self.camponombre.place(x=150, y=370, width=220, height=30)

        self.entrar = tk.Button(self, text="ENTRAR", bg="green", fg="white", font=("Segoe UI Black", 14), command=self.validar_login)
        self.entrar.place(x=200, y=490, width=120, height=30)



    def salir(self):
        self.destroy()

    def validar_login(self):
        nombre_ingresado = self.camponombre.get()
        id_ingresado = self.campoid_user.get()

        encontrado = False
        for cliente in listaClientes:
            if cliente.nombre == nombre_ingresado and cliente.id_cliente == id_ingresado:
                encontrado = True
                break

        if encontrado:
            messagebox.showinfo("Inicio de Sesión", "Bienvenido!")
            self.withdraw()
            segunda_ventana = SegundaVentana()
            segunda_ventana.mainloop()  # Llamar al método para mostrar la ventana principal
            self.destroy()
        else:
            messagebox.showerror("Error", "Nombre o ID incorrectos")

class SegundaVentana(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title('Tienda')
        w, h = 1024, 600        
        self.centrar_ventana(w, h)  # Llama al método para centrar la ventana
        self.perfil = self.leer_imagen("./imagenes/user.png", (100, 100))
        self.paneles()
        self.controles_barra_superior()
        self.controles_menu_lateral()
        self.controles_cuerpo()
    
    def leer_imagen(self, path, size): 
        return ImageTk.PhotoImage(Image.open(path).resize(size,  Image.ADAPTIVE))  

    def centrar_ventana(self, aplicacion_ancho, aplicacion_largo):
        pantall_ancho = self.winfo_screenwidth()
        pantall_largo = self.winfo_screenheight()
        x = int((pantall_ancho / 2) - (aplicacion_ancho / 2))
        y = int((pantall_largo / 2) - (aplicacion_largo / 2))
        self.geometry(f"{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}")

    def paneles(self):        
         # Crear paneles: barra superior, menú lateral y cuerpo principal
        self.barra_superior = tk.Frame(self, bg="#BEE1EE", height=50)
        self.barra_superior.pack(side=tk.TOP, fill='both')      

        self.menu_lateral = tk.Frame(self, bg="#B6D9E5", width=150)
        self.menu_lateral.pack(side=tk.LEFT, fill='both', expand=False) 
        
        self.cuerpo_principal = tk.Frame(
            self, bg="#ffffff")
        self.cuerpo_principal.pack(side=tk.RIGHT, fill='both', expand=True)
    
    def controles_barra_superior(self):
        # Configuración de la barra superior
        font_awesome = font.Font(family='FontAwesome', size=12)

        # Etiqueta de título
        self.labelTitulo = tk.Label(self.barra_superior, text="Menú")
        self.labelTitulo.config(fg="#000000", font=(
            "Roboto", 15), bg="#BEE1EE", pady=10, width=16)
        self.labelTitulo.pack(side=tk.LEFT)

        # Botón del menú lateral
        self.buttonMenuLateral = tk.Button(self.barra_superior, text="\uf0c9", font=font_awesome,
                                           command=self.toggle_panel, bd=0, bg="#BEE1EE", fg="black")
        self.buttonMenuLateral.pack(side=tk.LEFT)

        # Etiqueta de informacion
        self.labelTitulo = tk.Label(
            self.barra_superior, text="correo@gmail.com")
        self.labelTitulo.config(fg="#000000", font=(
            "Roboto", 10), bg="#BEE1EE", padx=10, width=20)
        self.labelTitulo.pack(side=tk.RIGHT)
    
    def controles_menu_lateral(self):
        # Configuración del menú lateral
        ancho_menu = 20
        alto_menu = 2
        font_awesome = font.Font(family='FontAwesome', size=15)
         
         # Etiqueta de perfil
        self.labelPerfil = tk.Label(
            self.menu_lateral, image=self.perfil, bg="#B6D9E5")
        self.labelPerfil.pack(side=tk.TOP, pady=10)

        # Botones del menú lateral
        self.buttonproductos= tk.Button(self.menu_lateral)        
        self.buttoncomprar = tk.Button(self.menu_lateral)        
        self.buttonorden = tk.Button(self.menu_lateral)       
        self.buttonSettings = tk.Button(self.menu_lateral)

        buttons_info = [
            ("Productos", "🛍️", self.buttonproductos,self.ver_productos),
            ("Comprar", "📤", self.buttoncomprar,self.comprar),
            ("Ordenes", "🛒", self.buttonorden,self.ver_ordenes),
            ("Salir", "❌", self.buttonSettings,self.destroy)
        ]
        for text, icon, button,comando in buttons_info:
            self.configurar_boton_menu(button, text, icon, font_awesome, ancho_menu, alto_menu,comando)                    

    def controles_cuerpo(self):
        # Imagen en el cuerpo principal
        logo_image = Image.open("./imagenes/tendas.png")
        logo_image = logo_image.resize((360, 336), Image.Resampling.LANCZOS)
        self.logo = ImageTk.PhotoImage(logo_image)

        label = tk.Label(self.cuerpo_principal, image=self.logo,
                         bg="#ffffff")
        label.place(x=0, y=0, relwidth=1, relheight=1)

    def configurar_boton_menu(self, button, text, icon, font_awesome, ancho_menu, alto_menu, comando):
        button.config(text=f"  {icon}    {text}", anchor="w", font=font_awesome,
                      bd=0, bg="#B6D9E5", fg="black", width=ancho_menu, height=alto_menu,
                      command = comando)
        button.pack(side=tk.TOP)
        self.bind_hover_events(button)

    def bind_hover_events(self, button):
        # Asociar eventos Enter y Leave con la función dinámica
        button.bind("<Enter>", lambda event: self.on_enter(event, button))
        button.bind("<Leave>", lambda event: self.on_leave(event, button))

    def on_enter(self, event, button):
        # Cambiar estilo al pasar el ratón por encima
        button.config(bg="#9BB9C3")

    def on_leave(self, event, button):
        # Restaurar estilo al salir el ratón
        button.config(bg="#B6D9E5")

    def toggle_panel(self):
        # Alternar visibilidad del menú lateral
        if self.menu_lateral.winfo_ismapped():
            self.menu_lateral.pack_forget()
        else:
            self.menu_lateral.pack(side=tk.LEFT, fill='y')

    def limpiar_cuerpo(self):
        for widget in self.cuerpo_principal.winfo_children():
            widget.destroy()

    def ver_productos(self):
        self.limpiar_cuerpo()

        # Crear un frame para contener el cuadro de texto y las barras de desplazamiento
        frame_texto = tk.Frame(self.cuerpo_principal)
        frame_texto.pack(fill=tk.BOTH, expand=True, padx=30, pady=30)

        # Crear barra de desplazamiento vertical
        scroll_y = tk.Scrollbar(frame_texto, orient=tk.VERTICAL)
        scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

        # Crear barra de desplazamiento horizontal
        scroll_x = tk.Scrollbar(frame_texto, orient=tk.HORIZONTAL)
        scroll_x.pack(side=tk.BOTTOM, fill=tk.X)

        # Crear cuadro de texto con barras de desplazamiento
        cuadro_texto = tk.Text(frame_texto, wrap="none", width=100, height=20,
                               yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        cuadro_texto.pack(fill=tk.BOTH, expand=True)

        scroll_y.config(command=cuadro_texto.yview)
        scroll_x.config(command=cuadro_texto.xview)

        for producto in lista_productos:
            info_producto = (
                f"Nombre: {producto.get_nombre()}\n"
                f"Precio: {producto.get_precio()}\n"
                f"Categoría: {producto.get_categoria()}\n\n"
            )
            cuadro_texto.insert(tk.END, info_producto)
        
        cuadro_texto.config(state=tk.DISABLED)
    def comprar(self):

        self.limpiar_cuerpo()
        def comprando():
            nombre_producto = self.entry_produc.get().strip()
            cantidad_text = self.entry_cantidad.get().strip()

            try:
                cantidad = int(cantidad_text)
                if cantidad <= 0:
                    messagebox.showerror("Error", "Por favor, ingrese una cantidad positiva")
                    return
            except ValueError:
                messagebox.showerror("Error", "Por favor, ingrese una cantidad válida")
                return

            producto_encontrado = False
            producto_seleccionado = None
            
            for producto in lista_productos:
                if producto.get_nombre().lower() == nombre_producto.lower():
                    producto_encontrado = True
                    producto_seleccionado = producto
                    break

            if not producto_encontrado:
                messagebox.showerror("Error", "El nombre del producto ingresado no existe")
            else:
                lista_items.append(Itemorden(producto_seleccionado, cantidad))
                messagebox.showinfo("Éxito", "Compra realizada exitosamente")
                self.entry_produc.delete(0, tk.END)
                self.entry_cantidad.delete(0, tk.END)

        self.label_produc = tk.Label(self.cuerpo_principal, text="Producto:", font=("Helvetica", 12), bg="#ffffff")
        self.label_produc.pack(pady=5)
        self.entry_produc = tk.Entry(self.cuerpo_principal)
        self.entry_produc.pack(pady=5)

        self.label_cantidad = tk.Label(self.cuerpo_principal, text="Cantidad:", font=("Helvetica", 12), bg="#ffffff")
        self.label_cantidad.pack(pady=5)
        self.entry_cantidad = tk.Entry(self.cuerpo_principal)
        self.entry_cantidad.pack(pady=5)

        # Botón para confirmar la compra
        self.btn_confirmar_compra = tk.Button(self.cuerpo_principal, text="Comprar", command=comprando)
        self.btn_confirmar_compra.pack(pady=10)

    def ver_ordenes(self):
        self.limpiar_cuerpo()

        self.cuadro_texto = tk.Text(self.cuerpo_principal, wrap="word", width=100, height=20)
        self.cuadro_texto.pack(padx=30, pady=30)

        for itemorden in lista_items:
            producto = itemorden.get_producto()
            info_item = (
                f"Nombre: {producto.get_nombre()}\n"
                f"Precio: {producto.get_precio()}\n"
                f"Categoría: {producto.get_categoria()}\n"
                f"Cantidad: {itemorden.get_cantidad()}\n\n"
            )
            self.cuadro_texto.insert(tk.END, info_item)
        
        self.cuadro_texto.config(state=tk.DISABLED)

        def calcular_total(lista_items):
            total = 0
            for item in lista_items:
                total += item.get_producto().get_precio() * item.get_cantidad()
            return total

        def mostrar_total():
            total = calcular_total(lista_items)
            messagebox.showinfo("Total", f"El total de las órdenes es: {total}")

        self.btn_total = tk.Button(self.cuerpo_principal, text="Total", command=mostrar_total)
        self.btn_total.pack(pady=10)


if __name__ == "__main__":
    listaClientes = [
        Cliente("Juan", "Perez", "001"),
        Cliente("Maria", "Gonzalez", "002"),
        Cliente("Pedro", "Martinez", "003"),
        Cliente("Ana", "Lopez", "004"),
        Cliente("Carlos", "Garcia", "005"),
        Cliente("Luisa", "Rodriguez", "006"),
        Cliente("Javier", "Sanchez", "007"),
        Cliente("Laura", "Diaz", "008"),
        Cliente("Miguel", "Hernandez", "009"),
        Cliente("Sofia", "Torres", "010")
    ]

    lista_productos = [
            Producto("Arroz", 5000.0, "Despensa"),
            Producto("Huevos", 16000.0, "Despensa"),
            Producto("Azúcar", 4800.0, "Despensa"),
            Producto("Queso", 12000.0, "Lácteos"),
            Producto("Yogur", 4000.0, "Lácteos"),
            Producto("Pan", 2500.0, "Panadería"),
            Producto("Pollo", 15000.0, "Carnicería"),
            Producto("Pescado", 18000.0, "Pescadería"),
            Producto("Manzanas", 3500.0, "Frutas y Verduras"),
            Producto("Plátanos", 3000.0, "Frutas y Verduras"),
            Producto("Zanahorias", 2000.0, "Frutas y Verduras"),
            Producto("Galletas", 4500.0, "Snacks"),
            Producto("Papas fritas", 3000.0, "Snacks"),
            Producto("Refresco", 2500.0, "Bebidas"),
            Producto("Jabón", 2000.0, "Higiene"),
            Producto("Shampoo", 7000.0, "Higiene")
        ]
    lista_items = [

    ]
    app = Interfaz()
    app.mainloop()