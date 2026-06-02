import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('graphics/backgroung.png').convert()
ground_surface = pygame.image.load('graphics/road.png').convert()
text_surface = text_font.render('My Game', False, 'Green')

gost_surface = pygame.image.load('graphics/gost.png').convert_alpha()
#gost_x_position = 734
#gost_y_position = 295
gost_rectangle = gost_surface.get_rect(topleft = (734,295))

player_surface = pygame.image.load('graphics/mario.png').convert_alpha()
player_rectangle = player_surface.get_rect(topleft = (80,290))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (345,50))
    if gost_rectangle.left < -68:
        gost_rectangle.left = 800
    else:
        gost_rectangle.left -=3

    screen.blit(gost_surface, gost_rectangle)
    screen.blit(player_surface, player_rectangle)



    pygame.display.update()
    clock.tick(60)