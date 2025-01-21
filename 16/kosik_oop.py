# Pripravim si tridu Kosik, ktera bude mit seznam polozek a metodu na pridani polozky

import uuid
import os

class Kosik:
    
    
    def __init__(self, id):
        self.id = id
        self.polozky = {}
        self.poradie = 0
        

    def pridaj_polozku(self, polozka: 'Polozka'):
        self.poradie += 1  
        self.polozky[self.poradie] = polozka

    def odstran_polozku_by_poradie(self, poradie):
        if poradie in self.polozky:
            del self.polozky[poradie]
        else:
            print(f"Polozka s poradim {poradie} neexistuje")

    def odstran_polozku(self, polozka: 'Polozka'):
        for poradie, polozka_v_kosiku in self.polozky.items():
            if polozka_v_kosiku == polozka:
                del self.polozky[poradie]
                return
        print(f"Polozka {polozka} neexistuje v kosiku")

    def list_kosik(self):
        for poradie, polozka in self.polozky.items():
            print(f"{poradie}: {polozka}")


class Polozka:
    def __init__(self, nazev, cena=0):
        self.nazev = nazev
        self.cena = cena

    def __str__(self):
        return f'{self.nazev}, cena: {self.cena}'
    
# Vytvorim polozky
boty_do_roboty = Polozka('Boty do roboty', 1000)
ponozky_na_nozky = Polozka('Ponozky na nozky', 100)

# 1. Vytvor objekt kosik
kosik = Kosik(uuid.uuid4())

#print(kosik.id)

kosik.pridaj_polozku(boty_do_roboty)
#kosik.odstran_polozku(boty_do_roboty)

#kosik.odstran_polozku(1)

kosik.list_kosik()

error = ""

while True:
    # Vymazem obsah konzoly
    os.system('cls')
    
    # Zobrazim kosik a items v nom ulozene
    kosik.list_kosik()
    
    print(f'\navailable commands:')
    print(f'add:<item name>, remove:<item_id>, exit')
    print('-----------------------------') 
    # Vymazem obsah premennej error s posledneho pripadu, tak nech sa dalej nezobrazuje    
    if error != "":
        print(error)  

    error = ""
    command = input('Zadaj prikaz: ')

    if command.startswith("add:"):
        item = command[4:].strip()
        print(item)
        if item:
            new_item = Polozka(item)
            kosik.pridaj_polozku(new_item)
            print(f'Produkt "{new_item}" bol pridany do Kosiku.')
        else:
            error = "!!! Nazov produktu nemôže byť prázdny. !!!"
    elif command.startswith("remove:"):
        produkt_poradie = int(command[7:].strip())
        #print(task_id)
        kosik.odstran_polozku_by_poradie(produkt_poradie)
    
    
    
    elif command == "exit":
        break