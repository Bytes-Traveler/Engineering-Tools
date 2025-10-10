import tkinter as tk
import core.config as config
from apps.calculator.UI.calculator_ui import CalculatorUI
from core.main_windows import MainWindow

class App(tk.Tk):
    
    def __init__(self):
        super().__init__()

        # Configuración básica de la ventana
        self.title("Engineering Tools")
        self.configure(bg=config.BG_COLOR)
        
        # Desactivar redimensionar y maximizar
        self.resizable(False, False)
        
        # Contenedor donde se cargan las pantallas
        self.container = tk.Frame(self, bg=config.BG_COLOR)
        self.container.grid(row=0, column=0, sticky="nsew")
        
        # Permitir que el contenedor se expanda
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        
        # Diccionario de pantallas
        self.frames = {
            'MainWindow': MainWindow,
            'calculator_ui': CalculatorUI,
        }
        
        # Mostrar pantalla
        self.show_frame('MainWindow')
        
    def show_frame(self, frame_key):

        # Limpiar el contenedor
        for widget in self.container.winfo_children():
            widget.destroy()

        # Crear y mostrar el nuevo frame
        frame_class = self.frames[frame_key]
        frame = frame_class(self.container, self)
        frame.grid(row=0, column=0, sticky="nsew")
        

if __name__ == '__main__':
    app = App()
    app.mainloop()