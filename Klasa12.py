# 19/10/2023 14:28
# w Python wszystko jest obiektem
# tworzenie własnego wyjątku

class MyException(Exception):  # dziedziczymy po głownej klasie z wyjątkami
    def __init__(self, message):
        super().__init__(message)


try:
    x = int(input("Podaj liczbę całkowitą"))
    if x<0:
        raise MyException("Liczba musi być dodatnia")
except MyException as e:
    print("Wystąpił mój własny wyjątek", e)
except ValueError:
    print("Wystąpił błąd wartości")
except Exception as e:
    print("wystąpił błąd", e)
