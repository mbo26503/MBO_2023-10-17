# 20/10/2023 13:27
# JSON z internetu
# REST API
# metody: get, post, pt, patch, delete, head, option
# podstwowe 4 operacje CRUD: create, read, update, delete - komunikacja http
# komunikacja między serwrem a klientem może wykorzystywać JSON

import json
import requests as re
from pydantic import BaseModel

# pip install requests

#url = "http://api.nbp.pl/api/exchangerates/tables/A/"
url = "http://api.nbp.pl/api/exchangerates/rates/A/EUR"

response = re.get(url)
print(response)
# 404 błędny adres
# 400 błędne zapytanie
# w przypadku braku danych dla prawidłowo określonego zakresu czasowego zwracany jest komunikat 404 Not Found
# w prypadku zdania nieprawidłoo sformułowanych zapytan serwis zwraca komunikat 400 Bad Rquest
# W prypadku zapytania przekraczaącego limit zwracanych danych serwis zwróci komunikat:
# 400 Bad REquest - Przekroczonyt limit

dane = response.json()
print(dane)  # {'table': 'A', 'currency': 'euro', 'code': 'EUR', 'rates': [{'no': '204/A/NBP/2023', 'effectiveDate': '2023-10-20', 'mid': 4.4675}]}
print(type(dane))  # <class 'list'>
#print(dane[0]['rates'])


class Rate(BaseModel):
    no: str
    effectiveDate: str
    mid: float

class CurrencyData(BaseModel):
    table: str
    currency: str
    code: str
    rates: list[Rate]

json_string = json.dumps(dane)
#currency_data = CurrencyData.parse_raw(json_string)  # tu jes problem z parse_raw,
currency_data2 = CurrencyData.model_validate_json(json_string)
print(currency_data2)