import pygame

import colors
from fileUtils import load_image
from textUtils import text_format, MENU_FONT

background_file = 'background_menu.png'
menu_line_file = 'menu_line.png'
clock = pygame.time.Clock()

TITLE_TEXT = "LEADERBOARD"


def leaderboard_menu(screen, menu_logos):
    in_leaderboard_menu = True

    # Load
    background_image = load_image(background_file)
    menu_line = load_image(menu_line_file)

    while in_leaderboard_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
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
        screen.blit(menu_line, (150, 320))

        for place in range(10):
            y_position = 330 + place * 16
            place_text = text_format(str(place+1) + ".", MENU_FONT, 16, colors.white)
            time_text = text_format("00:25:00m", MENU_FONT, 16, colors.white)
            name_text = text_format("J. Chaos", MENU_FONT, 16, colors.white)
            screen.blit(place_text, (150, y_position))
            screen.blit(time_text, (300, y_position))
            screen.blit(name_text, (500, y_position))

        screen.blit(menu_line, (150, 500))

        pygame.display.update()
        clock.tick(30)
