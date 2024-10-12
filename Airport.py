import Plane
class Airport:
    def __init__(self, 
                 xCoord: float, 
                 yCoord: float, 
                 arrivals: list, 
                 departures: list, 
                 max_capacity: int,
                 num_planes: int):
        self.x = xCoord
        self.y = yCoord
        self.arrivals = arrivals
        self.departures = departures
        self.max_capacity = max_capacity
        self.num_planes = num_planes
    def update(self, time):
        pass

