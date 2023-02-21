from controler import Controler
import keyboard
import time
import sys


def main():

    controler = Controler()
    RunGame = True

    while RunGame:

        keyboard.add_hotkey('w', controler.W_key_pressed, timeout=0.5)
        keyboard.add_hotkey('s', controler.S_key_pressed, timeout=0.5)
        keyboard.add_hotkey('a', controler.A_key_pressed, timeout=0.5)
        keyboard.add_hotkey('d', controler.D_key_pressed, timeout=0.5)

        if keyboard.is_pressed('esc'):
            RunGame = False
            controler.draw_playground()
            print("Game Over.")
            sys.exit()

        controler.snake.move_forward(controler.playground.playground)
        controler.draw_playground()
        time.sleep(0.5)

if __name__ == "__main__":
    main()
