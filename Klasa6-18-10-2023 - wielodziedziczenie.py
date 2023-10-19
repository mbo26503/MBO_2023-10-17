# podstawy wielodziedziczenia
class A:
    def method(self):
        print("Metoda z klasy A")


class B:
    def method(self):
        print("metoda z klasy B")


class C(A, B):  # kolejność ma znaczenie, w tym przypadku najpirrws szuak w A jesli nie znajdzie w C
    """
    klasa C dziedziczy po klasie A i B - kolejność dziedziczenia ma znaczenie
    """
    def method(self):
        super().method()  # Metoda z klasy A, bo A jest na pierwszym miejscu
        # funkcja super - użycie danej metody z klasy wyższej, w tym przypadku klasa A
        print(f"Metoda z klasy C")  # Medota z klasy C
        B.method(self)  # Metoda z klasy B

a = A()
a.method()
b = B()
b.method()
print(C.__mro__)  # (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
c = C()
print('----------')
print('----------')
c.method()  # Metoda z klasy A
