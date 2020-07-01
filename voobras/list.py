import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DB_URL='mysql+mysqldb://root:''@localhost:3306/flights'
engine = create_engine(DB_URL)
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights= db.execute("SELECT origin, destination, duration FROM flight").fetchall()
    for flight in flights:
        print(f"{flight.origin} para {flight.destination}, {flight.duration}h de viagem") 

if __name__=="__main__":
    main()
