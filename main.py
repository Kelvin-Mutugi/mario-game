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

sky_surface_1 = pygame.image.load('graphics/backgroung.png').convert()
sky_surface_2 = pygame.image.load('graphics/backgroung.png').convert()
sky_surface_1_rect = sky_surface_1.get_rect(left = 0)
sky_surface_2_rect = sky_surface_2.get_rect(left = 800)
sky_surface_speed = 3
ground_surface_1 = pygame.image.load('graphics/road.png').convert()
ground_surface_2 = pygame.image.load('graphics/road.png').convert()
ground_surface_1_rect = ground_surface_1.get_rect(topleft = (0,300))
ground_surface_2_rect = ground_surface_2.get_rect(topleft = (800,300))
ground_surface_speed = 2

start_time = 0

Game_over_surface = text_font.render(f'Score:', False, 'Green')
Game_over_rect = Game_over_surface.get_rect(midtop = (400, 50))

game_over_character = pygame.image.load(player_character).convert_alpha()
game_over_character_scaled = pygame.transform.scale_by(game_over_character, 1.5)
game_over_character_rect = game_over_character.get_rect(center = (380,190))

game_over_start_msg = start_instructions_font.render('press space or click on the screen to start', False, 'Green')
game_over_start_msg_rect = game_over_start_msg.get_rect(center=(400, 350))

gost_surface = pygame.image.load('graphics/gost.png').convert_alpha()
gost_rectangle = gost_surface.get_rect(topleft = (734,290))

walk_frames = [
     pygame.image.load('graphics/player/mario_1.png').convert_alpha(),
     pygame.image.load('graphics/player/mario_2.png').convert_alpha(),
     #pygame.image.load('graphics/player/mario_3.png').convert_alpha(), //makes the runing animation look alittle weird

]
current_frame_index = 0.0  # Must be a float to control animation speed
animation_speed = 0.15     # Controls how fast frames switch
is_moving = True

player_gravity = 0
player_surface = pygame.image.load(player_character).convert_alpha()
player_rectangle = player_surface.get_rect(midbottom = (80,355))

game_active = True

def sky_movement():
     sky_surface_1_rect.x -= sky_surface_speed
     sky_surface_2_rect.x -= sky_surface_speed

     if (sky_surface_1_rect.right < 0):
          sky_surface_1_rect.left = 800
     if (sky_surface_2_rect.right < 0):
          sky_surface_2_rect.left = 800  
     
     screen.blit(sky_surface_1, sky_surface_1_rect)
     screen.blit(sky_surface_2, sky_surface_2_rect)

def ground_movement():
     ground_surface_1_rect.x -= ground_surface_speed
     ground_surface_2_rect.x -= ground_surface_speed

     if (ground_surface_1_rect.right < 0):
          ground_surface_1_rect.left = 798
     if (ground_surface_2_rect.right < 0):
          ground_surface_2_rect.left = 800  
     
     screen.blit(ground_surface_1, ground_surface_1_rect)
     screen.blit(ground_surface_2, ground_surface_2_rect)




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
                    is_moving = True
                    start_time = pygame.time.get_ticks()/1000
            if event.type == pygame.KEYDOWN and pygame.K_SPACE:
                    game_active = True
                    gost_rectangle.left = 800
                    is_moving = True
                    start_time = pygame.time.get_ticks()/1000            

    if game_active:
        sky_movement()
        ground_movement()
        display_score()

        #ENEMYS
        gost_rectangle.left -= 6
        if gost_rectangle.right < 0 : gost_rectangle.left = 800
        screen.blit(gost_surface, gost_rectangle)
        

        #PLAYER animation
        if is_moving:
             current_frame_index += animation_speed
             if current_frame_index >= len(walk_frames):
                  current_frame_index = 0.0

        player_surface = walk_frames[int(current_frame_index)]           
        player_gravity += 1
        player_rectangle.y += player_gravity
        if player_rectangle.bottom >= 355 : player_rectangle.bottom = 355
        screen.blit(player_surface, player_rectangle)
        
        #COLLISION
        if gost_rectangle.colliderect(player_rectangle):
            game_active = False

    else:
        screen.blit(sky_surface_1, (0,0))
        screen.blit(Game_over_surface, Game_over_rect)
        screen.blit(game_over_character_scaled, game_over_character_rect)
        screen.blit(game_over_start_msg, game_over_start_msg_rect)



    pygame.display.update()
    clock.tick(60)