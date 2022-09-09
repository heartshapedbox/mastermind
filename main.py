import time
import tkinter
import customtkinter
import random
import pyglet
import os
from tkinter import *
from threading import Timer
from time import sleep

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
        
        self.color_1 = PhotoImage(file = 'assets\\color_1.png').subsample(10)
        self.color_2 = PhotoImage(file = 'assets\\color_2.png').subsample(10)
        self.color_3 = PhotoImage(file = 'assets\\color_3.png').subsample(10)
        self.color_4 = PhotoImage(file = 'assets\\color_4.png').subsample(10)
        self.color_5 = PhotoImage(file = 'assets\\color_5.png').subsample(10)
        
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
        
        self.dots_list = [self.dots_1,self.dots_2,self.dots_3,self.dots_4,self.dots_5,self.dots_6,self.dots_7,self.dots_8,self.dots_9,self.dots_10,self.dots_11,self.dots_12,self.dots_13,self.dots_14,self.dots_15,self.dots_16,self.dots_17,self.dots_18,self.dots_19,self.dots_20]
        self.colors_list = [self.basic_color1, self.basic_color2, self.basic_color3, self.basic_color4, self.basic_color5]
        self.pict_colors_list = [self.color_1, self.color_2, self.color_3, self.color_4, self.color_5]
        self.combinations_list = ['050','410','320','230','140','411','322','233','144','055','312','212','113','014','221','131','041','023','032','500']
        self.random_colors_list, self.input_colors_list = [], []
        self.unguessed_colors, self.guessed_colors, self.guessed_colors_and_positions, self.try_count = 0, 0, 0, 0
        self.result = ''
        self.show_base()
        
    
    def hover(self, btn, colorfdonHover, colorfdonLeave):
        btn.bind("<Enter>", func = lambda i: btn.configure(text_color = colorfdonHover))
        btn.bind("<Leave>", func = lambda i: btn.configure(text_color = colorfdonLeave))
    
    
    def show_rules(self):
        pass
    
        
    def reset(self):
        self.reset_btn_pressed = True
        self.try_count = 0
        self.result = ''
        self.input_colors_list, self.random_colors_list = [], []
        self.show_base()
        try:
            self.result_message_widget.destroy()
        except AttributeError:
            pass
    
    
    def show_stats(self):
        pass
       
        
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
        
        self.show_rules_btn = customtkinter.CTkButton(self, corner_radius = 8, text = 'Rules', text_font = self.accent_font_2, command = lambda:self.show_rules())
        self.show_rules_btn.place(x = 360, y = 10)
        self.show_rules_btn.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color5,
            text_color = self.accent_color2,
            hover_color = self.accent_color1,
            width = 80,
            height = 60
        )
        self.hover(self.show_rules_btn, self.accent_color5, self.accent_color2)
        
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
        
        self.doground_widget = customtkinter.CTkLabel(self, corner_radius = 8, text = '', text_font = self.accent_font_1)
        self.doground_widget.place(x = 100, y = 140)
        self.doground_widget.configure(
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
        
        self.base_color_1_btn = customtkinter.CTkButton(self, corner_radius = 8, text = '', command = lambda:self.make_color_choice('gold', self.color_1))
        self.base_color_1_btn.place(x = 360, y = 140)
        self.base_color_1_btn.configure(fg_color = self.basic_color1, hover_color = self.basic_color1, state = tkinter.DISABLED)
        self.base_color_2_btn = customtkinter.CTkButton(self, corner_radius = 8, text = '', command = lambda:self.make_color_choice('lime', self.color_2))
        self.base_color_2_btn.place(x = 360, y = 200)
        self.base_color_2_btn.configure(fg_color = self.basic_color2, hover_color = self.basic_color2, state = tkinter.DISABLED)
        self.base_color_3_btn = customtkinter.CTkButton(self, corner_radius = 8, text = '', command = lambda:self.make_color_choice('blue', self.color_3))
        self.base_color_3_btn.place(x = 360, y = 260)
        self.base_color_3_btn.configure(fg_color = self.basic_color3, hover_color = self.basic_color3, state = tkinter.DISABLED)
        self.base_color_4_btn = customtkinter.CTkButton(self, corner_radius = 8, text = '', command = lambda:self.make_color_choice('red', self.color_4))
        self.base_color_4_btn.place(x = 360, y = 320)
        self.base_color_4_btn.configure(fg_color = self.basic_color4, hover_color = self.basic_color4, state = tkinter.DISABLED)
        self.base_color_5_btn = customtkinter.CTkButton(self, corner_radius = 8, text = '', command = lambda:self.make_color_choice('magenta', self.color_5))
        self.base_color_5_btn.place(x = 360, y = 380)
        self.base_color_5_btn.configure(fg_color = self.basic_color5, hover_color = self.basic_color5, state = tkinter.DISABLED)
        for i in (self.base_color_1_btn,self.base_color_2_btn,self.base_color_3_btn,self.base_color_4_btn,self.base_color_5_btn):
            i.configure(
                bg_color = self.accent_color2,
                hover_color = self.accent_color5,
                width = 80,
                height = 50
            )
            self.hover(i, self.accent_color8, self.accent_color2)
        
        self.random_btn = customtkinter.CTkButton(self, corner_radius = 8, text = 'Random', text_font = self.accent_font_2, command = lambda:self.start())
        self.random_btn.place(x = 360, y = 80)
        self.reset_btn = customtkinter.CTkButton(self, corner_radius = 8, text = 'Reset', text_font = self.accent_font_2, command = lambda:self.reset())
        self.reset_btn.place(x = 360, y = 440)
        self.reset_btn.configure(state = tkinter.DISABLED)
        self.show_stats_btn = customtkinter.CTkButton(self, corner_radius = 8, text = 'Stats', text_font = self.accent_font_2, command = lambda:self.show_stats())
        self.show_stats_btn.place(x = 360, y = 500)
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
        
        for i in (self.random_btn,self.reset_btn,self.show_stats_btn):
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
        
        
    def show_result_message(self):
        self.result_message_widget = customtkinter.CTkLabel(self, text = f'Congratulation!\nIt took {self.try_count} attemp(s) to win!\nYour time: {self.time}', corner_radius = 8, text_font = self.accent_font_3)
        self.result_message_widget.place(relx = 0.5, rely = 0.5, anchor=tkinter.CENTER, width = 238, height = 100)
        self.result_message_widget.configure(
            bg_color = self.accent_color6,
            fg_color = self.accent_color8,
            text_color = self.accent_color6
        )
        self.result_message_widget_close_btn = customtkinter.CTkButton(self.result_message_widget, corner_radius = 5, text = 'x', command = lambda:self.reset())
        self.result_message_widget_close_btn.place(x = 213, y = 5, width = 20, height = 20)
        self.result_message_widget_close_btn.configure(
            bg_color = self.accent_color8,
            fg_color = self.accent_color3,
            text_color = self.accent_color6,
            hover_color = self.accent_color4
        )
        self.hover(self.result_message_widget_close_btn, self.accent_color1, self.accent_color4)

    
    def timer(self):
        try:
            if self.reset_btn_pressed == True:
                return
        except ValueError:
            pass
        
        if self.min_count < 10 and self.sec_count < 10:
            self.timer_widget.configure(text = f'0{self.min_count}:0{self.sec_count}')
            self.time = f'0{self.min_count}:0{self.sec_count}'
            self.after(1000, self.timer)

        elif self.min_count < 10 and self.sec_count >= 10 and self.sec_count != 60:
            self.timer_widget.configure(text = f'0{self.min_count}:{self.sec_count}')
            self.time = f'0{self.min_count}:{self.sec_count}'
            self.after(1000, self.timer)
            
        elif self.min_count < 10 and self.sec_count >= 10 and self.sec_count == 60:
            self.min_count += 1
            self.timer_widget.configure(text = f'0{self.min_count}:00')
            self.time = f'0{self.min_count}:00'
            self.sec_count = 0
            self.after(1000, self.timer)
            
        elif self.min_count >= 10 and self.min_count < 60 and self.sec_count >= 10 and self.sec_count == 60:
            self.min_count += 1
            self.timer_widget.configure(text = f'{self.min_count}:00')
            self.time = f'{self.min_count}:00'
            self.sec_count = 0
            self.after(1000, self.timer)
        
        elif self.min_count >= 10 and self.min_count < 60 and self.sec_count < 10:
            self.timer_widget.configure(text = f'{self.min_count}:0{self.sec_count}')
            self.time = f'{self.min_count}:0{self.sec_count}'
            self.after(1000, self.timer)
            
        elif self.min_count >= 10 and self.min_count < 60 and self.sec_count >= 10 and self.sec_count != 60:
            self.timer_widget.configure(text = f'{self.min_count}:{self.sec_count}')
            self.time = f'{self.min_count}:{self.sec_count}'
            self.after(1000, self.timer)
            
        elif self.min_count == 60:
            self.timer_widget.configure(text = 'Time is\nOver')
            return
        
        self.sec_count += 1
        
        
    def get_random_colors_list(self):
        for i in self.colors_list:
            self.random_color = random.choice(self.colors_list)
            self.random_colors_list.append(self.random_color)
    
        
    def get_unguessed_colors(self):
        self.result = ''
        self.unguessed_colors = 0
        for i in self.input_colors_list:
            if i not in self.random_colors_list:
                self.unguessed_colors += 1
        self.result += str(self.unguessed_colors)
    
    
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
        self.result += str(self.guessed_colors_and_positions)
        self.result += str(self.guessed_colors)
    
    
    def show_empty_dots(self):
        self.dots_0 = PhotoImage(file = 'assets\\dots_0.png').subsample(8)    
        self.dots_widget_0 = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_widget_0.place(x = 23, y = 155, width = 55, height = 40)
        self.dots_widget_1 = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_widget_1.place(x = 23, y = 195, width = 55, height = 40)
        self.dots_widget_2 = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_widget_2.place(x = 23, y = 235, width = 55, height = 40)
        self.dots_widget_3 = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_widget_3.place(x = 23, y = 275, width = 55, height = 40)
        self.dots_widget_4 = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_widget_4.place(x = 23, y = 315, width = 55, height = 40)
        self.dots_widget_5 = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_widget_5.place(x = 23, y = 355, width = 55, height = 40)
        self.dots_widget_6 = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_widget_6.place(x = 23, y = 395, width = 55, height = 40)
        self.dots_widget_7 = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_widget_7.place(x = 23, y = 435, width = 55, height = 40)
        self.dots_widget_8 = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_widget_8.place(x = 23, y = 475, width = 55, height = 40)
        self.dots_widget_9 = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_widget_9.place(x = 23, y = 515, width = 55, height = 40)
        self.dots_widget_10 = customtkinter.CTkLabel(self, image = self.dots_0, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.dots_widget_10.place(x = 23, y = 555, width = 55, height = 40)
        
    
    def show_hidden_colors(self):
        self.hidden_color = PhotoImage(file = 'assets\\color_hidden.png').subsample(10)
        self.hidden_color_widget = customtkinter.CTkLabel(self, image = self.hidden_color, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.hidden_color_widget.place(x = 110, y = 88, width = 35, height = 35)
        self.hidden_color_widget = customtkinter.CTkLabel(self, image = self.hidden_color, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.hidden_color_widget.place(x = 158, y = 88, width = 35, height = 35)
        self.hidden_color_widget = customtkinter.CTkLabel(self, image = self.hidden_color, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.hidden_color_widget.place(x = 207, y = 88, width = 35, height = 35)
        self.hidden_color_widget = customtkinter.CTkLabel(self, image = self.hidden_color, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.hidden_color_widget.place(x = 255, y = 88, width = 35, height = 35)
        self.hidden_color_widget = customtkinter.CTkLabel(self, image = self.hidden_color, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.hidden_color_widget.place(x = 305, y = 88, width = 35, height = 35)
    
    
    def show_empty_colors(self):
        self.try_color = PhotoImage(file = 'assets\\color_0.png').subsample(10)
        self.try_color_widget1_name = ''
        self.try_color_widget1 = customtkinter.CTkLabel(self, image = self.try_color, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.try_color_widget1.place(x = 110, y = 155, width = 35, height = 35)
        self.try_color_widget2_name = ''
        self.try_color_widget2 = customtkinter.CTkLabel(self, image = self.try_color, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.try_color_widget2.place(x = 158, y = 155, width = 35, height = 35)
        self.try_color_widget3_name = ''
        self.try_color_widget3 = customtkinter.CTkLabel(self, image = self.try_color, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.try_color_widget3.place(x = 207, y = 155, width = 35, height = 35)
        self.try_color_widget4_name = ''
        self.try_color_widget4 = customtkinter.CTkLabel(self, image = self.try_color, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.try_color_widget4.place(x = 255, y = 155, width = 35, height = 35)
        self.try_color_widget5_name = ''
        self.try_color_widget5 = customtkinter.CTkLabel(self, image = self.try_color, fg_color = self.accent_color6, bg_color = self.accent_color6)
        self.try_color_widget5.place(x = 305, y = 155, width = 35, height = 35)
    
    
    def start(self):
        self.reset_btn_pressed = False
        self.sec_count = 1
        self.min_count = 0
        self.try_count = 0
        self.reset_btn.configure(state = tkinter.NORMAL)
        self.base_color_1_btn.configure(state = tkinter.NORMAL)
        self.base_color_2_btn.configure(state = tkinter.NORMAL)
        self.base_color_3_btn.configure(state = tkinter.NORMAL)
        self.base_color_4_btn.configure(state = tkinter.NORMAL)
        self.base_color_5_btn.configure(state = tkinter.NORMAL)
        for i in (self.random_btn,self.show_stats_btn,self.quit_btn,self.show_rules_btn):
            i.configure(state = tkinter.DISABLED)
            
        self.get_random_colors_list()
        self.timer()
        self.show_hidden_colors()
        self.show_empty_colors()
        print(self.random_colors_list)
    
    
    def make_color_choice(self, i, y):
        if i in self.colors_list and y in self.pict_colors_list and self.try_color_widget1_name == '':
            self.try_color_widget1.configure(image = y)
            self.try_color_widget1_name = i
        elif i in self.colors_list and y in self.pict_colors_list and self.try_color_widget1_name != '' and self.try_color_widget2_name == '':
            self.try_color_widget2.configure(image = y)
            self.try_color_widget2_name = i
        elif i in self.colors_list and y in self.pict_colors_list and self.try_color_widget1_name != '' and self.try_color_widget2_name != '' and self.try_color_widget3_name == '':
            self.try_color_widget3.configure(image = y)
            self.try_color_widget3_name = i
        elif i in self.colors_list and y in self.pict_colors_list and self.try_color_widget1_name != '' and self.try_color_widget2_name != '' and self.try_color_widget3_name != '' and self.try_color_widget4_name == '':
            self.try_color_widget4.configure(image = y)
            self.try_color_widget4_name = i
        elif i in self.colors_list and y in self.pict_colors_list and self.try_color_widget1_name != '' and self.try_color_widget2_name != '' and self.try_color_widget3_name != '' and self.try_color_widget4_name != '' and self.try_color_widget5_name == '':
            self.try_color_widget5.configure(image = y)
            self.try_color_widget5_name = i
        
        self.input_colors_list.append(i)
            
        if self.try_color_widget5_name != '':
            self.try_count += 1
            self.main()
            self.input_colors_list = []
        
        if self.try_count == 11:
            for i in (self.try_color_widget1, self.try_color_widget2, self.try_color_widget3, self.try_color_widget4, self.try_color_widget5):
                i.destroy()
            self.reset()
             
    
    def main(self):
        self.get_unguessed_colors()
        self.guess()
        
        self.step = 40
        if self.try_count == 1 and self.result in self.combinations_list:
            x = self.dots_list[self.combinations_list.index(self.result)]
            self.dots_widget_0.configure(image = x)
            self.position = 155
        elif self.try_count == 2 and self.result in self.combinations_list:
            x = self.dots_list[self.combinations_list.index(self.result)]
            self.dots_widget_1.configure(image = x)
            self.position = 195
        elif self.try_count == 3 and self.result in self.combinations_list:
            x = self.dots_list[self.combinations_list.index(self.result)]
            self.dots_widget_2.configure(image = x)
            self.position = 235
        elif self.try_count == 4 and self.result in self.combinations_list:
            x = self.dots_list[self.combinations_list.index(self.result)]
            self.dots_widget_3.configure(image = x)
            self.position = 275
        elif self.try_count == 5 and self.result in self.combinations_list:
            x = self.dots_list[self.combinations_list.index(self.result)]
            self.dots_widget_4.configure(image = x)
            self.position = 315
        elif self.try_count == 6 and self.result in self.combinations_list:
            x = self.dots_list[self.combinations_list.index(self.result)]
            self.dots_widget_5.configure(image = x)
            self.position = 355
        elif self.try_count == 7 and self.result in self.combinations_list:
            x = self.dots_list[self.combinations_list.index(self.result)]
            self.dots_widget_6.configure(image = x)
            self.position = 395
        elif self.try_count == 8 and self.result in self.combinations_list:
            x = self.dots_list[self.combinations_list.index(self.result)]
            self.dots_widget_7.configure(image = x)
            self.position = 435
        elif self.try_count == 9 and self.result in self.combinations_list:
            x = self.dots_list[self.combinations_list.index(self.result)]
            self.dots_widget_8.configure(image = x)
            self.position = 475
        elif self.try_count == 10 and self.result in self.combinations_list:
            x = self.dots_list[self.combinations_list.index(self.result)]
            self.dots_widget_9.configure(image = x)
            self.position = 515
        elif self.try_count == 11 and self.result in self.combinations_list:
            x = self.dots_list[self.combinations_list.index(self.result)]
            self.dots_widget_10.configure(image = x)
            self.position = 555
        
        if self.result != '050':
            self.show_empty_colors()
            for i in (self.try_color_widget1, self.try_color_widget2, self.try_color_widget3, self.try_color_widget4, self.try_color_widget5):
                i.place(y = self.position + self.step) 
        else:
            self.reset_btn_pressed = True
            for i in (self.reset_btn,self.random_btn,self.show_stats_btn,self.quit_btn,self.show_rules_btn,self.base_color_1_btn,self.base_color_2_btn,self.base_color_3_btn,self.base_color_4_btn,self.base_color_5_btn):
                i.configure(state = tkinter.DISABLED)
            self.show_result_message()      


if __name__ == "__main__":
    App().mainloop()