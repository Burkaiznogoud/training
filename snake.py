class Snake:
    def __init__(self, num_rows, num_cols):
        self.body = ['^', 'o', 'o']
        self.segments = self.body[1:]
        self.head = self.body[0]
        self.lenght = len(self.body)
        self.starting_x = starting_column = int(num_cols // 2)
        self.starting_y = starting_row = int(num_rows // 2)

    def placing_snake(self, matrix, position):
        matrix_copy = matrix[:]
        self.starting_x = position['x']
        self.starting_y = position['y']
        for row_number in range(0, len(matrix_copy)):
            if row_number == self.starting_y:
                for i in range(self.lenght):
                    matrix_copy[row_number + i].pop(self.starting_y)
                    matrix_copy[row_number + i].insert(self.starting_y, self.body[i])

        return matrix_copy

    def segment_position(self, matrix, segment):
        segment_position = {'y': 0, 'x': 0}
        for index, row in enumerate(matrix):
            if segment in row:
                segment_position['y'] = index
                segment_position['x'] = row.index(segment)
        return segment_position

    def move_forward(self, matrix, snake):
        segment_pos_head = segment_position(matrix, snake[0])
        segment_pos_seg1 = segment_position(matrix, snake[1])
        segment_pos_seg2 = segment_position(matrix, snake[2])
        print(segment_pos_head)
        print(segment_pos_seg1)
        print(segment_pos_seg2)

        for segment in snake:
            segment_pos = segment_position(matrix, segment)
            new_y = segment_pos['y'] - 1
            new_x = segment_pos['x']
            matrix[new_y].pop(new_x)
            matrix[new_y].insert(new_x, segment)