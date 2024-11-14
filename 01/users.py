import os, json

DATA_PATH = "01/users.json"

# TRUE ak file existuje
if not os.path.isfile(DATA_PATH):
    raise FileNotFoundError(f'File: {DATA_PATH} do not exists, on the filesystem ...')
    
print(f'File: {DATA_PATH} found')


#print(f'tento file som skontroloval: {DATA_PATH}')

def check_password(password, password_repeat):
    if password != password_repeat:
        raise ValueError('Hesla sa nezhoduju')

def check_user(data, username):
    if username in data:
        raise ValueError('Uzivatel uz existuje')

def read_data():
    with open(DATA_PATH, encoding='utf-8') as file1:
        data = json.load(file1)
    return data

def write_data(data):
    with open(DATA_PATH, mode="w", encoding='utf-8') as file1:
        json.dump(data, file1)


def login(username, password):
    data = read_data()
    try:
        assert data[username] == password
        return True
    except(KeyError, AssertionError):
        return False
        

def register(username, password, password_repeat):
    check_password(password, password_repeat)
    data = read_data()
    check_user(data, username)
    data[username] = password
    write_data(data)


def change_password(username, old_password, new_password, password_repeat):
    data = read_data()
    if username in data and data[username] == old_password:
        if new_password == password_repeat:
            data[username] = new_password
            write_data(data)
            print(f'Password was changed ... new pass: {new_password}')
        else:
            print('Repeate password did not validate !!!')
    else:
        print('username or password issue !!!')

def delete_user(username, password):
    data = read_data()
    if username in data and data[username] == password: 
        del data[username]
        write_data(data)
    else:
        print('Uzivatel neexistuje')
        

#register('Fero', 'heslo', 'heslo')

#print(login('Fero','heslo'))

#delete_user('test', 'heslo')

change_password('dano-drevo', 'heslo-213', 'heslo-113', 'heslo-113')