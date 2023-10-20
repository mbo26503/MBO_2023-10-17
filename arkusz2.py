# 20/10/2023 15:28
import pandas as pd

lista = [[2,5,8, 9], [9, 8, 5, 4]]
slownik = {'imie': ['Ania', 'Michał', 'Przemek'], 'wiek': [18, 22,34]}
zbior = pd.DataFrame(lista)

zbior.columns = ['jeden', 'dwa', 'trzy', 'cztery']
sl = pd.DataFrame(slownik)

print(sl)
print(zbior)

#zbior.to_csv('test1.csv')
sl.to_csv('test2.csv', index=False)  # zapis bez indeksu

