import random


class Mastermind():
    def __init__(self):
        self.colors_list = ["YELLOW","BLUE","RED","ORANGE"]
        self.user_all_inputs_list = []
        
        
    def show_header(self):
        underscore = ""
        for i in range(1, 20):
            underscore += "_"
        print(f"{underscore}MASTER MIND{underscore}\nYOU HAVE 10 TRIES TO GUESS RANDOM COLORS LIST.")
        print(f"{underscore}COLORS LIST{underscore}\n {' * '.join(str(i) for i in self.colors_list)}\n")    
        
    
    def show_input_colors(self):
        underscore = ""
        for i in range(1, 20):
            underscore += "_"
        print(f"{underscore}YOUR COLORS{underscore}\n")
        for i in self.user_all_inputs_list:
            print(f"{(' * ').join(str(y) for y in i)}")
    
    
    def get_random_colors_list(self):
        self.random_colors_list = []
        for i in range(0, len(self.colors_list)):
            self.random_colors_list.append(random.choice(self.colors_list))
        return self.random_colors_list


    def get_user_inputs(self):
        print("\n")
        inputs_count = 0
        self.input_list = []
        while inputs_count < len(self.colors_list):
            user_input = input(f"Choose a color {inputs_count + 1}: ").upper()
            if user_input not in self.colors_list:
                print("COLOR IS NOT IN THE LIST! TRY AGAIN!")
            else:
                self.input_list.append(user_input)
                inputs_count += 1
        return self.input_list
    
    
    def get_user_all_inputs(self):
        self.user_all_inputs_list.append(self.input_list)
        return self.user_all_inputs_list
        
        
    def get_check_list(self):
        self.check_list = []
        for i in range(0, len(self.random_colors_list)):
            if self.input_list[i] == self.random_colors_list[i]:
                self.check_list.append("TRUE")
            else:
                self.check_list.append("FALSE")
        return self.check_list
        

    def tries(self):
        self.input_list, self.check_list = [], []
        tries_count = 1
        condition = False
        while condition == False and tries_count <= 10:
            print(f"TRY: {tries_count}")
            self.show_input_colors()
            self.get_user_inputs()
            self.get_user_all_inputs()
            self.get_check_list()
            if "FALSE" in self.check_list:
                print("\nWRONG COLORS LIST! TRY AGAIN!")
                condition = False
            else:
                print("\nCORRECT! YOU WON!") 
                condition = True
            tries_count += 1
        

    def play(self):
        self.show_header()
        self.get_random_colors_list()
        self.tries()


if __name__ == "__main__":
    Mastermind().play()
    