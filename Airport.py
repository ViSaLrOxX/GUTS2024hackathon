import pygame
from AirportState import AirportState
from Continents import Continent
class Airport:
    def __init__(self,
                 departures: int,
                 name: str,
                 code: str,
                 state: AirportState = AirportState.AVAILABLE,
                 continent: Continent = Continent.EU):
        self.pos = None
        self.name = name
        # print(arrivals)
        self.arrivals = []
        self.departures = min(int(departures),10)
        self.max_capacity = 2 *int(self.departures)
        self.num_planes = 0
        self.code = code
        self.state = state
        self.image = pygame.image.load("airport.png")
        self.image = pygame.transform.scale(self.image, (20,20))

        self.continent = Continent.EU
        match (continent):
            case "EU":
                self.continent = Continent.EU
                return
            case "AS":
                self.continent = Continent.MEA
                return
            case "AF":
                self.continent = Continent.AF
                return
            case "SA":
                self.continent = Continent.SA
                return
            case "OC":
                self.continent = Continent.PO
                return
            case "NA":
                self.continent = Continent.NA
                return
        
    def update(self, time):
        pass

    def process_request(self):
        return self.state

    def getCoord(self):
        print(self.x, self.y)

    def draw(self, surface): 
        surface.blit(self.image, (self.pos[0], self.pos[1]))

