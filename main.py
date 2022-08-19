from textwrap import fill
from tkinter import *
import customtkinter
import random
import pyglet
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\mastermind')
customtkinter.set_appearance_mode('light')
customtkinter.set_default_color_theme('blue')
pyglet.font.add_file('fonts\\Pacifico.ttf')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        x = int(self.winfo_screenwidth() // 2.5)
        y = int(self.winfo_screenheight() * 0.2)
        x, y = str(x), str(y)
        self.geometry(f'450x580+{x}+{y}')
        self.title('MasterMind')
        self.resizable(0, 0)
        
        self.accent_color1 = '#212325'
        self.accent_color2 = '#ededed'
        self.accent_color3 = '#3b65ad'
        self.accent_color4 = '#608bd5'
        self.accent_color5 = '#f878b6'
        self.accent_color6 = '#d6478d'
        self.accent_color7 = '#000000'
        self.accent_color8 = '#343638'
        self.accent_color9 = '#ffffff'
        self.accent_font_1 = ('TkMenuFont',18)
        self.accent_font_2 = ('TkMenuFont',8)
        
        self.random_colors_list = []
        self.input_colors_list = []
        self.unguessed_colors = 0
        self.guessed_colors = 0
        self.guessed_colors_and_positions = 0
        
        self.show_game()
        
    
    def hover(self, btn, colorfgOnHover, colorfgOnLeave):
        btn.bind("<Enter>", func = lambda i: btn.configure(text_color = colorfgOnHover))
        btn.bind("<Leave>", func = lambda i: btn.configure(text_color = colorfgOnLeave))
       
        
    def show_game(self):
        self.header_widget = customtkinter.CTkLabel(self, corner_radius = 15, text = '\nMastermind', text_font = self.accent_font_1)
        self.header_widget.place(x = -10, y = -30)
        self.header_widget.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color9,
            text_color = self.accent_color8,
            width = 380,
            height = 80
        )
        
        self.rules_btn = customtkinter.CTkButton(self, corner_radius = 15, text = '\n\nRules', text_font = self.accent_font_2)
        self.rules_btn.place(x = 380, y = -30)
        self.rules_btn.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color8,
            text_color = self.accent_color2,
            hover_color = self.accent_color1,
            width = 50,
            height = 80
        )
        self.hover(self.rules_btn, self.accent_color8, self.accent_color2)
        
        self.base_color_widget = customtkinter.CTkLabel(self, corner_radius = 15, text = '', text_font = self.accent_font_1)
        self.base_color_widget.place(x = 40, y = 80)
        self.base_color_widget.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color9,
            text_color = self.accent_color8,
            width = 50,
            height = 250
        )
        
        self.playground_widget = customtkinter.CTkLabel(self, corner_radius = 15, text = '', text_font = self.accent_font_1)
        self.playground_widget.place(x = 100, y = 80)
        self.playground_widget.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color9,
            text_color = self.accent_color8,
            width = 250,
            height = 430
        )
        
        self.result_widget = customtkinter.CTkLabel(self, corner_radius = 15, text = '', text_font = self.accent_font_1)
        self.result_widget.place(x = 360, y = 80)
        self.result_widget.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color9,
            text_color = self.accent_color8,
            width = 50,
            height = 430
        )
        
        self.play_btn = customtkinter.CTkButton(self, corner_radius = 15, text = '▷', text_font = self.accent_font_2)
        self.play_btn.place(x = 40, y = 340)
        self.reset_btn = customtkinter.CTkButton(self, corner_radius = 15, text = '↻', text_font = self.accent_font_2)
        self.reset_btn.place(x = 40, y = 400)
        self.quit_btn = customtkinter.CTkButton(self, corner_radius = 15, text = 'x', text_font = self.accent_font_2)
        self.quit_btn.place(x = 40, y = 460)
        self.quit_btn.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color5,
            text_color = self.accent_color2,
            hover_color = self.accent_color6,
            width = 50,
            height = 50
        )
        self.hover(self.quit_btn, self.accent_color8, self.accent_color2)
        
        for i in (self.play_btn,self.reset_btn):
            i.configure(
                bg_color = self.accent_color2,
                fg_color = self.accent_color9,
                text_color = self.accent_color8,
                hover_color = self.accent_color8,
                width = 50,
                height = 50
            )
            self.hover(i, self.accent_color2, self.accent_color8)
        
        
    def show_colors(self):
        self.colors_list = ['gold','lime','blue','magenta']
        print(self.colors_list)


    def get_random_colors_list(self):
        for i in self.colors_list:
            self.random_color = random.choice(self.colors_list)
            self.random_colors_list.append(self.random_color)


    def get_input_colors(self):
        self.input_colors_list = []
        for i in range(0, len(self.colors_list)):
            taken = False
            while taken == False:
                self.input_color = input(f'Enter a color {i+1}: ').lower()
                if self.input_color not in self.colors_list:
                    print('Incorrect color! Try again.')
                    taken = False
                else:
                    self.input_colors_list.append(self.input_color)
                    taken = True
        print(self.input_colors_list)           


    def get_unguessed_colors(self):
        self.unguessed_colors = 0
        for i in self.input_colors_list:
            if i not in self.random_colors_list:
                self.unguessed_colors += 1
        print(f'Unguessed colors: {self.unguessed_colors}')
                
    
    def guess(self):
        self.guessed_colors = 0
        self.guessed_colors_and_positions = 0
        for i in range(0, len(self.input_colors_list)):
            self.tmp_colors_list = [*self.random_colors_list]
            del self.tmp_colors_list[i]
            if self.input_colors_list[i] == self.random_colors_list[i]:
                self.guessed_colors_and_positions += 1
            elif self.input_colors_list[i] != self.random_colors_list[i] and self.input_colors_list[i] in self.tmp_colors_list:
                self.guessed_colors_and_positions += 0
                self.guessed_colors += 1
        print(f'Guessed colors and positions: {self.guessed_colors_and_positions}')
        print(f'Guessed colors and unguessed positions: {self.guessed_colors}')
                
        
    def main(self):
        self.count = 1
        self.show_colors()
        self.get_random_colors_list()
        
        while self.guessed_colors_and_positions != 4:
            self.get_input_colors()
            self.get_unguessed_colors()
            self.guess()
            self.count += 1
        print(f'It took {self.count} attempts.')
        

class GradientFrame(Canvas):
    def __init__(self, parent, color1, color2, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self._color1 = color1
        self._color2 = color2
        self.bind("<Configure>", self._draw_gradient)

    def _draw_gradient(self, event = None):
        width = self.winfo_width()
        height = self.winfo_height()
        limit = width
        (r1,g1,b1) = self.winfo_rgb(self._color1)
        (r2,g2,b2) = self.winfo_rgb(self._color2)
        r_ratio = float(r2-r1) / limit
        g_ratio = float(g2-g1) / limit
        b_ratio = float(b2-b1) / limit

        for i in range(limit):
            nr = int(r1 + (r_ratio * i))
            ng = int(g1 + (g_ratio * i))
            nb = int(b1 + (b_ratio * i))
            color = "#%4.4x%4.4x%4.4x" % (nr,ng,nb)
            self.create_line(i,0,i,height, tags = ("gradient",), fill = color)


if __name__ == "__main__":
    App().mainloop()