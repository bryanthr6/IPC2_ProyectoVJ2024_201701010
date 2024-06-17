import tkinter as tk
from tkinter import messagebox
import admin

class LoginWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("IPC 2 - carnet: 201701010 - Bryant Herrera Rubio")
        self.iconbitmap(r"C:\Users\Bryant Herrera\Documents\Repositorios\IPC2_ProyectoVJ2024_201701010\FIUSAC.ico")
        self.geometry("550x350")
        self.resizable(False, False)
        self.configure(bg='royalblue4')

        self.center_window()  # Centrar la ventana en la pantalla

        # Cargar la imagen del logotipo
        logo_path = r"C:\Users\Bryant Herrera\Documents\Repositorios\IPC2_ProyectoVJ2024_201701010\mercado.png"
        logo = tk.PhotoImage(file=logo_path)
        logo = logo.subsample(4)

        # Crear el label para la imagen
        label_logo = tk.Label(self, image=logo, bg='royalblue4')
        label_logo.image = logo  # Mantener referencia a la imagen para evitar que se elimine por el recolector de basura
        label_logo.place(x=90, y=20)

        self.create_widgets()

    def center_window(self):
        # Dimensiones de la ventana
        ancho_ventana = 550
        alto_ventana = 350

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
        fuente_Personalizada = ('Verdana', 11, 'bold')

        label_titulo = tk.Label(self, text='IPC 2 MARKET', bg=colorF, fg='medium spring green', font=('Comic Sans MS', 20, 'bold'))
        label_titulo.place(x=250, y=60)

        label_username = tk.Label(self, text="Usuario:", bg=colorF, fg=colorL, font=fuente_Personalizada)
        label_username.place(x=65, y=165)

        self.entry_username = tk.Entry(self, font=fuente_Personalizada)
        self.entry_username.place(x=185, y=165, width=270)

        label_password = tk.Label(self, text="Contraseña:", bg=colorF, fg=colorL, font=fuente_Personalizada)
        label_password.place(x=65, y=215)

        self.entry_password = tk.Entry(self, show="*", font=fuente_Personalizada)
        self.entry_password.place(x=185, y=215, width=270)

        button_login = tk.Button(self, text="Ingresar", command=self.login, font=fuente_Personalizada, bg='turquoise3')
        button_login.place(x=205, y=270, width=150, height=40)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        if username == "AdminIPC2" and password == "IPC2VJ2024":
            messagebox.showinfo("Login", "Login exitoso como administrador")
            self.destroy()  # Cierra la ventana de login

            # Abrir la ventana de admin
            admin_app = admin.AdminWindow()
            admin_app.mainloop()
        elif username == "usuario" and password == "contraseña":
            messagebox.showinfo("Login", "Login exitoso como usuario normal")
            self.destroy()  # Cierra la ventana de login
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos")

if __name__ == "__main__":
    app = LoginWindow()
    app.mainloop()
