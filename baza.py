# 19/10/2023 15:13
# baza danych
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')  # utworzenie DB
    cursor = sql_connection.cursor()  # ustwienie kursora do pobierania danych
    print("Baza danych została podłączona")
except sqlite3.Error as e:
    print("Błąd podczas podłączenia bazy danych", e)
finally:
    if sql_connection:
        sql_connection.close()
        print("Baza danych zamknięta")
# kontekst manadżer