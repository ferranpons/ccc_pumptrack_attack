#!/usr/bin/env python
import pygame
import datetime


class Score(pygame.sprite.Sprite):
    start_ticks = 0

    def __init__(self, score):
        self.score = score
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = pygame.Color('white')
        self.update()
        self.rect = self.image.get_rect().move(500, 50)
        self.start_ticks = pygame.time.get_ticks()

    def update(self):
        time_in_millis = (pygame.time.get_ticks() - self.start_ticks)
        msg = "Time: %s" % datetime.datetime.fromtimestamp(time_in_millis/1000.0).strftime('%S.%f')[:-3]
        self.image = self.font.render(msg, 0, self.color)
