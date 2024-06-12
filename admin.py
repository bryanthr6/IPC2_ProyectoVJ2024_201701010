import tkinter as tk


#Funciones estéticas para cambiar el color del botón al pasar el puntero sobre ellos
def cambiar_color_entrada1(event):
    btn_actividad.config(bg="turquoise1")
def cambiar_color_entrada2(event):
    btn_aceptar.config(bg="turquoise1")
def cambiar_color_entrada3(event):
    btn_cancelar.config(bg="turquoise1")
def cambiar_color_entrada4(event):
    btn_salir.config(bg="turquoise1")
def cambiar_color_salida1(event):
    btn_actividad.config(bg="turquoise3")
def cambiar_color_salida2(event):
    btn_aceptar.config(bg="turquoise3")
def cambiar_color_salida3(event):
    btn_cancelar.config(bg="turquoise3")
def cambiar_color_salida4(event):
    btn_salir.config(bg="turquoise3")


def ejemplo():
    print("hola mundo")

def borrar_texto():
    txt_compra.delete(1.0, tk.END)

# Crear la ventana principal
raiz = tk.Tk()
raiz.title("IPC 2 Market - ADMINISTRADOR")

#Todo esto es para que la ventana aparezca en el centro de la pantalla donde se ejecuta
ancho_ventana = 750
alto_ventana = 500
#Se obtiene informacion de las dimensiones de la pantalla donde se ejecuta el programa (Si es en windows)
ancho_pantalla = raiz.winfo_screenwidth()
alto_pantalla = raiz.winfo_screenheight()
#Calcular las coordenadas en posición x & y de la pantalla
x_pos = (ancho_pantalla - ancho_ventana) // 2
y_pos = ((alto_pantalla - alto_ventana) // 2) - 40
#Centrar la ventana
raiz.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

# Cambiar el icono de la ventana
raiz.iconbitmap(r"C:\Users\Bryant Herrera\Documents\Repositorios\IPC2_ProyectoVJ2024_201701010\FIUSAC.ico")

#Color de fondo de la ventana
colorF = 'royalblue4'
colorL = 'white'
fuente_Personalizada = ('Verdana',9, 'bold')
raiz.configure(bg=colorF)

#Evitar que la ventana se pueda redimensionar
raiz.resizable(False ,False)

# Etiqueta del título
label_titulo = tk.Label(raiz, text='Autorizar Compra', bg=colorF, fg='medium spring green' ,font= ('Comic Sans MS', 30, 'bold'))
label_titulo.place(x=30, y=30)

#Crear widget cargar
menu_bar = tk.Menu(raiz)

#Menú de cargar
menu_carga = tk.Menu(menu_bar, tearoff=0)
menu_carga.add_command(label="Cargar Usuarios", command=ejemplo)
menu_carga.add_separator()
menu_carga.add_command(label="Cargar Productos")

#Menú de reportes
menu_reportes = tk.Menu(menu_bar, tearoff=0)
menu_reportes.add_command(label="Reporte de Usuarios")
menu_reportes.add_command(label="Reporte de Productos")
menu_reportes.add_separator()
menu_reportes.add_command(label="Reporte de Cola")
menu_reportes.add_command(label="Reporte de Compras")


# Agregar el menú "Cargar" al menú principal
menu_bar.add_cascade(label="Cargar", menu=menu_carga)
menu_bar.add_cascade(label="Reportes", menu=menu_reportes)

# Asociar el menú con la ventana principal
raiz.config(menu=menu_bar)

#Crear un Scrollbar
scrollbar_vertical=tk.Scrollbar(raiz)
scrollbar_vertical.grid(row=1, column=1, padx=5, pady=5, sticky='ns')
# Crear y colocar los widgets
txt_compra = tk.Text(raiz, width= 49, height=24, wrap='none', yscrollcommand=scrollbar_vertical.set, font=fuente_Personalizada)
txt_compra.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
txt_compra.place(x=30, y=120)

#Configurar barras de desplazamiento
scrollbar_vertical.config(command=txt_compra.yview)
#Cambiar la posición de las barras de desplazamiento
scrollbar_vertical.place(x=474, y=120, height=340)

#Configurar boton actividades
btn_actividad = tk.Button(raiz, text="Ver Actividades de Hoy", font=fuente_Personalizada, justify="center", wraplength=110, bg='turquoise3')
btn_actividad.place(x=530, y=30, width=180, height=70)

#Configurar botón aceptar
btn_aceptar = tk.Button(raiz, text="Aceptar", font=fuente_Personalizada, bg='turquoise3')
btn_aceptar.place(x=530, y=200, width=180, height=50)

#Configurar botón Cancelar (Esto es para vaciar lo que haya en el texbox)
btn_cancelar = tk.Button(raiz, text="Cancelar", font=fuente_Personalizada, bg='turquoise3', command=borrar_texto)
btn_cancelar.place(x=530, y=280, width=180, height=50)

#Configurar botón Salir (Esto es para regresar al loggin screen de main.py)
btn_salir = tk.Button(raiz, text="Salir", font=fuente_Personalizada, bg='turquoise3')
btn_salir.place(x=530, y=410, width=180, height=50)

#Aca se aplica la función de cambiar los colores de los botones al pasar el puntero sobre ellos
btn_actividad.bind('<Enter>', cambiar_color_entrada1)
btn_actividad.bind('<Leave>', cambiar_color_salida1)
btn_aceptar.bind('<Enter>', cambiar_color_entrada2)
btn_aceptar.bind('<Leave>', cambiar_color_salida2)
btn_cancelar.bind('<Enter>', cambiar_color_entrada3)
btn_cancelar.bind('<Leave>', cambiar_color_salida3)
btn_salir.bind('<Enter>', cambiar_color_entrada4)
btn_salir.bind('<Leave>', cambiar_color_salida4)


#Iniciar el bucle principal de la interfaz gráfica
raiz.mainloop()
