# dekoratory - opakowanie jednej funkcji dodatkowymi cechami

def dekor(funk):
    def wew():
        print("Dekorujemy")
        return funk()

    return wew()


@dekor  # użycie dekoratora na naszej funkcji
def hej():
    print("Hej")



hej()


#Nie Działa