### !!!! Najhorsia uloha ever #####
###################################

# vytvořte soubor 08_regex.py

# kde bude funkce check_phone_number,
# která dokáže zkontrolovat,
# zda zadaný text je validní telefonní číslo

# příklady validních čísel:

# 777777777
# 777 777 777
# +420777777777
# +420 777 777 777

# 777777777  777 777 777  +420777777777  +420 777 777 777


# pro všechny tyto formáty vrátí True, jinak False

# print(check_phone_number('test')) # -> False
# print(check_phone_number('608 192 292')) # -> True (True pro všechny formáty uvedené výše)
# print(check_phone_number('608 192 292...')) # -> False

import re

# My own
def check_phone_no(p_number):
    # Defuine regex for various cases
    rx_tel_case_1 = re.compile(r'(?<!\d)\d{9}(?!\d)')
    rx_tel_case_2 = re.compile(r'^(\d{3} \d{3} \d{3})')
    rx_tel_case_3 = re.compile(r'(\+420[0-9]{9})')
    rx_tel_case_4 = re.compile(r'(\+420 [0-9]{3} [0-9]{3} [0-9]{3})')
    
    # run throught all cases
    result1 = re.search(rx_tel_case_1, p_number)
    result2 = re.search(rx_tel_case_2, p_number)
    result3 = re.search(rx_tel_case_3, p_number)
    result4 = re.search(rx_tel_case_4, p_number)

    # Will be removed after testing
    # -----------------------------
    if result1:
        print("Patern1 match", result1)
    if result2:
        print("Patern2 match", result2)
    if result3:
        print("Patern3 match", result3)
    if result4:
        print("Patern4 match", result4)
    # -------------------------------
    
    # check if at least one match
    if result1 or result2 or result3 or result4:
        return True
    else:
        return False
    

# Chat GPT optimalisation
def check_phone_no_gpt(pnumber):
    patterns = [
    r'(?<!\d)\d{9}(?!\d)',                   # 9 číslic bez medzier a predvoľby
    r'^(\d{3} \d{3} \d{3})',                 # 9 číslic s medzerami medzi trojicami
    r'(\+420[0-9]{9})',                      # +420 a 9 číslic bez medzier
    r'(\+420 [0-9]{3} [0-9]{3} [0-9]{3})',   # +420 a 9 číslic s medzerami medzi trojicami
    ]
    
    # Použitie any() na kontrolu, či sa niektorý regulárny výraz zhoduje
    return any(re.match(pattern, pnumber) for pattern in patterns)

while True:
    to_check = str(input('Gimme no: '))
    print(check_phone_no(to_check))
    print(check_phone_no_gpt(to_check))



