from config import SIMULATED_TIME_STEP, LANDING_DISTANCE, EUROPE, HEIGHT
import numpy as np
import math
from Airport import Airport
from PlaneState import PlaneState
import PlaneSizes
from Time import Time
from utils import to_pygame
import pygame

class Plane:
    def __init__(self, 
                 destination: Airport = None, 
                 size: Airport = None, 
                 departure: Airport = None, 
                 expectedArrival: Time = Time(0,2), 
                 delayedArrival: Time = Time(1, 3), 
                 xCoord: float = 0, yCoord: float = 0, heading: float = 10, v: float = 100, 
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
        self.image = pygame.transform.rotate(self.image, math.degrees(self.heading))

    def update(self):
        delta_t = SIMULATED_TIME_STEP
        try:
            r = min(SIMULATED_TIME_STEP* self.v, np.linalg.norm(np.array([self.xCoord - self.destination.pos[0],
                                                        self.yCoord - self.destination.pos[1]])))
        except:
            print(self.destination)
    
        if self.state == PlaneState.IN_FLIGHT:
            self.xCoord += SIMULATED_TIME_STEP* self.v* math.cos(self.heading)
            self.yCoord += SIMULATED_TIME_STEP* self.v* math.sin(self.heading)
        try:
            if np.linalg.norm(np.array([self.xCoord - self.destination.pos[0],
                                    self.yCoord - self.destination.pos[1]])) < LANDING_DISTANCE:
                state = PlaneState.LANDED
        except:
            print(self.destination)

        return PlaneState

    def emergency(self):
        if self.state.IN_FLIGHT & self.delayedArrival > self.expectedArrival + 2:
            self.emergency = True

    def delay_check(self):
        if self.state.IN_FLIGHT:
            pass
            # Math to check delay time

    def change_destination(self, airport: Airport):
        self.heading = math.atan2((self.yCoord - airport.pos[1]), (self.xCoord - airport.pos[0]))
        self.destination = airport
        self.state = PlaneState.IN_FLIGHT
        self.v = 2


    def draw(self, surface): 
        if EUROPE:
            surface.blit(self.image, to_pygame((self.xCoord, self.yCoord), HEIGHT, 10))

        else:

            surface.blit(self.image, to_pygame((self.xCoord, self.yCoord), HEIGHT, 10))



