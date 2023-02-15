from playground import Playground
from snake import Snake
import time


def main():

    RunGame = True

    playground = Playground()
    snake = Snake(num_rows=10, num_cols=10)
    snake.placing_snake(playground=playground.playground)
    playground.draw_playground()

    while RunGame:
        time.sleep(1)
        snake.move_forward(playground=playground.playground)
        playground.draw_playground()


if __name__ == "__main__":
    main()