class CalculatorLogic:
    def __init__(self):
        self.expression = ""

    def add_char(self, char: str) -> str:
        """Agrega un carácter a la expresión."""
        self.expression += str(char)
        return self.expression

    def clear(self) -> str:
        """Limpia la expresión."""
        self.expression = ""
        return self.expression

    def evaluate(self) -> str:
        """Evalúa la expresión matemática."""
        try:
            result = str(eval(self.expression))
            self.expression = result  # Permite seguir calculando desde el resultado
            return result
        except Exception:
            self.expression = ""
            return "Error"
