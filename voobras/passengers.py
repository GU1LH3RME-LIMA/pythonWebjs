import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

DB_URL='mysql+mysqldb://root:''@localhost:3306/flights'
engine = create_engine(DB_URL)
db = scoped_session(sessionmaker(bind=engine))

def main():
    flights= db.execute("SELECT id, origin, destination, duration FROM flight").fetchall()
    for flight in flights:
        print(f"{flight.id}: {flight.origin} para {flight.destination}, {flight.duration}h de viagem")

    ID=int(input("\n Selecione a viagem: "))

    flight= db.execute("SELECT origin, destination, duration FROM flight WHERE id = :id",
                       {"id":ID}).fetchone()

    if flight is None:
           print("Não há essa viagem")
           return

    passengers=db.execute("SELECT name FROM passengers WHERE flight_id = :flight_id",
                       {"flight_id":ID}).fetchall()

    print("\nPassageiros:")

    for passenger in passengers:
           print(f"{passenger.name}")
    if len(passengers)==0:
           print("Sem passageiros")

if __name__=='__main__':
    main()
