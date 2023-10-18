def f():
    print("Funkcja 1")
    def fwew(a, b):
        return a * b
    return fwew  # bez nawiasób bo zwracamy tylko adres funkji a nie wynik działania

x = f()
print(type(x))  # <class 'function'>
print(x)  # <function f.<locals>.fwew at 0x00000233E56A8AE0>

print(x(6, 7))  # 42



