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

BLUE = (0, 0, 128)
LIGHT_BLUE = (0, 0, 255)

GREEN = (0, 128, 0)
LIGHT_GREEN = (0, 255, 0)




def start_screen():
    screen.fill((128,0,55))


class Player:
    def __init__(self, index, status, selunit):
        self.index = index
        self.status = status
        self.selunit = selunit


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





units = []
def make_units(amount, color, radius, player, x1, y1, x2, y2):
    unittemp = []
    for i in range(amount):
        unittemp.append(Ball(radius, (random.randint(radius + min(x1,x2), max(x1,x2) - radius), random.randint(radius + min(y1,y2), max(y1,y2) - radius)), color, player, False))
    units.append(unittemp)


def highlight(player, basecolor, light_color, increment):
        units[player.index][player.selunit].selected = False       #sets the current to not selected
        units[player.index][player.selunit].color = basecolor           #Returns the original color
        
        if increment == False:
            player.selunit -= 1                                    #decrements by 1
            if player.selunit < 0:                                 #Checks whether sup1 overflows and resets if so
                player.selunit = len(units[player.index]) - 1
        else:
            player.selunit += 1                                    #increments by 1
            if player.selunit > len(units[player.index]) - 1:                 #Checks whether sup1 overflows and resets if so
                player.selunit = 0

        units[player.index][player.selunit].selected = True        #Sets the new unit to selected
        units[player.index][player.selunit].color = light_color     #Returns the original color





p1 = Player(0, "alive", 0)
p2 = Player(1, "alive", 0)


make_units(10, BLUE, 15, p1.index, 10, 10, 100, 600)
make_units(20, GREEN, 15, p2.index, 600, 10, 690, 600)

#bal1 = Ball(15, (100, 100), (0, 255, 0), "p1", False)
#bal2 = Ball(20, (200, 100), (255, 0, 0), "p2", False)






running = True # En boolean-variabel for at holde spillet kørende
while running: # Hovedspil-loop
    start_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


        #keyboard single-press detection
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_q:
                highlight(p1, BLUE, LIGHT_BLUE, False)
                

            if event.key == pygame.K_e:
                highlight(p1, BLUE, LIGHT_BLUE, True)       
                
    
            if event.key == pygame.K_y:
                highlight(p2, GREEN, LIGHT_GREEN, False)
                

            if event.key == pygame.K_i:
                highlight(p2, GREEN, LIGHT_GREEN, True)    






    #keyboard hold detection
    keys = pygame.key.get_pressed()
    

    

    #player 1
    #if keys[pygame.K_q]:
















    #Renders the units
    for p in units:
        for unit in p:
            unit.img()

    # Opdater skærmen
    pygame.display.flip() # Hver gang man flytter cirklen, opdateres skærmen så den viser den nye position


    # Begræns FPS
    pygame.time.Clock().tick(60)


# Afslut Pygame
pygame.quit()
sys.exit()


