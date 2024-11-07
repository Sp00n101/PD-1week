class InvalidArgumentsCountError(Exception):
    def __init__(self, count):
        super().__init__(f"INVALID_ARGUMENTS_COUNT: Expected at least 2 arguments, but got {count}.")
        self.count = count


class InvalidArgumentError(Exception):
    def __init__(self, argument):
        super().__init__(f"INVALID_ARGUMENT: '{argument}' is not a valid number.")
        self.argument = argument


def custom_sum(*args):
    if len(args) < 2:
        raise InvalidArgumentsCountError(len(args))

    for arg in args:
        if not isinstance(arg, (int, float)):
            raise InvalidArgumentError(arg)

    return sum(args)


try:
    print(custom_sum(1, 2, 3))
except (InvalidArgumentsCountError, InvalidArgumentError) as e:
    print(e)

try:
    print(custom_sum(0, 1, '1', 2))
except (InvalidArgumentsCountError, InvalidArgumentError) as e:
    print(e)

try:
    print(custom_sum())
except (InvalidArgumentsCountError, InvalidArgumentError) as e:
    print(e)
