import tkinter as tk
from tkinter import messagebox
import login

class AdminWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("IPC 2 Market - ADMINISTRADOR")
        self.iconbitmap(r"C:\Users\Bryant Herrera\Documents\Repositorios\IPC2_ProyectoVJ2024_201701010\FIUSAC.ico")
        self.geometry("750x500")
        self.resizable(False, False)
        self.configure(bg='royalblue4')

        self.center_window()
        self.create_widgets()

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

        # Etiqueta del título
        label_titulo = tk.Label(self, text='Autorizar Compra', bg=colorF, fg='medium spring green', font=('Comic Sans MS', 30, 'bold'))
        label_titulo.place(x=30, y=30)

        # Crear el menú principal
        self.menu_bar = tk.Menu(self)
        self.config(menu=self.menu_bar)  # Configurar el menú principal

        # Crear el menú "Cargar" y añadir opciones
        self.menu_carga = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_carga.add_command(label="Cargar Usuarios")
        self.menu_carga.add_separator()
        self.menu_carga.add_command(label="Cargar Productos")

        
        #Menú de reportes
        self.menu_reportes = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_reportes.add_command(label="Reporte de Usuarios")
        self.menu_reportes.add_command(label="Reporte de Productos")
        self.menu_reportes.add_separator()
        self.menu_reportes.add_command(label="Reporte de Cola")
        self.menu_reportes.add_command(label="Reporte de Compras")

        # Agregar el menú "Cargar" y "Reportes" al menú principal
        self.menu_bar.add_cascade(label="Cargar", menu=self.menu_carga)
        self.menu_bar.add_cascade(label="Reportes", menu=self.menu_reportes)

        # Crear un Scrollbar
        scrollbar_vertical = tk.Scrollbar(self)
        scrollbar_vertical.grid(row=1, column=1, padx=5, pady=5, sticky='ns')

        # Textbox que muestra lo subido
        self.txt_compra = tk.Text(self, width=49, height=24, wrap='none', yscrollcommand=scrollbar_vertical.set, font=fuente_Personalizada)
        self.txt_compra.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
        self.txt_compra.place(x=30, y=120)

        # Configurar barras de desplazamiento
        scrollbar_vertical.config(command=self.txt_compra.yview)
        # Cambiar la posición de las barras de desplazamiento
        scrollbar_vertical.place(x=474, y=120, height=340)

        # Configurar boton actividades
        btn_actividad = tk.Button(self, text="Ver Actividades de Hoy", font=fuente_Personalizada, justify="center", wraplength=110, bg='turquoise3')
        btn_actividad.place(x=530, y=30, width=180, height=70)

        # Configurar botón aceptar
        btn_aceptar = tk.Button(self, text="Aceptar", font=fuente_Personalizada, bg='turquoise3')
        btn_aceptar.place(x=530, y=200, width=180, height=50)

        # Configurar botón Cancelar
        btn_cancelar = tk.Button(self, text="Cancelar", font=fuente_Personalizada, bg='turquoise3', command=self.borrar_texto)
        btn_cancelar.place(x=530, y=280, width=180, height=50)

        # Botón que regrese al menú de login
        self.btn_salir = tk.Button(self, text="Salir", command=self.return_to_login, font=fuente_Personalizada, bg='turquoise3')
        self.btn_salir.place(x=530, y=410, width=180, height=50)

    def borrar_texto(self):
        self.txt_compra.delete(1.0, tk.END)

    def return_to_login(self):
        self.destroy()  # Cierra la ventana de admin

        # Abrir la ventana de login nuevamente
        login_app = login.LoginWindow()
        login_app.mainloop()

if __name__ == "__main__":
    admin_app = AdminWindow()
    admin_app.mainloop()
