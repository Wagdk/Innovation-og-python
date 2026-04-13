import time
import math
import pygame
import os
import sys



pygame.init()

WIDTH, HEIGHT = 1200, 600 # Bredde og højde på pygamevinduet (screen)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stilaris")

WHITE = (255, 255, 255)


running = True # En boolean-variabel for at holde spillet kørende
while running: # Hovedspil-loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tegn baggrund og cirkel
    screen.fill(WHITE) # henter info om baggrundsfarven fra variablen WHITE
    pygame.draw.circle(screen, (255,0,0) , (50, 50), 25)


    # Opdater skærmen
    pygame.display.flip() # Hver gang man flytter cirklen, opdateres skærmen så den viser den nye position


    # Begræns FPS
    pygame.time.Clock().tick(60)


# Afslut Pygame
pygame.quit()
sys.exit()


