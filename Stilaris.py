import time
import math
import pygame
import os
import sys
import random

pygame.init()





WIDTH, HEIGHT = 1200, 600 # Bredde og højde på pygamevinduet (screen)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stilaris")

WHITE = (255, 255, 255)



def start_screen():
    screen.fill((128,0,55))
    



class Ball:
    def __init__(self, radius, pos, color, player):
        self.radius = radius
        self.pos = list(pos)
        self.color = color
        self.player = player


    def img(self):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def move(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy



players = []
def make_players(amount, color, radius, player):
    for i in range(amount):
        players.append(Ball(radius, (random.randint(radius, WIDTH - radius), random.randint(radius, HEIGHT - radius)), color, player))


make_players(10, (255, 255, 255), 15, "p1")
make_players(20, (255, 0, 255), 15, "p2")

bal1 = Ball(15, (100, 100), (0, 255, 0), "p1")
bal2 = Ball(20, (200, 100), (255, 0, 0), "p2")







running = True # En boolean-variabel for at holde spillet kørende
while running: # Hovedspil-loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    start_screen()


    #keyboard detection
    keys = pygame.key.get_pressed()
    pygame.















    #Renders the balls
    for i in players:
        i.img()

    # Opdater skærmen
    pygame.display.flip() # Hver gang man flytter cirklen, opdateres skærmen så den viser den nye position


    # Begræns FPS
    pygame.time.Clock().tick(60)


# Afslut Pygame
pygame.quit()
sys.exit()


