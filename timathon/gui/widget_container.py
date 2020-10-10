import pygame

from collections import UserList

class WidgetContainer(UserList):

    def update(self):
        mouse_pos = pygame.mouse.get_pos()
        mouse_click = pygame.mouse.get_pressed()
        for widget in self:
            widget.update()

    def draw(self, surface):
        for widget in self:
            widget.draw(surface)

class ButtonContainer(WidgetContainer):
    def fg_hover_change(self, hover_fg):
        mouse_pos = pygame.mouse.get_pos()
        for button in self:
            if button.rect.collidepoint(mouse_pos):
                button.fg = hover_fg
            else:
                button.fg = button.original_fg

    def font_size_hover_change(self, hover_size, font = 'consolas'):
        mouse_pos = pygame.mouse.get_pos()
        for button in self:
            if button.rect.collidepoint(mouse_pos):
                button.font = pygame.font.SysFont(font, hover_size)
            else:
                button.font = button.original_font
