from datetime import datetime
from Time import Time
import csv

class Game:

    def __init__(self):
        # f = open("data.csv", "r")
        # self.airports = list(csv.reader(f, delimiter=","))
        # f.close()

        self.time = Time(int(datetime.now().strftime('%H:%M:%S')[:2]), int(datetime.now().strftime('%H:%M:%S')[3:5]))
        print(self.time)
        self.bottom = [49.605015, -12.482707] # Bottom left coordinates
        self.top = [61.160198, 1.686227] # Top right coordinates

    def update(self):
        self.time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == "__main__":
    Game()
    print(2)
