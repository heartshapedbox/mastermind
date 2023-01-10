import random


class Mastermind():
    def __init__(self):
        self.colors_list = ["yellow","blue","red","orange"]
        self.input_list, self.random_colors_list = [], []
    
    
    def get_random_colors_list(self):
        for i in range(0, len(self.colors_list)):
            self.random_colors_list.append(random.choice(self.colors_list))
        return self.random_colors_list


    def get_user_inputs(self):
        for i in range(0, len(self.colors_list)):
            user_input = input(f"Color {i + 1}: ").lower()
            if user_input in self.colors_list:
                self.input_list.append(user_input)
        return self.input_list


    def get_output(self):
        for i in range(0, len(self.input_list)):
            if self.input_list[i] != self.random_colors_list[i]:
                print("-")
            else:
                print("+")
                

    def play(self):
        print(self.colors_list)
        print(self.get_random_colors_list())
        print(self.get_user_inputs())
        self.get_output()


if __name__ == "__main__":
    Mastermind().play()
    