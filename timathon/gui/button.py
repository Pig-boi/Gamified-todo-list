import pygame

class Button:

    def __init__(self, x, y, width = 100, height = 50, fg = (0, 0, 0),
            bg = (255, 255, 255), font = pygame.font.SysFont('consolas', 50),
            text = '', light = False, light_color = (20, 20, 20),
            show_box = True, command = None):

        self.rect = pygame.Rect(x, y, width, height)
        self.fg = fg
        self.bg = bg
        self.font = font
        self.text = text
        self.light = light
        self.light_color = light_color
        self.show_box = show_box
        self.command = command

        self.original_fg = fg
        self.original_font = font

        self.clicked = False

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        if self.rect.collidepoint(mouse_pos) and mouse_click[0] and not self.clicked:
            self.clicked = True
            if self.command is not None:
                return self.command()
        elif not mouse_click[0]:
            self.clicked = False

    def draw(self, surface, camera = [0, 0]):
        if self.show_box:
            pygame.draw.rect(surface, self.bg, (self.rect.x - camera[0], self.rect.y - camera[1],
                            self.rect.width, self.rect.height))
        
        surface.blit(self.font.render(self.text, 1, self.fg), (self.rect.x - camera[0],
            self.rect.y - camera[1]))           
