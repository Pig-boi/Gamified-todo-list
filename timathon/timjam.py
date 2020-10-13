import pygame

pygame.init()

import sys
import random

from character import Character

from vfx import CircleDrop, ParticleContainer
from gui import Button, ButtonContainer
from utils import load_sprite
from menus.todo_menu import TodoMenu

class MainWindow:
    
    def __init__(self):
        self.window_size = (1000, 700)
        self.window = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)
        self.todo_menu = TodoMenu(self)

        self.font = pygame.font.SysFont('consolas', 40)
        
        self.characters = { # Add player buttons
            'dave': Character(50, 10, 950, 1, exp_color = (0, 0, 255), sprites = [
                pygame.transform.scale(load_sprite('characters\\dave\\1.png', (255, 255, 255)), (500, 500)),
                pygame.transform.scale(load_sprite('characters\\dave\\2.png', (255, 255, 255)), (500, 500)),
                pygame.transform.scale(load_sprite('characters\\dave\\3.png', (255, 255, 255)), (500, 500)),
                pygame.transform.scale(load_sprite('characters\\dave\\4.png', (255, 255, 255)), (500, 500))
            ])
        }
        
        self.current_character = self.characters['dave']

        self.buttons = ButtonContainer([
                Button(10, 10, text = 'Todo menu', command = self.todo_menu.main, font = pygame.font.SysFont('consolas', 20), fg = (255, 255, 255),
                       show_box = False),
        ])

        self.particles = ParticleContainer()

        self.last_time = pygame.time.get_ticks()

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            elif event.type == pygame.VIDEORESIZE:
                self.window_size = (event.w, event.h)
                self.window = pygame.display.set_mode(self.window_size, pygame.RESIZABLE)

            elif event.type == pygame.KEYDOWN: 
                self.current_character.exp += 10

    def draw(self):
        self.window.fill((10, 10, 20))

        self.buttons.draw(self.window)
        self.particles.draw(self.window)
        
        self.window.blit(self.current_character.current_sprite, (self.window_size[0] / 2 - self.current_character.current_sprite.get_rect().width / 2,
                                                                 self.window_size[1] / 2 - self.current_character.current_sprite.get_rect().height / 2))
        self.window.blit(self.font.render(str(self.current_character.level), True, (255, 255, 255)), (self.window_size[0] / 2 - self.current_character.current_sprite.get_rect().width / 2 + 20,
                                                    self.window_size[1] / 2
                                                    - self.current_character.current_sprite.get_rect().height / 2))

        pygame.draw.rect(self.window, self.current_character.exp_color, (self.window_size[0] / 2 - self.current_character.current_sprite.get_rect().width / 2,
                                                    self.window_size[1] / 2 + self.current_character.current_sprite.get_rect().height / 2,
                                                    self.current_character.exp / 2, 50)) 
        
        pygame.display.update()
        
    def main(self):
        while True:
            self.event_loop()

            self.delta_time = pygame.time.get_ticks() - self.last_time
            self.delta_time /= 1000
            self.delta_time *= 60
            self.last_time = pygame.time.get_ticks()

            self.current_character.handle_level_up()

            if self.current_character.prev_level < self.current_character.level:
                if self.current_character.level % 5 == 0:
                    particle_num = 130
                    size_range = (1, 30)
                else:
                    particle_num = 60
                    size_range = (1, 20)
                    
                for _ in range(particle_num): 
                    self.particles.append(CircleDrop(self.window_size[0] / 2, self.window_size[1] / 2,
                                             random.randint(size_range[0], size_range[1]), fall_vel = random.uniform(-0.3, 0.3), color = random.choice([(200, 0, 0),
                                             (200, 0, 0), (200, 200, 0), (255, 183, 0)]), light = True, light_color = (50, 0, 0), decay_start = 1000, x_vel = random.randint(-10, 10),
                                             y_vel = random.randint(-5, 5)))

                self.current_character.prev_level = self.current_character.level
            
            self.particles.update(self.delta_time)
            self.buttons.update()

            self.draw()

main_window = MainWindow()
main_window.main()





