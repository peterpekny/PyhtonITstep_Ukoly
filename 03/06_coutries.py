import pprint

countries = {
    "CZ": "Česko",
    "SK": "Slovensko",
    "DE": "Německo",
    "AT": "Rakousko",
    "PL": "Polsko",
}

countries_name = {}
countries_len = {} 

for key, value in countries.items():
    countries_name[value] = key

for key, value in countries.items():
    countries_len[key] = len(value)


print(countries_name)
print(countries_len)

pprint.pprint(countries_name)
pprint.pprint(countries_len, width=10)