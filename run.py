from Game import Game
import pygame
from Plane import Plane


pygame.init()
screen = pygame.display.set_mode((300, 300))
clock = pygame.time.Clock()

running = True

plane = Plane()

while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False


    screen.fill((255,255,255)) # fill the screen with white
    plane.draw(screen) # draw the bird to the screen
    pygame.display.update() # update the screen

    clock.tick(40)