import os.path
import pygame

from colors import black

main_dir = os.path.split(os.path.abspath(__file__))[0]


class DummySound:
    def play(self): pass


def load_image(file):
    color_key = (255, 0, 255)
    file = os.path.join(main_dir, 'data', file)
    try:
        surface = pygame.image.load(file)
        if surface.get_alpha():
            surface = surface.convert_alpha()
        else:
            surface = surface.convert()
            surface.set_colorkey(color_key)
    except pygame.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pygame.get_error()))
    return surface


def load_images(*files):
    images = []
    for file in files:
        images.append(load_image(file))
    return images


def load_all_gfx(directory, colorkey=(255, 0, 255), accept=(".png", ".jpg", ".bmp")):
    """Load all graphics with extensions in the accept argument.  If alpha
    transparency is found in the image the image will be converted using
    convert_alpha().  If no alpha transparency is detected image will be
    converted using convert() and colorkey will be set to colorkey."""
    graphics = {}
    for pic in os.listdir(directory):
        name, ext = os.path.splitext(pic)
        if ext.lower() in accept:
            img = pygame.image.load(os.path.join(directory, pic))
            if img.get_alpha():
                img = img.convert_alpha()
            else:
                img = img.convert()
                img.set_colorkey(colorkey)
            graphics[name] = img
    return graphics


def load_sound(file):
    if not pygame.mixer:
        return DummySound()
    file = os.path.join(main_dir, 'data', file)
    try:
        sound = pygame.mixer.Sound(file)
        return sound
    except pygame.error:
        print('Warning, unable to load, %s' % file)
    return DummySound()


def load_music(file):
    if not pygame.mixer:
        return DummySound()
    file = os.path.join(main_dir, 'data', file)
    try:
        pygame.mixer.music.load(file)
    except pygame.error:
        print('Warning, unable to load, %s' % file)


def text_objects(text, font):
    text_surface = font.render(text, True, black)
    return text_surface, text_surface.get_rect()

"""
        screen.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("A bit Racey", largeText)
        TextRect.center = ((DISPLAY_WIDTH / 2), (DISPLAY_HEIGHT / 2))
        screen.blit(TextSurf, TextRect)
        pygame.display.update()
        clock.tick(15)
"""
