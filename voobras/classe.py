class Flight:

    def __init__(this,origin,destination,duration):

        this.origin=origin
        this.destination=destination
        this.duration=duration
def main():

    f=Flight(origin="Maranhão",destination="Rio de Janeiro",duration=4)

    f.duration+=1

    print(f.origin)
    print(f.destination)
    print(f.duration)


if __name__=="__main__":
    main()
    
