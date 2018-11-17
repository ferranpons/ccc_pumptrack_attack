#!/usr/bin/env python

import pygame
from pygame.rect import Rect


class Player(pygame.sprite.Sprite):
    speed = 10
    bounce = 24
    gun_offset = -11
    screen_rect = Rect(0, 0, 1280, 768)
    lap = 0

    def __init__(self, new_rect, way_points, loop=False):
        self.screen_rect = new_rect
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[0]
        self.rect = self.image.get_rect(midbottom=self.screen_rect.midbottom)
        self.reloading = 0
        self.origtop = self.rect.top
        self.facing = -1

        self.loop = loop

        self.speed = 0

        self.way_points = way_points
        self.next_point = 0

        # set current position
        # I use Vector2 because it keeps position as float numbers
        # and it makes calcuations easier and more precise
        self.current = pygame.math.Vector2(self.way_points[0])

        # set position in rect to draw it
        self.rect.center = self.current

        # set end point if exists on list
        self.target_index = 1
        if self.target_index < len(self.way_points) - 1:
            self.target = pygame.math.Vector2(self.way_points[self.target_index])
            self.moving = True
        else:
            self.target = self.current
            self.moving = False

    def move(self):
        '''
        if direction:
            self.facing = direction
        self.rect.move_ip(direction * self.speed, 0)
        self.rect = self.rect.clamp(self.screen_rect)
        if direction < 0:
            self.image = self.images[0]
        elif direction > 0:
            self.image = self.images[1]
        self.rect.top = self.origtop - (self.rect.left // self.bounce % 2)
        '''
        if self.moving:
            self.speed = 10

            # get distance to taget
            distance = self.current.distance_to(self.target)

            #
            if distance > self.speed:
                self.current = self.current + (self.target - self.current).normalize() * self.speed
                self.rect.center = self.current
            else:
                # put player in tagert place,
                # and find new target on list with waypoints

                self.current = self.target
                self.rect.center = self.current

                # set next end point if exists on list
                self.target_index += 1
                if self.target_index < len(self.way_points):
                    self.target = pygame.math.Vector2(self.way_points[self.target_index])
                else:
                    if self.loop:
                        self.lap += 1
                        self.target_index = 0
                    else:
                        self.moving = False

            self.speed = 0
