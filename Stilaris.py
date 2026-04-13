import time
import math
import pygame
import os
import sys

pygame.init()

sqheight, sqwidth, posx, posy = 50, 100, 300, 300


def start_screen():
    screen.fill((128,0,55))
    pygame.draw.polygon(screen,(0,255,0),([sqheight+posx,sqwidth+posy],[sqheight+posx,posy],[posx,posy],[posx,sqwidth+posy]))








WIDTH, HEIGHT = 1200, 600 # Bredde og højde på pygamevinduet (screen)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stilaris")

WHITE = (255, 255, 255)


running = True # En boolean-variabel for at holde spillet kørende
while running: # Hovedspil-loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
    start_screen()








    # Opdater skærmen
    pygame.display.flip() # Hver gang man flytter cirklen, opdateres skærmen så den viser den nye position


    # Begræns FPS
    pygame.time.Clock().tick(60)


# Afslut Pygame
pygame.quit()
sys.exit()


