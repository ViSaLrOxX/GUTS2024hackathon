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
import random

class Plane:
    accum_delay = 0
    crashes = 0
    def __init__(self,
                 game, 
                 destination: Airport = None, 
                 size: Airport = None, 
                 departure: Airport = None, 
                 expectedArrival: Time = Time(0,2), 
                 delayedArrival: Time = Time(1, 3), 
                 xCoord: float = 0, yCoord: float = 0, heading: float = 0, v: float = 100, 
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
        self.image = pygame.transform.scale(self.image, (20,20))
        self.image = pygame.transform.rotate(self.image, math.degrees(self.heading) - 90)
        self.delay = 0
        self.was_redirected = False
        # self.time_expected = self.time_to_reach()
         # self.delayedArrival = (self.time_expected + 1200*60)* SIMULATED_TIME_STEP
        self.time_up = 0
  
    def time_to_reach(self):
        try:
            distance = math.sqrt((self.xCoord-self.destination.pos[0])**2+ (self.yCoord-self.destination.pos[1])**2)
            time_taken = distance/self.v
            return time_taken *100000
        except:
            for i in range(len(self.game.planes)):
                if self.game.planes[i] == self:
                    Plane.crashes +=1
                    del self.game.planes[i]
                    del self

    def update(self, i):


        delta_t = SIMULATED_TIME_STEP
        try:
            r = min(SIMULATED_TIME_STEP* self.v, np.linalg.norm(np.array([self.xCoord - self.destination.pos[0],
                                                        self.yCoord - self.destination.pos[1]])))
        except:
            del self
    
        # self.xCoord += SIMULATED_TIME_STEP* self.v* math.cos(self.heading)
        # self.yCoord += SIMULATED_TIME_STEP* self.v* math.sin(self.heading)

        rock_hard = pygame.math.Vector2(self.xCoord, self.yCoord)
        rock_hard.move_towards_ip(self.game.rock_solid_locations[self.destination.code], self.v)
        self.xCoord = rock_hard.x
        self.yCoord = rock_hard.y
            
        
        if np.linalg.norm(np.array([self.xCoord - self.game.rock_solid_locations[self.destination.code].x,
                                self.yCoord - self.game.rock_solid_locations[self.destination.code].y])) < LANDING_DISTANCE:
            state = PlaneState.LANDED
            # if self.time_up - self.time_expected:
            #     Plane.accum_delay += (self.time_up - self.time_expected)

            self.game.planes[i] = None
            del self
            print("bruh")
        

        return PlaneState

    def emergency(self,i):
        if self.state.IN_FLIGHT & self.delayedArrival > self.expectedArrival + 2:
            self.emergency = True
            self.state = PlaneState.EMERGENCY
            temp = random.randint(0, 100)
            if temp>=40:
                Plane.crashes +=1
            del self

    def delay_check(self):
        if self.state.IN_FLIGHT:
            pass
            # Math to check delay time

    def change_destination(self, airport: Airport, state: PlaneState):
        if airport.code== "SOS":
            Plane.crashes +=1 
            del self
        if state == PlaneState.EMERGENCY and (len(airport.arrivals)> airport.max_capacity or airport.state == AirportState.EMERGENCY):
            self.game.redirect(self,airport)
        else:
            self.heading = math.atan2((self.yCoord - airport.pos[1]), (self.xCoord - airport.pos[0])) + math.pi/2
            self.destination = airport
            airport.arrivals.append(self)
            self.state = PlaneState.IN_FLIGHT
            self.v = 2


    def draw(self, surface):
        rot_image = pygame.transform.rotate(self.image, math.degrees(self.heading)+45)
        surface.blit(rot_image, to_pygame((self.xCoord, self.yCoord), HEIGHT, 10))



