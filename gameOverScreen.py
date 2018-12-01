import datetime

import pygame

import colors
from fileUtils import load_leaderboard
from gameState import GameState
from textUtils import text_format, MENU_FONT

GAME_OVER_TITLE = 'GAME OVER'
MENU_START = "TRY AGAIN"
MENU_QUIT = "RETURN TO MAIN MENU"

MENU_START_DESCRIPTION = "Start again to try to beat your current record"
MENU_QUIT_DESCRIPTION = "Quit game and return to Main Menu"

menu_options = [MENU_START, MENU_QUIT]
menu_options_descriptions = [MENU_START_DESCRIPTION,
                             MENU_QUIT_DESCRIPTION]


class GameOverScreen:
    state = GameState.STARTING
    final_time = 0
    leaderboard_list = None

    def __init__(self):
        self.game_over_title_text = text_format(GAME_OVER_TITLE, MENU_FONT, 35, colors.white)
        self.game_over_title_text_rect = self.game_over_title_text.get_rect()
        self.leaderboard_list = load_leaderboard()

    def set_state(self, game_state):
        self.state = game_state

    def update(self):
        pass

    def draw(self, screen, screen_rect, background, background_in_alpha):
        screen.blit(background, screen_rect)
        screen.blit(background_in_alpha, screen_rect)
        screen.blit(self.game_over_title_text,
                    (screen_rect.size[0] / 2 - self.game_over_title_text_rect.size[0] / 2,
                     screen_rect.size[1] / 2 - 200))

        msg = "Your final Time: %ss" % datetime.datetime.fromtimestamp(self.final_time / 1000.0).strftime('%S.%f')[:-3]
        final_time_text = text_format(msg, MENU_FONT, 20, colors.white)
        final_time_text_rect = final_time_text.get_rect()
        screen.blit(final_time_text,
                    (screen_rect.size[0] / 2 - final_time_text_rect.size[0] / 2 - 100, screen_rect.size[1] / 2 - 100))

        for place in range(10):
            y_position = 230 + place * 16
            place_text = text_format(str(place+1) + ".", MENU_FONT, 16, colors.white)
            time_text = text_format(self.leaderboard_list[place][0], MENU_FONT, 16, colors.white)
            name_text = text_format(self.leaderboard_list[place][1], MENU_FONT, 16, colors.white)

            screen.blit(place_text, (screen_rect.size[0] / 2 + 150, y_position))
            screen.blit(time_text, (screen_rect.size[0] / 2 + 180, y_position))
            screen.blit(name_text, (screen_rect.size[0] / 2 + 240, y_position))

    def set_final_time(self, time_in_millis):
        self.final_time = time_in_millis
