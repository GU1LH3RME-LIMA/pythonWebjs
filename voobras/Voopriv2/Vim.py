from flask import Flask, render_template, request
from classeprin import *

app=Flask(__name__)
DB_URL='mysql+mysqldb://root:''@localhost:3306/flights'
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)


@app.route("/")
def index():
    flights=Flights.query.all()
    return render_template("index.html",flights=flights)

@app.route("/decolagem",methods=["POST"])

def deco():
    name= request.form.get("name")
    try:
        flight_id= int(request.form.get("flight_id"))
    except:
        return render_template("error.html",message="Viagem invalida.")
    flight = Flights.query.get(flight_id)
    if flight is None:
        return render_template("error.html",message="Não há mais essa viagem.")

    flight.add_passenger(name)
    return render_template("success.html")

@app.route("/flights")
def flights():
    flights=Flights.query.all()
    return render_template("flights.html",flights=flights)

@app.route("/flights/<int:flight_id>")

def flight(flight_id):
    flight=Flights.query.get(flight_id)
    if flight is None:
        return render_template("error.html",message="Não há mais essa viagem.")
    passengers=flight.passenger
    
    
    return render_template("flight.html",passengers=passengers,flight=flight)
        
        
