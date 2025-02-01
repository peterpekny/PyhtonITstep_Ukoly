from django.http import HttpResponse
from django.shortcuts import render

import random
import datetime as dt

# Create your views here.

def index_page(request):
    
    print(request.method)
    print(request.path)

    number = random.randint(1, 100)
    d = dt.datetime.now()

    return HttpResponse(f"""<div style="text-align: center;">
                            <h1 >Hellou</h1><p>Django meloun</p>
                            <p>teraz je: {d}</p>
                            <p>Rand cislo je {number}</p>""")

# Puzitie klasickeho pristupu, bez renderu a template
def time_page(request):
    date = dt.datetime.now().strftime("%Y-%m-%d")
    time = dt.datetime.now().strftime("%H:%M:%S")

    return HttpResponse(f"""
        <html>
            <head>
                <style>
                    body {{
                        margin: 0;
                        background-color: lightyellow;
                        font-family: Arial, sans-serif;
                    }}
                    .content {{
                        position: absolute;
                        top: 50%; 
                        left: 50%; 
                        transform: translate(-50%, -50%); 
                        text-align: center;
                        font-size: 20px;
                        background-color: lightblue;
                        padding: 20px;
                        border-radius: 10px;
                    }}
                </style>
            </head>
            <body>
                <div class="content">
                    <h1>My Time Page</h1>
                    <h3>Today is: {date}</h3>
                    <h3>Time is: {time}</h3>
                </div>
            </body>
        </html>
    """)

# Puzitie renderu , a template time_page.html
from django.shortcuts import render

def time_page_2(request):
    # Do funcie si pripdame aktualny cas a datum
    date = dt.datetime.now().strftime("%Y-%m-%d")
    time = dt.datetime.now().strftime("%H:%M:%S")
    # pouzijeme render a vratime template time_page.html s premennymi date a time v dictionary
    return render(request, 'time_page.html', {'date': date, 'time': time})


def url_paths(request):

    print(request.GET)
    print(request.GET['value'])

    return HttpResponse(f"Toto je stranka s URL adresou: {request.path} {request.GET['value']} ") # vypise URL adresu

def my_math(request):
    """
    operation = plus | minus | multiple | div
    ?operation=plus&a=10&b=100
    a = ?
    b = ?
    """

    a = int(request.GET['a'])
    b = int(request.GET['b'])
    operation = request.GET['operation']
    
    # print(operation, a, b)

    if operation == 'plus':
        vysledek = a + b
    
    elif operation == 'minus':
        vysledek = a - b
    
    elif operation == 'multiple':
        vysledek = a * b
    
    elif operation == 'div':
        vysledek = a / b
    
    else: 
        vysledek = 'N/A'

    return HttpResponse(f"""Ahoj - ja som tvoj: my_math ...
                            <br><br> vysledek pro opraci: <b> {operation} </b> cisel: <b> {a} </b> a <b> {b} </b> je: <b> {vysledek}</b> """)

def test_template(request):
    
    # http://127.0.0.1:8000/test-template/?operation=plus&a=10&b=100&name=Peter

    try:
        a = int(request.GET['a'])
    except KeyError:
        a = False
    
    try:
        b = int(request.GET['b'])
    except KeyError:
        b = False

    try:
        operation = request.GET['operation']
    except KeyError:
        operation = False

    # Osetrime chybu - ak nieje zadane ziadne meno:
    # name = request.GET.get('name', '')
    
    # alebo takto sa da osetrit chyba:

    try:
        name = request.GET['name']
    except KeyError:
        name = 'Default'

    try:
        age = int(request.GET['age'])
    except KeyError:
        age = 0

    # osetrime age na cislo, a default hodnotu ak nebola zadana
    # age = int(age) if age.isdecimal() else 0

    # alebo takto osetrime zaznam

    # if 'name' in request.GET:
    #     name = request.GET['name']
    # else:
    #     name = 'Default'
   

    if operation and a and b:
        status = 'OK - all data was given'
        
        # Starting calculator
        if operation == 'plus':
            vysledek = a + b
        
        elif operation == 'minus':
            vysledek = a - b
        
        elif operation == 'multiple':
            vysledek = a * b
        
        elif operation == 'div':
            vysledek = a / b
        
    else: 
        vysledek = 'N/A'
        a = 'N/A'
        b = 'N/A'
        operation = 'N/A'
        status = 'Not all prerequsities was given !!!'

    context = {
        'date': dt.datetime.now(),
        'name': name,
        'vysledek': vysledek,
        'operation': operation,
        'a': a,
        'b': b,
        'status': status,
        'age': age
    }

    # return render (request, 'test_template.html', {'operation': operation, 'a': a, 'b': b } )
    return render (request, 'test_template.html', context )


def calculator(request):

    # http://127.0.0.1:8000/calculator/?operation=plus&a=10&b=100

    try:
        a = int(request.GET['a'])
    except KeyError:
        a = ''
    
    try:
        b = int(request.GET['b'])
    except KeyError:
        b = ''

    try:
        operation = request.GET['operation']
    except KeyError:
        operation = ''

    vysledek = ''
    status = ''

    if operation != '' and a != '' and b != '':
        status = 'OK - all data was given'
        
        # Starting calculator
        if operation == 'plus':
            vysledek = a + b
        
        elif operation == 'minus':
            vysledek = a - b
        
        elif operation == 'multiple':
            vysledek = a * b
        
        elif operation == 'div':
            vysledek = a / b
        

    context = {
                
        'vysledek': vysledek,
        'operation': operation,
        'a': a,
        'b': b,
        'status': status,
    }

    # return render (request, 'test_template.html', {'operation': operation, 'a': a, 'b': b } )
    return render (request, 'calculator.html', context )

# odkaz na funkciu login z ineho suboru
# from my_views.view_login import login 


def my_page(request, name):
    # return HttpResponse(f'Jmeno: { name }')
    context = {'name': name}
    return render(request, 'my_page.html', context)

def article(request, slug, number):
    context = {'slug': slug, 'number': number}
    return render(request, 'article.html', context)

def pages(request, slug, slug1, slug2 = '0'):
    context = {'slug': slug, 'slug1': slug1, 'slug2': slug2}
    return render(request, 'pages.html', context)

# ===========
# Ukol - 18
# ===========

def age_view(request):
    result = None
    error = None

    if request.method == "POST":
        birth_year = request.POST.get("birth_year")
        try:
            birth_year = int(birth_year)
            current_year = dt.datetime.now().year

            # Ošetření hodnoty roku (například nepříliš starý ani budoucí rok)
            if birth_year < 1900 or birth_year > current_year:
                error = "Zadejte prosím validní rok."
            else:
                age = current_year - birth_year
                result = f"Je vám asi {age} rokov"
        except (ValueError, TypeError):
            error = "Zadejte prosím číselnu hodnotu roku."

    return render(request, "age.html", {"result": result, "error": error})

# ===========
# Ukol - 19
# ===========

def signup(request):
    if request.method == "POST":
        try:
            # odchytime hodnoty z formulara
            name = request.POST.get("name") if request.POST.get("name") else "N/A"
            surname = request.POST.get("surname") if request.POST.get("surname") else "N/A"
            email = request.POST.get("email")
            password = request.POST.get("password")
            password_repeat = request.POST.get("password_repeat")
            
            # kontrola vyplnenia vsetkych poli
            if not email or not password or not password_repeat:
                raise ValueError("Vsetky polia musia byt vyplnene.")
            
            # Kontrola hesiel
            if password == password_repeat:
                # Ak se hesla zhoduju
                return render(request, "signup_success.html", {"name": name, "surname":surname, "email": email})
            else:
                # Ak se hesla nezhoduju
                return render(request, "signup_failed.html", {"error": "Hesla se nezhoduju."})
        except Exception as error:
            # Ak nastane nejaka chyba
            return render(request, "signup_failed.html", {"error": str(error)})
    else:
        # Rada od chatGPT - ak nieje POST, tak vratime prazdny formular
        return render(request, "signup.html")