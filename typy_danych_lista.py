lista = []  # pusta lista
print(lista)
print(type(lista))  # <class 'list'

lista.append("Radek")  # dodanie do listy
print(lista)  # ['Radek']

lista.append("Tomek")
lista.append("Asia")
lista.append("Renata")
lista.append("Darek")
lista.append("Paweł")
lista.append("Marcin")
print(lista)  # ['Radek', 'Tomek', 'Asia', 'Renata', 'Darek', 'Paweł', 'Marcin']
# lista zachowuje kolejność dodawania

print(lista[1])

# nazwa listy, nawias [], numer indeksu
# indeksowani jest od 0, pierwszy element ma numer 0
print(lista[0])
lista[1] = "Magda"
print(len(lista))

lista.insert(1, "Lukasz")
print(lista)
print(len(lista))

lista.append("Asia")
print(lista)
lista.remove("Asia")  # usuwa piewsze wystąpienie elementu zgodnego
print(lista)

#  lista.removeAll()  # nie ma takiej metody w standardowej bibliotece Python
lista.append("dupa")
print(lista)

element_index = lista.index('Renata')
print(lista.pop(element_index))  # Renata
print(lista)

a = 1
b = 1
print(a, b)  # 1 1
a = 7
print(a, b)  # 7 1

lista_copy = lista
lista2 = lista.copy()  # skopiowanie listy do nowej listy
print(lista)
print(lista_copy)  # to jest referncja (miejsce w pamięci) a nie kopia listy
# obiek zmienne lista i lista_copy wskazują na to samo miejsze w pamięci
lista.clear()  # kasowanie wszystkich elementów listy
print(lista)
print(lista_copy)
print(id(lista))
print(id(lista_copy))
print(lista2)
print(id(lista2))

liczby = [54, 999, 34, 22, 12.34, 876]
#  liczby = [54, 999, 34, 22, 12.34, 876, "A"]  # TypeError nie sortuje liczb ze string
print(liczby)
liczby.sort()
print(liczby)

print(lista.copy().__doc__)  # wysietlenie dokumentacji
liczby.reverse()
print(liczby)
liczby2 = liczby.copy()
print(liczby2)
liczby.clear()
print(liczby2)  # [999, 876, 54, 34, 22, 12.34]
print("--------------")
print(liczby2[:3])  # od indeksu 0 do 2 [999, 876, 54]
print(liczby2[2:])  #  od indeksu 2 włącznie do końca włacznie, [54, 34, 22, 12.34]
print(liczby2[:-1])  # -1 ostatni od 0 do -1 (bez -1) czyli do przedostatniego, [999, 876, 54, 34, 22]
print(liczby2[-1])  # element ostatni, 12.34
print(len(liczby2))  # 6
liczby2.remove(54)
print(liczby2)
#  liczby.remove(54)  # ValueError: list.remove(x): x not in list
print(liczby2)
print('----------------')
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.append(lista2)
print(lista1)  # [1, 2, 3, [4, 5, 6]]
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista1.extend(lista2)
print(lista1)  # # [1, 2, 3, 4, 5, 6]
print("------------------")

lista3 = ['a', 'b', 'c']
napis = 'def'
lista3.extend(napis)
print(lista3)  # ['a', 'b', 'c', 'd', 'e', 'f']
lista3.append(napis)
print(lista3)  # ['a', 'b', 'c', 'd', 'e', 'f', 'def']
wart = [1,2,3]
lista3.append(wart)
print(lista3)  # ['a', 'b', 'c', 'd', 'e', 'f', 'def', [1, 2, 3]]
lista3.extend(wart)
print(lista3)  # ['a', 'b', 'c', 'd', 'e', 'f', 'def', [1, 2, 3], 1, 2, 3]
tekst = 'Python'
lista_z_tekstu = list(tekst) # rzutowanie na listę
print(lista_z_tekstu)  # ['P', 'y', 't', 'h', 'o', 'n']
lista_2 = [tekst]
print(lista_2)
print('-------------')
print(liczby2)  # [999, 876, 34, 22, 12.34]
krotka = tuple(liczby2)  # rzutowanie listy na tuble (krotka)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # (999, 876, 34, 22, 12.34), zmienił się nawias na okrągły


