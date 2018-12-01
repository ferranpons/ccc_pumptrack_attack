import pygame

MENU_FONT = 'data\\freesansbold.ttf'


def text_format(message, text_font, text_size, text_color):
    new_font = pygame.font.Font(text_font, text_size)
    new_text = new_font.render(message, True, text_color)

    return new_text
