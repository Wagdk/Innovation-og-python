import time
import math
import pygame
import os
import sys
import random
from os.path import join
import myclass 


pygame.init()



#varibles for screen size and factors
screenx = 1280
screeny = 720
xfactor = 1
yfactor = 1


 
window_width, window_height = screenx, screeny
move_speed = 0.5
WIDTH, HEIGHT = 1200, 600 # Bredde og højde på pygamevinduet (screen)
screen = pygame.display.set_mode((window_width, window_height))
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
 
 
 
 
make_units(1, BLUE, 15, p1.index, 10, 10, 100, 600)
make_units(1, GREEN, 15, p2.index, 600, 10, 690, 600)
make_units(1, RED, 15, p3.index, 1000, 10, 1100, 600)
 
 
cursers = [
    mouse(100, 100, 0, (255, 255, 255), False, False, True, [False, False, False, False]), 
    mouse(200, 100, 1, (200, 100, 255), False, False, True, [False, False, False, False]),
    mouse(300, 100, 2, ORANGE, False, False, True, [False, False, False, False])
        ]
 
 













current_screen = "menu"
runningmenu = True
while runningmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runningmenu = False
                runninggame = False
    
        #menu screen
        if current_screen == 'menu':
    
            #menu screen surfaces decorations
            surfwall = pygame.surface.Surface((10 * xfactor, 720 * yfactor))
            surfwall.fill('black')
            surffloor = pygame.surface.Surface((1280 * xfactor, 10 * yfactor))
            surffloor.fill('black')
            surfstart = pygame.surface.Surface((700 * xfactor, 400 * yfactor))
            surfstart.fill('green')

            #images
            startimage = pygame.image.load(join('menu ui', 'images', 'start.png')).convert_alpha()
            quitimage = pygame.image.load(join('menu ui', 'images', 'quit.png')).convert_alpha()
            settingsimage = pygame.image.load(join('menu ui', 'images', 'settings.png')).convert_alpha()

            #button instances
            start_button = myclass.Buttono(480 * xfactor, 75 * yfactor, startimage, 0.5 * xfactor) 
            quit_button = myclass.Buttono(480 * xfactor, 275 * yfactor, quitimage, 0.245 * xfactor)
            settings_button = myclass.Buttono(520 * xfactor, 475 * yfactor, settingsimage, 0.7 * xfactor)

            #draw screen
            screen.fill('darkgreen')
            screen.blit(surfwall, (0 * xfactor, 0 * yfactor))
            screen.blit(surfwall, (1270 * xfactor, 0 * yfactor))
            screen.blit(surffloor, (0 * xfactor, 0 * yfactor))
            screen.blit(surffloor, (0 * xfactor, 710 * yfactor))
            screen.blit(surfstart, (290 * xfactor, 160 * yfactor))
    
            #button actions
            if start_button.draw(surface=screen):
                runninggame = True
                runningmenu = False
            if quit_button.draw(surface=screen):
                running = False
            if settings_button.draw(surface=screen):
                current_screen = 'settings'
            #looping around
            pygame.display.update()
            pass

        #settings screen
        elif current_screen == 'settings':
       
            #images
            image640x480 = pygame.image.load(join('menu ui', 'images', '640x480.png')).convert_alpha()
            image1280x720 = pygame.image.load(join('menu ui', 'images', '1280x720.png')).convert_alpha()
            image1920x1080 = pygame.image.load(join('menu ui', 'images', '1920x1080.png')).convert_alpha()
            image2560x1440 = pygame.image.load(join('menu ui', 'images', '2560x1440.png')).convert_alpha()
            image3840x2160 = pygame.image.load(join('menu ui', 'images', '3840x2160.png')).convert_alpha()
            image5120x2880 = pygame.image.load(join('menu ui', 'images', '5120x2880.png')).convert_alpha()
            image7680x4320 = pygame.image.load(join('menu ui', 'images', '7680x4320.png')).convert_alpha()
            imagemenu = pygame.image.load(join('menu ui', 'images', 'menu.png')).convert_alpha()
            
            #button instances
            butono_640x480 = myclass.Buttono(50 * xfactor, 150 * yfactor, image640x480, 1 * yfactor)
            buttono_1280x720 = myclass.Buttono(50 * xfactor, 210 * yfactor, image1280x720, 1 * yfactor)
            buttono_1920x1080 = myclass.Buttono(50 * xfactor, 270 * yfactor, image1920x1080, 1 * yfactor)
            buttono_2560x1440 = myclass.Buttono(50 * xfactor, 330 * yfactor, image2560x1440, 1 * yfactor)
            buttono_3840x2160 = myclass.Buttono(50 * xfactor, 390 * yfactor, image3840x2160, 1 * yfactor)
            buttono_5120x2880 = myclass.Buttono(50 * xfactor, 450 * yfactor, image5120x2880, 1 * yfactor)
            buttono_7680x4320 = myclass.Buttono(50 * xfactor, 510 * yfactor, image7680x4320, 1 * yfactor)
            buttono_menu = myclass.Buttono(800 * xfactor, 240 * yfactor, imagemenu, 1 * yfactor)
            
            #draw screen
            screen.fill('darkgreen')

            #button actions
            if butono_640x480.draw(surface=screen):
                screenx = 640
                screeny = 480
                xfactor = 0.5
                yfactor = 0.6666666666666666
                screen = pygame.display.set_mode((screenx, screeny,))
            if buttono_1280x720.draw(surface=screen):
                screenx = 1280
                screeny = 720
                xfactor = 1
                yfactor = 1
                screen = pygame.display.set_mode((screenx, screeny,))
            if buttono_1920x1080.draw(surface=screen):
              screenx = 1920
              screeny = 1080
              xfactor = 1.5
              yfactor = 1.5
              screen = pygame.display.set_mode((screenx, screeny,))
            if buttono_2560x1440.draw(surface=screen):
              screenx = 2560
              screeny = 1440
              xfactor = 2
              yfactor = 2
              screen = pygame.display.set_mode((screenx, screeny,))
            if buttono_3840x2160.draw(surface=screen):
                screenx = 3840
                screeny = 2160
                xfactor = 3
                yfactor = 3
                screen = pygame.display.set_mode((screenx, screeny,))
            if buttono_5120x2880.draw(surface=screen):
                screenx = 5120
                screeny = 2880
                xfactor = 4
                yfactor = 4
                screen = pygame.display.set_mode((screenx, screeny,))
            if buttono_7680x4320.draw(surface=screen):
                screenx = 7680
                screeny = 4320
                xfactor = 6
                yfactor = 6
                screen = pygame.display.set_mode((screenx, screeny,))
            if buttono_menu.draw(surface=screen):
                current_screen = 'menu'
            
            #looping around
            pygame.display.update()
            pass







runninggame = True # En boolean-variabel for at holde spillet kørende
while runninggame: # Hovedspil-loop
    start_screen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runningmenu = False
            runninggame = False
    

 
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

    
    if not units[0] and not units[2]:
        runningmenu = True
        runninggame = False
    
    if not units[1] and not units[2]:
        runningmenu = True
        runninggame = False
    
    if  not units[0] and not units[1]:
        runningmenu = True
        runninggame = False
 
 
 
    # Opdater skærmen
    pygame.display.flip() # Hver gang man flytter cirklen, opdateres skærmen så den viser den nye position
 
 
    # Begræns FPS
    pygame.time.Clock().tick(60)
 


if not runningmenu and not runninggame:
    pygame.quit()
    sys.exit()