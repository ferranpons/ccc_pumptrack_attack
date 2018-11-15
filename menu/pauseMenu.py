
import pygame

import colors
from fileUtils import load_image
from textUtils import text_format, MENU_FONT

background_file = 'background_menu.png'
menu_line_file = 'menu_line.png'
clock = pygame.time.Clock()

TITLE_TEXT = "PAUSE MENU"
MENU_START = "CONTINUE"
MENU_QUIT = "QUIT"

MENU_START_DESCRIPTION = "Continue playing the game"
MENU_QUIT_DESCRIPTION = "Quit game and return to Main Menu"

menu_options = [MENU_START, MENU_QUIT]
menu_options_descriptions = [MENU_START_DESCRIPTION,
                             MENU_QUIT_DESCRIPTION]


def pause_menu(screen, screen_rect):
    menu = True
    selected = 0

    # Load
    menu_line = load_image(menu_line_file)

    # Draw Background
    background_in_alpha = pygame.Surface((screen_rect.size[0], screen_rect.size[1]))
    background_in_alpha.set_alpha(128)
    background_in_alpha.fill(colors.black)
    screen.blit(background_in_alpha, screen_rect)

    while menu:
        for event in pygame.event.get():
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
                        menu = False
                    if selected == 1:
                        menu = False

        title = text_format(TITLE_TEXT, MENU_FONT, 50, colors.white)
        if selected == 0:
            text_start = text_format(MENU_START, MENU_FONT, 25, colors.white)
        else:
            text_start = text_format(MENU_START, MENU_FONT, 25, colors.light_gray)
        if selected == 1:
            text_quit = text_format(MENU_QUIT, MENU_FONT, 25, colors.white)
        else:
            text_quit = text_format(MENU_QUIT, MENU_FONT, 25, colors.light_gray)

        text_option_description = text_format(menu_options_descriptions[selected], MENU_FONT, 16, colors.white)

        screen.blit(title, (150, 220))
        screen.blit(menu_line, (150, 350))
        screen.blit(text_start, (150, 370))
        screen.blit(text_quit, (150, 460))
        screen.blit(menu_line, (150, 500))
        screen.blit(text_option_description, (150, 520))

        pygame.display.update()
        clock.tick(30)
