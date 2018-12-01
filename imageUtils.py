import pygame

from colors import black


def blit_alpha(target, source, location, opacity):
    x = location[0]
    y = location[1]
    temp = pygame.Surface((source.get_width(), source.get_height())).convert()
    temp.blit(target, (-x, -y))
    temp.blit(source, (0, 0))
    temp.set_alpha(opacity)
    target.blit(temp, location)


def fade_in(target, image, image_rect):
    for alpha in range(255):
        target.fill(black)
        blit_alpha(target, image, image_rect, alpha)
        pygame.display.update(image_rect)


def fade_out(target, image, image_rect):
    for alpha in range(254, 0, -1):
        target.fill(black)
        blit_alpha(target, image, image_rect, alpha)
        pygame.display.update(image_rect)
