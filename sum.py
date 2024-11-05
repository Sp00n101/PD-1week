class InvalidArgumentsCountError(Exception):
    pass

class InvalidArgumentError(Exception):
    pass

def custom_sum(*args):
    try:
        if len(args) < 2:
            raise InvalidArgumentsCountError("INVALID_ARGUMENTS_COUNT")

        for arg in args:
            if not isinstance(arg, (int, float)):
                raise InvalidArgumentError("INVALID_ARGUMENT")

        return sum(args)

    except (InvalidArgumentsCountError, InvalidArgumentError) as e:
        return str(e)


print(custom_sum(1, 2, 3))
print(custom_sum())
print(custom_sum(0, 1, '1', 2))

