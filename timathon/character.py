import pygame

class Character:

    def __init__(self, hp, exp, exp_limit, level, sprites, exp_color):
        self.hp = hp
        self.exp = exp
        self.exp_limit = exp_limit
        self.level = level
        self.prev_level = level
        self.sprite_count = 0
        self.sprites = sprites
        self.current_sprite = sprites[self.sprite_count]
        self.exp_color = exp_color
        
    def handle_level_up(self):
        if self.exp >= self.exp_limit:
            self.prev_level = self.level
            self.level += 1
##            self.exp_limit += self.exp 
            self.exp = 0
            try:
                self.sprite_count += 1
                self.current_sprite = self.sprites[self.sprite_count]
            except IndexError:
                pass

    

