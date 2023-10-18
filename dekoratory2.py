def uppercase_decorator(function):
    def wrapper():
        result = function()
        return result.upper()

    return wrapper

def bold_decorator(function):
    def wrapper():
        result = function()
    #    return f"<b>{result}</b>"  # nie działa na konsoli Windows
        return f"\033[1m" + "Tekst" + "\033[0m"  # to działa

    return wrapper

@bold_decorator
@uppercase_decorator
def greeting():
    return "hello, world!"


print(greeting())