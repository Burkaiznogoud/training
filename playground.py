MIN_ROWS_AND_COLUMNS = 9
MAX_ROWS_AND_COLUMNS = 100
BLANK_FIELD = ' '

class Playground:
    def __init__(self):
        self.num_rows = 10 # self.input_rows_or_cols(name='rows')
        # self.num_rows = self.check_amount(number=self.num_rows, name='rows')
        self.num_cols = 10 # self.input_rows_or_cols(name='cloumns')
        # self.num_cols = self.check_amount(number=self.num_cols, name='columns')
        self.playground = []
        self.create_playground()

    def input_rows_or_cols(self, name):
        return int(input(f"Number of {name} between 9 and 100: "))

    def check_amount(self, number, name):
        while number < MIN_ROWS_AND_COLUMNS or number > MAX_ROWS_AND_COLUMNS:
                print(f"Wrong number of {name}.")
                number = self.input_rows_or_cols(name=name)
        return number

    def create_playground(self):
        matrix = []
        for i in range(self.num_rows):
            row = []
            for j in range(self.num_cols):
                row.append(BLANK_FIELD)
            matrix.append(row)
        self.playground = matrix[:]



