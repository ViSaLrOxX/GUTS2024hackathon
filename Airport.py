
class Airport:
    def __init__(self, 
                 xCoord: float, 
                 yCoord: float, 
                 arrivals: int, 
                 departures: int, 
                 max_capacity: int,
                 total_flights: int):
        self.x = xCoord
        self.y = yCoord
        self.arrivals = arrivals
        self.departures = departures
        self.max_capacity = max_capacity
        self.total_flights = total_flights

    def update(self, time):
        pass

    def getCoord(self):
        print(self.x, self.y)

