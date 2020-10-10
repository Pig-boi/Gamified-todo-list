import pygame

import sys
import tkinter as tk

from gui import Button, ButtonContainer
from task import Task

class TodoMenu:

    def __init__(self, parent):
        self.parent = parent

        button_font = pygame.font.SysFont('consolas', 20)
        self.font = pygame.font.SysFont('consolas', 25)

        self.task_coor = [10, 90]
        self.task_id = 0
        self.tasks = ButtonContainer()
        self.selected_tasks = []
        
        self.buttons = ButtonContainer([
                    Button(self.parent.window_size[0] - button_font.size('Back')[0],
                           10, text = 'Back', fg = (255, 0, 0), font = button_font,
                           show_box = False, command = self.parent.main),
                    Button(10, 40, 120, 20, text = 'Add a task', font = button_font, 
                           show_box = False, fg = (255, 255, 255), command = self.input_task)
            ])

    def input_task(self):
        root = tk.Tk() # Change this to your own text widget
        root.title('Enter your task')

        text_area = tk.Entry(root, font = ('consolas', 15))
        text_area.pack()
        submit = tk.Button(root, text = 'Enter',  
                           command = lambda: self.add_task(text_area.get(), root))
        submit.pack(fill = 'both', expand = True)
        
        root.mainloop()

    def add_task(self, text, input_window = None):
        if input_window is not None:
            input_window.destroy()
        if text.strip() != '' :
            self.tasks.append({
                        'button': Button(self.task_coor[0], self.task_coor[1], self.font.size(text)[0], self.font.size(text)[1], text = text,
                                       font = self.font, show_box = False, fg = (255, 255, 255)),
                        'id': self.task_id

            })
    
            self.task_coor[1] += 40
            self.task_id += 1

    def select_task(self, task_id):
        if self.tasks[task_id]['button'].fg == (0, 0, 255):
            self.tasks[task_id]['button'].fg = (255, 255, 255)
            self.selected_tasks.remove(self.tasks[task_id])
        else:
            self.tasks[task_id]['button'].fg = (0, 0, 255)

            if self.tasks[task_id] not in self.selected_tasks:
                self.selected_tasks.append(self.tasks[task_id])

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def draw(self):
        self.parent.window.fill((10, 10, 20))
        
        self.buttons.draw(self.parent.window)

        for task in self.tasks:
            task['button'].draw(self.parent.window)
        
        pygame.display.update()
    
    def main(self):
        while True:
            self.event_loop()

            self.buttons.update()

            for task in self.tasks:
                task['button'].update()

            for task in self.tasks:
                task['button'].command = lambda: self.select_task(task['id'])
                
            self.draw()
