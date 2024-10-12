from config import SIMULATED_TIME_STEP
import numpy as np
import math
from Airport import Airport
from PlaneState import PlaneState
import PlaneSizes
import Time
class Plane:
    def __init__(self, 
                 destination: Airport, 
                 size: Airport, 
                 departure: Airport, 
                 expectedArrival: Time, 
                 delayedArrival: Time, 
                 xCoord: float, yCoord: float, heading: float, v: float, 
                 state: PlaneState):
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
        r = min(SIMULATED_TIME_STEP* self.v, np.linalg.norm(self.x - self.destination.x,
                                                            self.y - self.destination.y))
        if self.state == PlaneState.IN_FLIGHT:
            self.x += SIMULATED_TIME_STEP* self.v* math.cos(self.heading)
            self.y += SIMULATED_TIME_STEP* self.v* math.sin(self.heading)




