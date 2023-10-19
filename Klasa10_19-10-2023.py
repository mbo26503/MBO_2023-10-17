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



