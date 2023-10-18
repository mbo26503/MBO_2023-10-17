print("Mariusz")  # wypisz/wydrukuj
# pep8
# ctrl alt l - sformatuje kod do zasad PEP8

imie = "Radek"  # str czy; i typ tekstowy
imie2 = 'Radek'
print(imie)
# zmienna - takie pudełko na dane
# typowanie dynamiczne
# silne typowanie
wiek = 39
print(wiek)
print(type(wiek))  # <class 'int'>
imie: str = "radek"  # to jest tylko adnotacja, nie jest sprawdzany typ danych
a = 6  # int
b = "7"  # str
print(a * b)  # 777777
temp = 36.6  # float zmiennoprzecinkowy
rok = 2023
print(wiek / rok)
print(wiek // rok)  # 0
print(wiek % rok)
a = "7"
b = int(a)  # rzutowanie na int, czyli zamiana str na int
print(int(a) + b)
# znaki sterujące
print("\tSprawdzam zmienną temp: {} {}\n".format(wiek, temp))
print(f"\tSprawdzam zmienna temp {wiek} {temp}")
print(f"""
zmienna {temp}
    zmienna {wiek}""")
imie = "Radek Radek"
print(imie.lower())  # Retufn a copy of the string converted do lowercase, zwraca ciąg ze zmienionymi znakami na małe
imie2 = imie.lower()
print(imie2)
print(imie)

# bollean - zmienna logiczna
czy_znasz_Pythona = True
print(czy_znasz_Pythona)
print(int(True))
print(int(False))
print(bool(100))  # rzutowanie na typ boolean - True
print(bool(""))  # False
print(bool("Radek"))  # True
print(bool(-1))  # True
# komentarz
"""
komentarz wielolinijkowy
też komentarz
przerwa do 11:00 do 11:30
"""
