import random


class Mastermind():
    def __init__(self):
        self.colors_list = ["YELLOW","BLUE","RED","ORANGE"]
        self.input_list, self.random_colors_list = [], []
        
        
    def show_header(self):
        underscore = ""
        for i in range(1, 13):
            underscore += "_"
        print(f"{underscore}COLORS{underscore}\n {' * '.join(str(i) for i in self.colors_list)}\n")
    
    
    def get_random_colors_list(self):
        for i in range(0, len(self.colors_list)):
            self.random_colors_list.append(random.choice(self.colors_list))
        return self.random_colors_list


    def get_user_inputs(self):
        tries_count = 0
        while tries_count < len(self.colors_list):
            user_input = input(f"Enter a color {tries_count + 1}: ").upper()
            if user_input not in self.colors_list:
                print("Color is not in the list! Try again!")
            else:
                self.input_list.append(user_input)
                tries_count += 1
        return self.input_list


    def get_output(self):
        for i in range(0, len(self.input_list)):
            if self.input_list[i] != self.random_colors_list[i]:
                print("-")
            else:
                print("+")
                

    def play(self):
        self.show_header()
        self.get_random_colors_list()
        print(self.get_user_inputs())
        self.get_output()


if __name__ == "__main__":
    Mastermind().play()
    