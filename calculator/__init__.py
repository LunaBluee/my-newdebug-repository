Number = int | float


class Calculator:

    def __init__(self):
        self.expression = ""

    def _ensure_is_digit(self, value: int | str):
        if isinstance(value, str):
            value = int(value)
        if value not in range(10):
            raise ValueError("Value must a digit in [0, 9]: " + value)
        return value

    def _append(self, value):
        self.expression += str(value)
    
    def digit(self, value: int | str):
        value = self._ensure_is_digit(value)
        self._append(value)
    
    def plus(self):
        self._append("+")

    def minus(self):
        self._append("-")
    
    def multiply(self):
        self._append("*")
    
    def divide(self):
        self._append("/")

    def dot(self):
        self._append(".")

    def clear_expression(self):
        self.expression = ""  

    def __init__(self):
        # Your existing initialization code here
        self.history = []  # Initialize an empty list to store history

    def add_to_history(self, expression, result):
        self.history.append(f"{expression} = {result}")

    def clear_history(self):
        self.history.clear()

    # Update your compute_result or similar method to add successful calculations to history
    def compute_result(self):
        # Your existing result computation logic here
        result = "some computation"  # Placeholder for actual computation result
        self.add_to_history(self.expression, result)
        return result
    
    def compute_result(self) -> Number:
        try:
            result = eval(self.expression)
            if isinstance(result, Number):
                self.expression = str(result)
                return result
            else:
                raise ValueError("Result is not a number: " + str(result))
        except Exception as e:
            expression = self.expression
            self.expression = ""
            raise ValueError("Invalid expression: " + expression) from e
