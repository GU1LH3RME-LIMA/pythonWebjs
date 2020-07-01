from flask_sqlalchemy import SQLAlchemy 

db=SQLAlchemy()

class Flights(db.Model):
    __tablename__= "flight"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    origin=db.Column(db.VARCHAR,nullable=False)
    destination=db.Column(db.VARCHAR,nullable=False)
    duration=db.Column(db.Integer,nullable=False)

class Passenger(db.Model):
    __tablename__ = "passengers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR, nullable=False)
    flight_id = db.Column(db.Integer, db.ForeignKey("flight.id"), nullable=False)