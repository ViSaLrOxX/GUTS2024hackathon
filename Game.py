from datetime import datetime
from Time import Time
import numpy as np
import random
import csv
from utils import wgs84_web_mercator_point
from Airport import Airport
from Plane import Plane
from config import NUM_PLANES, NUM_AIRPORTS
class Game:
    total_airports = {} 

    def __init__(self, seed=0):
        self.airport_connections = {}
        self.time = Time(int(datetime.now().strftime('%H:%M:%S')[:2]), int(datetime.now().strftime('%H:%M:%S')[3:5]))
        self.bottom = [49.605015, -12.482707] # Bottom left coordinates
        self.top = [61.160198, 1.686227] # Top right coordinates
        self.airports = []
        self.planes = []
        self.readFiles()
        self.seed = 0
        self.generate_planes(NUM_PLANES)

        pygame.init()
        self.screen = pygame.display.set_mode((1000, 700))
        self.clock = pygame.time.Clock()

        self.running = True

        self.game_loop()

    def game_loop(self):
        while self.running:
            # handle every event since the last frame.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # quit the screen
                    self.running = False


            self.screen.fill((255,255,255)) # fill the screen with white
            for plane in self.planes:
                print(plane.xCoord,plane.yCoord)
                plane.draw(self.screen) # draw the bird to the screen
            pygame.display.update() # update the screen

            self.clock.tick(40)
        
    def update(self):
        self.time.set_time(2, 1)

    def add_connection(self, main: Airport, other:Airport, weight: float):
        self.airport_connections[main][other] = weight
        pass

    def getAirports(self):
        for airport in Game.total_airports:
            print(airport)
            print(Game.total_airports[airport].name,Game.total_airports[airport].pos)
            print("-------")
    
    def readFiles(self):
        with open("airport_traffic_2016.csv", 'r', encoding="utf8") as file1:
            file1.readline()
            for line in file1.readlines()[:NUM_AIRPORTS]:
                csvReader = line.split(",")
                airport =  Airport(csvReader[8], csvReader[7], csvReader[5], csvReader[4])
                Game.total_airports[csvReader[4]] = airport

        with open('GlobalAirportDatabase.txt', 'r') as file2:
            data = file2.readlines() 
        for airport in data:
            details = airport.strip().split(':')
            airport = Game.total_airports.get(details[0])
            if airport:
                mercator = wgs84_web_mercator_point(int(details[9]), int(details[5]))
                airport.pos = mercator

        self.airports = list(Game.total_airports.values())
        self.weights = [int(airport.arrivals) for airport in self.airports]

    def assign_destination(self,departure_airport, i):
        finished = False
        while finished == False:
            selection = random.choices(self.airports, self.weights, k=5)
            for i in range(len(selection)):
                if selection[i].num_planes < selection[i].max_capacity:
                    self.planes[i].change_destination(selection[i])
                    finished = True
                    break

    def generate_planes(self, num_planes):
        planes_generated = 0
        while planes_generated < num_planes:
            selection = random.choice(self.airports)
            if selection.num_planes < selection.max_capacity and (selection.pos):
                
                planes_generated += 1
                self.planes.append(Plane(destination=None, 
                                        departure=selection,
                                        xCoord=selection.pos[0],
                                        yCoord=selection.pos[1],
                                        expectedArrival=Time(self.time.hours, self.time.minutes).add_minutes(120),
                                        ))
                try:
                    self.assign_destination(selection, -1)
                except:
                    print(selection.pos)
                    print(selection.code)
            if planes_generated >= num_planes:
                break
        

if __name__ == "__main__":
    game1 = Game()


