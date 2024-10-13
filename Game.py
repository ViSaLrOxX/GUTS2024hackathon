from datetime import datetime
from Time import Time
import numpy as np
import random
import csv
from utils import wgs84_web_mercator_point, rescale_coordinates
from Airport import Airport
from Plane import Plane
from config import NUM_PLANES, NUM_AIRPORTS, EUROPE, WIDTH, HEIGHT, MOVEMENT, FPS
import pygame

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

class Game:
    total_airports = {} 

    def __init__(self, seed=0):

        self.airports_used = set()
        self.time = Time(int(datetime.now().strftime('%H:%M:%S')[:2]), int(datetime.now().strftime('%H:%M:%S')[3:5]))
        self.bottom = [49.605015, -12.482707] # Bottom left coordinates
        self.top = [61.160198, 1.686227] # Top right coordinates
        self.airports = []
        self.planes = []
        self.readFiles()
        self.seed = 0
        self.generate_planes()
        # print([airport.name for airport in self.airports])

        pygame.init()

        self.BackGround = Background('Mercator_projection_Square.JPG', [0,0])

        if EUROPE:
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        else:
            self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
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
                if event.type == pygame.KEYDOWN:
                    print(pygame.mouse.get_pos())


            if MOVEMENT:
                self.update()

            self.screen.fill((255,255,255)) # fill the screen with white
            self.screen.blit(self.BackGround.image, self.BackGround.rect)
            for airport in self.airports_used:
                # print(plane.xCoord,plane.yCoord)
                airport.draw(self.screen) # draw the airport to the screen
            
            for plane in self.planes:
                # print(plane.xCoord,plane.yCoord)
                plane.draw(self.screen) # draw the bird to the screen
            
            pygame.display.update() # update the screen

            self.clock.tick(FPS)
        
    def update(self):
        self.time.set_time(2, 1)
        for i in range(len(self.planes)):
            self.planes[i].update()

    def add_connection(self, main: Airport, other:Airport, weight: float):
        self.airport_connections[main][other] = weight
        pass

    def getAirports(self):
        for airport in Game.total_airports:
            print(airport)
            print(Game.total_airports[airport].name,Game.total_airports[airport].pos)
            print("-------")
    
    def readFiles(self):
        if EUROPE:
            with open("airport_traffic_2016.csv", 'r', encoding="utf8") as file1:
                file1.readline()
                for line in file1.readlines()[:NUM_AIRPORTS]:
                    csvReader = line.split(",")
                    airport =  Airport(csvReader[8], csvReader[7], csvReader[5], csvReader[4])
                    Game.total_airports[csvReader[4]] = airport

            with open('GlobalAirportDatabase.txt', 'r') as file2:
                data = file2.readlines() 
                random.shuffle(data)
        
            for airport in data:
                details = airport.strip().split(':')
                airport = Game.total_airports.get(details[0])
                if airport:
                    mercator = rescale_coordinates(int(details[9]), int(details[5]),WIDTH,HEIGHT)
                    airport.pos = mercator
                    # airport.pos = rescale_coordinates(float(details[9]), float(details[5]), WIDTH,700)
                    # airport.pos = rescale_coordinates(float(7.710992), float(45.865565), WIDTH,700)
        else:
            with open("world-airports.csv", 'r', encoding="utf8") as f:
                data = f.readlines()[1:]
                random.shuffle(data)
                print(data)
                for line in data[:NUM_AIRPORTS]:
                    csvReader = line.split(",")
                    flights_planned = int(str(csvReader[-2])[:2])//4+2
                    airport =  Airport(flights_planned, csvReader[3], csvReader[1])
                    try:
                        mercator = rescale_coordinates(float(csvReader[5]), float(csvReader[4]),WIDTH,HEIGHT)
                        airport.pos = mercator
                        Game.total_airports[csvReader[4]] = airport
                    except:
                        pass


        self.airports = list(Game.total_airports.values())
        self.weights = [int(airport.departures) for airport in self.airports]

    def generate_planes(self):
        for count in range(81):
            while True:
                selection = random.choices(self.airports, self.weights, k=1)
                if selection[0] not in self.airports_used:
                    break
                break
            self.airports_used.add(selection[0])
            num_planes = 0
            total_planes = random.choice(range(selection[0].departures//2))
            while num_planes < total_planes:
                plane = Plane(destination=None,
                                        departure=selection[0],
                                        xCoord=selection[0].pos[0],
                                        yCoord=selection[0].pos[1],
                                        v = 0.5 if MOVEMENT else 0,
                                        expectedArrival=Time(self.time.hours, self.time.minutes).add_minutes(120),
                                        )
                plane.change_destination(random.choice(list(self.airports_used)))
                self.planes.append(plane)
                
                num_planes +=1 
        print(len(self.airports_used), num_planes, total_planes)


if __name__ == "__main__":
    game1 = Game()


