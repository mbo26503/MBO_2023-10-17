class Sample:
    def __init__(
            self,
            a: int,
            b: int,
            c: int,
            d: int,
            e: Optional[str] = None) -> None:  # wskazanie jaką wartość zwraca metoda, # optional zapewnia, że coś tam zostani zawsze zwrócone
        # Optional jest raczej informacją dla programisty, że funkjca może być używana z tym arbumentem lub bez niego.
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e

    def __repr__(self):  # funcja wbudowana Python - funkcja magiczna, pokazywanie obiektów w sposób bardziej czytelny
        if self.e is None:
            self.e = 'nieznane'
        return (
            f'a = {self.a}, '
            f'b = {self.b}, '
            f'c = {self.c}, '
            f'd = {self.d}, '
            f'e = {self.e} '
        )


# class sample:  # nazwa klasy z małej litery jest poprawan, ale niezgodna z PEP8


ob = Sample(1, 2, 3, 4, 5)
print(ob)
ob2 = Sample(1, 2, 3, 4)
print(ob2)
