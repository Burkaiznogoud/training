class NewSegment:
    def __new__(cls, char):
        segment = super().__new__(cls)
        segment.char = char
        return segment

    def __repr__(self):
        return f"'{self.char}'"

class Snake:
    def __init__(self, num_rows, num_cols):
        self.body = []
        self.head = '^'
        self.create_snake()
        self.lenght = len(self.body)
        self.starting_x = int(num_cols // 2)
        self.starting_y = int(num_rows // 2)

    def create_new_segment(self, char):
        segment = NewSegment(char)
        return segment

    def create_snake(self):
        self.body.append(self.create_new_segment('^'))
        self.body.append(self.create_new_segment('o'))
        self.body.append(self.create_new_segment('o'))

    def placing_snake(self, playground):
        playground_copy = playground[:]
        for row_number in range(0, len(playground_copy)):
            if row_number == self.starting_y:
                for i in range(self.lenght):
                    playground_copy[row_number + i].pop(self.starting_y - 1)
                    playground_copy[row_number + i].insert(self.starting_y - 1, self.body[i])

        return playground_copy

    def segment_position(self, playground, segment):
        for row in playground:
            if segment is segment in row:
                pos_y = playground.index(row)
                pos_x = row.index(segment)
                return {'pos_y': pos_y, 'pos_x': pos_x}

    def move_forward(self, playground):
        self.head = self.create_new_segment('^')
        for segment in self.body:
            if segment is segment:
                segment_pos = self.segment_position(playground=playground, segment=segment)
                pos_x = segment_pos['pos_x']
                pos_y = segment_pos['pos_y']
                new_x_pos = pos_x
                new_y_pos = pos_y - 1
                playground[new_y_pos].pop(new_x_pos)
                playground[new_y_pos].insert(new_x_pos, segment)
                if segment is self.body[-1]:
                    playground[pos_y].pop(pos_x)
                    playground[pos_y].insert(pos_x, ' ')



