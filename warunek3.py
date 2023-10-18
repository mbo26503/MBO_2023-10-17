# match case
informacje_o_ksiazce = {
    'autor': input("Podaj autora"),
    'tytul': input("Podaj tytul"),
    'rok wydania': int(input("Podaj rok wydania"))
}

status = ""
match informacje_o_ksiazce['autor'].lower():
    case "tolkien" | "rowling":
        status = "bestseller"
    case "sapkowski" | "luk":
        status = "popularne"
    case "lem" | "asimow":
        status = "Klasyka sf"
    case _:  # wartość domyslna
        satus = "nieznany"

print(f"Książka '{informacje_o_ksiazce['tytul']}' to {status}")