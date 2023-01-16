import random


class Mastermind():
    def __init__(self):
        self.colors_list = ["YELLOW","BLUE","RED","ORANGE"]
        self.user_inputs_log = []
        self.tries_count = 1
        self.color_and_position_match, self.color_match_but_position_wrong, self.no_such_color  = 0, 0, 0
    

    def show_header(self):
        underscore = ""
        for i in range(1, 20):
            underscore += "_"
        print(f"{underscore}MASTER MIND{underscore}\nPLAYER TRIES TO GUESS A RANDOM PATTERN, IN BOTH\nCOLOR AND COLOR ORDER, WITHIN 10 TRIES.\n")
        print(f"{underscore}COLORS LIST{underscore}\n {' * '.join(str(i) for i in self.colors_list)}\n")
    
    
    def show_input_colors(self):
        tries_count_log = 1
        underscore = ""
        for i in range(1, 20):
            underscore += "_"
        print(f"\n{underscore}YOUR TRIES{underscore}\n")
        for i in self.user_inputs_log:
            print(f"TRY {tries_count_log}: {(' * ').join(str(y) for y in i)}")
            tries_count_log += 1
    
    
    def get_random_colors_list(self):
        self.random_colors_list = []
        for i in range(0, len(self.colors_list)):
            self.random_colors_list.append(random.choice(self.colors_list))
        return self.random_colors_list
    
    
    def get_user_inputs(self):
        print("\n")
        input_colors_count = 0
        self.input_list = []
        print(f"TRY {self.tries_count}: ")
        while input_colors_count < len(self.colors_list):
            user_input = input(f"Choose a color {input_colors_count + 1}: ").upper()
            if user_input not in self.colors_list:
                print("COLOR IS NOT IN THE LIST! TRY AGAIN!")
            else:
                self.input_list.append(user_input)
                input_colors_count += 1
        self.tries_count += 1
        return self.input_list
    
    
    def get_user_inputs_log(self):
        self.user_inputs_log.append(self.input_list)
        return self.user_inputs_log
    
     
    def get_check_list(self):
        self.check_list = []
        for i in range(0, len(self.random_colors_list)):
            if self.input_list[i] == self.random_colors_list[i]:
                self.check_list.append("TRUE")
            else:
                self.check_list.append("FALSE")
        return self.check_list
    
    
    def matching(self):
        self.color_and_position_match, self.color_match_but_position_wrong, self.no_such_color  = 0, 0, 0
        for i in range(0, len(self.input_list)):
            if self.input_list[i] == self.random_colors_list[i]:
                self.color_and_position_match += 1
            elif self.input_list[i] != self.random_colors_list[i] and self.input_list[i] in self.random_colors_list:
                self.color_match_but_position_wrong += 1
            else:
                self.no_such_color += 1
    
    
    def tries(self):
        self.input_list, self.check_list = [], []
        tries_count = 1
        victory = False
        while victory == False and tries_count <= 10:
            self.show_input_colors()
            self.get_user_inputs()
            self.get_user_inputs_log()
            self.get_check_list()
            self.matching()
            if "FALSE" in self.check_list and tries_count < 10:
                print(f"\nWRONG!\nMATCHED COLOR AND POSITION: {self.color_and_position_match}\nMATCHED COLOR BUT WRONG POSITION: {self.color_match_but_position_wrong}\nNO SUCH A COLOR: {self.no_such_color}\nTRY AGAIN!\n")
                victory = False
            elif "FALSE" in self.check_list and tries_count == 10:
                print(f"\nWRONG! GAME OVER! RANDOM COLORS:\n{' * '.join(str(i) for i in self.random_colors_list)}\n")
                victory = False
                self.user_inputs_log = []
                self.tries_count = 1
            else:
                print(f"\nCONGRATULATION! YOU WON! RANDOM COLORS:\n{' * '.join(str(i) for i in self.random_colors_list)}\n") 
                victory = True
                self.user_inputs_log = []
                self.tries_count = 1
            tries_count += 1
    
    
    def play(self):
        self.show_header()
        playing = True
        while playing == True:
            player_answer = input("WOULD YOU LIKE TO PLAY? (Y/N): ").upper()
            if player_answer == "Y":
                self.get_random_colors_list()
                self.tries()
            else:
                print("GAME IS OVER!")
                break


if __name__ == "__main__":
    Mastermind().play()