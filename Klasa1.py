# Klasa - szablon zawiera wskazanie dla pól i funkcji
# np. człowiek
# nadanie konkretnych cech - obiekt

import math

class MyFirstClass:
    # dokumentacja
    """
    Repreentuje punkty x i y
    """


    def __init__(self, x=0, y=0):  # konstruktor, inicjator
        """
        metoda inicjalizująca
        :param x:
        :param y:
        :return:
        """

        self.move(x, y)  # wywołanie metody move

    def move(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def reset(self):
        self.move(0, 0)

    def calculate(self, other: "MyFirstClass") -> float:  # bez adnotacji fl
        return math.hypot(self.x - other.x, self.y - other.y)

    # reprezentacja obbiektu w sposób czytelny
    def __repr__(self):  # funcja wbudowana Python - funkcja magiczna, pokazywanie obiektów w sposób bardziej czytelny
        return f"x = {self.x}, y = {self.y}"

#print(MyFirstClass.__doc__)  # to jest traktowane jako dokumentacja
#print(print.__doc__)

ob = MyFirstClass()
print("ob.x=",ob.x)  # ob.x= 0
ob.move(45, 67)
print("ob= ",ob)  # ob=  x = 45, y = 67
print(ob.y)  # 67
print(ob)
print(ob.__str__())
print(ob.__repr__())
ob.move(0, 0)
ob.reset()
print(ob.x)


# pogubiłm się

a = MyFirstClass(3, 5)
b = MyFirstClass(0, 5)
print(a)
print(b.calculate(a))
print(a.calculate(b))
assert b.calculate(a) == a.calculate(b)
a.move(3, 4)
print(a.calculate(b))  # 3.1622776601683795

