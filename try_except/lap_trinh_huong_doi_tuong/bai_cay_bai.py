class Flight:
    counter = 1

    def __init__(self,origin,destination,duration):
        self.id = Flight.counter
        Flight.counter+=1
        self.passengers = []
        self.origin = origin
        self.destination = destination
        self.duration = duration
    
    def print_info(self):
        print(f'Flight id: {self.id}')
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")
        print()
        print("Passengers")
        for passengers in self.passengers:
            print(f"{passengers.name}")

    def delay(self,amount):
        self.duration += amount

    def add_passenger(self,p):
        self.passengers.append(p)

def main():

    f1 = Flight(origin="New York",destination="Paris",duration=540)
    f1.print_info()

    f2 = Flight(origin="Tokyo",destination="VietNam",duration=185)
    f2.print_info()

if __name__ == "__main__":
    main()