import pickle
from klasa9 import Person  # z pliku klasa9.py zaimportujemy klasę

with open('dane.txt', 'r') as stream:
    p2 = stream.read()  # wczytanie plku do pamięci

# kontekst manager

print(p2)  # [Person(first_name='Jacek', last_name='Kowalski', id=1), Person(first_name='Mateus', last_name='Zegar', id=2)]
print(type(p2))  # <class 'str'>

with open('data_pickle.bin', 'rb') as stream:
    p = pickle.load(stream)

print(p)  # [Person(first_name='Jacek', last_name='Kowalski', id=1), Person(first_name='Mateus', last_name='Zegar', id=2)]
print(type(p))  # <class 'list'>
for person in p:
    person.greet()
    print(pickle.dumps(person))
# b'\x80\x04\x95N\x00\x00\x00\x00\x00\x00\x00\x8c\x06klasa9\x94\x8c\x06Person\x94\x93\x94)\x81\x94}\x94(\x8c\nfirst_name\x94\x8c\x06Mateus\x94\x8c\tlast_name\x94\x8c\x05Zegar\x94\x8c\x02id\x94K\x02ub.'
    print('------------')
    sd = pickle.dumps(person)
    print(sd)  # zserializowany obiekt
    print(pickle.loads(sd))  # zdeserializowany obiekt: Person(first_name='Mateusz', last_name='Zegar', id=2)



