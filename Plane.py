from config import SIMULATED_TIME_STEP
import numpy as np
import math
from Airport import Airport
from PlaneState import PlaneState
import PlaneSizes
from Time import Time
import pygame

class Plane:
    def __init__(self, 
                 destination: Airport = None, 
                 size: Airport = None, 
                 departure: Airport = None, 
                 expectedArrival: Time = Time(0,2), 
                 delayedArrival: Time = Time(1, 3), 
                 xCoord: float = 0, yCoord: float = 0, heading: float = 10, v: float = 2, 
                 state: PlaneState = PlaneState.IN_FLIGHT):
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
        self.emergency = False
        self.image = pygame.image.load("plane.png")
        self.image = pygame.transform.scale(self.image, (20,20))

    def update(self):
        delta_t = SIMULATED_TIME_STEP
        r = min(SIMULATED_TIME_STEP* self.v, np.linalg.norm(self.x - self.destination.x,
                                                            self.y - self.destination.y))
        if self.state == PlaneState.IN_FLIGHT:
            self.x += SIMULATED_TIME_STEP* self.v* math.cos(self.heading)
            self.y += SIMULATED_TIME_STEP* self.v* math.sin(self.heading)

    def emergency(self):
        if self.state.IN_FLIGHT & self.delayedArrival > self.expectedArrival + 2:
            self.emergency = True

    def delay_check(self):
        if self.state.IN_FLIGHT:
            pass
            # Math to check delay time

    def change_destination(self):
        if self.state.IN_FLIGHT:
            pass
            # How to calculate local airports?



    def draw(self, surface):
        self.image = pygame.transform.rotate(self.image, math.degrees(self.heading))
        surface.blit(self.image, (self.xCoord, self.yCoord))


