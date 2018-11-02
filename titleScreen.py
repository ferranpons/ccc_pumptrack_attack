import pygame

import colors
from fileUtils import load_music, load_image
from textUtils import text_format, MENU_FONT

background_file = 'background_title.png'
main_theme = 'A_A_Aalto_-_Admin.mp3'
clock = pygame.time.Clock()


def title_screen(screen, screen_rect):
    in_title_screen = True

    # Load
    background_image = load_image(background_file)

    # Main Theme
    load_music(main_theme)
    pygame.mixer.music.play(-1)

    while in_title_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                return

        # Draw Background
        background_rect = background_image.get_rect()
        background_rect.left, background_rect.top = [0, 0]
        screen.fill([255, 255, 255])
        screen.blit(background_image, background_rect)

        press_any_key = text_format("Press any key to continue", MENU_FONT, 18, colors.white)
        press_any_key_rect = press_any_key.get_rect()
        press_any_key_rect.center = (screen_rect.size[0] / 2, 500)
        screen.blit(press_any_key, press_any_key_rect)

        pygame.display.update()
        clock.tick(30)
