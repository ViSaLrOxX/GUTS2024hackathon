from config import SIMULATED_TIME_STEP, LANDING_DISTANCE, EUROPE, HEIGHT, WIDTH
import numpy as np
import math
from Airport import Airport
from AirportState import AirportState
from PlaneState import PlaneState
import PlaneSizes
from Time import Time
from utils import to_pygame
import pygame

class Plane:
    def __init__(self,
                 game, 
                 destination: Airport = None, 
                 size: Airport = None, 
                 departure: Airport = None, 
                 expectedArrival: Time = Time(0,2), 
                 delayedArrival: Time = Time(1, 3), 
                 xCoord: float = 0, yCoord: float = 0, heading: float = 10, v: float = 100, 
                 state: PlaneState = PlaneState.IN_FLIGHT):
        self.game = game
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
        #self.image.set_alpha(0)
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

            self.xCoord %= WIDTH
            self.yCoord %= HEIGHT
            
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

    def change_destination(self, airport: Airport, state: PlaneState):
        if state == PlaneState.EMERGENCY and (len(airport.arrivals)> airport.max_capacity or airport.state == AirportState.EMERGENCY):
            self.game.redirect(self,airport)
        else:
            self.heading = math.atan2((self.yCoord - airport.pos[1]), (self.xCoord - airport.pos[0]))
            self.destination = airport
            airport.arrivals.append(self)
            self.state = PlaneState.IN_FLIGHT
            self.v = 2


    def draw(self, surface):
        rot_image = pygame.transform.rotate(self.image, math.degrees(self.heading))
        surface.blit(rot_image, to_pygame((self.xCoord, self.yCoord), HEIGHT, 10))



