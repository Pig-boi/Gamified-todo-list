import pygame

def load_sprite(sprite_dir, colorkey, alpha = None):
    sprite = pygame.image.load(sprite_dir)
    sprite.set_colorkey(colorkey)
    sprite.set_alpha(alpha)

    return sprite
