class BankAccount:
    def __init__(self, account_number, owner, currency, balance=0):
        """Inicializuje bankovní účet."""
        self.account_number = account_number
        self.owner = owner
        self.currency = currency
        self.balance = balance

    def deposit(self, amount):
        """Vloží peníze na účet."""
        if amount > 0:
            self.balance += amount
            print(f"Úspěšně vloženo {amount} {self.currency}. Nový stav konta: {self.balance} {self.currency}.")
        else:
            print(f"Částka musí být větší než 0 {self.currency}.")

    def withdraw(self, amount):
        """Odebere peníze z účtu."""
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Úspěšně odebráno {amount} {self.currency}. Nový stav konta: {self.balance} {self.currency}.")
            else:
                print(f"!!! Nedostatek prostředků na účtu. Výběr: {amount} {self.currency} nepovolen, zústatek na účtu: {self.balance} {self.currency}.")
        else:
            print("Částka musí být větší než 0.")

    def print_balance(self):
        """Tiskne aktuální stav konta."""
        print(f"Stav konta majitele {self.owner} (Číslo účtu: {self.account_number}): {self.balance} {self.currency}.")

# TEST

# Account initialisation: add 1000CZK
account = BankAccount("1011011101", "Bender Bending Rodríguez", "CZK", 1000)

# Print ballance:
account.print_balance()

# Deposit - 500CZK
account.deposit(500)

# Successfull withdraw - 300 CZK
account.withdraw(300)

# Unsuccess withdraw - 1500 CZK
account.withdraw(1500)

# Print balance
account.print_balance()
