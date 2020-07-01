import os

from flask import Flask, render_template, request
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

app = Flask(__name__)

DB_URL='mysql+mysqldb://root:''@localhost:3306/flights'
engine = create_engine(DB_URL)
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")

def index():
    flights=db.execute("select * from flight").fetchall() 
    return render_template("index.html", flights=flights)

@app.route("/decolagem",methods=["POST"])

def deco():
    #pega as informações
    name= request.form.get("name")
    try:
        flight_id= int(request.form.get("flight_id"))
    except:
        return render_template("error.html",message="Viagem invalida.")

    if db.execute("select * from flight WHERE id= :id",
                  {"id":flight_id}).rowcount==0:
        return render_template("error.html",message="Não há mais essa viagem.")
    
    db.execute("insert into passengers(name,flight_id) VALUES (:name,:flight_id)",
               {"name": name, "flight_id": flight_id})
    if name=="":
        return render_template("error.html",message="Nome do passageiro não foi inserido")
    db.commit()
    return render_template("success.html")

@app.route("/flights")
def flights():
    flights=db.execute("select * FROM flight").fetchall()
    return render_template("flights.html",flights=flights)

@app.route("/flights/<int:flight_id>")

def flight(flight_id):
    #detail about a single flight

    flight= db.execute("select * FROM flight WHERE id=:id",{"id":flight_id}).fetchone()
    if flight is None:
        return render_template("error.html",message="Não há mais essa viagem.")
    passengers=db.execute("select name from passengers WHERE flight_id=:flight_id",{"flight_id":flight_id}).fetchall()

    return render_template("flight.html",passengers=passengers,flight=flight)
        
        
