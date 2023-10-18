# krotka - kolekcja niezmienna
# po utworzeni nie można zminić tej kolekcji, nie można nic dodawać ani usuwac
# indeksy liczone od 0

tupla = "Tomek", "Michal", "Asia", "Daniel"  # ('Tomek', 'Michal', 'Asia', 'Daniel')
print(tupla)
print(type(tupla))  # <class 'tuple'>
tupla2 = "Radek"
print(type(tupla2))  # <class 'str'>
tupla2 = ("Radek",)
print(type(tupla2))  # <class 'tuple'>
print(tupla2)  # ('Radek',)
print('---------------')
tupla3 = 44, 34, 22.43, 11, 200
print(tupla3)  # (44, 34, 22.43, 11, 200)
print(tupla3[1])  # 34
print(type(tupla3))  # <class 'tuple'>
print('------------')
print(tupla.index("Tomek"))  # 0
print(tupla.count('Asia'))  # 1, zlicza ilość wystąpień
asia = tupla[2]
print(asia)
#  tupla[0] = "Radek"  # TypeError: 'tuple' object does not support item assignment
#"""
#Traceback (most recent call last):
#  File "C:\Users\CSComarch\PycharmProjects\pythonProject\MBO_2023-10-17\typy_danych_krotka.py", line 23, in <module>
#    tupla[0] = "Radek"
#    ~~~~~^^^
#TypeError: 'tuple' object does not support item assignment
#"""
print('------------------')
a, b = 1, 2  # rozpakowanie tupli
print(a, b)
a, *b = 1, 2, 3
print(a)
print(b)  # [2, 3]
print(tupla)  # ('Tomek', 'Michal', 'Asia', 'Daniel')
imie1, imie2, *imie3 = tupla  # gwiazdkę można dać tylko na 1 miejscu
print(imie1)  # Tomek
print(imie2)  # Michal
print(imie3)  # ['Asia', 'Daniel']
print('--------------')
# tuplę można rzutować na liste
lista = list(tupla)
print(lista)  # ['Tomek', 'Michal', 'Asia', 'Daniel']
# 13:00 - przerwa do 13:30



