import pygame
from sys import exit
import random


def display_score():
    current_time = int(pygame.time.get_ticks()/1000 - start_time)
    score_surf = text_font.render(f'Score: {current_time}', False, 'Green')
    score_rect = score_surf.get_rect(center=(400, 50))
    screen.blit(score_surf, score_rect)
    return(current_time)


pygame.init()
pygame.mixer.init()

# SOUNDS
game_start_sound = pygame.mixer.Sound("sounds/game_start.wav")
pygame.mixer.music.load("sounds/background_sound.ogg")
pygame.mixer.music.set_volume(0.15)
pygame.mixer.music.play(-1)
jump_sound = pygame.mixer.Sound("sounds/woosh.wav")
game_over_sound = pygame.mixer.Sound("sounds/game_over.wav")

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)
start_instructions_font = pygame.font.Font(None, 40)

player_character = 'graphics/player/mario_1.png'

# Sky — two pieces that loop seamlessly
sky_surface_1 = pygame.image.load('graphics/background.png').convert()
sky_surface_2 = pygame.image.load('graphics/background_2.png').convert()
sky_surface_1_rect = sky_surface_1.get_rect(left=0)
sky_surface_2_rect = sky_surface_2.get_rect(left=800)
sky_surface_speed = 1

# Ground levels — y positions each ground piece can sit at
ground_low  = 344
ground_mid  = 300
ground_high = 250

# Each ground piece tracks its own level separately
ground_1_level = ground_low
ground_2_level = ground_low

# Ground — two pieces that loop and can change height
ground_surface_1 = pygame.image.load('graphics/road.png').convert_alpha()
ground_surface_2 = pygame.image.load('graphics/road.png').convert_alpha()
ground_surface_1_rect = ground_surface_1.get_rect(topleft=(0, ground_1_level))
ground_surface_2_rect = ground_surface_2.get_rect(topleft=(800, ground_2_level))

# Trees — two pieces, same speed as ground, bottom anchored to ground level
background_trees_surf_1 = pygame.image.load('graphics/background_trees_1.png').convert_alpha()
background_trees_rect_1 = background_trees_surf_1.get_rect(bottomleft=(0, ground_1_level + 10))
background_trees_surf_2 = pygame.image.load('graphics/background_trees_2.png').convert_alpha()
background_trees_rect_2 = background_trees_surf_2.get_rect(bottomleft=(800, ground_2_level + 10))
# Both trees and ground move at the same speed
ground_surface_speed = 5
background_speed = 5


def ground_movement(current_score):
    global ground_1_level, ground_2_level
    global ground_surface_1_rect, ground_surface_2_rect
    global background_trees_rect_1, background_trees_rect_2
    ground_levels = [ground_low, ground_mid, ground_high]

    if ground_surface_1_rect.right < 0:
        ground_surface_1_rect.left = ground_surface_2_rect.right
        ground_1_level = random.choice(ground_levels)
        ground_surface_1_rect.top = ground_1_level
        background_trees_rect_1.left = ground_surface_1_rect.left
        # Tree y updates at the same moment ground changes — fixes floating tree bug
        background_trees_rect_1.bottom = ground_1_level + 10

    if ground_surface_2_rect.right < 0:
        ground_surface_2_rect.left = ground_surface_1_rect.right
        ground_2_level = random.choice(ground_levels)
        ground_surface_2_rect.top = ground_2_level
        background_trees_rect_2.left = ground_surface_2_rect.left
        # Tree y updates at the same moment ground changes — fixes floating tree bug
        background_trees_rect_2.bottom = ground_2_level + 10

    # Draw trees before ground so ground renders on top
    screen.blit(background_trees_surf_1, background_trees_rect_1)
    screen.blit(background_trees_surf_2, background_trees_rect_2)
    screen.blit(ground_surface_1, ground_surface_1_rect)
    screen.blit(ground_surface_2, ground_surface_2_rect)


start_time = 0

# Game over screen
Game_over_surface = text_font.render(f'Score:', False, 'Green')
Game_over_rect = Game_over_surface.get_rect(midtop=(400, 50))

game_over_character = pygame.image.load(player_character).convert_alpha()
game_over_character_scaled = pygame.transform.scale_by(game_over_character, 1.5)
game_over_character_rect = game_over_character.get_rect(center=(380, 190))

game_over_start_msg = start_instructions_font.render('press space or click on the screen to start', False, 'Green')
game_over_start_msg_rect = game_over_start_msg.get_rect(center=(400, 350))

# Ghost enemy
gost_surface = pygame.image.load('graphics/gost.png').convert_alpha()
gost_rectangle = gost_surface.get_rect(top=290)
gost_speed = 6

# Player animation frames
walk_frames = [
    pygame.image.load('graphics/player/mario_1.png').convert_alpha(),
    pygame.image.load('graphics/player/mario_2.png').convert_alpha(),
]
current_frame_index = 0.0
animation_speed = 0.15
is_moving = False

player_gravity = 0
player_surface = pygame.image.load(player_character).convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 355))

coin_surface = pygame.image.load('graphics/coins/image_2.png').convert_alpha()
coin_rect = coin_surface.get_rect(midbottom = (100,300))
coin_frames = [
    pygame.image.load('graphics/coins/image_11.png').convert_alpha(),
    pygame.image.load('graphics/coins/image_10.png').convert_alpha(),
    pygame.image.load('graphics/coins/image_9.png').convert_alpha(),
    pygame.image.load('graphics/coins/image_8.png').convert_alpha(),
    pygame.image.load('graphics/coins/image_7.png').convert_alpha(),
    pygame.image.load('graphics/coins/image_6.png').convert_alpha(),
    pygame.image.load('graphics/coins/image_5.png').convert_alpha(),
    pygame.image.load('graphics/coins/image_4.png').convert_alpha(),
    pygame.image.load('graphics/coins/image_3.png').convert_alpha(),
    pygame.image.load('graphics/coins/image_2.png').convert_alpha(),
]
current_coin_frame_index = 0.0
coin_animation_speed = 0.15
is_coin_not_collected = True

def coins_logic():
    global current_coin_frame_index
    if is_coin_not_collected:
        current_coin_frame_index += coin_animation_speed
        if current_coin_frame_index >= len(coin_frames):
            current_coin_frame_index = 0.0
    coin_surface = coin_frames[int(current_coin_frame_index)]
    screen.blit(coin_surface, coin_rect)





def get_ground_level_at_player():
    # Returns the y level of whichever ground piece is under the player's x.
    # Returns None if the player is over a gap.
    player_x = player_rectangle.centerx

    if ground_surface_1_rect.left <= player_x <= ground_surface_1_rect.right:
        return ground_1_level

    if ground_surface_2_rect.left <= player_x <= ground_surface_2_rect.right:
        return ground_2_level

    return None  # over a gap


def player_ground_snaping_logic():
    global player_gravity

    ground_y = get_ground_level_at_player()

    if ground_y is None:
        return  # over a gap, let gravity keep pulling down

    # Only snap when falling AND feet have reached the ground
    if player_gravity > 0 and player_rectangle.bottom >= ground_y:
        player_rectangle.bottom = ground_y + 12
        player_gravity = 0  # reset gravity on landing


def is_player_grounded():
    # Returns True if the player is standing on a ground piece
    ground_y = get_ground_level_at_player()
    if ground_y is None:
        return False
    return player_rectangle.bottom >= ground_y


def player_logic():
    global current_frame_index, player_gravity

    # Only animate when a direction key is held
    if is_moving:
        current_frame_index += animation_speed
        if current_frame_index >= len(walk_frames):
            current_frame_index = 0.0

    player_surface = walk_frames[int(current_frame_index)]
    player_gravity += 1
    player_rectangle.y += player_gravity
    player_ground_snaping_logic()
    screen.blit(player_surface, player_rectangle)


def sky_movement():
    # Sky wraps around when it goes off screen
    if sky_surface_1_rect.right < 0:
        sky_surface_1_rect.left = 800
    if sky_surface_2_rect.right < 0:
        sky_surface_2_rect.left = 800

    screen.blit(sky_surface_1, sky_surface_1_rect)
    screen.blit(sky_surface_2, sky_surface_2_rect)


def game_enemies(current_score):
    speed_increase = (current_score // 5) * 1

    # Ghost only moves when player is moving (option B — world freezes when still)
    if is_moving:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            gost_rectangle.left -= gost_speed
        if keys[pygame.K_LEFT]:
            gost_rectangle.left += gost_speed

        if gost_rectangle.right < 0:
            gost_rectangle.left = 800
            gost_rectangle.bottom = ground_2_level

    screen.blit(gost_surface, gost_rectangle)


def reset_game():
    # Resets all positions and levels to starting state
    global ground_1_level, ground_2_level, player_gravity, start_time, is_moving
    gost_rectangle.left = 800
    ground_1_level = ground_low
    ground_2_level = ground_low
    ground_surface_1_rect.topleft = (0, ground_low)
    ground_surface_2_rect.topleft = (800, ground_low)
    background_trees_rect_1.bottomleft = (0, ground_low + 10)
    background_trees_rect_2.bottomleft = (800, ground_low + 10)
    player_rectangle.midbottom = (80, ground_low)
    player_gravity = 0
    is_moving = False
    start_time = pygame.time.get_ticks() / 1000


game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rectangle.collidepoint(event.pos) and is_player_grounded():
                    jump_sound.play()
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and is_player_grounded():
                    jump_sound.play()
                    player_gravity = -20

        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
                reset_game()

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                reset_game()

    if game_active:
        sky_movement()
        current_score = display_score()
        ground_movement(current_score)
        game_enemies(current_score)
        player_logic()
        coins_logic()

        keys = pygame.key.get_pressed()
        is_moving = keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]


        if keys[pygame.K_RIGHT]:
            ground_surface_1_rect.x -= ground_surface_speed
            ground_surface_2_rect.x -= ground_surface_speed
            sky_surface_1_rect.x -= sky_surface_speed
            sky_surface_2_rect.x -= sky_surface_speed
            background_trees_rect_1.x -= background_speed
            background_trees_rect_2.x -= background_speed

        if keys[pygame.K_LEFT]:
            ground_surface_1_rect.x += ground_surface_speed
            ground_surface_2_rect.x += ground_surface_speed
            sky_surface_1_rect.x += sky_surface_speed
            sky_surface_2_rect.x += sky_surface_speed
            background_trees_rect_1.x += background_speed
            background_trees_rect_2.x += background_speed

        if gost_rectangle.colliderect(player_rectangle):
            game_over_sound.play()
            game_active = False

    else:
        screen.blit(sky_surface_1, (0, 0))
        screen.blit(Game_over_surface, Game_over_rect)
        screen.blit(game_over_character_scaled, game_over_character_rect)
        screen.blit(game_over_start_msg, game_over_start_msg_rect)

    pygame.display.update()
    clock.tick(60)