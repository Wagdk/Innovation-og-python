import pygame
import sys

# Initialiser Pygame
pygame.init()

# vinduesstørrelse
WIDTH, HEIGHT = 1200, 600 # Bredde og højde på pygamevinduet (screen)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simpelt Pygame Program")

# Farver
WHITE = (255, 255, 255) # Hvid baggrund
BLUE = (0, 0, 255) # Blå cirkel


# Startposition for cirklen
x, y = WIDTH // 2, HEIGHT // 2
radius = 20 # 30 pixels radius
speed = 2 # 5 pixels per frame
vx = 2
vy = 2


# Spil-loop
running = True # En boolean-variabel for at holde spillet kørende
while running: # Hovedspil-loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    pygame.draw.rect(screen, (255,0,255), 10, 10)

    # Tjek tastetryk på piletasterne
    keys = pygame.key.get_pressed()
    #if keys[pygame.K_LEFT]: # Flyt cirklen til venstre med venstre piletast

    if y >= HEIGHT - radius:
        vy *= -1
    
    if y <= 100 + radius:
        vy *= -1

    if x >= WIDTH - radius:
        vx *= -1

    if x <= 0 + radius:
        vx *= -1



    x += vx
    y += vy




    # Tegn baggrund og cirkel
    screen.fill(WHITE) # henter info om baggrundsfarven fra variablen WHITE
    pygame.draw.circle(screen, BLUE, (x, y), radius) # Henter info om cirkelfarven fra variablen BLUE
    # og om positionen og radiusen fra variablerne x, y og radius


    # Opdater skærmen
    pygame.display.flip() # Hver gang man flytter cirklen, opdateres skærmen så den viser den nye position


    # Begræns FPS
    pygame.time.Clock().tick(60)


# Afslut Pygame
pygame.quit()
sys.exit()


