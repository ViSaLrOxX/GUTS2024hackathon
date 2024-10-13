import pygame
from config import HEIGHT
from utils import to_pygame

class Typhoon:
    def __init__(self, pos):
        self.pos = pos
        self.image = pygame.image.load("spiral2.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.image.fill((255,255,255,1),None, pygame.BLEND_RGB_MULT)
        self.image.set_alpha(128)
        self.image.convert_alpha()

    def draw(self, surface):
            self.image = pygame.transform.rotate(self.image, 90)
            surface.blit(self.image, to_pygame((self.pos[0], self.pos[1]), HEIGHT, 10))
