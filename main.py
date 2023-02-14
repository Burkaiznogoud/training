from playground import Playground
from snake import Snake


def main():

    playground = Playground()
    playground.draw_playground()
    print(playground.num_cols)

    # rows = input_rows()
    # rows = check_amount_rows(rows)
    # columns = input_columns()
    # columns = check_amount_columns(columns)
    # rows = 9
    # columns = 9
    # generated_matrix = create_matrix(rows=rows, cols=columns)
    # snake = create_snake()
    # snake_position = starting_position(rows=rows, cols=columns)
    # generated_matrix = placing_snake(matrix=generated_matrix, snake=snake, position=snake_position)
    # draw_playground(generated_matrix)
    # print('----------------')
    # move_forward(matrix=generated_matrix, snake=snake)
    # draw_playground(generated_matrix)


if __name__ == "__main__":
    main()