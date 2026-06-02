import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load('graphics/backgroung.png').convert()
ground_surface = pygame.image.load('graphics/road.png').convert()

score_surface = text_font.render('My Game', False, 'Green')
score_rect = score_surface.get_rect(center = (400, 50))

gost_surface = pygame.image.load('graphics/gost.png').convert_alpha()
#gost_x_position = 734
#gost_y_position = 295
gost_rectangle = gost_surface.get_rect(topleft = (734,290))

player_surface = pygame.image.load('graphics/mario.png').convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,355))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEMOTION:
            if player_rectangle.collidepoint(event.pos) : print('mouse hover')


    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    pygame.draw.rect(screen, 'Red', score_rect)
    pygame.draw.rect(screen, 'Red', score_rect, 10)
    screen.blit(score_surface, score_rect)
    #pygame.draw.line(screen, 'red', (0,0), (800,400), width=1)
    #pygame.draw.ellipse(screen, 'Red', pygame.Rect(50,50, 100,100))

    gost_rectangle.left -= 4
    if gost_rectangle.right < 0 : gost_rectangle.left = 800

    #if player_rectangle.colliderect(gost_rectangle):
     #   print('')
    

    screen.blit(gost_surface, gost_rectangle)
    screen.blit(player_surface, player_rectangle)



    pygame.display.update()
    clock.tick(60)