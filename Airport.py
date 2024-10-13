import pygame
from AirportState import AirportState
from Continents import Continent
class Airport:
    def __init__(self,
                 departures: int,
                 name: str,
                 code: str,
                 state: AirportState = AirportState.AVAILABLE,
                 continent: Continent = "EU"):
        self.pos = None
        self.name = name
        # print(arrivals)
        self.arrivals = []
        self.departures = min(int(departures),10)
        self.max_capacity = 2 *int(self.departures)
        self.num_planes = 0
        self.code = code
        self.state = state
        self.prev_state = None
        self.image = pygame.image.load("airport.png")
        self.image = pygame.transform.scale(self.image, (20,20))

        self.continent = Continent.EU
        continents = {"EU": Continent.EU,
                      "AF": Continent.AF,
                      "AS": Continent.MEA,
                      "SA": Continent.SA,
                      "OC": Continent.PO,
                      "NA": Continent.NA,}
        
        self.continent = continents[continent]
        
    def update(self, time):
        pass

    def process_request(self):
        return self.state

    def getCoord(self):
        print(self.x, self.y)

    def draw(self, surface): 
        surface.blit(self.image, (self.pos[0], self.pos[1]))

    def getImage(self):
        return self.image
    
    def typhoon(self):
        self.prev_state = self.state
        self.state = AirportState.EMERGENCY
        return

    def typhoonOver(self):
        self.state = self.prev_state
        return
