# 19/10/2023 15:26
import sqlite3
# użycie kontakst manadżera do zamykania pliku DB

class SQLiteDBContextManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = None


    def __enter__(self):
        self.conn = sqlite3.connect(self.db_name)
        return self.conn


    def __exit__(self, exc_type, exc_value, traceback):
        if self.conn:
            self.conn.commit()  # zmiany na DB zostaną zapisane
            self.conn.close()  # zamknięcie DB

lista = []
db_name = "my_database.db"

with SQLiteDBContextManager(db_name) as conn:
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY, name TEXT)")
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("John",))
    # wyżej jest typ tupla
    cursor.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    select = cursor.execute("SELECT * FROM users")
    print(select)  # <sqlite3.Cursor object at 0x00000245D86A4E40>
    for i in select:
        print(i)
        lista.append(i)  # lista krotek

    for i, p in lista:
        print (i, p)

