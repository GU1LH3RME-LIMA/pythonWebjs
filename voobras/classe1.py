class Flight:

    def __init__(this,origin,destination,duration):

        this.origin=origin
        this.destination=destination
        this.duration=duration
    def self_print(this):

        print(f"de: {this.origin}")
        print(f"para:{this.destination}")
        print(f"{this.duration}h")

def main():

    fli= Flight(origin="Vitoria",destination="Brasília",duration=2)
    fli2=Flight("Caraguatatuba","Ouro Preto",4)
    Flight.self_print(fli)
    fli2.self_print()
if __name__=="__main__":
    main()
