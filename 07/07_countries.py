from datetime import datetime
import timeit, random

countries = {
    "Irsko": 4593100,
    "Chorvatsko": 4290612,
    "Moldavsko": 3559500,
    "Litva": 2941953,
    "Albánie": 2821977,
    "Slovensko": 5415949,
    "Norsko": 5109056,
    "Itálie": 59943933,
    "Španělsko": 46609700,
    "Ukrajina": 45426200,
    "Polsko": 38502396,
    "Mkedonie": 2062294,
    "Slovinsko": 2061963,
    "Lotyšsko": 2003900,
    "Kosovo": 1815606,
    "Estonsko": 1311870,
    "Rusko": 143700000,
    "Německo": 80619000,
    "Turecko": 76667864,
    "Francie": 65844000,
    "Velká Británie": 63705000,
    "Portugalsko": 10487289,
    "Maďarsko": 9906000,
    "Švédsko": 9651531,
    "Bělorusko": 9468100,
    "Rakousko": 8504850,
    "Švýcarsko": 8112200,
    "Bulharsko": 7282041,
    "Srbsko": 7181505,
    "Dánsko": 5627235,
    "Finsko": 5452821,
    "Rumunsko": 20121641,
    "Nizozemsko": 16842200,
    "Belgie": 11132269,
    "Řecko": 10815197,
    "Česko": 10513800,
}

# Definice funkce prumer n prvku v dict bez build in functions
def vypocitejPrumerDict(dataSet):
    peopleTogether = 0
    countOfItems = 0
    for country, numberOfPeople in dataSet.items():
        peopleTogether += numberOfPeople
        countOfItems += 1
    return round(peopleTogether / countOfItems)

# definice funkce s kontrolu hodnoty int, float
def vypocitejSoucetDictWitConditions(dataSet):
    countOfPeople = 0
    countOfItems = 0
    for country in dataSet:
        numberOfPeople = dataSet[country]
        if isinstance(numberOfPeople, (int, float)):
            countOfPeople += numberOfPeople
            countOfItems += 1
    return round(countOfPeople / countOfItems)

# Definice funkce s build in functions
def vypocitejPrumerDictWithBuild(dataSet):
    average_population = round(sum(dataSet.values()) / len(dataSet))
    print(f"Priemerná populácia je: {average_population}:")

def check_max_min(dataset):
    # Najväčšia populácia
    max_country = max(countries, key=countries.get)
    max_population = countries[max_country]

    # Najmenšia populácia
    min_country = min(countries, key=countries.get)
    min_population = countries[min_country]

    print(f"Najväčšia populácia je v {max_country}: {max_population}")
    print(f"Najmenšia populácia je v {min_country}: {min_population}")



# start_time = datetime.now()
# print('Prumer:', vypocitejPrumerDict(countries))
# print('celkovy cas procesu:', datetime.now() - start_time)

# start_time = datetime.now()
# print('Prumer:', vypocitejSoucetDictWitConditions(countries))
# print('celkovy cas procesu:', datetime.now() - start_time)

vypocitejPrumerDictWithBuild(countries)
check_max_min(countries)



        
