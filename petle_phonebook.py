# utworznie książki telefonicznej z wykoryztganiem pętli whila jako głownej pętli programu
# dodaj kontakt, usuń kontakt, wyszukaj kontakt, wyśiwtl wszystkie kontakty
# wyjcie z programu
# do 10:30
# moje
print("Dodaj kontakt")
print("Usuń kontakt")
print("Wyszukaj kontakt")
print("Wyjście")
act = ['add', 'del', 'src', 'quit']
opt = [1, 2, 3]

print("--------------------")
# propozycja nauczyciela
contacts = {}
while True:
    print(f"""
    1. Dodaj kontkt
    2. Usuń kontakt
    3. Wyszukaj kotnakt
    4. Wyswietl wszystkie kontakty
    5. Koniec
""")
    odp = input('wybierz opcję: ')  # input zawsze daje stinga
    try:
        if odp == '1':
            name = input("Podaj imię kontaktu: ")
            number = input("Podaj numer telefonu (tylko cyfry): ")
            if not number.isdigit():
                print("To nie jest cyfra")
                # ZAMIAST w/w może być
                raise ValueError("Numer tele. powinien zawierać cyfry!")
            if name in contacts:
                print(f"Kontakt {name} już istnieje.")
            else:
                contacts[name] = number
                print("Kontakt {name} został dodany")
        elif odp == '2':
            name = input("Podaj imię konaktu do usunięcia: ")
            if name in contacts:
                del contacts[name]  # usunięcie elementu ze słownika
                #conatcts.pop(name)  # usunięcie elementu ze słownika, pop zwróci element który usunął
                print(f"Kontakt {name} został usunięty.")
            else:
                print(f"Nie znaleziono konaktu o imieniu {name}")
        elif odp == '3':
            pass
        elif odp == '4':
            if not contacts:
                print("Lista kontaktów jest pusta")
            for name, number in contacts.items():
                print(f"Kontakt {name} : {number}")
        elif odp == '5':
            break
    except KeyError:
        print(f"Nie znaleziono kontaktu o imieni {name}.")
    except ValueError as ve:
        print(f"Bląd wartości {ve}")
    except Exception as e:
        print("wystapił błąd:", e)
    finally: # zawsze jest wykonana
        print("Dziękuje za skorzystanie z programu")