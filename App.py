import sqlite3
from datetime import datetime

from flask import Flask, render_template, request

app = Flask(__name__)

SUKUPUOLI =[
    "Mies",
    "Nainen",
    "En halua sano"
]
HARRASTUKSET =[
    "Jalkapalloa",
    "Lentopalloa",
    "Sulkapalloa",
    "Musiikkia",
    "Kävelyä",
    "Tanssia"
]
# the main route if nothing specified
@app.route('/')
def index():
    otsikko = 'This is also the landing page'   
    # otsikko = request.headers.get('User-Agent')
    return render_template("index.html",terv=otsikko)
    
@app.route("/register")
def register():    
    otsikko = 'Rekisteröidy'
    conn = sqlite3.connect('test.db')
    # conn.execute('CREATE TABLE users (id int, nimi TEXT, salasana TEXT, sahkoposti TEXT, code TEXT)')
    # print("Table created successfully");
    # conn.close()
    
    now = datetime.now()        
    paiva = now.strftime("%d %b, %Y Kello on %X")
    
    if conn:
        conn = 'Connection to database is up and running'
    else:
        conn = "Couldn't connect to database"
    return render_template('register.html', terv=otsikko, sukupuoli=SUKUPUOLI,harrastukset=HARRASTUKSET, conn=conn, paiva=paiva)
