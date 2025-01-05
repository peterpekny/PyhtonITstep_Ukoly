import datetime

mesice = range(12)
rok = 2024

for mesic in mesice:
    d = datetime.date(rok, mesic+1, 1)
    print(d.strftime('%d/%m/%Y'))
