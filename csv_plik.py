# 20/10/2023 14:12
# pliki csv - pliki w których dane są oddzielone znakiem podziału np. , ; tab
# Radek, Michał, Zene
import csv

fields = ["name", "branch", "year", "cgpa"]

my_dict = [
    {'branch': "COE", 'cgpa': 9.1, 'name':"Radek", "year": 3},
    {'branch': "COK", 'cgpa': 9, 'name':"Zenek", "year": 4},
    {'branch': "COS", 'cgpa': 8.1, 'name': "Marek", "year": 3},
    {'branch': "COL", 'cgpa': 8.12, 'name': "Tomek", "year": 2}
]


filename = 'records.csv'
# with open(filename, "w", encoding="utf-8") as csv_f:  # uwaga: w Windows w pliku są puse linie, to jest wynik różnej interpretacji znaku końca lini w Windows i Linux
with open(filename, "w", encoding="utf-8", newline='') as csv_f:  # tu już nie ma pustych linii
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields)
    csvwriter.writeheader()
    csvwriter.writerows(my_dict)

new_fields = []
new_rows = []

with open(filename, "r", encoding="utf-8", newline="") as csv_f:
#    csvreader = csv.DictReader(csv_f)
    csvreader = csv.reader(csv_f)
    new_fields = next(csvreader)  # odczytanie wiersza o indeksie 0, wpisanie do zmiennej i ustawienie wskaźnika na następny
    for row in csvreader:  # ta pętla wystrtuje od indeksu 1 a nie 0
        new_rows.append(row)

print(new_fields)  # ['name', 'branch', 'year', 'cgpa']
print(new_rows)  # [['Radek', 'COE', '3', '9.1'], ['Zenek', 'COK', '4', '9'], ['Marek', 'COS', '3', '8.1'], ['Tomek', 'COL', '2', '8.12']]

print('---------------')
new_dict = []
with open(filename, "r", encoding="utf-8", newline="") as c:
    csvreader = csv.DictReader(c)
    for row in csvreader:
        new_dict.append(row)

print(new_dict)
for i in new_dict:
    print(i)

