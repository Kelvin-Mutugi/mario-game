import pygame
from sys import exit


def display_score():
     current_time = int(pygame.time.get_ticks()/1000 - start_time)
     score_surf = text_font.render(f'Score: {current_time}', False, 'Green')
     score_rect = score_surf.get_rect(center = (400, 50))
     screen.blit(score_surf,score_rect)


pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)
start_instructions_font = pygame.font.Font(None, 40)

player_character = 'graphics/player/mario_1.png'

sky_surface = pygame.image.load('graphics/backgroung.png').convert()
ground_surface = pygame.image.load('graphics/road.png').convert()

start_time = 0

Game_over_surface = text_font.render(f'Score:', False, 'Green')
Game_over_rect = Game_over_surface.get_rect(midtop = (400, 50))

game_over_character = pygame.image.load(player_character).convert_alpha()
game_over_character_scaled = pygame.transform.scale_by(game_over_character, 1.5)
game_over_character_rect = game_over_character.get_rect(center = (380,190))

game_over_start_msg = start_instructions_font.render('press space or click on the screen to start', False, 'Green')
game_over_start_msg_rect = game_over_start_msg.get_rect(center=(400, 350))


#game_over_start_msg = start_instructions_font.render('press space or click on the screen to start', False, 'Green')
#game_over_start_msg_rect = game_over_start_msg.get_rect(topleft = (0, 0))

gost_surface = pygame.image.load('graphics/gost.png').convert_alpha()
gost_rectangle = gost_surface.get_rect(topleft = (734,290))

player_gravity = 0
player_surface = pygame.image.load(player_character).convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,355))

game_active = False

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
                    start_time = pygame.time.get_ticks()/1000
            if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                    game_active = True
                    gost_rectangle.left = 800
                    start_time = pygame.time.get_ticks()/1000            

    if game_active:
        screen.blit(sky_surface, (0,0))
        screen.blit(ground_surface, (0,300))
        display_score()

        #pygame.draw.line(screen, 'red', (0,0), (800,400), width=1)
        #pygame.draw.ellipse(screen, 'Red', pygame.Rect(50,50, 100,100))

        #ENEMYS
        gost_rectangle.left -= 6
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
        screen.blit(Game_over_surface, Game_over_rect)
        screen.blit(game_over_character_scaled, game_over_character_rect)
        screen.blit(game_over_start_msg, game_over_start_msg_rect)



    pygame.display.update()
    clock.tick(60)