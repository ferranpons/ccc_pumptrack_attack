import pygame

import colors
from fileUtils import load_image
from textUtils import text_format, MENU_FONT

background_file = 'background_menu.png'
menu_line_file = 'menu_line.png'
clock = pygame.time.Clock()

TITLE_TEXT = "SETTINGS"
MENU_SFX_VOLUME = "SFX VOLUME: "
MENU_MUSIC_VOLUME = "MUSIC VOLUME: "
MENU_FULL_SCREEN_MODE = "FULL SCREEN MODE: "
MENU_RETURN = "RETURN"

MENU_SFX_VOLUME_DESCRIPTION = "Select the volume of the sound effects"
MENU_MUSIC_VOLUME_DESCRIPTION = "Select the volume of the music"
MENU_FULL_SCREEN_MODE_DESCRIPTION = "Change between full screen mode and windowed"
MENU_RETURN_DESCRIPTION = "Return to Main Menu"

menu_options = [MENU_SFX_VOLUME, MENU_MUSIC_VOLUME, MENU_FULL_SCREEN_MODE, MENU_RETURN]
menu_options_descriptions = [MENU_SFX_VOLUME_DESCRIPTION,
                             MENU_MUSIC_VOLUME_DESCRIPTION,
                             MENU_FULL_SCREEN_MODE_DESCRIPTION,
                             MENU_RETURN_DESCRIPTION]
menu_options_default_values = [.5, .5, False]


def change_sound_volume():
    current_volume = pygame.mixer.Channel(0).get_volume()
    if current_volume < 1:
        pygame.mixer.Channel(0).set_volume(current_volume + 0.1)
    else:
        pygame.mixer.Channel(0).set_volume(0)


def change_music_volume():
    current_volume = pygame.mixer.music.get_volume()
    if current_volume < 1:
        pygame.mixer.music.set_volume(current_volume + 0.1)
    else:
        pygame.mixer.music.set_volume(0)


def is_full_screen():
    screen = pygame.display.get_surface()
    flags = screen.get_flags()
    if flags ^ pygame.FULLSCREEN == 0:
        return "ON"
    else:
        return "OFF"


def toggle_full_screen():
    screen = pygame.display.get_surface()
    tmp = screen.convert()
    caption = pygame.display.get_caption()
    cursor = pygame.mouse.get_cursor()  # Duoas 16-04-2007

    w, h = screen.get_width(), screen.get_height()
    flags = screen.get_flags()
    bits = screen.get_bitsize()

    pygame.display.quit()
    pygame.display.init()

    screen = pygame.display.set_mode((w, h), flags ^ pygame.FULLSCREEN, bits)
    screen.blit(tmp, (0, 0))
    pygame.display.set_caption(*caption)

    pygame.key.set_mods(0)  # HACK: work-a-round for a SDL bug??

    pygame.mouse.set_cursor(*cursor)  # Duoas 16-04-2007

    return screen


def settings_menu(menu_logos):
    menu = True
    selected = 0

    # Load
    background_image = load_image(background_file)
    menu_line = load_image(menu_line_file)

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if selected <= 0:
                        selected = len(menu_options) - 1
                    else:
                        selected -= 1
                elif event.key == pygame.K_DOWN:
                    if selected == len(menu_options) - 1:
                        selected = 0
                    else:
                        selected += 1
                if event.key == pygame.K_RETURN:
                    if selected == 0:
                        change_sound_volume()
                    if selected == 1:
                        change_music_volume()
                    if selected == 2:
                        toggle_full_screen()
                    if selected == 3:
                        menu = False

        # Draw Background
        background_rect = background_image.get_rect()
        background_rect.left, background_rect.top = [0, 0]
        screen = pygame.display.get_surface()
        screen.fill([255, 255, 255])
        screen.blit(background_image, background_rect)

        # Draw Logos
        menu_logos.draw(screen)

        # Main Menu UI
        # screen.fill(colors.light_blue)
        title = text_format(TITLE_TEXT, MENU_FONT, 50, colors.white)
        sfx_volume = MENU_SFX_VOLUME + str(int(pygame.mixer.Channel(0).get_volume() * 10))
        music_volume = MENU_MUSIC_VOLUME + str(int(pygame.mixer.music.get_volume()*10))
        full_screen_mode = MENU_FULL_SCREEN_MODE + is_full_screen()
        if selected == 0:
            text_start = text_format(sfx_volume, MENU_FONT, 25, colors.white)
        else:
            text_start = text_format(sfx_volume, MENU_FONT, 25, colors.light_gray)
        if selected == 1:
            text_settings = text_format(music_volume, MENU_FONT, 25, colors.white)
        else:
            text_settings = text_format(music_volume, MENU_FONT, 25, colors.light_gray)
        if selected == 2:
            text_credits = text_format(full_screen_mode, MENU_FONT, 25, colors.white)
        else:
            text_credits = text_format(full_screen_mode, MENU_FONT, 25, colors.light_gray)
        if selected == 3:
            text_quit = text_format(MENU_RETURN, MENU_FONT, 25, colors.white)
        else:
            text_quit = text_format(MENU_RETURN, MENU_FONT, 25, colors.light_gray)

        text_option_description = text_format(menu_options_descriptions[selected], MENU_FONT, 16, colors.white)

        # Main Menu Text
        screen.blit(title, (150, 220))
        screen.blit(menu_line, (150, 320))
        screen.blit(text_start, (150, 340))
        screen.blit(text_settings, (150, 370))
        screen.blit(text_credits, (150, 400))
        screen.blit(text_quit, (150, 460))
        screen.blit(menu_line, (150, 500))
        screen.blit(text_option_description, (150, 520))
        pygame.display.update()
        clock.tick(30)
