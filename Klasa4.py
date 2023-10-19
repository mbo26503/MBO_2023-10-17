class ContactList(list['contact']):

    def search(self, name):
        matching_contacts = []
        for c in self:
            if name in c.name:
                matching_contacts.append(c)
        return matching_contacts


class Contact:
    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    def __repr__(self):
        return f'{self.name!r}, {self.email!r}'


class Suplier(Contact):
    def order(self, order):
        print(f"{order} zamówiono od {self.name}")


class Friend(Suplier, Contact):
    """
    dziedziczenie po wielu klasach, po klasie Suplier i Contact
    """
    def __init__(self, name, email, phone):
        super().__init__(name, email)
        self.phone = phone

    def order(self, order):
        # super(Friend, self).order(order)  # wymuszenie użycia metody z klasy wyższej
        # Suplier.order(self, order)
        print("To ja", self.name, f"{order}")

    def __repr__(self):
        return f'{self.name!r}, {self.email!r}, {self.phone!r}'


cl = ContactList()
print(cl)
cl.append("e")
print(cl)
c1 = Contact("Adam", "adam@wp.pl")
print(c1)  # 'Adam', 'adam@wp.pl'

print('------------')
s = Suplier("Radek", "radek@wp.pl")
s.order("kawa")  # kawa zamówiono od Radek
print(s.all_contacts)  # ['Adam', 'adam@wp.pl', 'Radek', 'radek@wp.pl']
print('--------------')
f = Friend("Jarek", "jarek@wp.pl", "123456")
print(f)
# funkcja do sprawdzania po czym dziedziczy dana klasa
print(Friend.__mro__)  # (<class '__main__.Friend'>, <class '__main__.Suplier'>, <class '__main__.Contact'>, <class 'object'>)
# powyżej sprawdzanie kolejności dziedziczenia, kolejności rozwiązaywania nazw
f.order("herbata")
print(f)  # 'Jarek', 'jarek@wp.pl', '123456'
print(f.all_contacts)  # ['Adam', 'adam@wp.pl', 'Radek', 'radek@wp.pl', 'Jarek', 'jarek@wp.pl', '123456']

