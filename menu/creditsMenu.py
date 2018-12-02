import pygame

import colors
from fileUtils import load_image
from textUtils import text_format, MENU_FONT
import webbrowser

background_file = 'background_menu.png'
menu_line_file = 'menu_line.png'
clock = pygame.time.Clock()

CCC_URL = 'https://sickbicycle.co/pages/chainbreakers-cc'
CCC_FACEBOOK_URL = 'https://www.facebook.com/groups/428058410999948/'

TITLE_TEXT = "CREDITS"
MENU_ABOUT_CCC = "ABOUT CHAINBREAKERS CYCLING CLUB"
MENU_GO_TO_WEB = "GO TO CHAINBREAKERS FACEBOOK PAGE"
MENU_RETURN = "RETURN"

MENU_ABOUT_CCC_DESCRIPTION = "Get to know where CCC came from"
MENU_CCC_FACEBOOK_DESCRIPTION = "Do you want to join? Go to the Facebook page"
MENU_RETURN_DESCRIPTION = "Return to the Main Menu"

menu_options = [MENU_ABOUT_CCC, MENU_GO_TO_WEB, MENU_RETURN]
menu_options_descriptions = [MENU_ABOUT_CCC_DESCRIPTION,
                             MENU_CCC_FACEBOOK_DESCRIPTION,
                             MENU_RETURN_DESCRIPTION]


def go_to_web(url):
    webbrowser.open(url, new=2)


def credits_menu(screen, menu_logos):
    in_credits_menu = True
    selected = 0

    # Load
    background_image = load_image(background_file)
    menu_line = load_image(menu_line_file)

    while in_credits_menu:
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
                        go_to_web(CCC_URL)
                    if selected == 1:
                        go_to_web(CCC_FACEBOOK_URL)
                    if selected == 2:
                        return

        # Draw Background
        background_rect = background_image.get_rect()
        background_rect.left, background_rect.top = [0, 0]
        screen.fill([255, 255, 255])
        screen.blit(background_image, background_rect)

        # Draw Logos
        menu_logos.draw(screen)

        title = text_format(TITLE_TEXT, MENU_FONT, 50, colors.white)
        screen.blit(title, (150, 220))

        developed_by = text_format("DEVELOPED BY FERRAN PONS (PROGRAMMING AND GRAPHICS)", MENU_FONT, 16, colors.white)
        screen.blit(developed_by, (150, 300))

        screen.blit(menu_line, (150, 320))

        if selected == 0:
            text_ccc_about = text_format(MENU_ABOUT_CCC, MENU_FONT, 25, colors.white)
        else:
            text_ccc_about = text_format(MENU_ABOUT_CCC, MENU_FONT, 25, colors.light_gray)
        if selected == 1:
            text_ccc_facebook = text_format(MENU_GO_TO_WEB, MENU_FONT, 25, colors.white)
        else:
            text_ccc_facebook = text_format(MENU_GO_TO_WEB, MENU_FONT, 25, colors.light_gray)
        if selected == 2:
            text_quit = text_format(MENU_RETURN, MENU_FONT, 25, colors.white)
        else:
            text_quit = text_format(MENU_RETURN, MENU_FONT, 25, colors.light_gray)

        text_option_description = text_format(menu_options_descriptions[selected], MENU_FONT, 16, colors.white)

        screen.blit(text_ccc_about, (150, 340))
        screen.blit(text_ccc_facebook, (150, 370))
        screen.blit(text_quit, (150, 460))
        screen.blit(menu_line, (150, 500))
        screen.blit(text_option_description, (150, 520))

        music_title_text = text_format("MUSIC", MENU_FONT, 18, colors.white)
        screen.blit(music_title_text, (800, 300))
        screw_wave = text_format("Screw Wave by Windom Earle", MENU_FONT, 16, colors.white)
        screen.blit(screw_wave, (800, 330))
        screw_wave_license = \
            text_format("licensed under a Attribution-NonCommercial-ShareAlike 3.0 International License.",
                        MENU_FONT, 10, colors.white)
        screen.blit(screw_wave_license, (800, 350))

        pygame.display.update()
        clock.tick(30)
