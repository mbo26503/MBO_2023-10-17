def kwadrat(n):
    for x in range(n):
        print (x ** 2)

def kwadrat2(n):
    for x in range(n):
        yield x ** 2  # wykonaj działanie i zapamiętaj gdzie zakończyłeś





kwadrat(5)
kwa = kwadrat2(5)
print(kwa)  # <generator object kwadrat2 at 0x0000019E0771F780>
print(type(kwa))  # <class 'generator'>

print(next(kwa))  # 0
print(next(kwa))
print(next(kwa))
print(next(kwa))  # 9
print('cos tam')
print('zrobic dos tam')
lista = []
lista.append("1234567")
print(next(kwa))
# print(next(kwa))  # błąd: StopIteration - skończył się argument
kwa2 = kwadrat2(6)
print(next(kwa2))