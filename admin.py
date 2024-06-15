import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import xml.etree.ElementTree as ET
import re
import login

class Nodo:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class ListaDoble:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Nodo(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def __iter__(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def __str__(self):
        usuarios = [str(node) for node in self]
        return "\n".join(usuarios)

class NodoCircular:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class ListaCircularDoble:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = NodoCircular(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
            self.head.prev = self.head
        else:
            tail = self.head.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.head
            self.head.prev = new_node

    def __iter__(self):
        if not self.head:
            return
        current = self.head
        while True:
            yield current.data
            current = current.next
            if current == self.head:
                break

    def __str__(self):
        productos = [str(node) for node in self]
        return "\n".join(productos)

class NodoSimple:
    def __init__(self, data):
        self.data = data
        self.next = None

class ListaCircularSimple:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = NodoSimple(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def __iter__(self):
        if not self.head:
            return
        current = self.head
        while True:
            yield current.data
            current = current.next
            if current == self.head:
                break

    def __str__(self):
        empleados = [str(node) for node in self]
        return "\n".join(empleados)

class NodoOrtogonal:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.down = None

class ListaOrtogonal:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = NodoOrtogonal(data)
        if not self.head:
            self.head = new_node
        else:
            # Insert in a row-wise and column-wise manner
            # Note: Simplified insertion logic, may need adjustments for real use cases
            current = self.head
            while current.down:
                current = current.down
            current.down = new_node

    def __iter__(self):
        current_row = self.head
        while current_row:
            current_col = current_row
            while current_col:
                yield current_col.data
                current_col = current_col.right
            current_row = current_row.down

    def __str__(self):
        actividades = [str(node) for node in self]
        return "\n".join(actividades)

class Usuario:
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")

    def __init__(self, id, password, nombre, edad, email, telefono):
        self.id = id
        self.password = password
        self.nombre = nombre
        self.edad = edad
        self.email = email
        self.telefono = telefono
        self.validate()

    def validate(self):
        if not Usuario.email_regex.match(self.email):
            raise ValueError(f"Email inválido: {self.email}")
        if not self.telefono.isdigit() or len(self.telefono) != 8:
            raise ValueError(f"Teléfono inválido: {self.telefono}")

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Edad: {self.edad}, Email: {self.email}, Teléfono: {self.telefono}"

class Producto:
    def __init__(self, id, nombre, precio, descripcion, categoria, cantidad, imagen):
        self.id = id
        self.nombre = nombre
        self.precio = float(precio.replace(',', ''))
        self.descripcion = descripcion
        self.categoria = categoria
        self.cantidad = int(cantidad)
        self.imagen = imagen
        self.validate()

    def validate(self):
        if not isinstance(self.precio, float):
            raise ValueError(f"Precio inválido: {self.precio}")
        if not isinstance(self.cantidad, int):
            raise ValueError(f"Cantidad inválida: {self.cantidad}")

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Precio: {self.precio}, Descripción: {self.descripcion}, Categoría: {self.categoria}, Cantidad: {self.cantidad}, Imagen: {self.imagen}"

class Empleado:
    def __init__(self, codigo, nombre, puesto):
        self.codigo = codigo
        self.nombre = nombre
        self.puesto = puesto

    def __str__(self):
        return f"Código: {self.codigo}, Nombre: {self.nombre}, Puesto: {self.puesto}"

class Actividad:
    def __init__(self, id, nombre, descripcion, empleado, dia, hora):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.empleado = empleado
        self.dia = int(dia)
        self.hora = int(hora)
        self.validate()

    def validate(self):
        if not (1 <= self.dia <= 7):
            raise ValueError(f"Día inválido: {self.dia}")
        if not (0 <= self.hora <= 23):
            raise ValueError(f"Hora inválida: {self.hora}")

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Descripción: {self.descripcion}, Empleado: {self.empleado}, Día: {self.dia}, Hora: {self.hora}"

class AdminWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("IPC 2 Market - ADMINISTRADOR")
        self.iconbitmap(r"C:\Users\Bryant Herrera\Documents\Repositorios\IPC2_ProyectoVJ2024_201701010\FIUSAC.ico")
        self.geometry("750x500")
        self.resizable(False, False)
        self.config(bg='royalblue4')

        self.center_window()
        self.create_widgets()

        self.usuarios = ListaDoble()
        self.productos = ListaCircularDoble()
        self.empleados = ListaCircularSimple()
        self.actividades = ListaOrtogonal()

        fuente_Personalizada = ("Arial", 12)

    def center_window(self):
        # Dimensiones de la ventana
        ancho_ventana = 750
        alto_ventana = 500

        # Dimensiones de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        x_pos = (ancho_pantalla - ancho_ventana) // 2
        y_pos = (alto_pantalla - alto_ventana) // 2

        # Establecer la geometría de la ventana (ancho x alto + x_pos + y_pos)
        self.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

    def create_widgets(self):
        colorF = 'royalblue4'
        colorL = 'white'
        fuente_Personalizada = ('Verdana', 9, 'bold')


        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)

        self.menu_carga = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_carga.add_command(label="Cargar Usuarios", command=self.cargar_archivo_usuarios)
        self.menu_carga.add_command(label="Cargar Productos", command=self.cargar_archivo_productos)
        self.menu_carga.add_separator()
        self.menu_carga.add_command(label="Cargar Empleados", command=self.cargar_archivo_empleados)
        self.menu_carga.add_command(label="Cargar Actividades", command=self.cargar_archivo_actividades)
        self.menu_bar.add_cascade(label="Cargar Archivos", menu=self.menu_carga)

        #Etiqueta del título:
        label_titulo = tk.Label(self, text='Autorizar Compra', bg=colorF, fg='medium spring green', font=('Comic Sans MS', 30, 'bold'))
        label_titulo.place(x=30, y=30)

        # Crear un Scrollbar
        scrollbar_vertical = tk.Scrollbar(self)
        scrollbar_vertical.grid(row=1, column=1, padx=5, pady=5, sticky='ns')

        #Cuadro de texto de la ventana
        self.txt_compra = tk.Text(self, width=49, height=24, wrap='none', yscrollcommand=scrollbar_vertical.set, font=fuente_Personalizada)
        self.txt_compra.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
        self.txt_compra.place(x=30, y=120)

        # Configurar barras de desplazamiento
        scrollbar_vertical.config(command=self.txt_compra.yview)
        # Cambiar la posición de las barras de desplazamiento
        scrollbar_vertical.place(x=474, y=120, height=340)

        #Botón Aceptar
        btn_aceptar = tk.Button(self, text="Aceptar", font=fuente_Personalizada, bg='turquoise3', command=lambda: messagebox.showinfo("Aceptar", "Operación aceptada."))
        btn_aceptar.place(x=530, y=200, width=180, height=50)

        #Botón Cancelar
        btn_cancelar = tk.Button(self, text="Cancelar", font=fuente_Personalizada, bg='turquoise3', command=self.borrar_texto)
        btn_cancelar.place(x=530, y=280, width=180, height=50)

        #Botón Salir (su función regresa al loadin Screen)
        self.btn_salir = tk.Button(self, text="Salir", command=self.return_to_login, font=fuente_Personalizada, bg='turquoise3')
        self.btn_salir.place(x=530, y=410, width=180, height=50)

    def borrar_texto(self):
        self.txt_compra.delete(1.0, tk.END)

    def cargar_archivo_usuarios(self):
        ruta = filedialog.askopenfilename(title='Cargar Archivo XML de Usuarios', filetypes=[('Archivos XML', '*.xml')])
        if ruta:
            try:
                tree = ET.parse(ruta)
                root = tree.getroot()
                for usuario in root.findall('usuario'):
                    id = usuario.get('id')
                    password = usuario.get('password')
                    nombre = usuario.find('nombre').text
                    edad = usuario.find('edad').text
                    email = usuario.find('email').text
                    telefono = usuario.find('telefono').text
                    nuevo_usuario = Usuario(id, password, nombre, int(edad), email, telefono)
                    self.usuarios.append(nuevo_usuario)
                messagebox.showinfo("Éxito", "Archivo de usuarios cargado correctamente.")
                self.txt_compra.insert(tk.END, str(self.usuarios) + "\n")
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar el archivo de usuarios: {e}")

    def cargar_archivo_productos(self):
        ruta = filedialog.askopenfilename(title='Cargar Archivo XML de Productos', filetypes=[('Archivos XML', '*.xml')])
        if ruta:
            try:
                tree = ET.parse(ruta)
                root = tree.getroot()
                for producto in root.findall('producto'):
                    id = producto.get('id')
                    nombre = producto.find('nombre').text
                    precio = producto.find('precio').text
                    descripcion = producto.find('descripcion').text
                    categoria = producto.find('categoria').text
                    cantidad = producto.find('cantidad').text
                    imagen = producto.find('imagen').text
                    nuevo_producto = Producto(id, nombre, precio, descripcion, categoria, int(cantidad), imagen)
                    self.productos.append(nuevo_producto)
                messagebox.showinfo("Éxito", "Archivo de productos cargado correctamente.")
                self.txt_compra.insert(tk.END, str(self.productos) + "\n")
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar el archivo de productos: {e}")

    def cargar_archivo_empleados(self):
        ruta = filedialog.askopenfilename(title='Cargar Archivo XML de Empleados', filetypes=[('Archivos XML', '*.xml')])
        if ruta:
            try:
                tree = ET.parse(ruta)
                root = tree.getroot()
                for empleado in root.findall('empleado'):
                    codigo = empleado.get('codigo')
                    nombre = empleado.find('nombre').text
                    puesto = empleado.find('puesto').text
                    nuevo_empleado = Empleado(codigo, nombre, puesto)
                    self.empleados.append(nuevo_empleado)
                messagebox.showinfo("Éxito", "Archivo de empleados cargado correctamente.")
                self.txt_compra.insert(tk.END, str(self.empleados) + "\n")
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar el archivo de empleados: {e}")

    def cargar_archivo_actividades(self):
        ruta = filedialog.askopenfilename(title='Cargar Archivo XML de Actividades', filetypes=[('Archivos XML', '*.xml')])
        if ruta:
            try:
                tree = ET.parse(ruta)
                root = tree.getroot()
                for actividad in root.findall('actividad'):
                    id = actividad.get('id')
                    nombre = actividad.find('nombre').text
                    descripcion = actividad.find('descripcion').text
                    empleado = actividad.find('empleado').text
                    dia = actividad.find('dia').text
                    hora = actividad.find('dia').get('hora')
                    nueva_actividad = Actividad(id, nombre, descripcion, empleado, dia, hora)
                    self.actividades.append(nueva_actividad)
                messagebox.showinfo("Éxito", "Archivo de actividades cargado correctamente.")
                self.txt_compra.insert(tk.END, str(self.actividades) + "\n")
            except Exception as e:
                messagebox.showerror("Error", f"Error al cargar el archivo de actividades: {e}")

    def return_to_login(self):
        self.destroy()
        login_app = login.LoginWindow()
        login_app.mainloop()

if __name__ == "__main__":
    admin_app = AdminWindow()
    admin_app.mainloop()
