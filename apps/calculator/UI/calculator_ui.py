import tkinter as tk
from core import config
from apps.calculator.logic.operations import CalculatorLogic

class CalculatorUI(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent,bg=controller['bg'])
        
        # Instancia de la lógica
        self.logic = CalculatorLogic()
        self.text_input = tk.StringVar()
        
        # Pantalla de entrada
        entry = tk.Entry(self, font=("Arial", 18), textvariable=self.text_input, justify="right")
        entry.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=5, pady=5)
        
        # Botones
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("C", 5, 0), ("Volver", 5, 1, 3)
        ]

        for btn in buttons:
            text, row, col, *span = btn
            colspan = span[0] if span else 1
            b = tk.Button(
                self, text=text, font=("Arial", 14),
                command=lambda t=text: self.on_button_click(t)
            )
            b.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=2, pady=2)
        
        # Configurar pesos de filas y columnas
        for i in range(6):
            self.grid_rowconfigure(i, weight=1)
        for j in range(4):
            self.grid_columnconfigure(j, weight=1)
        
        # Guardar referencia al controlador (para volver al menú principal)
        self.controller = controller    

    def on_button_click(self, char):
        """Maneja la interacción de los botones."""
        if char == "=":
            result = self.logic.evaluate()
            self.text_input.set(result)
        elif char == "C":
            self.logic.clear()
            self.text_input.set("")
        elif char == "Volver":
            self.controller.show_frame('MainWindow')
        else:
            result = self.logic.add_char(char)
            self.text_input.set(result)