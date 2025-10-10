import tkinter as tk
from core import config

class MainWindow(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent,bg=controller['bg'])

        label = tk.Label(self, text="Bienvenido a Engineering Tools", font=("Arial", 16), bg=controller['bg'], fg="white")
        label.pack(pady=20)
        
        # Botón para abrir la calculadora
        btn_calc = tk.Button(self, text="Abrir Calculadora", command=lambda: controller.show_frame('calculator_ui'))
        btn_calc.pack(pady=10)
        