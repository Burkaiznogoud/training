from playground import Playground
from snake import Snake
import keyboard
import os
import sys

class Controler:
    def __init__(self):
        self.playground = Playground()
        self.snake = Snake(num_rows=10, num_cols=10)
        self.snake.placing_snake(playground=self.playground.playground)
        self.draw_playground()


    def draw_playground(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        return [print(f"{self.playground.playground.index(_)} {_}\n") for _ in self.playground.playground]

    def W_key_pressed(self):
        self.snake.move_forward(self.playground.playground)
        self.draw_playground()
        print("W pressed")

    def S_key_pressed(self):
        print("S pressed")

    def A_key_pressed(self):
        print("A pressed")

    def D_key_pressed(self):
        print("D pressed")

    def ESC_key_pressed(self):
        try:
            sys.exit()
        except NameError:
            print(f"{NameError} occured.")
        finally:
            self.draw_playground()
            print("Game Over.")
            sys.exit()


