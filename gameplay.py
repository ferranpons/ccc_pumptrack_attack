from enum import Enum

import pygame

import colors
import fileUtils
from countdown import CountDown
from gameState import GameState
from menu.pauseMenu import pause_menu
from player import Player
from pumptrackWayonits import way_points
from rider import Rider
from textUtils import text_format, MENU_FONT
from timecounter import TimeCounter


def game_play(screen, screen_rect):
    playing = True
    game_state = GameState.STARTING

    # Load images, assign to sprite classes
    img = fileUtils.load_image('rider1-placeholder.png')
    Player.images = [img, pygame.transform.flip(img, 1, 0)]

    # decorate the game window
    #icon = pygame.transform.scale(Rider.images[0], (32, 32))
    #pygame.display.set_icon(icon)
    #pygame.display.set_caption('Pygame Aliens')
    #pygame.mouse.set_visible(0)

    # create the background, tile the bgd image
    background = fileUtils.load_image('pumptrack1-placeholder.png')
    background_rect = background.get_rect()
    screen.blit(background, background_rect)
    pygame.display.flip()

    background_in_alpha = pygame.Surface((screen_rect.size[0], screen_rect.size[1]))
    background_in_alpha.set_alpha(128)
    background_in_alpha.fill(colors.black)

    # load the sound effects
    # shoot_sound = load_sound('car_door.wav')
    """if pygame.mixer:
        music = os.path.join(main_dir, 'data', 'house_lo.wav')
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)"""
    #fileUtils.load_music("Lame_Drivers_-_01_-_Frozen_Egg.mp3")
    #pygame.mixer.music.play(-1)

    # Initialize Game Groups
    aliens = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()
    lastalien = pygame.sprite.GroupSingle()

    # assign default groups to each sprite class
    Player.containers = all
    Rider.containers = aliens, all, lastalien
    TimeCounter.containers = all

    # Create Some Starting Values
    clock = pygame.time.Clock()

    # initialize our starting sprites
    player = Player(screen_rect, way_points, True)
    time_counter = TimeCounter()
    time_countdown = CountDown()
    if pygame.font:
        all.add(time_counter)

    while playing:

        # get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                quit_game = pause_menu(screen, screen_rect)
                if quit_game:
                    return
                screen.blit(background, background_rect)
                pygame.display.flip()

        key_state = pygame.key.get_pressed()

        all.clear(screen, background)
        all.update()
        #player.update_state(game_state)
        time_counter.set_state(game_state)
        time_countdown.set_state(game_state)
        time_countdown.update()

        if game_state == GameState.PLAYING:
            if key_state[pygame.K_SPACE]:
                player.move()

        if game_state == GameState.STARTING:
            time_countdown.draw(screen, screen_rect, background, background_in_alpha)
            pygame.display.update()
            if time_countdown.countdown <= 0:
                game_state = GameState.PLAYING

        dirty = all.draw(screen)
        pygame.display.update(dirty)

        clock.tick(30)
