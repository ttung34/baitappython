from add_more_attrinut import CheapFlight, NormalFlight
from passenger import Passenger

cheapflighthnhcm = CheapFlight("HN", "HCM", "150","nuoc loc")
print(cheapflighthnhcm)

passenger1 = Passenger("Long")
passenger2 = Passenger("Khanh")
cheapflighthnhcm.add_passenger(passenger1)
cheapflighthnhcm.add_passenger(passenger2)

cheapflighthnhcm.print_info()

normalflighthnhcm = NormalFlight("HN","HCM","150",["Pho","bun","my y","Nuoc ngot"],100)
print(normalflighthnhcm)

passenger1 = Passenger("Vuong")
passenger2 = Passenger("Tuan")
normalflighthnhcm.add_passenger(passenger1)
normalflighthnhcm.add_passenger(passenger2)

normalflighthnhcm.print_info()
