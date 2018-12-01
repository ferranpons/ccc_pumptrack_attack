import datetime
from enum import Enum

import pygame

import colors
from fileUtils import load_leaderboard, load_image
from gameState import GameState
from textUtils import text_format, MENU_FONT

menu_line_file = 'menu_line.png'

GAME_OVER_TITLE = 'GAME OVER'
MENU_START = "TRY AGAIN"
MENU_QUIT = "RETURN TO MAIN MENU"

MENU_START_DESCRIPTION = "Start again to try to beat your current record"
MENU_QUIT_DESCRIPTION = "Quit game and return to Main Menu"

menu_options = [MENU_START, MENU_QUIT]
menu_options_descriptions = [MENU_START_DESCRIPTION,
                             MENU_QUIT_DESCRIPTION]


class GameOverState(Enum):
    RESTART = 0
    QUIT = 1
    IDLE = 2


class GameOverScreen:
    state = GameState.STARTING
    final_time = 0
    leaderboard_list = None
    selected = 0

    def __init__(self):
        self.menu_line = load_image(menu_line_file)
        self.leaderboard_list = load_leaderboard()

    def set_state(self, game_state):
        self.state = game_state

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
                    return GameOverState.RESTART
                if self.selected == 1:
                    return GameOverState.QUIT
        return GameOverState.IDLE

    def draw(self, screen, screen_rect, background, background_in_alpha):
        screen.blit(background, screen_rect)
        screen.blit(background_in_alpha, screen_rect)

        msg = "Your final Time: %ss" % datetime.datetime.fromtimestamp(self.final_time / 1000.0).strftime('%S.%f')[:-3]
        final_time_text = text_format(msg, MENU_FONT, 20, colors.white)
        screen.blit(final_time_text,
                    (screen_rect.size[0] / 2 + 150, screen_rect.size[1] / 2 - 100))

        for place in range(10):
            y_position = 330 + place * 16
            place_text = text_format(str(place+1) + ".", MENU_FONT, 16, colors.white)
            time_text = text_format(self.leaderboard_list[place][0], MENU_FONT, 16, colors.white)
            name_text = text_format(self.leaderboard_list[place][1], MENU_FONT, 16, colors.white)

            screen.blit(place_text, (screen_rect.size[0] / 2 + 150, y_position))
            screen.blit(time_text, (screen_rect.size[0] / 2 + 180, y_position))
            screen.blit(name_text, (screen_rect.size[0] / 2 + 240, y_position))

        title = text_format(GAME_OVER_TITLE, MENU_FONT, 50, colors.white)
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

    def set_final_time(self, time_in_millis):
        self.final_time = time_in_millis
