import pygame

class Shockwave:

    def __init__(self, x, y, size = 0, decay_start = 1000, size_limit = 100, color = (255, 255, 255), border_width = 6, inflate_speed = 1, decay_speed = 0.1):
        self.x = x
        self.y = y
        self.size = size
        self.decay_start = decay_start
        self.size_limit = size_limit
        self.color = color
        self.border_width = border_width
        self.inflate_speed = inflate_speed
        self.decay_speed = decay_speed

        self.start_time = pygame.time.get_ticks()

    def update(self, container, delta_time = 1):
        self.size += self.inflate_speed * delta_time
        if self.border_width < 1 or self.size >= self.size_limit:
            container.remove(self)
        if pygame.time.get_ticks() - self.start_time > self.decay_start:
            self.border_width -= self.decay_speed * delta_time

    def circle_surf(self, radius, color):
        surf = pygame.Surface((radius * 2, radius * 2))
        pygame.draw.circle(surf, color, (radius, radius), radius)

        return surf

    def draw(self, surface, camera = [0, 0]):
        pygame.draw.circle(surface, self.color, (self.x - camera[0], self.y - camera[1]), self.size, int(self.border_width))

    def draw_with_light(self, surface, camera):
        for self in self.particles:
            pygame.draw.circle(surface, self.color, (self.x - camera[0], self.y - camera[1]), self.size, int(self.border_width))

            radius = self.size 

            surface.blit(self.circle_surf(radius, (0, 0, 100)), (self.x - camera[0] - radius, self.y - camera[1] - radius), special_flags = pygame.BLEND_RGB_ADD)
