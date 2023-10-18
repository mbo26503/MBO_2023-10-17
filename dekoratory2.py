def uppercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()

    return wrapper


@uppercase_decorator
def greeting():
    return "hello, world!"


print(greeting())