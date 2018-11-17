import pygame

import fileUtils
from menu.pauseMenu import pause_menu
from player import Player
from pumptrackWayonits import way_points
from rider import Rider
from score import Score

SCORE = 0


def game_play(screen, screen_rect):
    playing = True

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
    Score.containers = all

    # Create Some Starting Values
    global score
    clock = pygame.time.Clock()

    # initialize our starting sprites
    global SCORE
    player = Player(screen_rect, way_points, True)
    if pygame.font:
        all.add(Score(SCORE))

    one_hit = False

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

        # clear/erase the last drawn sprites
        all.clear(screen, background)

        # update all the sprites
        all.update()

        # handle player input
        #direction = key_state[pygame.K_SPACE] - key_state[pygame.K_LEFT]
        if key_state[pygame.K_SPACE]:
            player.move()
            one_hit = True


        # draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # cap the framerate
        clock.tick(40)
