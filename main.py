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

Game_over_surface = text_font.render('GAME OVER', False, 'Green')
Game_over_rect = Game_over_surface.get_rect(center = (400, 200))

gost_surface = pygame.image.load('graphics/gost.png').convert_alpha()
#gost_x_position = 734
#gost_y_position = 295
gost_rectangle = gost_surface.get_rect(topleft = (734,290))

player_character = 'graphics/player/mario_1.png'
player_gravity = 0
player_surface = pygame.image.load(player_character).convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,355))

game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and player_rectangle.bottom >= 355:
                    player_gravity = -20
                    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and player_rectangle.bottom >= 355:
                    player_gravity = -20

        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                    game_active = True
                    gost_rectangle.left = 800         
            if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                    game_active = True
                    gost_rectangle.left = 800

                

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        pygame.draw.rect(screen, 'Red', score_rect)
        pygame.draw.rect(screen, 'Red', score_rect, 10)
        screen.blit(score_surface, score_rect)
        #pygame.draw.line(screen, 'red', (0,0), (800,400), width=1)
        #pygame.draw.ellipse(screen, 'Red', pygame.Rect(50,50, 100,100))

        gost_rectangle.left -= 5
        if gost_rectangle.right < 0 : gost_rectangle.left = 800

        #if player_rectangle.colliderect(gost_rectangle):
        #   print('')
        
        screen.blit(gost_surface, gost_rectangle)

        #PLAYER
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 355 : player_rectangle.bottom = 355
        screen.blit(player_surface, player_rectangle)
        
        #COLLISION
        if gost_rectangle.colliderect(player_rectangle):
            game_active = False
    else:
        screen.blit(sky_surface, (0,0))
        pygame.draw.rect(screen, 'Red', Game_over_rect)
        pygame.draw.rect(screen, 'Red', Game_over_rect, 10)
        screen.blit(Game_over_surface, Game_over_rect)


    




    pygame.display.update()
    clock.tick(60)