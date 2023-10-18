# while - pętla sterowana warunkiem

licznik = 0
while True:  # ta pętla nigy się nie zatrzyma
    licznik += 1
    print("Komunikat")
    if licznik > 10:
        break # przerwanie działania pętli
print("-----------------------")
licznik = 0
while licznik <10:
    print("Komunikat2")
    licznik += 1

lista = []
while True:  # często jest sotosana jako główna pętla programu
    wej = input("Podaj liczbe")  # str
    if not wej.isnumeric():
        break
    lista.append(int(wej))