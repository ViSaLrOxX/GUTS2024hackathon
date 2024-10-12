from datetime import datetime
from Time import Time
import numpy as np
import random
import csv
from utils import wgs84_web_mercator_point
from Airport import Airport
from Plane import Plane

class Game:
    total_airports = {} 

    def __init__(self, seed=0):
        self.airport_connections = {}
        self.time = Time(int(datetime.now().strftime('%H:%M:%S')[:2]), int(datetime.now().strftime('%H:%M:%S')[3:5]))
        print(self.time)
        self.bottom = [49.605015, -12.482707] # Bottom left coordinates
        self.top = [61.160198, 1.686227] # Top right coordinates
        self.readFiles()
        self.airports = list[Airport]
        self.planes = list[Plane]
        self.seed = 0

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
            for line in file1.readlines():
                csvReader = line.split(",")
                airport =  Airport(csvReader[8], csvReader[7], csvReader[5])
                Game.total_airports[csvReader[4]] = airport

        with open('GlobalAirportDatabase.txt', 'r') as file2:
            data = file2.readlines() 
        for airport in data:
            details = airport.strip().split(':')
            airport = Game.total_airports.get(details[0])
            if airport:
                mercator = wgs84_web_mercator_point(int(details[9]), int(details[5]))
                airport.pos = mercator
        self.airports = list(self.total_airports.values())
        self.weights = [airport.total_flights for airport in self.airports]

    def assign_destinations(self,departure_airport, i):
        finished = False
        while finished == False:
            selection = random.choices(self.airports, self.weights, k=5)
            for i in range(len(selection)):
                if selection[i].num_planes < selection[i].max_capacity:
                    self.planes[i].setDestination(selection[i])
                    finished = True
                    break

    def generate_planes(self, num_planes):
        planes_generated = 0
        selection = random.choice(self.airports)
        if selection.num_planes < selection.max_capacity:
            self.planes.append(Plane(destination=, ))
if __name__ == "__main__":
    game1 = Game()
    game1.getAirports()


