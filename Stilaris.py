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
    def __init__(self, radius, pos, color, player, selected):
        self.radius = radius
        self.pos = list(pos)
        self.color = color
        self.player = player
        self.selected = selected


    def img(self):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def move(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy


class keypress:
    def __init__(self, pressed):
        self.pressed = pressed





players = []
def make_players(amount, color, radius, player):
    playertemp = []
    for i in range(amount):
        playertemp.append(Ball(radius, (random.randint(radius, WIDTH - radius), random.randint(radius, HEIGHT - radius)), color, player, False))
    players.append(playertemp)


make_players(10, (255, 255, 255), 15, "p1")
make_players(20, (255, 0, 255), 15, "p2")

#bal1 = Ball(15, (100, 100), (0, 255, 0), "p1", False)
#bal2 = Ball(20, (200, 100), (255, 0, 0), "p2", False)


sup1 = 0
sup2 = 0



running = True # En boolean-variabel for at holde spillet kørende
while running: # Hovedspil-loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    start_screen()


    #keyboard detection
    keys = pygame.key.get_pressed()
    

    

    #player 1
    if keys[pygame.K_q]:
        players[0][sup1].selected = False   #sets the current to not selected
        sup1 -= 1                           #decrements by 1
        if sup1 < 1:                        #Checks whether sup1 overflows and resets if so
            sup1 = 0
        players[0][sup1].selected = True    #Sets the new unit to selected



    if keys[pygame.K_e]:
        players[0][sup1].selected = False   #sets the current to not selected
        sup1 += 1                           #increments by 1
        if sup1 > len(players[0]):          #Checks whether sup1 overflows and resets if so
            sup1 = 0
        players[0][sup1].selected = True    #Sets the new unit to selected















    #Renders the balls
    for p in players:
        for unit in p:
            unit.img()

    # Opdater skærmen
    pygame.display.flip() # Hver gang man flytter cirklen, opdateres skærmen så den viser den nye position


    # Begræns FPS
    pygame.time.Clock().tick(60)


# Afslut Pygame
pygame.quit()
sys.exit()


