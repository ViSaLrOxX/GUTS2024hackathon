from config import SIMULATED_TIME_STEP
import numpy as np
import math
import Airport
import PlaneState
import PlaneSizes
class plane:
    def __init__(self, 
                 destination: Airport, 
                 size: Airport, 
                 departure: Airport, expectedArrival, delayedArrival, xCoord, yCoord, heading,v, state):
        self.destination = destination
        self.size = size
        self.departure = departure
        self.expectedArrival = expectedArrival
        self.delayedArrival = delayedArrival
        self.xCoord = xCoord
        self.yCoord = yCoord
        self.v = v
        self.heading = heading
        self.state = state

    def update(self):
        delta_t = SIMULATED_TIME_STEP
        x += SIMULATED_TIME_STEP* self.v* math.cos(self.heading)
        y += SIMULATED_TIME_STEP* self.v* math.sin(self.heading)



