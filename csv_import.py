# 20/10/2023 14:43
# import pliku csv
# matplotlib - bibioteka do wizualizacji danych - np wykresy
import csv
import matplotlib.pyplot as plt
# pip install matplotlib
from datetime import datetime

filename = 'pog.csv'
with open(filename) as f:  # jak nie podamy parametru to dymyślnie jest 'r' czyli odczyt
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        high = int(row[1])
        low = int(row[3])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

print(highs)
plt.style.use('seaborn-v0_8')
print(plt.style.available)  # wypisanie dostępnych styli
_, ax = plt.subplots()
#for _ in range (10):
#print(_)
ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='green')
ax.set_xlabel('', fontsize=16)
_.autofmt_xdate()
ax.set_ylabel("Temeperatura(F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.2)
plt.show()
