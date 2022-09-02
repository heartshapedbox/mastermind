from multiprocessing.resource_sharer import stop
from multiprocessing.sharedctypes import Value
from tkinter import *
from threading import Timer
from time import sleep
import time
import tkinter
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
        self.geometry(f'450x620+{x}+{y}')
        self.title('Mastermind')
        self.resizable(0, 0)
        
        self.accent_color1 = '#212325'
        self.accent_color2 = '#ededed'
        self.accent_color3 = '#f878b6'
        self.accent_color4 = '#d6478d'
        self.accent_color5 = '#4d5154'
        self.accent_color6 = '#ffffff'
        self.accent_color7 = '#3b65ad'
        self.accent_color8 = '#608bd5'
        self.basic_color1 = 'gold'
        self.basic_color2 = 'lime'
        self.basic_color3 = 'blue'
        self.basic_color4 = 'red'
        self.basic_color5 = 'magenta'
        self.accent_font_1 = ('TkMenuFont',18)
        self.accent_font_2 = ('TkMenuFont',8)
        self.accent_font_3 = ('TkMenuFont',10)
        self.accent_font_4 = ('Pacifico',20)
        self.accent_font_5 = ('TkMenuFont',24)
        
        self.random_colors_list = []
        self.input_colors_list = []
        self.unguessed_colors = 0
        self.guessed_colors = 0
        self.guessed_colors_and_positions = 0
        self.show_base()
        
    
    def hover(self, btn, colorfgOnHover, colorfgOnLeave):
        btn.bind("<Enter>", func = lambda i: btn.configure(text_color = colorfgOnHover))
        btn.bind("<Leave>", func = lambda i: btn.configure(text_color = colorfgOnLeave))
       
        
    def show_base(self):
        self.header_widget = customtkinter.CTkLabel(self, corner_radius = 8, text = '      Mastermind', text_font = self.accent_font_4)
        self.header_widget.place(x = 10, y = 10)
        self.header_widget.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color6,
            text_color = self.accent_color4,
            width = 340,
            height = 60
        )
        
        self.rules_btn = customtkinter.CTkButton(self, corner_radius = 8, text = 'Rules', text_font = self.accent_font_2)
        self.rules_btn.place(x = 360, y = 10)
        self.rules_btn.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color5,
            text_color = self.accent_color2,
            hover_color = self.accent_color1,
            width = 80,
            height = 60
        )
        self.hover(self.rules_btn, self.accent_color5, self.accent_color2)
        
        self.random_colors_widget = customtkinter.CTkLabel(self, corner_radius = 8, text = '', text_font = self.accent_font_1)
        self.random_colors_widget.place(x = 100, y = 80)
        self.random_colors_widget.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color6,
            text_color = self.accent_color5,
            width = 250,
            height = 50
        )
        
        self.timer_widget = customtkinter.CTkLabel(self, corner_radius = 8, text = '00:00', text_font = self.accent_font_3)
        self.timer_widget.place(x = 10, y = 80)
        self.timer_widget.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color6,
            text_color = self.accent_color5,
            width = 80,
            height = 50
        )
        
        self.playground_widget = customtkinter.CTkLabel(self, corner_radius = 8, text = '', text_font = self.accent_font_1)
        self.playground_widget.place(x = 100, y = 140)
        self.playground_widget.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color6,
            text_color = self.accent_color5,
            width = 250,
            height = 470
        )
        
        self.result_widget = customtkinter.CTkLabel(self, corner_radius = 8, text = '', text_font = self.accent_font_1)
        self.result_widget.place(x = 10, y = 140)
        self.result_widget.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color6,
            text_color = self.accent_color5,
            width = 80,
            height = 470
        )
        
        self.base_color_1_btn = customtkinter.CTkButton(self, corner_radius = 8, text = '')
        self.base_color_1_btn.place(x = 360, y = 140)
        self.base_color_1_btn.configure(fg_color = self.basic_color1, hover_color = self.basic_color1)
        self.base_color_2_btn = customtkinter.CTkButton(self, corner_radius = 8, text = '')
        self.base_color_2_btn.place(x = 360, y = 200)
        self.base_color_2_btn.configure(fg_color = self.basic_color2, hover_color = self.basic_color2)
        self.base_color_3_btn = customtkinter.CTkButton(self, corner_radius = 8, text = '')
        self.base_color_3_btn.place(x = 360, y = 260)
        self.base_color_3_btn.configure(fg_color = self.basic_color3, hover_color = self.basic_color3)
        self.base_color_4_btn = customtkinter.CTkButton(self, corner_radius = 8, text = '')
        self.base_color_4_btn.place(x = 360, y = 320)
        self.base_color_4_btn.configure(fg_color = self.basic_color4, hover_color = self.basic_color4)
        self.base_color_5_btn = customtkinter.CTkButton(self, corner_radius = 8, text = '')
        self.base_color_5_btn.place(x = 360, y = 380)
        self.base_color_5_btn.configure(fg_color = self.basic_color5, hover_color = self.basic_color5)
        for i in (self.base_color_1_btn,self.base_color_2_btn,self.base_color_3_btn,self.base_color_4_btn,self.base_color_5_btn):
            i.configure(
                bg_color = self.accent_color2,
                width = 80,
                height = 50
            )
            self.hover(i, self.accent_color8, self.accent_color2)
        
        self.random_btn = customtkinter.CTkButton(self, corner_radius = 8, text = 'Random', text_font = self.accent_font_2, command = lambda:self.play())
        self.random_btn.place(x = 360, y = 80)
        self.reset_btn = customtkinter.CTkButton(self, corner_radius = 8, text = 'Reset', text_font = self.accent_font_2, command = lambda:self.reset())
        self.reset_btn.place(x = 360, y = 440)
        self.reset_btn.configure(state = tkinter.DISABLED)
        self.stats_btn = customtkinter.CTkButton(self, corner_radius = 8, text = 'Stats', text_font = self.accent_font_2, command = lambda:self.stats())
        self.stats_btn.place(x = 360, y = 500)
        self.quit_btn = customtkinter.CTkButton(self, corner_radius = 8, text = 'Quit', text_font = self.accent_font_2, command = lambda:quit())
        self.quit_btn.place(x = 360, y = 560)
        self.quit_btn.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color3,
            text_color = self.accent_color2,
            hover_color = self.accent_color4,
            width = 80,
            height = 50
        )
        self.hover(self.quit_btn, self.accent_color3, self.accent_color2)
        
        for i in (self.random_btn,self.reset_btn,self.stats_btn):
            i.configure(
                bg_color = self.accent_color2,
                fg_color = self.accent_color8,
                text_color = self.accent_color2,
                hover_color = self.accent_color7,
                width = 80,
                height = 50
            )
            self.hover(i, self.accent_color8, self.accent_color2)
        self.show_empty_dots()

    
    def timer(self):
        try:
            if self.reset_btn_pressed == True:
                return
        except ValueError:
            pass
        
        if self.min_count < 10 and self.sec_count < 10:
            self.timer_widget.configure(text = f'0{self.min_count}:0{self.sec_count}')
            self.after(1000, self.timer)

        elif self.min_count < 10 and self.sec_count >= 10 and self.sec_count != 60:
            self.timer_widget.configure(text = f'0{self.min_count}:{self.sec_count}')
            self.after(1000, self.timer)
            
        elif self.min_count < 10 and self.sec_count >= 10 and self.sec_count == 60:
            self.min_count += 1
            self.timer_widget.configure(text = f'0{self.min_count}:00')
            self.sec_count = 0
            self.after(1000, self.timer)
            
        elif self.min_count >= 10 and self.min_count < 60 and self.sec_count >= 10 and self.sec_count == 60:
            self.min_count += 1
            self.timer_widget.configure(text = f'{self.min_count}:00')
            self.sec_count = 0
            self.after(1000, self.timer)
        
        elif self.min_count >= 10 and self.min_count < 60 and self.sec_count < 10:
            self.timer_widget.configure(text = f'{self.min_count}:0{self.sec_count}')
            self.after(1000, self.timer)
            
        elif self.min_count >= 10 and self.min_count < 60 and self.sec_count >= 10 and self.sec_count != 60:
            self.timer_widget.configure(text = f'{self.min_count}:{self.sec_count}')
            self.after(1000, self.timer)
            
        elif self.min_count == 60:
            self.timer_widget.configure(text = 'Time is\nOver')
            return
        
        self.sec_count += 1
    
    
    def show_empty_dots(self):
        self.dots_0 = PhotoImage(file = 'assets\\dots_0.png').subsample(8)
        self.dots_1 = PhotoImage(file = 'assets\\dots_1.png').subsample(8)
        self.dots_2 = PhotoImage(file = 'assets\\dots_2.png').subsample(8)
        self.dots_3 = PhotoImage(file = 'assets\\dots_3.png').subsample(8)
        self.dots_4 = PhotoImage(file = 'assets\\dots_4.png').subsample(8)
        self.dots_5 = PhotoImage(file = 'assets\\dots_5.png').subsample(8)
        self.dots_6 = PhotoImage(file = 'assets\\dots_6.png').subsample(8)
        self.dots_7 = PhotoImage(file = 'assets\\dots_7.png').subsample(8)
        self.dots_8 = PhotoImage(file = 'assets\\dots_8.png').subsample(8)
        self.dots_9 = PhotoImage(file = 'assets\\dots_9.png').subsample(8)
        self.dots_10 = PhotoImage(file = 'assets\\dots_10.png').subsample(8)
        self.dots_11 = PhotoImage(file = 'assets\\dots_11.png').subsample(8)
        self.dots_12 = PhotoImage(file = 'assets\\dots_12.png').subsample(8)
        self.dots_13 = PhotoImage(file = 'assets\\dots_13.png').subsample(8)
        self.dots_14 = PhotoImage(file = 'assets\\dots_14.png').subsample(8)
        self.dots_15 = PhotoImage(file = 'assets\\dots_15.png').subsample(8)
        self.dots_16 = PhotoImage(file = 'assets\\dots_16.png').subsample(8)
        self.dots_17 = PhotoImage(file = 'assets\\dots_17.png').subsample(8)
        self.dots_18 = PhotoImage(file = 'assets\\dots_18.png').subsample(8)
        self.dots_19 = PhotoImage(file = 'assets\\dots_19.png').subsample(8)
        self.dots_20 = PhotoImage(file = 'assets\\dots_20.png').subsample(8)
            
        self.dots_0_widget = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_0_widget.place(x = 23, y = 155, width = 55, height = 40)
        self.dots_1_widget = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_1_widget.place(x = 23, y = 195, width = 55, height = 40)
        self.dots_2_widget = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_2_widget.place(x = 23, y = 235, width = 55, height = 40)
        self.dots_3_widget = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_3_widget.place(x = 23, y = 275, width = 55, height = 40)
        self.dots_4_widget = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_4_widget.place(x = 23, y = 315, width = 55, height = 40)
        self.dots_5_widget = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_5_widget.place(x = 23, y = 355, width = 55, height = 40)
        self.dots_6_widget = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_6_widget.place(x = 23, y = 395, width = 55, height = 40)
        self.dots_7_widget = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_7_widget.place(x = 23, y = 435, width = 55, height = 40)
        self.dots_8_widget = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_8_widget.place(x = 23, y = 475, width = 55, height = 40)
        self.dots_9_widget = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_9_widget.place(x = 23, y = 515, width = 55, height = 40)
        self.dots_10_widget = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_10_widget.place(x = 23, y = 555, width = 55, height = 40)
    
    
    def play(self):
        self.reset_btn_pressed = False
        self.sec_count = 1
        self.min_count = 0
        self.reset_btn.configure(state = tkinter.NORMAL)
        for i in (self.random_btn,self.stats_btn,self.quit_btn,self.rules_btn):
            i.configure(state = tkinter.DISABLED)
        self.timer()
        
        
        
        
    def reset(self):
        self.reset_btn_pressed = True
        self.show_base()
    
    
    def stats(self):
        pass
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
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


if __name__ == "__main__":
    App().mainloop()