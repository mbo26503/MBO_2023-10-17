generator_1 = (x for x in [1, 2, 3, 5])
print(type(generator_1))  # <class 'generator'>

print(next(generator_1))
print(next(generator_1))
print(next(generator_1))
print(next(generator_1))


def generator2():  # tworzenie nieskończonego generaota bez koneczności obciążania systemu
    i = 1  # licznik jest inicjowany tylko przy pierwszym użyciu generatora
    while True:
        yield i * i
        i += 1


def fibo():
    a,b = 0, 1  # zmienne są inicjowany tylko raz przy pierwszym wejścio do generatora
    while True:  # pętla jest niby nieskończona, ale słówko yield przerywa tą pętlę
        yield b  # słówko yield służy do zapamiętania wartości i wyjścia z pętli
        a, b = b, a + b

def fibo_with_index(n):
    a, b = 0, 1
    for idx in range(n):
        yield idx, a
        a, b = b, a + b

# x = idx, a - tupla(krotka)


print("----------------")
g = generator2()
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print("----------------")
fib = fibo()
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print('------------------')
print(next(fib))
print(next(fib))
print(next(fib))

# przerwa od 14:48 do 14:55
for i in fibo_with_index(10):
    print(f"element: {i} ")

for i, n in fibo_with_index(10):
    print(f"pozycja: {i}: {n}")

    print("-----------------------")

    # kolejny generator
    def counter(start=0):
        n = start
        while True:
            result = yield n
            print(result)
            if result == 'q': # sterowanie generatorem
                break
            n += 1

try:
    c = counter(10)
    print(next(c))
    print(next(c))
    print(next(c))
    print(next(c))
    print(c.send('OK'))
    print(c.send('q'))
    print(next(c)) # błąd StopIteration
except StopIteration:
    print("generator zakończył działanie")
