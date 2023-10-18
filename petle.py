# for - petla iteracyjna

lista = []

for i in range(6):  # 0..5
    print(i)
    if i % 2 ==0:
        print("jest parzysta", i, end='')
        lista.append(i)

print(lista)  # [0, 2, 4]
print('--------------------')
lista2 = [j for j in range(6) if j % 2 ==0]  # jeśli warunek jest spełniony to jest robione to co po prawej
print("Lista2=",lista2)
lista3 = [j if j % 2 == 0 else 10 for j in range(6)]
print("lista3=",lista3)

print('--------------------')
for c in lista2:
    if c ==2:
        c += 1  # c = c +1
    print(c)  # 3

# +=, -=, *=, /=, %=
a=1
a+=1
print('a=',a)
a -= 3
print('a=',a)
a *= 2
print('a=',a)
a /= 2  # dzielenie daje wynik float
print('a=',a)
a %= 2
print('a=',a)


#================
# 2023/10/23
print("===============================")
imiona = ["Radek", "Zenek", "Monika"]
print(imiona)  # ['Radek', 'Zenek', 'Monika']
print(type(imiona))  # <class 'list'>

for p in imiona:
    print(p)
# Radek
# Zenek
# Monika

for p in enumerate(imiona):  # enumrate zwraca tuple
    print(p)  # (1, 'Zenek')
print('-----------')
for pozycja, osoba in enumerate(imiona):
    print(pozycja, osoba) # 1 Zenek
print('-----------')
for pozycja, osoba in enumerate(imiona, start=1):
    print(pozycja, osoba)
print('-----------')
print(imiona.index("Radek"))  # 0

ludzie = ['Radek', 'Janek', 'Asia', 'Michał'] #, 'Tadek']
wiek = [47, 67, 32, 34]
for i in ludzie:
    print(i, wiek[ludzie.index(i)])

# jeśli do ludzie dodamy "Tadek" to będzie błąd, bo różne długości list

# zip() - łączy kolekcje
print('-----------')
for l, w in zip(ludzie, wiek):  # uwaga, połączył dwie listy różnych długości
    print(l,w)


print('=====================')
from itertools import zip_longest  # pobierać z oficjalnego repozytorium Python, sprawdzać sumy kontrolne bibliotek
zipped = zip_longest(ludzie, wiek, fillvalue='Nan')
print(type(zipped))  # <class 'itertools.zip_longest'>

for item in zipped:
    print(item)  # ('Tadek', 'Nan')

print(zipped)  # <itertools.zip_longest object at 0x0000025F16312480>

for name, age in zipped:
    print("Zaczynam drugą pętlę")
    for (name, age) in zipped:
        print(name, age)
#  druba pętla się nie wykonała
# ctrl / - komentaowani linii
# aby wykonać drubą pętlę trzeba zrobić listę
zipped_list = list(zipped)
print("Zaczynam drugą pętlę")
for (name, age) in zipped_list:
    print(name, age)
print('-----------')
c = {'name': 'Radek', 'age': 5}  # słownik
print({v: k for k, v in c.items()})  # {'Radek': 'name', 5: 'age'}
# to samo co:
d = {}
for k, v in c.items():
    d[v] = k
print(d)  # {'Radek': 'name', 5: 'age'}

name = ['John', 'Alice', 'Bob']
age = [25, 30, 35]
people = [(name, age) for name, age in zip(name, age]
print(people)