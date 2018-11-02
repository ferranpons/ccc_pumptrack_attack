import pygame

import fileUtils
from player import Player
from rider import Rider
from score import Score

SCORE = 0


def game_play(screen, screen_rect):
    # Load images, assign to sprite classes
    # (do this before the classes are used, after screen setup)
    img = fileUtils.load_image('intro_ball.gif')
    Player.images = [img, pygame.transform.flip(img, 1, 0)]
    Rider.images = fileUtils.load_images('intro_ball.gif', 'intro_ball.gif', 'intro_ball.gif')

    # decorate the game window
    icon = pygame.transform.scale(Rider.images[0], (32, 32))
    pygame.display.set_icon(icon)
    pygame.display.set_caption('Pygame Aliens')
    pygame.mouse.set_visible(0)

    # create the background, tile the bgd image
    bgdtile = fileUtils.load_image('intro_ball.gif')
    background = pygame.Surface(screen_rect.size)
    for x in range(0, screen_rect.width, bgdtile.get_width()):
        background.blit(bgdtile, (x, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # load the sound effects
    # shoot_sound = load_sound('car_door.wav')
    """if pygame.mixer:
        music = os.path.join(main_dir, 'data', 'house_lo.wav')
        pygame.mixer.music.load(music)
        pygame.mixer.music.play(-1)"""

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
    player = Player(screen_rect)
    Rider(screen_rect)  # note, this 'lives' because it goes into a sprite group
    if pygame.font:
        all.add(Score(SCORE))

    while player.alive():

        # get input
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return
        keystate = pygame.key.get_pressed()

        # clear/erase the last drawn sprites
        all.clear(screen, background)

        # update all the sprites
        all.update()

        # handle player input
        direction = keystate[pygame.K_RIGHT] - keystate[pygame.K_LEFT]
        player.move(direction)
        firing = keystate[pygame.K_SPACE]
        player.reloading = firing

        # draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # cap the framerate
        clock.tick(40)
