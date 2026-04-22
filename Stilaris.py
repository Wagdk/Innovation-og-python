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


class mouse:
    def __init__(self, posx, posy, player, color, selecting, unit_move, rendered, points):
        self.posx = posx
        self.posy = posy
        self.player = player
        self.color = color
        self.selecting = selecting
        self.unit_move = unit_move
        self.rendered = rendered
        self.points = points
    
    def move(self, dx, dy):
        self.posx += dx
        self.posy += dy





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

def select(player, basecolor, light_color):
    global units
    for i in units[player]:
        if min(cursers[player].points[0], cursers[player].points[2]) < i.pos[0] and max(cursers[player].points[0], cursers[player].points[2]) > i.pos[0] and min(cursers[player].points[1], cursers[player].points[3]) < i.pos[1] and max(cursers[player].points[1], cursers[player].points[3]) > i.pos[1]:
            i.color = light_color
            i.selected = True


        else:    
            i.color = basecolor
            i.selected = False








p1 = Player(0, "alive", 0)
p2 = Player(1, "alive", 0)


make_units(10, BLUE, 15, p1.index, 10, 10, 100, 600)
make_units(20, GREEN, 15, p2.index, 600, 10, 690, 600)

#bal1 = Ball(15, (100, 100), (0, 255, 0), "p1", False)
#bal2 = Ball(20, (200, 100), (255, 0, 0), "p2", False)

cursers = [
    mouse(100, 100, 0, (255, 255, 255), False, False, True, [False, False, False, False]), 
    mouse(200, 100, 1, (200, 100, 255), False, False, True, [False, False, False, False])
        ]



running = True # En boolean-variabel for at holde spillet kørende
while running: # Hovedspil-loop
    start_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    


        #keyboard single-press detection
        if event.type == pygame.KEYDOWN:

            #Player 1
            if event.key == pygame.K_q:
                cursers[p1.index].selecting = True
                cursers[p1.index].points[0] = cursers[p1.index].posx
                cursers[p1.index].points[1] = cursers[p1.index].posy
                print(cursers[p1.index].points[0],cursers[p1.index].points[1])

            
            #Player 2
            if event.key == pygame.K_y:
                pass

    
        if event.type == pygame.KEYUP:
            
            #Player 1
            if event.key == pygame.K_q:
                cursers[p1.index].selecting = False
                cursers[p1.index].points[2] = cursers[p1.index].posx
                cursers[p1.index].points[3] = cursers[p1.index].posy
                print(cursers[p1.index].points[2],cursers[p1.index].points[3])
                select(0, BLUE, LIGHT_BLUE)
            

            #Player 2
            if event.key == pygame.K_y:
                pass





    #keyboard hold detection
    keys = pygame.key.get_pressed()
    

    

    #player 1
    if keys[pygame.K_w]:
        cursers[p1.index].move(0, -2)

    if keys[pygame.K_s]:
        cursers[p1.index].move(0, 2)
    
    if keys[pygame.K_a]:
        cursers[p1.index].move(-2, 0)
    
    if keys[pygame.K_d]:
        cursers[p1.index].move(2, 0)
    


    if keys[pygame.K_e]:
        pass



    #player 2
    if keys[pygame.K_u]:
        cursers[p2.index].move(0, -2)

    if keys[pygame.K_j]:
        cursers[p2.index].move(0, 2)
    
    if keys[pygame.K_h]:
        cursers[p2.index].move(-2, 0)
    
    if keys[pygame.K_k]:
        cursers[p2.index].move(2, 0)

















    #Rendering
    for p in units:
        for unit in p:
            unit.img()

    for i in cursers:
        pygame.draw.circle(screen, i.color , (i.posx, i.posy), 5)


    # Opdater skærmen
    pygame.display.flip() # Hver gang man flytter cirklen, opdateres skærmen så den viser den nye position


    # Begræns FPS
    pygame.time.Clock().tick(60)


# Afslut Pygame
pygame.quit()
sys.exit()


