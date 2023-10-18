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


