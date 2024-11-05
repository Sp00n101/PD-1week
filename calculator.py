class Calculator:
    def __init__(self):
        self.operations = {}

    def add_method(self, operation, func):
        if not isinstance(operation, str) or not callable(func):
            return "Error: INVALID_ARGUMENT"
        self.operations[operation] = func

    def calculate(self, expression):
        if not isinstance(expression, str):
            return "Error: INVALID_ARGUMENT"

        parts = expression.split()
        if len(parts) != 3:
            return "Error: INVALID_ARGUMENT"

        a, operator, b = parts

        try:
            a = float(a)
            b = float(b)
        except ValueError:
            return "Error: INVALID_ARGUMENT"

        if operator not in self.operations:
            return "Error: UNKNOWN_OPERATION"

        return self.operations[operator](a, b)


calc = Calculator()

calc.add_method("+", lambda a, b: a + b)
calc.add_method("-", lambda a, b: a - b)
calc.add_method("*", lambda a, b: a * b)
calc.add_method("/", lambda a, b: a / b if b != 0 else "Error: DIVISION_BY_ZERO")
calc.add_method("**", lambda a, b: a ** b)

print(calc.calculate("12 + 4"))
print(calc.calculate("5 - 3"))
print(calc.calculate("2 * 3"))
print(calc.calculate("8 / 2"))
print(calc.calculate("2 ** 3"))
print(calc.calculate("h - 10"))
print(calc.calculate("3 * 5"))
print(calc.calculate("1 + 3"))
print(calc.calculate("2 / 0"))
print(calc.add_method(1, lambda a, b: a + b))
print(calc.add_method("+", 10))
print(calc.calculate("2 ^ 3"))
