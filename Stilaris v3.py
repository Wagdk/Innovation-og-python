import time
import math
import pygame
import os
import sys
import random
 
pygame.init()
 
 
 
 
move_speed = 0.5
WIDTH, HEIGHT = 1200, 600 # Bredde og højde på pygamevinduet (screen)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stilaris")
 
WHITE = (255, 255, 255)
 
BLUE = (0, 0, 128)
LIGHT_BLUE = (0, 0, 255)
 
GREEN = (0, 128, 0)
LIGHT_GREEN = (0, 255, 0)
 
RED = (128, 0, 0)
LIGHT_RED = (255, 0, 0)
ORANGE = (255, 165, 0)
 
 
 
def start_screen():
    screen.fill((0,0,0))
 
 
class Player:
    def __init__(self, index, status, selunit, repositioning):
        self.index = index
        self.status = status
        self.selunit = selunit
        self.repositioning = repositioning
 
 
class Ball:
    def __init__(self, radius, pos, color, player, selected, gotopos, health, rendered):
        self.radius = radius
        self.pos = list(pos)
        self.color = color
        self.player = player
        self.selected = selected
        self.gotopos = list(gotopos)
        self.health = health
        self.rendered = rendered
 
 
    def img(self):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)
 
    def move(self, dx, dy):
        self.pos[0] += dx
        self.pos[1] += dy
 
    def collision(self):
        for group in units:
            # FIX 1: Spring tomme grupper over (undgår IndexError på group[0])
            if not group:
                continue
            if group[0].player != self.player:
                for unit in group:
                    # FIX 2: Brug rigtig cirkel-kollision med afstand i stedet
                    # for den umulige box-check
                    dx = unit.pos[0] - self.pos[0]
                    dy = unit.pos[1] - self.pos[1]
                    distance = math.sqrt(dx**2 + dy**2)
                    if distance < self.radius + unit.radius:
                        return True
        # FIX 2 fortsat: Return False EFTER alle grupper er tjekket,
        # ikke inde i inner-loopet
        return False
    
 
 
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
        unittemp.append(Ball(radius, (random.randint(radius + min(x1,x2), max(x1,x2) - radius), random.randint(radius + min(y1,y2), max(y1,y2) - radius)), color, player, False, (False, False), 100, True))
    units.append(unittemp)
    for p in units:
        for unit in p:
            unit.gotopos[0] = unit.pos[0]
            unit.gotopos[1] = unit.pos[1]
 
def select(player, basecolor, light_color):
    global units
    for i in units[player]:
        if min(cursers[player].points[0], cursers[player].points[2]) < i.pos[0] and max(cursers[player].points[0], cursers[player].points[2]) > i.pos[0] and min(cursers[player].points[1], cursers[player].points[3]) < i.pos[1] and max(cursers[player].points[1], cursers[player].points[3]) > i.pos[1]:
            i.color = light_color
            i.selected = True
 
 
        else:    
            i.color = basecolor
            i.selected = False
 
def globalmove():
    global move_speed
    for p in units:
        for unit in p:
            if not unit.collision():
                if (unit.pos[1] - unit.gotopos[1]) != -(unit.pos[0] - unit.gotopos[0]) and (unit.pos[0] - unit.gotopos[0]) != 0 and (unit.pos[1] - unit.gotopos[1]) != 0 and not unit.selected and not(unit.gotopos[0] < unit.pos[0] + 5 and unit.gotopos[0] > unit.pos[0] - 5 and unit.gotopos[1] < unit.pos[1] + 5 and unit.gotopos[1] > unit.pos[1] - 5):
                    unit.move(-(abs((unit.pos[0] - unit.gotopos[0]))/(unit.pos[0] - unit.gotopos[0])) * min(abs(move_speed / (1 + (unit.pos[1] - unit.gotopos[1]) / (unit.pos[0] - unit.gotopos[0]))), move_speed/2), (-abs((unit.pos[1] - unit.gotopos[1]))/(unit.pos[1] - unit.gotopos[1])) * min(abs((move_speed / (1 + (unit.pos[0] - unit.gotopos[0]) / (unit.pos[1] - unit.gotopos[1])))), move_speed/2))
                elif not(unit.gotopos[0] < unit.pos[0] + 5 and unit.gotopos[0] > unit.pos[0] - 5 and unit.gotopos[1] < unit.pos[1] + 5 and unit.gotopos[1] > unit.pos[1] - 5) and not unit.selected:
                    unit.move(2,1)
        
 
 
 
 
 
 
 
 
p1 = Player(0, "alive", 0, False)
p2 = Player(1, "alive", 0, False)
p3 = Player(2, "alive", 0, False)
 
 
make_units(10, BLUE, 15, p1.index, 10, 10, 100, 600)
make_units(20, GREEN, 15, p2.index, 600, 10, 690, 600)
make_units(15, RED, 15, p3.index, 1000, 10, 1100, 600)
 
 
cursers = [
    mouse(100, 100, 0, (255, 255, 255), False, False, True, [False, False, False, False]), 
    mouse(200, 100, 1, (200, 100, 255), False, False, True, [False, False, False, False]),
    mouse(300, 100, 2, ORANGE, False, False, True, [False, False, False, False])
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
                if not p1.repositioning:
                    cursers[p1.index].selecting = True
                    cursers[p1.index].points[0] = cursers[p1.index].posx
                    cursers[p1.index].points[1] = cursers[p1.index].posy
                
            if event.key == pygame.K_e:
                p1.repositioning = not p1.repositioning
 
 
 
            #Player 2
            if event.key == pygame.K_y:
                if not p2.repositioning:
                    cursers[p2.index].selecting = True
                    cursers[p2.index].points[0] = cursers[p2.index].posx
                    cursers[p2.index].points[1] = cursers[p2.index].posy
            
            if event.key == pygame.K_i:
                p2.repositioning = not p2.repositioning
            
 
 
            #Player 3
            if event.key == pygame.K_KP_7:
                if not p3.repositioning:
                    cursers[p3.index].selecting = True
                    cursers[p3.index].points[0] = cursers[p3.index].posx
                    cursers[p3.index].points[1] = cursers[p3.index].posy
            
            if event.key == pygame.K_KP_9:
                p3.repositioning = not p3.repositioning
 
 
    
        if event.type == pygame.KEYUP:
            
            #Player 1
            if event.key == pygame.K_q:
                cursers[p1.index].selecting = False
                cursers[p1.index].points[2] = cursers[p1.index].posx
                cursers[p1.index].points[3] = cursers[p1.index].posy
                select(0, BLUE, LIGHT_BLUE)
            
 
            #Player 2
            if event.key == pygame.K_y:
                cursers[p2.index].selecting = False
                cursers[p2.index].points[2] = cursers[p2.index].posx
                cursers[p2.index].points[3] = cursers[p2.index].posy
                select(1, GREEN, LIGHT_GREEN)
            
 
            #Player 3
            if event.key == pygame.K_KP_7:
                cursers[p3.index].selecting = False
                cursers[p3.index].points[2] = cursers[p3.index].posx
                cursers[p3.index].points[3] = cursers[p3.index].posy
                select(2, RED, LIGHT_RED)
 
 
 
 
 
    #keyboard hold detection
    keys = pygame.key.get_pressed()
    
 
    #player 1
    if keys[pygame.K_w]:
        if not p1.repositioning:
            cursers[p1.index].move(0, -2)
 
        if p1.repositioning:
            for i in units[p1.index]:
                if i.selected:
                    i.gotopos[1] += -2
    
    
    if keys[pygame.K_s]:
        if not p1.repositioning:
            cursers[p1.index].move(0, 2)
    
        if p1.repositioning:
            for i in units[p1.index]:
                if i.selected:
                    i.gotopos[1] += 2
 
 
    
    if keys[pygame.K_a]:
        if not p1.repositioning:
            cursers[p1.index].move(-2, 0)
    
        if p1.repositioning:
            for i in units[p1.index]:
                if i.selected:
                    i.gotopos[0] += -2
 
    
    
    if keys[pygame.K_d]:
        if not p1.repositioning:
            cursers[p1.index].move(2, 0)
    
        if p1.repositioning:
            for i in units[p1.index]:
                if i.selected:
                    i.gotopos[0] += 2  
 
 
 
    #player 2
    if keys[pygame.K_u]:
        if not p2.repositioning:
            cursers[p2.index].move(0, -2)
 
        if p2.repositioning:
            for i in units[p2.index]:
                if i.selected:
                    i.gotopos[1] += -2
 
 
 
    if keys[pygame.K_j]:
        if not p2.repositioning:
            cursers[p2.index].move(0, 2)
 
        if p2.repositioning:
            for i in units[p2.index]:
                if i.selected:
                    i.gotopos[1] += 2
 
 
 
    if keys[pygame.K_h]:
        if not p2.repositioning:
            cursers[p2.index].move(-2, 0)
 
        if p2.repositioning:
            for i in units[p2.index]:
                if i.selected:
                    i.gotopos[0] += -2
 
 
 
    if keys[pygame.K_k]:
        if not p2.repositioning:
            cursers[p2.index].move(2, 0)
 
        if p2.repositioning:
            for i in units[p2.index]:
                if i.selected:
                    i.gotopos[0] += 2  
 
 
 
    #player 3
    if keys[pygame.K_KP_8]:
        if not p3.repositioning:
            cursers[p3.index].move(0, -2)
 
        if p3.repositioning:
            for i in units[p3.index]:
                if i.selected:
                    i.gotopos[1] += -2
 
 
 
    if keys[pygame.K_KP_5]:
        if not p3.repositioning:
            cursers[p3.index].move(0, 2)
 
        if p3.repositioning:
            for i in units[p3.index]:
                if i.selected:
                    i.gotopos[1] += 2
 
 
 
    if keys[pygame.K_KP_4]:
        if not p3.repositioning:
            cursers[p3.index].move(-2, 0)
 
        if p3.repositioning:
            for i in units[p3.index]:
                if i.selected:
                    i.gotopos[0] += -2
 
 
 
    if keys[pygame.K_KP_6]:
        if not p3.repositioning:
            cursers[p3.index].move(2, 0)
 
        if p3.repositioning:
            for i in units[p3.index]:
                if i.selected:
                    i.gotopos[0] += 2  
 
 
    
    globalmove()
 
    # Rendering
    for p in units:
        # FIX 3a: Iterer over en kopi (p[:]) så vi kan fjerne fra originalen
        # uden at ødelægge loopet
        for unit in p[:]:
            if unit.collision():
                if random.randint(0, 20) == 0:
                    unit.health -= 1
            
            # FIX 3b: Var >= 0 (fjernede LEVENDE units!) — skal være <= 0
            if unit.health <= 0:
                p.remove(unit)
                continue
            
            unit.img()
            if not(unit.gotopos[0] < unit.pos[0] + 5 and unit.gotopos[0] > unit.pos[0] - 5 and unit.gotopos[1] < unit.pos[1] + 5 and unit.gotopos[1] > unit.pos[1] - 5):
                pygame.draw.line(screen,(100,100,100),unit.pos, unit.gotopos, 3)
 
    for i in cursers:
        pygame.draw.circle(screen, i.color , (i.posx, i.posy), 5)
 
 
 
 
    # Opdater skærmen
    pygame.display.flip() # Hver gang man flytter cirklen, opdateres skærmen så den viser den nye position
 
 
    # Begræns FPS
    pygame.time.Clock().tick(60)
 
 
# Afslut Pygame
pygame.quit()
sys.exit()