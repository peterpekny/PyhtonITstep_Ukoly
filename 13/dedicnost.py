# Priklad kompozice:
# ==================

# - car >> engine
# - human >> eye
# - Department >> Employee

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}, salary: {self.salary}'
    
class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []


# Priklad dedicnosti: 
# ===================
# - car >> mercedes >> mercedes_amg
# - human >> gender >> person  
# - Employee >> ITtechnician >> ITtechnician_teamleader

class Employee:
    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}, salary: {self.salary}'


class ITtechnician(Employee):
    def __init__(self, first_name, last_name, salary, on_call_duty):
        super().__init__(first_name, last_name, salary)
        self.on_call_duty = on_call_duty


class ITtechnician_teamleader(ITtechnician):
    def __init__(self, first_name, last_name, salary, on_call_duty, management_dutys):
        super().__init__(first_name, last_name, salary, on_call_duty)
        self.management_dutys = management_dutys


my = ITtechnician('Peter', 'P', 1_000_000, True)

Martin = ITtechnician_teamleader('Martin', 'C', 1_000_001, True, True)

print(my)
print(Martin)