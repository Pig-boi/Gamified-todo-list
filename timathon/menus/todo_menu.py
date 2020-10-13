import pygame

import sys
import random
import tkinter as tk

from vfx import CircleDrop, ParticleContainer
from gui import Button, ButtonContainer

class TodoMenu:

    def __init__(self, parent):
        self.parent = parent

        self.last_time = pygame.time.get_ticks()

        self.button_font = pygame.font.SysFont('consolas', 20)
        self.font = pygame.font.SysFont('consolas', 25)

        self.tasks = ButtonContainer()
        self.selected_tasks = []
        self.task_start_y = 100
        
        self.buttons = ButtonContainer([
                    Button(self.parent.window_size[0] - self.button_font.size('Back')[0], # Make these buttons position themselves when resizing 
                           10, text = 'Back', fg = (255, 0, 0), font = self.button_font,
                           show_box = False, command = self.parent.main),
                    Button(10, 40, 120, 20, text = 'Add a task', font = self.button_font, 
                           show_box = False, fg = (255, 255, 255), command = self.input_task),
                    Button(10, self.parent.window_size[1] - self.button_font.size('Complete')[1], self.button_font.size('Complete')[0], 
                           self.button_font.size('Complete')[1], text = 'Complete', font = self.button_font,
                           show_box = False, fg = (255, 255, 255), command = self.complete_tasks),
                    Button(self.button_font.size('Complete')[0] + 30, self.parent.window_size[1] - self.button_font.size('Complete')[1], self.button_font.size('Abandon')[0], 
                           self.button_font.size('Abandon')[1], text = 'Abandon', font = self.button_font,
                           show_box = False, fg = (255, 255, 255), command = self.abandon_task)
            ])

        self.particles = ParticleContainer()

    def input_task(self):
        root = tk.Tk() # Change this to your own text widget. Or atleast center the window
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
        if text.strip() != '':
            self.tasks.append({
                        'button': Button(10, 0, self.font.size(text)[0], self.font.size(text)[1], text = text,
                                       font = self.font, bg = (10, 10, 20), fg = (255, 255, 255)),
                        'id': None

            })

    def select_task(self, task_id):
        if self.tasks[task_id]['button'].fg == (0, 0, 255):
            self.tasks[task_id]['button'].fg = (255, 255, 255)
            self.tasks[task_id]['button'].bg = (10, 10, 20)
            self.selected_tasks.remove(self.tasks[task_id])
        else:
            self.tasks[task_id]['button'].bg = (10, 30, 10)
            self.tasks[task_id]['button'].fg = (0, 0, 255)

            if self.tasks[task_id] not in self.selected_tasks:
                self.selected_tasks.append(self.tasks[task_id])

    def complete_tasks(self): # Clean the code | Make the player see the level up particles
        for task in self.selected_tasks:
            self.parent.current_character.exp += 150 # Make it add the experience points when the player hits 'back'
            
            for _ in range(15):
                self.particles.append(CircleDrop(task['button'].rect.x + task['button'].font.size(task['button'].text)[0] / 2, task['button'].rect.y, 
                                                 random.randint(1, 20), fall_vel = random.uniform(-0.2, 0.2), decay_start = 0, light = True,
                                                 x_vel = random.randint(-3, 3), color = self.parent.current_character.exp_color))
            try:
                self.tasks.remove(task)
            except ValueError:
                pass
            
        for task in self.selected_tasks:
            self.selected_tasks.remove(task)    
            
    def abandon_task(self):

        for task in self.selected_tasks:
            for _ in range(15):
                self.particles.append(CircleDrop(task['button'].rect.x + task['button'].font.size(task['button'].text)[0] / 2, task['button'].rect.y, 
                                             random.randint(1, 20), fall_vel = random.uniform(-0.2, 0.2), decay_start = 0, light = True,
                                             x_vel = random.randint(-3, 3), color = (255, 0, 0), light_color = (50, 0, 0)))
        
            self.tasks.remove(task)
            
        for task in self.selected_tasks:
            self.selected_tasks.remove(task)
                
    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.VIDEORESIZE:
                self.parent.window_size = (event.w, event.h)
                self.parent.window = pygame.display.set_mode(self.parent.window_size, pygame.RESIZABLE)
                
                self.buttons = ButtonContainer([
                            Button(self.parent.window_size[0] - self.button_font.size('Back')[0], 
                                   10, text = 'Back', fg = (255, 0, 0), font = self.button_font,
                                   show_box = False, command = self.parent.main),
                            Button(10, 40, 120, 20, text = 'Add a task', font = self.button_font, 
                                   show_box = False, fg = (255, 255, 255), command = self.input_task),
                            Button(10, self.parent.window_size[1] - self.button_font.size('Complete')[1], self.button_font.size('Complete')[0], 
                                   self.button_font.size('Complete')[1], text = 'Complete', font = self.button_font,
                                   show_box = False, fg = (255, 255, 255), command = self.complete_tasks),
                            Button(self.button_font.size('Complete')[0] + 30, self.parent.window_size[1] - self.button_font.size('Complete')[1], self.button_font.size('Abandon')[0], 
                                   self.button_font.size('Abandon')[1], text = 'Abandon', font = self.button_font,
                                   show_box = False, fg = (255, 255, 255), command = lambda: print('continue this | abandon button'))
                    ])

    def draw(self):
        self.parent.window.fill((10, 10, 20))
        
        self.buttons.draw(self.parent.window)
        self.particles.draw(self.parent.window)

        for task in self.tasks:
            task['button'].draw(self.parent.window)
        
        pygame.display.update()
    
    def main(self):
        while True:
            self.event_loop()

            self.delta_time = pygame.time.get_ticks() - self.last_time
            self.delta_time /= 1000
            self.delta_time *= 60
            self.last_time = pygame.time.get_ticks()

            self.buttons.update()
            self.particles.update(self.delta_time)

            for task in self.tasks:
                task['button'].update()

            for task in self.tasks:
                task['button'].command = lambda: self.select_task(task['id'])
                task['button'].rect.y = self.tasks.index(task) * 40 + self.task_start_y
                task['id'] = self.tasks.index(task) 
                
            self.draw()
    
