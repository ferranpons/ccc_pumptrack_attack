import pygame

import colors
from menu.creditsMenu import credits_menu
from fileUtils import load_image
from gameplay import game_play
from menu.menulogos import MenuLogos
from menu.settingsMenu import settings_menu
from textUtils import text_format, MENU_FONT

background_file = 'background_menu.png'
menu_line_file = 'menu_line.png'
clock = pygame.time.Clock()

TITLE_TEXT = "MAIN MENU"
MENU_START = "START"
MENU_SETTINGS = "SETTINGS"
MENU_CREDITS = "CREDITS"
MENU_QUIT = "QUIT"

MENU_START_DESCRIPTION = "Start a new game"
MENU_START_SETTINGS_DESCRIPTION = "Change the settings of the game"
MENU_CREDITS_DESCRIPTION = "Checkout who made this game"
MENU_QUIT_DESCRIPTION = "Leave this game"

menu_options = [MENU_START, MENU_SETTINGS, MENU_CREDITS, MENU_QUIT]
menu_options_descriptions = [MENU_START_DESCRIPTION,
                             MENU_START_SETTINGS_DESCRIPTION,
                             MENU_CREDITS_DESCRIPTION,
                             MENU_QUIT_DESCRIPTION]


def main_menu(screen, screen_rect):
    menu = True
    selected = 0
    menu_logos = MenuLogos()

    # Load
    background_image = load_image(background_file)
    menu_line = load_image(menu_line_file)
    menu_logos.load()

    while menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
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
                        game_play(screen, screen_rect)
                    if selected == 1:
                        settings_menu(menu_logos)
                    if selected == 2:
                        credits_menu(screen, menu_logos)
                    if selected == 3:
                        pygame.quit()
                        quit()

        # Draw Background
        background_rect = background_image.get_rect()
        background_rect.left, background_rect.top = [0, 0]
        screen.fill([255, 255, 255])
        screen.blit(background_image, background_rect)

        # Draw Logos
        menu_logos.draw(screen)

        # Main Menu UI
        title = text_format(TITLE_TEXT, MENU_FONT, 50, colors.white)
        if selected == 0:
            text_start = text_format(MENU_START, MENU_FONT, 25, colors.white)
        else:
            text_start = text_format(MENU_START, MENU_FONT, 25, colors.light_gray)
        if selected == 1:
            text_settings = text_format(MENU_SETTINGS, MENU_FONT, 25, colors.white)
        else:
            text_settings = text_format(MENU_SETTINGS, MENU_FONT, 25, colors.light_gray)
        if selected == 2:
            text_credits = text_format(MENU_CREDITS, MENU_FONT, 25, colors.white)
        else:
            text_credits = text_format(MENU_CREDITS, MENU_FONT, 25, colors.light_gray)
        if selected == 3:
            text_quit = text_format(MENU_QUIT, MENU_FONT, 25, colors.white)
        else:
            text_quit = text_format(MENU_QUIT, MENU_FONT, 25, colors.light_gray)

        text_option_description = text_format(menu_options_descriptions[selected], MENU_FONT, 16, colors.white)

        # Main Menu Text
        screen.blit(title, (150, 220))
        screen.blit(menu_line, (150, 350))
        screen.blit(text_start, (150, 370))
        screen.blit(text_settings, (150, 400))
        screen.blit(text_credits, (150, 430))
        screen.blit(text_quit, (150, 460))
        screen.blit(menu_line, (150, 500))
        screen.blit(text_option_description, (150, 520))
        #screen.blit(menu_line, (150, 600))
        pygame.display.update()
        clock.tick(30)


"""
For documentation of the webbrowser module,
see http://docs.python.org/library/webbrowser.html

import webbrowser
new = 2 # open in a new tab, if possible

# open a public URL, in this case, the webbrowser docs
url = "http://docs.python.org/library/webbrowser.html"
webbrowser.open(url,new=new)

# open an HTML file on my own (Windows) computer
url = "file://X:/MiscDev/language_links.html"
webbrowser.open(url,new=new)
"""