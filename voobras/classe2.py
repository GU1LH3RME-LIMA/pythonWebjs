class Flight:
    count=1
    def __init__(this,origin,destination,duration):
        this.id=Flight.count
        Flight.count+=1

        this.passengers=[]
        this.origin=origin
        this.destination=destination
        this.duration=duration
    def self_print(this):

        print(f"de: {this.origin}")
        print(f"para:{this.destination}")
        print(f"{this.duration}h")
        print("\n ==Passageiros====")

        for passenger in this.passengers:
            print(f"{passenger.name}")
    
    def delay(this,amount):
        this.duration+=amount

    def add_passenger(this,p):
        this.passengers.append(p)
        p.flight_id=this.id
class Passenger:
    def __init__(this,name):
        this.name=name

def main():
    fli=Flight("Caraguatatuba","Ouro Preto",4)

    Pele=Passenger("Pelé")
    Roma=Passenger("Romario")

    fli.add_passenger(Pele)
    fli.add_passenger(Roma)
    fli.delay(1)
    fli.self_print()

if __name__=="__main__":
    main()