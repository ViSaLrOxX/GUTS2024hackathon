from datetime import datetime
from Time import Time
import csv
from utils import wgs84_web_mercator_point
from Airport import Airport

class Game:

    def __init__(self):
        self.airport_connections = {}
        self.time = Time(int(datetime.now().strftime('%H:%M:%S')[:2]), int(datetime.now().strftime('%H:%M:%S')[3:5]))
        print(self.time)
        self.bottom = [49.605015, -12.482707] # Bottom left coordinates
        self.top = [61.160198, 1.686227] # Top right coordinates
        self.readFiles()

    def update(self):
        self.time.set_time(2, 1)

    def add_connection(self, main: Airport, other:Airport, weight: float):
        self.airport_connections[main][other] = weight
        pass

    def getAirports(self):
        #for airport in self.airports:
            #print(airport)
        return self.airports[0].getCoord()
    
    def readFiles(self):
        self.airports = []
        csvAirports = []

        with open("airport_traffic_2016.csv", 'r', encoding="utf8") as file1:
            csvReader = csv.reader(file1)
            next(csvReader)
            
            for row in csvReader:
                csvAirports.append(row)

        with open('GlobalAirportDatabase.txt', 'r') as file2:
            data = file2.readlines()
        
        for airport in data:
            details = airport.strip().split(':')
            IACO = details[0]

            for iaco in csvAirports:
                if iaco[4] == IACO:
                    mercator = wgs84_web_mercator_point(int(details[9]), int(details[5]))
                    self.airports.append(Airport(mercator[0],mercator[1],iaco[8],iaco[7],int(iaco[8])+5,iaco[9])) #change +5 with constant


if __name__ == "__main__":
    game1 = Game()
    game2 = game1
    print(game2)
    game2.update()
    print(game2)
    print(game1 == game2)
    game1.getAirports()
