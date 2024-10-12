import pygame
class Airport:
    def __init__(self,
                 arrivals: int, 
                 departures: int,
                 name: str,
                 code: str):
        self.pos = None
        self.name = name
        self.arrivals = min(int(arrivals),10)
        self.departures = min(int(departures),10)
        self.max_capacity = 2 *int(self.departures )
        self.num_planes = 0
        self.code = code
        self.image = pygame.image.load("airport.png")
        self.image = pygame.transform.scale(self.image, (20,20))

    def update(self, time):
        pass

    def getCoord(self):
        print(self.x, self.y)

    def draw(self, surface): 
        surface.blit(self.image, (self.pos[0], self.pos[1]))

