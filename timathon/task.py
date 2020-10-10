import pygame

from gui import Button

class Task:

    def __init__(self, x, y, text, button_container, font, character, reward, main_window):
        self.x = x
        self.y = y
        self.text = text
        self.character = character
        self.reward = reward
        self.main_window = main_window
        
        self.button = Button(x, y, font.size(self.text)[0], text = self.text, font = font, fg = (255, 255, 255), show_box = False,
                             command = self.select)
        
        button_container.append(self.button)

    def abandon(self):
        pass

    def complete(self):
        self.character.exp += self.reward
        self.main_window.main()
