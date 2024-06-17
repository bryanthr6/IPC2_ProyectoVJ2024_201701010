import tkinter as tk
import login

class userWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("IPC 2 Market - USUARIO")
        self.iconbitmap(r"C:\Users\Bryant Herrera\Documents\Repositorios\IPC2_ProyectoVJ2024_201701010\FIUSAC.ico")
        self.geometry("750x500")
        self.resizable(False,False)
        self.config(bg='royalblue4')

        self.center_window()
        self.create_widgets()


    def center_window(self):
        #Dimensiones de la ventana
        ancho_ventana = 750
        alto_ventana = 500

        #Dimensiones de la pantalla
        ancho_pantalla = self.winfo_screenwidth()
        alto_pantalla = self.winfo_screenheight()

        #Calcular las coordenadas para centrar la ventana
        x_pos = (ancho_pantalla - ancho_ventana) // 2
        y_pos = (alto_pantalla - alto_ventana) // 2

        #Establecer la geometría de la ventana
        self.geometry(f"{ancho_ventana}x{alto_ventana}+{x_pos}+{y_pos}")

    def create_widgets(self):
        fuente_Personalizada = ('Verdana', 11, 'bold')

        #Crear un botón de salir o regresar al menú de login screen
        btn_salir = tk.Button(self, text="salir", font=fuente_Personalizada, bg='turquoise3', command=self.return_to_login)
        btn_salir.place(x=200, y=200, width=150, height=40)

    def return_to_login(self):
        self.destroy()
        login_app = login.LoginWindow()
        login_app.mainloop()



if __name__ == "__main__":
    user_app = userWindow()
    user_app.mainloop()