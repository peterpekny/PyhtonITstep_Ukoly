def append_to_file(text):
    with open('02/04_file.txt', mode = 'a', encoding='utf-8') as file:
        file.write(text + '\n')

while True:
    coTamMamDat = input('Zadaj text: ')
    if coTamMamDat == 'c':
        break
    append_to_file(coTamMamDat)

