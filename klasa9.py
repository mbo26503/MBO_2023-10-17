import pickle
from dataclasses import dataclass

@dataclass  # dekorator, automatycznie kodał do klasy konstruktor na podstawie pól z wywołania
# bez tego dekoratora jest błąd:
#Traceback (most recent call last):
#  File "C:\Users\CSComarch\PycharmProjects\pythonProject\MBO_2023-10-17\klasa9.py", line 14, in <module>
#    Person("Jacek", "Kowalski", 1),
#    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
#TypeError: Person() takes no arguments

class Person:
    first_name: str
    last_name: str
    id: int


    def greet(self):
        print(f"Witam, jestem {self.first_name} {self.last_name}, Id to{id}")

if __name__ == '__main__':
   people = [
        Person("Jacek", "Kowalski", 1),
        Person("Mateusz", "Zegar", 2)
    ]

# działania na plikach
# kontekst menadżera, automatycznie za nas zamyka plik, nawet w przypadku awarii, używa metody 'exit'

   print(people)  # [Person(first_name='Jacek', last_name='Kowalski', id=1), Person(first_name='Mateus', last_name='Zegar', id=2)]
   with open('dane.txt', 'w') as stream:  # zapisane tekstowo
       stream.write(str(people))

   with open('data_pickle.bin', 'wb') as stream:
       pickle.dump(people, stream)
