import pygame

import colors
import fileUtils
from countdown import CountDown
from gameOverScreen import GameOverScreen, GameOverState
from gameState import GameState
from menu.pauseMenu import PauseScreen
from player import Player
from pumptrackWayonits import way_points
from rider import Rider
from timeCounter import TimeCounter


def game_play(screen, screen_rect):
    playing = True
    game_state = GameState.STARTING
    number_of_laps = 1

    # Load images, assign to sprite classes
    img = fileUtils.load_image('rider1-placeholder.png')
    Player.images = [img, pygame.transform.flip(img, 1, 0)]

    # decorate the game window
    # icon = pygame.transform.scale(Rider.images[0], (32, 32))
    # pygame.display.set_icon(icon)
    # pygame.display.set_caption('Pygame Aliens')
    # pygame.mouse.set_visible(0)

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
    # fileUtils.load_music("Lame_Drivers_-_01_-_Frozen_Egg.mp3")
    # pygame.mixer.music.play(-1)

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
    game_over = GameOverScreen()
    pause_menu = PauseScreen()
    if pygame.font:
        all.add(time_counter)

    button_down = False

    while playing:

        # get input
        for event in pygame.event.get():
            game_over_state = game_over.update_input(event)
            if game_over_state == GameOverState.RESTART:
                game_state = GameState.RESTART
            elif game_over_state == GameOverState.QUIT:
                return

            quit_game = pause_menu.update_input(event)
            if quit_game:
                return

            if event.type == pygame.QUIT \
                    or (event.type == pygame.KEYDOWN
                        and event.key == pygame.K_ESCAPE
                        and game_state == GameState.PLAYING):
                game_state = GameState.PAUSED

            if event.type == pygame.KEYDOWN \
                    and event.key == pygame.K_SPACE \
                    and button_down is False \
                    and game_state == GameState.PLAYING:
                button_down = True

        all.clear(screen, background)
        all.update()
        # player.update_state(game_state)
        time_counter.set_state(game_state)
        time_countdown.set_state(game_state)
        game_over.set_state(game_state)
        time_countdown.update()

        if time_countdown.countdown <= 0 and game_state == GameState.STARTING:
            game_state = GameState.PLAYING
            screen.blit(background, background_rect)
            pygame.display.flip()

        if game_state == GameState.PLAYING:
            player.pump()
            if button_down is True:
                player.add_pump()
                button_down = False
            if player.lap >= number_of_laps:
                game_state = GameState.GAME_OVER
                game_over.set_final_time(time_counter.time_in_millis)

        if game_state == GameState.STARTING:
            time_countdown.draw(screen, screen_rect, background, background_in_alpha)
            pygame.display.update()

        if game_state == GameState.PAUSED:
            pause_menu.draw(screen, screen_rect, background, background_in_alpha)
            pygame.display.update()

        if game_state == GameState.GAME_OVER:
            game_over.draw(screen, screen_rect, background, background_in_alpha)
            pygame.display.update()

        if game_state == GameState.RESTART:
            clock = pygame.time.Clock()
            player = Player(screen_rect, way_points, True)
            time_counter = TimeCounter()
            time_countdown = CountDown()
            game_state = GameState.STARTING

        dirty = all.draw(screen)
        pygame.display.update(dirty)

        clock.tick(30)
