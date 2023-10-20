# 20/10/2023 12:28
# JSON - obiekt podobny do słownika, typu klucz - wartość
# {"name" : "Radek"}
import json  # uwaga, nie nazywać pliku json.py, bo będzie importować ten plik a nie bibliotekę


print(json)
# <module 'json' from 'C:\\Users\\CSComarch\\AppData\\Local\\Programs\\Python\\Python312\\Lib\\json\\__init__.py'>

json_string = '{"name":"Jan", "age" : 30, "city":"Lodz"}'
data = json.loads(json_string)  # zaminana jsona na słownik
print(data)  # {'name': 'Jan', 'age': 30, 'city': 'Lodz'}
print(type(json_string))  # <class 'str'>
print(type(data))  # <class 'dict'>

data2 = {
    "name": "Jan",
    "age": 30,
    "city": "Lodz"
}

json_string2 = json.dumps(data2)  # zamiana jsona
print(json_string2)  # {"name": "Jan", "age": 30, "city": "Lodz"}
print(type(json_string2))  # <class 'str'>

data = json.loads(json_string2)
print(data['name'])
print(data['age'])
print(data['city'])

data['country'] = "Polska"
print(data)  # {'name': 'Jan', 'age': 30, 'city': 'Lodz', 'country': 'Polska'}
del data['city']
print (data)  # {'name': 'Jan', 'age': 30, 'country': 'Polska'}
print("-------------")

data['car'] = [{"color":"blue"}, {"brand": "fiat"}]  # dodanie json w json

modified_json = json.dumps(data)
print(modified_json)  # {"name": "Jan", "age": 30, "country": "Polska"}

print('---------------')
person_dict = {'name' : 'Radek', 'age':"38", 'city': "Łódź", "czy_pali": None}  # uwaga na ' i ", używane zamiennie
with open('dane.json', 'w', encoding='utf-8') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)

with open('dane.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(data)  # {'age': '38', 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>


