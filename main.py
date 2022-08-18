import random

class App():
    def __init__(self):
        self.random_colors_list = []
        self.input_colors_list = []
        self.unguessed_colors = 0
        self.guessed_colors = 0
        self.guessed_colors_and_positions = 0
        
        
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
    App().main()