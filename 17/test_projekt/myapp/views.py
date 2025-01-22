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