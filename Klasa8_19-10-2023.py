from abc import ABC, abstractmethod


class Counter(ABC):
    def __init__(self, values=0):
        self.values = values

    @abstractmethod  # dekorator
    def drukuj(self):
        pass

    def increment(self, by=1):
        self.values += by

    @classmethod  # dekorator
    def from_counter(cls, counter):
        return cls(counter.values)

    @staticmethod  # metoda statyczne, można użyć nie tworząc obiektu klasy
    def format_string():
        return '%d'


class BoundedCounter(Counter):
    MAX = 100

    def __init__(self, values=0):
        if values > self.MAX:
            raise ValueError("Wartość noie może przekroczyć MAX")
        super(BoundedCounter, self).__init__(values)

    def drukuj(self):
        print("Drukuję...", self.values)

# po dodaniu @abstactmethod
# TypeError: Can't instantiate abstract class Counter without an
# implementacion for abstract  method 'druku'

#c = Counter()
#c.increment()
#print(c)  # <__main__.Counter object at 0x00000224FF77D340>
#c.drukuj()  # nic nie wydrukowało bo pass w metodzie drukuj
#po wykomentowaniu powyższego działa

print('---------')
b = BoundedCounter()
b.increment()
b.drukuj()

c = BoundedCounter()
c.drukuj()
d = BoundedCounter.from_counter(b)
d.drukuj()
print(d.format_string())  # %d
print(BoundedCounter.format_string())


