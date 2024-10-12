from datetime import datetime
from Time import Time
import csv
from Airport import Airport
class Game:

    def __init__(self):
        # f = open("data.csv", "r")
        # self.airports = list(csv.reader(f, delimiter=","))
        # f.close()
        self.airport_connections = {}
        self.time = Time(int(datetime.now().strftime('%H:%M:%S')[:2]), int(datetime.now().strftime('%H:%M:%S')[3:5]))
        print(self.time)
        self.bottom = [49.605015, -12.482707] # Bottom left coordinates
        self.top = [61.160198, 1.686227] # Top right coordinates

    def update(self):
        self.time.set_time(2, 1)

    def add_connection(self, main: Airport, other:Airport, weight: float):
        self.airport_connections[main][other] = weight
        pass
if __name__ == "__main__":
    game1 = Game()
    game2 = game1
    print(game2)
    game2.update()
    print(game2)
    print(game1 == game2)
