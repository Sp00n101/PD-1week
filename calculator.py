class InvalidArgumentError(Exception):
    def __init__(self, argument):
        super().__init__(f"INVALID_ARGUMENT: '{argument}' is not valid.")
        self.argument = argument

class UnknownOperationError(Exception):
    def __init__(self, operation):
        super().__init__(f"UNKNOWN_OPERATION: '{operation}' is not defined.")
        self.operation = operation

class Calculator:
    def __init__(self):
        self.operations = {}

    def add_method(self, operation, func):
        if not isinstance(operation, str) or not callable(func):
            raise InvalidArgumentError((operation, func))
        self.operations[operation] = func

    def calculate(self, expression):
        if not isinstance(expression, str):
            raise InvalidArgumentError(expression)

        parts = expression.split()
        if len(parts) != 3:
            raise InvalidArgumentError(parts)

        a, operator, b = parts

        try:
            a = float(a)
            b = float(b)
        except ValueError:
            raise InvalidArgumentError((a, b))

        if operator not in self.operations:
            raise UnknownOperationError(operator)

        return self.operations[operator](a, b)


calc = Calculator()

calc.add_method("+", lambda a, b: a + b)
calc.add_method("-", lambda a, b: a - b)
calc.add_method("*", lambda a, b: a * b)
calc.add_method("/", lambda a, b: a / b if b != 0 else "Error: DIVISION_BY_ZERO")
calc.add_method("**", lambda a, b: a ** b)


try:
    print(calc.calculate("12 + 4"))
    print(calc.calculate("5 - 3"))
    print(calc.calculate("2 * 3"))
    print(calc.calculate("8 / 2"))
    print(calc.calculate("2 ** 3"))
    print(calc.calculate("h - 10"))
except (InvalidArgumentError, UnknownOperationError) as e:
    print(e)

try:
    print(calc.calculate("3 * 5"))
    print(calc.calculate("1 + 3"))
    print(calc.calculate("2 / 0"))
except (InvalidArgumentError, UnknownOperationError) as e:
    print(e)

try:
    print(calc.add_method(1, lambda a, b: a + b))
except InvalidArgumentError as e:
    print(e)

try:
    print(calc.add_method("+", 10))
except InvalidArgumentError as e:
    print(e)

try:
    print(calc.calculate("2 ^ 3"))
except (InvalidArgumentError, UnknownOperationError) as e:
    print(e)
