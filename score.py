#!/usr/bin/env python

import pygame


class Score(pygame.sprite.Sprite):

    def __init__(self, score):
        self.score = score
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.Font(None, 20)
        self.font.set_italic(1)
        self.color = pygame.Color('white')
        self.lastscore = -1
        self.update()
        self.rect = self.image.get_rect().move(10, 450)

    def update(self):
        if self.score != self.lastscore:
            self.lastscore = self.score
            msg = "Score: %d" % self.score
            self.image = self.font.render(msg, 0, self.color)
