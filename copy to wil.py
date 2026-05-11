#import pygame and joins
import pygame
from os.path import join
import myclass

#varibles for screen size and factors
screenx = 1280
screeny = 720
xfactor = 1
yfactor = 1

#screen size and caption
pygame.init()
window_width, window_height = screenx, screeny
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('control c control v')
running = True

#variable for current screen
current_screen = 'menu'

#loop and event handling
running = True
while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    
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
                print('Start button clicked')
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
        
        