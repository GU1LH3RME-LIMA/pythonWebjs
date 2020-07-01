
from flask import Flask,render_template,request
from classeprin import *

app=Flask(__name__)
DB_URL='mysql+mysqldb://root:''@localhost:3306/flights'
app.config["SQLALCHEMY_DATABASE_URI"] = DB_URL
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)

def main():
    flights=Flights.query.all()
    for f in flights:
        print(f"de {f.origin} para {f.destination} em {f.duration} h")

if __name__=="__main__":
    with app.app_context():
        main()


