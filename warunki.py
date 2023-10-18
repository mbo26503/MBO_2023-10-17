czy_znasz_Python = True

if czy_znasz_Python:
    print("Super")  # wcięcie obowiązkowe
else:
    print("Musisz się dalej uczyć")

print("Dalsza część programu")

if czy_znasz_Python:
    pass # nic nie rób

print("Dalsza część 2")

name = "Tomek"
if name == "Radek": # ==przyrównanie
    print(f"Twoje imię {name}")

if name :="Radek":  #przypisz wartość do ziennej i poównaj, trochę bez sensu, warunek ma zawsze wartość True
    print(f"Twoje imię {name}")

#To jest to samo co:
name = "Radek"
if name == "Radek":
    print("ok")
print('---------------------------')

word_len = len(name)
if word_len > 2:
    print("Długość ok")

if word_len := len(name) >2:
    print("Długość ok 2")

if len(name) > 2:
    print("dlg > 2")

if (word_len := len(name)) >2:
    print("Długość ok 2 {word_len}")

typ_samochodu = "pieszo"
wiek = int(input("Podaj swoj wiek: "))
if wiek < 18:
    typ_samochoud = 'pieszo'
elif wiek < 25:
        typ_samododu = "sportowy"
elif wiek < 60:
    typ_samochodu = "małe auto"
else:
    typ_samochodu = 'kabriolet'

print(f"Na podstawie Twojego wieku sugeruję: {typ_samochodu}")
# dodać wrunek, gdzie dla wieku 25 do 59 zaproponujemy mały samochód
# kolejność ma znaczenie
# po wejściu w pierwszy spełniony warunek po wykonaiu instrukcji wychodzi do głownego programu


