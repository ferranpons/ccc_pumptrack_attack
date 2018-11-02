#!/usr/bin/env python

import pygame
import random
from pygame.rect import Rect


class Rider(pygame.sprite.Sprite):
    speed = 13
    animcycle = 12
    images = []
    screen_rect = Rect(0, 0, 1280, 768)

    def __init__(self, new_rect):
        self.screen_rect = new_rect
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
        self.facing = random.choice((-1, 1)) * Rider.speed
        self.frame = 0
        if self.facing < 0:
            self.rect.right = self.screen_rect.right

    def update(self):
        self.rect.move_ip(self.facing, 0)
        if not self.screen_rect.contains(self.rect):
            self.facing = -self.facing
            self.rect.top = self.rect.bottom + 1
            self.rect = self.rect.clamp(self.screen_rect)
        self.frame = self.frame + 1
        self.image = self.images[self.frame // self.animcycle % 3]

