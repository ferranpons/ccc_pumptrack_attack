#!/usr/bin/env python
import pygame
import datetime

from gameState import GameState

MENU_FONT = 'data\\freesansbold.ttf'


class TimeCounter(pygame.sprite.Sprite):
    start_ticks = 0
    state = GameState.STARTING
    time_in_millis = 0
    image = None

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(MENU_FONT, 20)
        self.font.set_italic(1)
        self.color = pygame.Color('white')
        self.update()
        self.rect = self.image.get_rect().move(60, 660)
        self.start_ticks = pygame.time.get_ticks()

    def set_state(self, game_state):
        self.state = game_state

    def update(self):
        if self.state == GameState.PLAYING:
            self.time_in_millis = (pygame.time.get_ticks() - self.start_ticks)
        elif self.state == GameState.GAME_OVER or self.time_in_millis == GameState.STARTING:
            self.time_in_millis = 0
        msg = "Time: %ss" % datetime.datetime.fromtimestamp(self.time_in_millis / 1000.0).strftime('%S.%f')[:-3]
        self.image = self.font.render(msg, 0, self.color)
