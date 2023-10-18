# funkcja - wydzielony fragment kodu, który można wykonac wielokrotnie
# najpierw definicja funkcji a potem wywołanie
a = 8
b = 7
def dodaj():  # definicja funkcji bez argumentów
    print(a + b)


def dodaj2(a, b):  # definicja funkcji z argumentami obowiązkowymi
    print(a + b)


def dodaj3(a, b, c=0): # funkcja z trzema argumentami, treci ma domyślną wartość, symulujemy przeciążenie
    print(a + b + c)

dodaj()  # uruchomienie funkcji
dodaj2(3,4)
dodaj3(1, 2)
dodaj3(6, 7, 8)
dodaj3(c=7, b=0, a=9)  # argumnty po nzazwie
dodaj3(1, c=0, b=9)

print(dodaj())  # None - nic nie zwraca
#print(dodaj(1, 3) + dodaj2(6, 7))  #  Błąd: TypeError: dodaj() takes 0 positional arguments but 2 were given

def mnozenie(a, b):  # funcje zwracajaca wynik (return)
    return a *b

wyn = mnozenie(4, 6)
print(wyn)

