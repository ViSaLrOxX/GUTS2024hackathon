
class Airport:
    def __init__(self,
                 arrivals: int, 
                 departures: int,
                 name: str):
        self.pos = None
        self.name = name
        self.arrivals = arrivals
        self.departures = departures
        self.max_capacity = 2 *self.departures 

    def update(self, time):
        pass

    def getCoord(self):
        print(self.x, self.y)

