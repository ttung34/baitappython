class Flight:
    def __init__(self,origin,destination,duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration
    
    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

    def delay(self, amount):
        self.duration+= amount
    
def main():
    
    f1 = Flight(origin="New York",destination="Paris",duration=540)
    f1.print_info()
    print("-------------flight will be delayed 10 minutes---------")
    f1.delay(10)
    f1.print_info()