import pygame

from .drop import Drop

class RectDrop(Drop):

    def update(self, container, delta_time = 1):
        self.x -= self.x_vel * delta_time
        self.y -= self.y_vel * delta_time
        self.y_vel -= self.fall_vel * delta_time

        if pygame.time.get_ticks() - self.start_time > self.decay_start:
            self.size -= self.decay_speed * delta_time
            self.size -= self.decay_speed * delta_time

        if self.size < self.size_limit or self.size < self.size_limit:
            container.remove(self)

    def draw(self, surface, camera = [0, 0]):
        pygame.draw.rect(surface, self.color, (self.x - camera[0], self.y - camera[1], self.size, self.size), self.border_width)
            
