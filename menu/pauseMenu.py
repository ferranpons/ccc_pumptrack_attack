
import pygame

import colors
from fileUtils import load_image
from gameState import GameState
from textUtils import text_format, MENU_FONT

background_file = 'background_menu.png'
menu_line_file = 'menu_line.png'

TITLE_TEXT = "PAUSE MENU"
MENU_START = "CONTINUE"
MENU_QUIT = "QUIT"

MENU_START_DESCRIPTION = "Continue playing the game"
MENU_QUIT_DESCRIPTION = "Quit game and return to Main Menu"

menu_options = [MENU_START, MENU_QUIT]
menu_options_descriptions = [MENU_START_DESCRIPTION,
                             MENU_QUIT_DESCRIPTION]


class PauseScreen:
    selected = 0

    def __init__(self):
        self.menu_line = load_image(menu_line_file)

    def update_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if self.selected <= 0:
                    self.selected = len(menu_options) - 1
                else:
                    self.selected -= 1
            elif event.key == pygame.K_DOWN:
                if self.selected == len(menu_options) - 1:
                    self.selected = 0
                else:
                    self.selected += 1
            if event.key == pygame.K_RETURN:
                if self.selected == 0:
                    return False
                if self.selected == 1:
                    return True

    def draw(self, screen, screen_rect, background, background_in_alpha):
        screen.blit(background, screen_rect)
        screen.blit(background_in_alpha, screen_rect)

        title = text_format(TITLE_TEXT, MENU_FONT, 50, colors.white)
        if self.selected == 0:
            text_start = text_format(MENU_START, MENU_FONT, 25, colors.white)
        else:
            text_start = text_format(MENU_START, MENU_FONT, 25, colors.light_gray)
        if self.selected == 1:
            text_quit = text_format(MENU_QUIT, MENU_FONT, 25, colors.white)
        else:
            text_quit = text_format(MENU_QUIT, MENU_FONT, 25, colors.light_gray)

        screen.blit(title, (150, 220))
        screen.blit(self.menu_line, (150, 350))
        screen.blit(text_start, (150, 370))
        screen.blit(text_quit, (150, 400))
        screen.blit(self.menu_line, (150, 500))
