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
            print(f"Položka s poradím {poradie} neexistuje")

    def list_kosik(self):
        if not self.polozky:
            print("Košík je prázdny.")
        else:
            print("Obsah košíka:")
            for poradie, polozka in self.polozky.items():
                print(f"{poradie}: {polozka}")


class Polozka:
    def __init__(self, nazev, cena):
        self.nazev = nazev
        self.cena = cena

    def __str__(self):
        return f"{self.nazev}, cena: {self.cena}"


# Vytvorím zoznam dostupných produktov
dostupne_produkty = [
    Polozka("Boty do roboty", 1000),
    Polozka("Ponožky na nožky", 100),
    Polozka("Čapica na hlavu", 300),
    Polozka("Rukavice do mrazu", 500),
]

# Vytvorím objekt košíka
kosik = Kosik(uuid.uuid4())

error = ""

while True:
    # Vyčistím konzolu
    os.system("cls" if os.name == "nt" else "clear")

    # Zobrazím dostupné produkty
    print("Dostupné produkty:")
    for i, produkt in enumerate(dostupne_produkty, start=1):
        print(f"{i}: {produkt}")

    print("\n" + "-" * 30)

    # Zobrazím obsah košíka
    kosik.list_kosik()

    print("\nDostupné príkazy:")
    print("add:<číslo produktu> - pridaj produkt do košíka")
    print("remove:<číslo v košíku> - odstráň produkt z košíka")
    print("exit - ukonči program")
    print("-" * 30)

    if error:
        print(f"Chyba: {error}")

    # Vymazanie chyby pre ďalšiu iteráciu
    error = ""

    # Načítanie príkazu od používateľa
    command = input("Zadaj príkaz: ").strip()

    if command.startswith("add:"):
        try:
            produkt_id = int(command[4:])
            if 1 <= produkt_id <= len(dostupne_produkty):
                produkt = dostupne_produkty[produkt_id - 1]
                kosik.pridaj_polozku(produkt)
                print(f'Produkt "{produkt}" bol pridaný do košíka.')
            else:
                error = "Neplatné ID produktu."
        except ValueError:
            error = "Zadajte platné číslo produktu."
    elif command.startswith("remove:"):
        try:
            kosik_id = int(command[7:])
            kosik.odstran_polozku_by_poradie(kosik_id)
        except ValueError:
            error = "Zadajte platné číslo položky v košíku."
    elif command == "exit":
        break
    else:
        error = "Neplatný príkaz."

    input("\nStlač Enter pre pokračovanie...")
