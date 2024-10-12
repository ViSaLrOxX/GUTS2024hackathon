class plane:
    def __init__(self, destination, size, departure, expectedArrival, delayedArrival, xCoord, yCoord):
        self.destination = destination
        self.size = size
        self.departure = departure
        self.expectedArrival = expectedArrival
        self.delayedArrival = delayedArrival
        self.xCoord = xCoord
        self.yCoord = yCoord

    def update(self, newDest):
        self.destination = newDest

