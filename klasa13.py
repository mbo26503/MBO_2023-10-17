# 19/10/2023 14:42
# własna obsługa błędów
class MyError(Exception):  # klasa dziedziczy po klaszie Exception
    def __init__(self, message, err_code):
        super().__init__(message)
        self.err_code = err_code


class MyValueError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=100)


class MyTypeError(MyError):
    def __init__(self, message):
        super().__init__(message, err_code=200)


def my_function(x: int, y):
    if not isinstance(x, int):
        raise MyTypeError("x must be integer")
    if y == 0:
        raise MyValueError("y cannot be zero")
    return x / y


print("my_function: ", my_function(2,5))

try:
    result = my_function(5, 0)
except MyValueError as e:
    print("Caught a MyValueError", e)
    print ("Error code", e.err_code)
except MyTypeError as e:
    print("Caught a MyTypeError", e)
    print("Error code", e.err_code)
except MyTypeError as e:
    print("Caught a MyTypeError", e)
    print("Error code", e.err_code)