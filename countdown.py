import pygame

import colors
from gameState import GameState
from textUtils import text_format, MENU_FONT


class CountDown:
    start_ticks = 0
    state = GameState.STARTING
    countdown = 5
    time_in_millis = 0

    def __init__(self):
        self.start_ticks = pygame.time.get_ticks()
        self.start_text = text_format("RACE STARTS", MENU_FONT, 25, colors.white)
        self.start_text_rect = self.start_text.get_rect()
        self.countdown_text = text_format(str(self.countdown), MENU_FONT, 25, colors.white)
        self.countdown_text_rect = self.countdown_text.get_rect()

    def set_state(self, game_state):
        self.state = game_state

    def update(self):
        if self.state == GameState.STARTING:
            self.time_in_millis = (pygame.time.get_ticks() - self.start_ticks) / 1000
        else:
            self.time_in_millis = 0

        if self.time_in_millis >= 1:
            self.countdown -= 1
            self.time_in_millis = 0

    def draw(self, screen, screen_rect, background, background_in_alpha):
        self.countdown_text = text_format(str(self.countdown), MENU_FONT, 25, colors.white)
        self.countdown_text_rect = self.countdown_text.get_rect()
        screen.blit(background, screen_rect)
        screen.blit(background_in_alpha, screen_rect)
        screen.blit(self.start_text, (screen_rect.size[0] / 2 - self.start_text_rect.size[0] / 2, screen_rect.size[1] / 2))
        screen.blit(self.countdown_text,
                    (screen_rect.size[0] / 2 - self.countdown_text_rect.size[0] / 2, screen_rect.size[1] / 2 + 50))


