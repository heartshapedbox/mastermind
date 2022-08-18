from textwrap import fill
from tkinter import *
import customtkinter
import random
import pyglet
import os
os.chdir('C:\\Users\\baben\\Documents\\GitHub\\mastermind')
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('blue')
pyglet.font.add_file('fonts\\Pacifico.ttf')

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.accent_color1 = "#141627"
        self.accent_color2 = "#232640"
        self.accent_color3 = "#1f2139"
        self.accent_color4 = "#d6478d"
        self.accent_color5 = "#202340"
        self.accent_color6 = "#161829"
        self.accent_color7 = "#1d1d32"
        self.accent_color8 = "#1a1a2d"
        self.accent_color9 = "#ffffff"
        self.accent_header_font1 = ('Pacifico', 26)
        self.accent_header_font2 = ('Pacifico', 12)
        
        x = int(self.winfo_screenwidth() // 2.5)
        y = int(self.winfo_screenheight() * 0.1)
        x, y = str(x), str(y)
        self.geometry(f'500x700+{x}+{y}')
        self.title('Mastermind')
        self.resizable(0, 0)
        self.gradient_frame = GradientFrame(self, self.accent_color1, self.accent_color2, borderwidth = 0, highlightthickness = 0)
        self.gradient_frame.pack(fill = "both", expand = True)
        self.show_home_widget()
        
        self.random_colors_list = []
        self.input_colors_list = []
        self.unguessed_colors = 0
        self.guessed_colors = 0
        self.guessed_colors_and_positions = 0
       
        
    def show_home_widget(self):
        self.header_widget = customtkinter.CTkLabel(self.gradient_frame, corner_radius = 10, text = 'MasterMind', text_font = self.accent_header_font1)
        self.header_widget.place(x = -10, y = -10)
        self.header_widget.configure(
            bg_color = self.accent_color2,
            fg_color = self.accent_color1,
            text_color = self.accent_color4,
            width = 490,
            height = 100 
        )
        
        self.base_colors_widget = customtkinter.CTkLabel(self.gradient_frame, corner_radius = 10, text = '')
        self.base_colors_widget.place(x = 385, y = 110)
        self.base_colors_widget.configure(
            bg_color = self.accent_color3,
            fg_color = self.accent_color1,
            text_color = self.accent_color4,
            width = 130,
            height = 500 
        )
        
        self.play_colors_widget = customtkinter.CTkLabel(self.gradient_frame, corner_radius = 10, text = '')
        self.play_colors_widget.place(x = -10, y = 110)
        self.play_colors_widget.configure(
            bg_color = self.accent_color3,
            fg_color = self.accent_color1,
            text_color = self.accent_color4,
            width = 370,
            height = 500 
        )
        
        self.color_1_button = customtkinter.CTkButton(self.gradient_frame, text = '', text_font = self.accent_header_font2)
        self.color_1_button.place(x = 420, y = 150)
        self.color_1_button.configure(fg_color = 'gold')
        self.color_2_button = customtkinter.CTkButton(self.gradient_frame, text = '', text_font = self.accent_header_font2)
        self.color_2_button.place(x = 420, y = 240)
        self.color_2_button.configure(fg_color = 'lime')
        self.color_3_button = customtkinter.CTkButton(self.gradient_frame, text = '', text_font = self.accent_header_font2)
        self.color_3_button.place(x = 420, y = 335)
        self.color_3_button.configure(fg_color = 'blue')
        self.color_4_button = customtkinter.CTkButton(self.gradient_frame, text = '', text_font = self.accent_header_font2)
        self.color_4_button.place(x = 420, y = 430)
        self.color_4_button.configure(fg_color = 'red')
        self.color_5_button = customtkinter.CTkButton(self.gradient_frame, text = '', text_font = self.accent_header_font2)
        self.color_5_button.place(x = 420, y = 520)
        self.color_5_button.configure(fg_color = 'magenta')
        for i in (self.color_1_button, self.color_2_button, self.color_3_button, self.color_4_button, self.color_5_button):
            i.configure(
                bg_color = self.accent_color1,
                text_color = self.accent_color1,
                width = 150,
                height = 50,
                corner_radius = 10
            )
        
        
        self.start_button = customtkinter.CTkButton(self.gradient_frame, text = '🏁', text_font = self.accent_header_font2)
        self.start_button.place(x = 425, y = 630)
        self.start_button.configure(bg_color = self.accent_color5)
        self.reset_button = customtkinter.CTkButton(self.gradient_frame, text = '🔄', text_font = self.accent_header_font2)
        self.reset_button.place(x = 325, y = 630)
        self.reset_button.configure(bg_color = self.accent_color3)
        self.stat_button = customtkinter.CTkButton(self.gradient_frame, text = '⭐', text_font = self.accent_header_font2)
        self.stat_button.place(x = 225, y = 630)
        self.stat_button.configure(bg_color = self.accent_color7)
        self.rules_button = customtkinter.CTkButton(self.gradient_frame, text = '📝', text_font = self.accent_header_font2)
        self.rules_button.place(x = 125, y = 630)
        self.rules_button.configure(bg_color = self.accent_color8)
        self.quit_button = customtkinter.CTkButton(self.gradient_frame, text = '❌', text_font = self.accent_header_font2)
        self.quit_button.place(x = 25, y = 630)
        self.quit_button.configure(bg_color = self.accent_color6)
        for i in (self.start_button, self.reset_button, self.quit_button, self.rules_button, self.stat_button):
            i.configure(
                fg_color = self.accent_color1,
                text_color = self.accent_color9,
                width = 50,
                height = 50,
                corner_radius = 8
            )
    
        
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