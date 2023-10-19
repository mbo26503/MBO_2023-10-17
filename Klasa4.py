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
