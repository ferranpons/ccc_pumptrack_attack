import pygame

from fileUtils import load_image


class MenuLogos:
    logo_one = None
    logo_two = None

    def __init__(self):
        pass

    def load(self):
        if self.logo_one is None:
            self.logo_one = load_image('fps_logo.png')
        if self.logo_two is None:
            self.logo_two = load_image('ccc_logo.png')

    def draw(self, screen):
        screen_rect = screen.get_rect()
        self.logo_one = pygame.transform.smoothscale(self.logo_one, (350, 200))
        logo_one_rect = self.logo_one.get_rect()
        screen.blit(self.logo_one, (screen_rect.size[0] - (logo_one_rect[2] / 2) - 400, 500))
        self.logo_two = pygame.transform.smoothscale(self.logo_two, (100, 100))
        logo_two_rect = self.logo_two.get_rect()
        screen.blit(self.logo_two, (screen_rect.size[0] - (logo_two_rect[2] / 2) - 200, 500))
