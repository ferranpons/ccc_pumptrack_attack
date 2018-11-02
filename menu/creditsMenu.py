import pygame

import colors
from fileUtils import load_image
from textUtils import text_format, MENU_FONT

background_file = 'background_title.png'
menu_line_file = 'menu_line.png'
clock = pygame.time.Clock()

TITLE_TEXT = "CREDITS"


def credits_menu(screen, menu_logos):
    in_credits_menu = True

    # Load
    background_image = load_image(background_file)

    while in_credits_menu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or \
                    (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                return

        # Draw Background
        background_rect = background_image.get_rect()
        background_rect.left, background_rect.top = [0, 0]
        screen.fill([255, 255, 255])
        screen.blit(background_image, background_rect)

        # Draw Logos
        menu_logos.draw(screen)

        title = text_format(TITLE_TEXT, MENU_FONT, 50, colors.white)
        screen.blit(title, (150, 220))

        developed_by = text_format("DEVELOPED BY FERRAN PONS", MENU_FONT, 25, colors.white)
        screen.blit(developed_by, (150, 370))

        pygame.display.update()
        clock.tick(30)
