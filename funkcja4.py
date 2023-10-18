# napisać funkcję, która za pomocą przekazanych argumentów stworzy słownik
# pobrać dane od użytkownika
# first, last, age
def build_person(first, last, age=None):
    person = {'first': first, 'last': last}
    if age:
        person['age'] = age
    return person

while True:
    print("Podaj i mię i nazwisko: ")
    print("wpisz q by zakończyć")
    f_name = input("Imię: ")
    if f_name == 'q':
        break
    l_name = input("nazwisko: ")
    if  l_name == 'q':
     break
    age = input("Wiek: ")
    if age == 'q':
        break
print(build_person(f_name, l_name, age))
