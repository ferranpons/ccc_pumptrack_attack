import os

import pygame

import colors
from fileUtils import load_image, main_dir
from textUtils import text_format, MENU_FONT

background_file = 'background_menu.png'
menu_line_file = 'menu_line.png'
clock = pygame.time.Clock()

TITLE_TEXT = "LEADERBOARD"


def load_leaderboard():
    file_name = os.path.join(main_dir, 'data', 'leaderboard.txt')
    file = open(file_name, 'r')
    file_content = file.readlines()
    file.close()

    leaders_array = []
    for item in file_content:
        leaders_array.append(item.replace('\n', '').split(','))
    return leaders_array


def leaderboard_menu(screen, menu_logos):
    in_leaderboard_menu = True

    # Load
    background_image = load_image(background_file)
    menu_line = load_image(menu_line_file)
    leaderboard_list = load_leaderboard()

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

        position_header_text = text_format("POSITION", MENU_FONT, 16, colors.white)
        screen.blit(position_header_text, (150, 300))
        time_header_text = text_format("TIME (seconds)", MENU_FONT, 16, colors.white)
        screen.blit(time_header_text, (300, 300))
        name_header_text = text_format("NAME", MENU_FONT, 16, colors.white)
        screen.blit(name_header_text, (500, 300))

        screen.blit(menu_line, (150, 320))

        for place in range(10):
            y_position = 330 + place * 16
            place_text = text_format(str(place+1) + ".", MENU_FONT, 16, colors.white)
            time_text = text_format(leaderboard_list[place][0], MENU_FONT, 16, colors.white)
            name_text = text_format(leaderboard_list[place][1], MENU_FONT, 16, colors.white)
            screen.blit(place_text, (150, y_position))
            screen.blit(time_text, (300, y_position))
            screen.blit(name_text, (500, y_position))

        screen.blit(menu_line, (150, 500))

        press_escape_text = text_format("Press 'Escape' key to return to the Main Menu", MENU_FONT, 16, colors.white)
        screen.blit(press_escape_text, (150, 520))

        pygame.display.update()
        clock.tick(30)
