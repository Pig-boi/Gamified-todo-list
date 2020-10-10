import pygame

import random

class Drop:

    def __init__(self, x = 0, y = 0, size = 0, decay_start = 1000, size_limit = 1, color = (255, 255, 255), border_width = 0, x_vel = None, y_vel = None, fall_vel = None, decay_speed = 0.1):
        self.x = x
        self.y = y
        self.size = size
        self.decay_start = decay_start
        self.size_limit = size_limit
        self.color = color
        self.border_width = border_width
        self.decay_speed = decay_speed

        self.start_time = pygame.time.get_ticks()

        if x_vel is None:
           self.x_vel = random.randint(-1, 1)
        else:
           self.x_vel = x_vel
        if y_vel is None:
           self.y_vel = random.randint(-1, 1)
        else:
           self.y_vel = y_vel
        if fall_vel is None:
           self.fall_vel = random.uniform(0.1, 2)
        else:
            self.fall_vel = fall_vel

        self.particles = [] # Remove this later


