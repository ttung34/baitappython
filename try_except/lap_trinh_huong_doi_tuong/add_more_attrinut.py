class Flight:
    """
    The function takes in a list of numbers and returns the sum of the numbers.
    """
     
    counter = 1

    def __init__(self, origin, destination,duration):

        self.id =Flight.counter
        Flight.counter+=1

        self.passeners =[]
        self.origin =origin
        self.destination=destination
        self.duration=duration
    
    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        # Printing the duration of the flight.
        print(f"Flight duration: {self.duration}")

        print()
        print("Passengers:")
        for passenger in self.passengers:
            print(f"{passenger.name}")


    def add_passenger(self,p):
        self.passengers.append(p)

class Passenger:
     
    def __init__(self,name):
        self.name = name

    def main():
        f1 = Flight(origin="New York",destination="Paris",duration=540)

        Long = Passenger(name="Long")
        Vuong = Passenger(name="Vuong")

        f1.add_passenger(Long)
        f1.add_passenger(Vuong)
    
        f1.print_info()

    if __name__ =="__main__":
        main()

class CheapFlight(Flight):

    def __init__(self,origin, destination, duration, drink):
        super().__init__(origin,destination,duration)
        self.drink=drink

    def print_info(self):
        super().print_info()
        print(f"drink: {self.drink}")

class NormalFlight(Flight):
    
    def __init__(self,origin, destination, duration, meal, memberPoint):
        super().__init__(origin,destination,duration)
        self.meal =meal
        self.memberPoint =memberPoint

    def print_info(self):
        super().print_info()
        print(f"Meal:{self.meal}")
        print(f"memberPoint: {self.memberPoint}")