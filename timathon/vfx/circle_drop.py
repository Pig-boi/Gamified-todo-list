import pygame

from .drop import Drop

class CircleDrop(Drop): 
            
    def __init__(self, x, y, size = 5, decay_start = 1000, size_limit = 1, color = (255, 255, 255), border_width = 0, x_vel = None, y_vel = None, fall_vel = None,
                 light_color = (20, 20, 20), decay_speed = 0.2, light = False, outline = False, outline_color = (0, 0, 0), outline_width = 2):
        Drop.__init__(self, x, y, size, decay_start, size_limit, color, border_width, x_vel, y_vel, fall_vel, decay_speed)
        self.light_color = light_color
        self.outline = outline
        self.outline_color = outline_color
        self.light = light
        self.outline_width = outline_width
        
    def update(self, container, delta_time = 1):
        self.x -= self.x_vel * delta_time
        self.y -= self.y_vel * delta_time
        self.y_vel -= self.fall_vel * delta_time

        if pygame.time.get_ticks() - self.start_time > self.decay_start:
            self.size -= self.decay_speed * delta_time

        if self.size < self.size_limit:
            container.remove(self)

    def circle_surf(self, radius, color):
        surf = pygame.Surface((radius * 2, radius * 2))
        pygame.draw.circle(surf, color, (radius, radius), radius)
            
        return surf
            
    def draw(self, surface, camera = [0, 0]): 
        pygame.draw.circle(surface, self.color, (self.x - camera[0], self.y - camera[1]), self.size, self.border_width)

        if self.light:
            radius = self.size * 2
            surface.blit(self.circle_surf(radius, self.light_color), (self.x - camera[0] - radius, self.y - camera[1] - radius), special_flags = pygame.BLEND_RGB_ADD)

        if self.outline:
            pygame.draw.circle(surface, self.outline_color, (self.x - camera[0], self.y - camera[1]), self.size, self.outline_width)









