import math
from Continents import Continent

FPS = 60
REAL_TIME_STEP = 1/FPS
SIMULATED_TIME_STEP = 100/FPS
AIRPORT_CAPACITY_MODIFIER = 5
LANDING_DISTANCE = 500
NUM_AIRPORTS = 100
NUM_PLANES = 320
EUROPE = False 
MOVEMENT = False
WIDTH = 1200
HEIGHT = 1200
MAX_TRIES = 20
CONTINENT_RELATIONSHIPS = {Continent.EU: {Continent.EU: 17,
                                          Continent.AF:2.8,
                                          Continent.PO:0.5,
                                          Continent.MEA:4.3,
                                          Continent.NA:2.0,
                                          Continent.SA:0.3},
                            Continent.AF: {Continent.EU: 2.8,
                                          Continent.AF:3.7,
                                          Continent.PO:0.0,
                                          Continent.MEA:1.9,
                                          Continent.NA:0.0,
                                          Continent.SA:0.0},
                            Continent.PO: {Continent.EU: 0.5,
                                          Continent.AF:0.0,
                                          Continent.PO:11.8,
                                          Continent.MEA:5.7,
                                          Continent.NA:1.1,
                                          Continent.SA:0.0},
                            Continent.MEA: {Continent.EU: 4.3,
                                          Continent.AF:1.9,
                                          Continent.PO:5.7,
                                          Continent.MEA:16.7,
                                          Continent.NA:0.6,
                                          Continent.SA:0.0},
                            Continent.SA: {Continent.EU: 0.3,
                                          Continent.AF:0.0,
                                          Continent.PO:0.0,
                                          Continent.MEA:0.0,
                                          Continent.NA:1.4,
                                          Continent.SA:7.3},
                            Continent.NA: {Continent.EU: 2.0,
                                          Continent.AF:0.0,
                                          Continent.PO:1.1,
                                          Continent.MEA:0.6,
                                          Continent.NA:23.2,
                                          Continent.SA:1.4}}
MODIFIED_CONTINENT_RELATIONSHIPS = CONTINENT_RELATIONSHIPS


