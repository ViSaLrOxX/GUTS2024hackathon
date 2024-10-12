from Game import Game
import pygame
from Plane import Plane


pygame.init()

running = True

while running:
    # handle every event since the last frame.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # quit the screen
            running = False

    bird.handle_keys() # handle the keys

    screen.fill((255,255,255)) # fill the screen with white
    bird.draw(screen) # draw the bird to the screen
    pygame.display.update() # update the screen

    clock.tick(40)