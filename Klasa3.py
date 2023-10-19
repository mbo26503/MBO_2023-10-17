# dziedziczenie klas
from pprint import pprint

class Contact:
    all_contacts = []  # pusta lista

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)  # dopisanie kontaktów do listy


    def __repr__(self):
        return f'{self.name!r}, {self.email!r}'

class Suplier(Contact):
    """
    Dziedziczy po Contact
    """

#    pass
    def order(self, order):
        print(f"{order} zamówiono od {self.name}")

c1 = Contact("Adam", "admin@wp.pl")
c2 = Contact("Radek", "admina@wp.pl")
c3 = Contact("Krzys", "admin2@wp.pl")
c4 = Contact("Arek", "admin4@wp.pl")
print(c1)  # <__main__.Contact object at 0x0000022D9A36D8E0>
print(c1.all_contacts)
print("-------------")
s = Suplier("Tomasz", "tomasz@wp.pl")
print(s)
print("prints : ")
print(s.all_contacts)
s.order("kawa")
pprint(c1.all_contacts)