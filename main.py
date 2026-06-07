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
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
text_font = pygame.font.Font(None, 50)
start_instructions_font = pygame.font.Font(None, 40)

player_character = 'graphics/player/mario_1.png'

# Sky
sky_surface_1 = pygame.image.load('graphics/backgroung.png').convert()
sky_surface_2 = pygame.image.load('graphics/backgroung.png').convert()
sky_surface_1_rect = sky_surface_1.get_rect(left=0)
sky_surface_2_rect = sky_surface_2.get_rect(left=800)
sky_surface_speed = 3

# Ground levels — these are the y positions each ground piece can sit at
ground_low  = 344
ground_mid  = 300
ground_high = 250

# FIX 1: We now store each ground piece's level separately.
# Before, one variable 'current_ground_level' was shared and being
# overwritten randomly by both pieces — causing the player snap
# logic to read the wrong value. Now each piece tracks its own level.
ground_1_level = ground_low
ground_2_level = ground_low

ground_surface_1 = pygame.image.load('graphics/road.png').convert_alpha()
ground_surface_2 = pygame.image.load('graphics/road.png').convert_alpha()
ground_surface_1_rect = ground_surface_1.get_rect(topleft=(0, ground_1_level))
ground_surface_2_rect = ground_surface_2.get_rect(topleft=(800, ground_2_level))
ground_surface_speed = 2


def ground_movement(current_score):
    # FIX 1 continued: use 'global' on both separate level variables
    global ground_1_level, ground_2_level
    ground_levels = [ground_low, ground_mid, ground_high]

    ground_surface_1_rect.x -= ground_surface_speed
    ground_surface_2_rect.x -= ground_surface_speed

    if ground_surface_1_rect.right < 0:
        ground_surface_1_rect.left = 798
        # Pick a new random level for piece 1 only
        ground_1_level = random.choice(ground_levels)
        ground_surface_1_rect.top = ground_1_level

    if ground_surface_2_rect.right < 0:
        ground_surface_2_rect.left = 800
        # Pick a new random level for piece 2 only
        ground_2_level = random.choice(ground_levels)
        ground_surface_2_rect.top = ground_2_level

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

gost_surface = pygame.image.load('graphics/gost.png').convert_alpha()
gost_rectangle = gost_surface.get_rect(top=290)
gost_speed = 6

walk_frames = [
    pygame.image.load('graphics/player/mario_1.png').convert_alpha(),
    pygame.image.load('graphics/player/mario_2.png').convert_alpha(),
]
current_frame_index = 0.0
animation_speed = 0.15
is_moving = True

player_gravity = 0
player_surface = pygame.image.load(player_character).convert_alpha()
player_rectangle = player_surface.get_rect(midbottom=(80, 355))


def get_ground_level_at_player():
    # FIX 2: This function figures out which ground piece the player
    # is currently standing above, and returns that piece's y level.
    #
    # Before, the code checked ground_surface_1_rect and ground_surface_2_rect
    # with if/elif — meaning if rect 1 matched, rect 2 was never checked.
    # Also it never verified the player's x was actually over the piece.
    #
    # Now we check: is the player's x position within the horizontal
    # range of each ground piece? If yes, return that piece's level.
    # If the player is over a gap (neither piece), return None.

    player_x = player_rectangle.centerx

    if ground_surface_1_rect.left <= player_x <= ground_surface_1_rect.right:
        return ground_1_level

    if ground_surface_2_rect.left <= player_x <= ground_surface_2_rect.right:
        return ground_2_level

    # Player is over a gap — no ground beneath them
    return None


def player_ground_snaping_logic():
    global player_gravity

    ground_y = get_ground_level_at_player()

    if ground_y is None:
        # FIX 3: Player is over a gap — let gravity keep pulling them down.
        # Before there was no gap handling at all, the player would just
        # snap to a ground level even when floating over empty space.
        return

    # FIX 4: Only snap if the player is falling (gravity > 0) AND
    # their feet have reached or passed the ground surface.
    # Before, the snap happened even when jumping upward through the ground.
    if player_gravity > 0 and player_rectangle.bottom >= ground_y:
        player_rectangle.bottom = ground_y
        player_gravity = 0  # FIX 5: Reset gravity to 0 on landing.
                            # Before, gravity kept increasing even after landing,
                            # so after a jump gravity would be a huge number and
                            # the player would slam through the ground next frame.


def is_player_grounded():
    # FIX 6: A clean helper to check if the player is standing on ground.
    # Before, the jump condition used 'current_ground_level' which was
    # being randomly overwritten — so the player could sometimes jump in mid-air
    # or couldn't jump even when standing. Now we check the actual ground
    # beneath the player's feet directly.
    ground_y = get_ground_level_at_player()
    if ground_y is None:
        return False
    return player_rectangle.bottom >= ground_y


def player_logic():
    global current_frame_index, player_gravity

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
    sky_surface_1_rect.x -= sky_surface_speed
    sky_surface_2_rect.x -= sky_surface_speed

    if sky_surface_1_rect.right < 0:
        sky_surface_1_rect.left = 800
    if sky_surface_2_rect.right < 0:
        sky_surface_2_rect.left = 800

    screen.blit(sky_surface_1, sky_surface_1_rect)
    screen.blit(sky_surface_2, sky_surface_2_rect)


def game_enemies(current_score):
    # FIX 7: Ghost spawn y position now follows the current ground level
    # instead of being hardcoded to [290, 250, 240].
    # Before, the ghost would float at random heights unrelated to where
    # the ground actually was after a level change.
    speed_increase = (current_score // 5) * 1
    gost_rectangle.left -= gost_speed + speed_increase

    if gost_rectangle.right < 0:
        gost_rectangle.left = 800
        # Spawn ghost just above whichever ground piece is coming in from the right.
        # ground_2_level is the piece currently at x=800 (the incoming piece).
        gost_rectangle.bottom = ground_2_level

    screen.blit(gost_surface, gost_rectangle)


game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # FIX 6 applied: use is_player_grounded() for jump check
                if player_rectangle.collidepoint(event.pos) and is_player_grounded():
                    player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and is_player_grounded():
                    player_gravity = -20

        else:
            if event.type == pygame.MOUSEBUTTONDOWN:
                game_active = True
                gost_rectangle.left = 800
                is_moving = True
                # FIX 8: Reset ground levels and player position on restart.
                # Before, the ground pieces stayed at whatever random level
                # they were at when the game ended — the player would spawn
                # at y=355 but the ground might be at y=250.
                ground_1_level = ground_low
                ground_2_level = ground_low
                ground_surface_1_rect.topleft = (0, ground_low)
                ground_surface_2_rect.topleft = (800, ground_low)
                player_rectangle.midbottom = (80, ground_low)
                player_gravity = 0
                start_time = pygame.time.get_ticks() / 1000

            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # FIX 9: Added 'event.key == pygame.K_SPACE' check.
                # Before it was just 'pygame.K_SPACE' (the integer 32) which
                # is always truthy — so ANY key press would restart the game.
                game_active = True
                gost_rectangle.left = 800
                is_moving = True
                ground_1_level = ground_low
                ground_2_level = ground_low
                ground_surface_1_rect.topleft = (0, ground_low)
                ground_surface_2_rect.topleft = (800, ground_low)
                player_rectangle.midbottom = (80, ground_low)
                player_gravity = 0
                start_time = pygame.time.get_ticks() / 1000

    if game_active:
        sky_movement()
        current_score = display_score()
        ground_movement(current_score)
        game_enemies(current_score)
        player_logic()

        if gost_rectangle.colliderect(player_rectangle):
            game_active = False

    else:
        screen.blit(sky_surface_1, (0, 0))
        screen.blit(Game_over_surface, Game_over_rect)
        screen.blit(game_over_character_scaled, game_over_character_rect)
        screen.blit(game_over_start_msg, game_over_start_msg_rect)

    pygame.display.update()
    clock.tick(60)