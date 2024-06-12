import tkinter as tk
from tkinter import messagebox

def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Aquí puedes agregar la lógica para validar las credenciales
    if username == "AdminIPC2" and password == "IPC2VJ2024":
        messagebox.showinfo("Inicio de sesión", "Inicio de sesión exitoso")
    else:
        messagebox.showerror("Error", "Usuario o contraseña incorrectos")

# Crear la ventana principal
root = tk.Tk()
root.title("IPC 2 - carnet: 201701010 - Bryant Herrera Rubio")

#Todo esto es para que la ventana aparezca en el centro de la pantalla donde se ejecuta
ancho_ventana = 550
alto_ventana = 350
#Se obtiene informacion de las dimensiones de la pantalla donde se ejecuta el programa (Si es en windows)
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()
#Calcular las coordenadas en posición x & y de la pantalla
x_pos = (ancho_pantalla - ancho_ventana) // 2
y_pos = ((alto_pantalla - alto_ventana) // 2) - 40
#Centrar la ventana
root.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

# Cambiar el icono de la ventana
root.iconbitmap(r"C:\Users\Bryant Herrera\Documents\Repositorios\IPC2_ProyectoVJ2024_201701010\FIUSAC.ico")

#Color de fondo de la ventana
colorF = 'royalblue4'
colorL = 'white'
fuente_Personalizada = ('Verdana',11, 'bold')
root.configure(bg=colorF)

#Evitar que la ventana se pueda redimensionar
root.resizable(False ,False)


# Crear y colocar los widgets

label_titulo = tk.Label(root, text='IPC 2 MARKET', bg=colorF, fg='medium spring green' ,font= ('Comic Sans MS', 20, 'bold'))
label_titulo.place(x=250, y=60)

# Cargar la imagen del logotipo
logo = tk.PhotoImage(file=r"C:\Users\Bryant Herrera\Documents\Repositorios\IPC2_ProyectoVJ2024_201701010\mercado.png")
logo = logo.subsample(4)

# Crear y colocar los widgets
label_logo = tk.Label(root, image=logo, bg=colorF)
label_logo.place(x=90, y=20)


label_username = tk.Label(root, text="Usuario:", bg=colorF, fg=colorL, font=fuente_Personalizada)
label_username.grid(row=0, column=0, padx=5, pady=5, sticky='w')
label_username.place(x=65, y=165)

entry_username = tk.Entry(root, font=fuente_Personalizada)
entry_username.grid(row=1, column=0, padx=5, pady=5, sticky='ew')
entry_username.place(x=185 ,y=165, width=270 )

label_password = tk.Label(root, text="Contraseña:", bg= colorF, fg=colorL, font=fuente_Personalizada)
label_password.grid(row=0, column=0, padx=5, pady=5, sticky='w')
label_password.place(x=65, y=215)

entry_password = tk.Entry(root, show="*", font=fuente_Personalizada)
entry_password.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
entry_password.place(x=185 ,y=215, width= 270) 

button_login = tk.Button(root, text="Iniciar sesión", command=login, font=fuente_Personalizada, bg='turquoise3')
button_login.place(x=205 , y=270, width= 150, height=40 )

#Esto es para que cambie de color cuando presiona el usuario presiona el botón
def cambiar_color_entrada(event):
    button_login.config(bg='turquoise1')
def cambiar_color_salida(event):
    button_login.config(bg='turquoise3')

button_login.bind('<Enter>', cambiar_color_entrada)
button_login.bind('<Leave>', cambiar_color_salida)

# Iniciar el bucle principal de la interfaz gráfica
root.mainloop()
