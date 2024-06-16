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



if __name__ == "__main__":
    user_app = userWindow()
    user_app.mainloop()