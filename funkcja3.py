def example(a, b, **kwargs):  # ** - argumenty słownikowe
    print(a, b)
    print(kwargs)
    return a * b

print(type(example))  # <class 'function'>
print(example.__code__.co_varnames)
print(example(1, 2))
print(example(1,2, l=8))
print(example(1, 2, c="Radek", l=8))  # {'c': 'Radek', 'l': 8}


# lambda - skrócony zapis funkcji, moze być zdefiniowana w miejscu wywołania
liczymy = lambda x,y: x * y  # lambda ma return domyślnie
print(liczymy(200, 50))  # 10000

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 55]  # lista bo nawiasy kwadratowe
# funkcja map()
print(f"Użycie map() {list(map(lambda x: x * 2, lista))}")  # lambda jako funkcja anonimowa
# Użycie map() [2, 4, 6, 8, 10, 12, 14, 16, 18, 40, 110]

# filter() - filtruje dane na odstawie funkcji z warunkiet
print(f"użycie filter(): {list(filter(lambda x: x < 5, lista))}")  # użycie filter(): [1, 2, 3, 4]
print("----------------------")
r0 = {'miasto': 'Kielce'}
r1 = {'miasto' : 'Kielce', 'ZIP': "25-900"}
print(r0['miasto'])
print(r1['miasto'])
print(r1['ZIP'])
#print(r0['ZIP'])  # BŁĄD: KeyError: 'ZIP'
d_zip = lambda row: row.setdefault('ZIP', '00-000')  # domyślne ustawienie klucza,
print(d_zip(r0))  # 00-000
print(r0)  # {'miasto': 'Kielce', 'ZIP': '00-000'}
print(r1)  # {'miasto': 'Kielce', 'ZIP': '25-900'}

# do ustawienia wartości domyślnej można użyć ponizszego
r1.setdefault("Test", "1")  # {'miasto': 'Kielce', 'ZIP': '25-900', 'Test': '1'}
print(r1)
print("--------------------")
lata = [(2000, 29.97), (2001, 33.12), (2010, 32.92)]  # lista tupli
print(max(lata))  # (2010, 32.92)
print(max(lata, key=lambda c: c[1]))  # (2001, 33.12)
print(max(map(lambda c: (c[1], c), lata)))  # (33.12, (2001, 33.12))

# 12:55 - przerwa do 13:25

