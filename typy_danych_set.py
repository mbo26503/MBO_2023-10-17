# set - lista przechowuje niepowtarzające się element
# set nie zachowuje koljności dodawania elementów, nie ma indeksu

lista = [44, 55, 66, 77, 33, 22, 11, 55, 33, 11]
print(lista)  # [44, 55, 66, 77, 33, 22, 11, 55, 33, 11]
zbior = set(lista)
print(zbior)  # {33, 66, 11, 44, 77, 22, 55}
print(type(zbior))  # <class 'set'>
zbior1 = set()
print(zbior1)  # set()
print(type(zbior1))  # <class 'set'>
# do listy można dodać elementy, do zbioru też można
zbior1.add("1")
print(zbior1)  # {'1'}

zbior.add(18)
zbior.add(18)  # nie zostanie dodany, bo już jest
zbior.add(62)  # w zbiorze nie polegamy na kolejności przy dodawaniu
print(zbior)  # {33, 66, 11, 44, 77, 18, 22, 55, 62}
# można usuwać pierwszy element ze zbioru
print(zbior.pop())  # 33
print(zbior.pop())  # 66
print(zbior.pop())  # 11
print(zbior)  # {44, 77, 18, 22, 55, 62}
print('------------')
zbior_liczb ={66, 11, 44, 18, 55, 62, 999, 999}
print(zbior_liczb)  # {66, 18, 55, 999, 11, 44, 62}
lista2 = list(zbior_liczb)
print(lista)  # [44, 55, 66, 77, 33, 22, 11, 55, 33, 11]
zbior_test = set(lista2)
print(zbior_test)  # {66, 999, 11, 44, 18, 55, 62}
print('------------------------')
print(zbior | zbior_test)  # suma zbiorów {66, 999, 11, 44, 77, 18, 22, 55, 62}
print(zbior & zbior_test)  # część wspólna zbiorów {18, 44, 62, 55}
print(zbior - zbior_test)  # różnica {77, 22}
print(zbior.difference(zbior_test))  # różnica {77, 22}
print('-------------------')
set1 = {1, 2, 3}
set2 = {3, 4, 5}
new_set = set1 | set2
print(new_set)  # {1, 2, 3, 4, 5, 6}
print(set1, set2)
# dodanie set2 do set1
set1.update(set2)
print(set1)  # {1, 2, 3, 4, 5}, 3 dodana tylko raz
print('-----------------')
set1 = {1, 2, 3}
print(set2)  # {3, 4, 5}
lista3 = [1, 2, 3]
new_set2 = set(lista3).union(set2)
#albo
new_set3 = set1.union(set2)
print(new_set2)  # {1, 2, 3, 4, 5}
print(new_set3)  # {1, 2, 3, 4, 5}
print(set1)  # {1, 2, 3}
print('-----------------------')