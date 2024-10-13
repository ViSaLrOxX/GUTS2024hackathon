import pygame
from config import HEIGHT
from utils import to_pygame

class Plane:
    def __init__(self, pos):
        self.pos = pos
        self.image = pygame.image.load("typhoon.jpeg")
    def draw(self, surface):
            surface.blit(self.image, to_pygame((self.pos[0], self.pos[1]), HEIGHT, 10))
