# 19/10/2023 14:00
# hermetyzacja - zabezpiecznie pól tak, by nie był do nich dostępu spoza klasy
class Boat:
    """
    dokumentacja klasy
    """


    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__speed = 0  # definicja pola prywatnego "__" dwa podkreślniki, hermetyzacja, enkapsulacja
        # jeśli chcemy zmienić wartość takiego pola to robimy to przez metodę.

    def sail(self):
        self.__speed += 20  # speed = speed + 20


    def speedomenter(self):
        print("Speed in knots", self.__speed)


b1 = Boat("Omega", 2023)
b1.sail()
b1.sail()
b1.sail()
# print(b1.__speed)  # AttributeError: 'Boat' object has no attribute '__speed'
# błąd jest wyżej
b1.speedomenter()
b1.__speed = 0
b1.speedomenter()  # Speed in knots 60
print(b1.__speed)  # pokazue 0



