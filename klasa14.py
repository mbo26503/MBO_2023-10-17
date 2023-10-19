# 19/10/2023 14:57
# klasa14.py

class MyDict(dict):
    def __missing__(self, key):  # definiuje sposób obsłużenia przypadku, gdy klucza nie ma w słowniku
        return "Nie ma takiego klucza"

class DefaultDict(dict):  # ustawia wartość domyślną
    def __missing__(self, key):
        return "default"

class AutoKeyDict(dict):  # automatycznie doda klucz do słownika
    def __missing__(self, key):
        self[key] = 0

class CaseInsensitiveDict(dict):
    def __missing__(self, key):
        if isinstance(key, str):
            return self.get(key.lower())



d = MyDict()
d['name'] = 'Radek'
print(d['name'])  # Radek
print(d['imie'])  # Nie ma takiego klucza

d2 = DefaultDict()
d2['name'] = 'Radek'
print(d2)
print(d2['imie'])  # default

d3 = AutoKeyDict()
d3['name'] = 'Radek'
print(d3['imie'])
print(d3)

d4 = CaseInsensitiveDict()
d4['name'] = 'Radek'
print("d4= ", d4['Name'])