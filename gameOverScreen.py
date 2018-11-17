import pygame

import colors
from gameState import GameState
from textUtils import text_format, MENU_FONT

GAME_OVER_TITLE = 'GAME OVER'


class GameOverScreen:
    state = GameState.STARTING

    def __init__(self):
        self.game_over_title_text = text_format(GAME_OVER_TITLE, MENU_FONT, 25, colors.white)
        self.game_over_title_text_rect = self.game_over_title_text.get_rect()

    def set_state(self, game_state):
        self.state = game_state

    def update(self):
        pass

    def draw(self, screen, screen_rect, background, background_in_alpha):
        screen.blit(background, screen_rect)
        screen.blit(background_in_alpha, screen_rect)
        screen.blit(self.game_over_title_text, (screen_rect.size[0] / 2 - self.game_over_title_text_rect.size[0] / 2, screen_rect.size[1] / 2))

    def set_final_time(self, time_in_millis):
        pass
