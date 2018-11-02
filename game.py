#!/usr/bin/env python

import pygame
from pygame.locals import *
import fileUtils
from colors import black
from menu.mainMenu import main_menu
from titleScreen import title_screen

if not pygame.image.get_extended():
    raise SystemExit("Sorry, extended image module required")

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720

screen_rect = Rect(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT)
clock = pygame.time.Clock()


def splash_intro(screen):
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.fill(black)

        splash_fps = fileUtils.load_image("fps_logo.png")
        splash_fps_rect = splash_fps.get_rect()
        splash_fps_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)

        splash_pygame = fileUtils.load_image("pygame-badge-SMA.png")
        splash_pygame_rect = splash_pygame.get_rect()
        splash_pygame_rect.center = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)

        screen.blit(splash_fps, splash_fps_rect)
        pygame.display.flip()

        pygame.time.wait(3000)

        screen.blit(splash_pygame, splash_pygame_rect)
        pygame.display.flip()

        pygame.time.wait(3000)

        intro = False


def main(window_style=0):
    pygame.init()
    if pygame.mixer and not pygame.mixer.get_init():
        print('Warning, no sound')
        pygame.mixer = None

    window_style = 0  # |FULLSCREEN
    best_depth = pygame.display.mode_ok(screen_rect.size, window_style, 32)
    screen = pygame.display.set_mode(screen_rect.size, window_style, best_depth)
    pygame.display.set_caption("Chainbreakers' Pumtrack Attack")

    splash_intro(screen)
    title_screen(screen, screen_rect)
    main_menu(screen, screen_rect)

    if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)
    pygame.quit()


if __name__ == '__main__':
    main()
