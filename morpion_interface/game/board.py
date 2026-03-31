class Board:
    def __init__(self):
        self.state = [" " for _ in range(9)]
        self.current_winner = None
    def reset(self):
        self.state = [" " for _ in range(9)]
        self.current_winner = None
    def available_moves(self):
        return [i for i, x in enumerate(self.state) if x == " "]
    def empty_squares(self):
        return " " in self.state
    def num_empty_squares(self):
        return self.state.count(" ")
    def make_move(self, square, letter):
        if self.state[square] == " ":
            self.state[square] = letter
            if self.winner(square, letter):
                self.current_winner = letter
            return True
        return False
    def winner(self, square, letter):
        # row
        row_ind = square // 3
        row = self.state[row_ind*3:(row_ind+1)*3]
        if all([s == letter for s in row]):
            return True
        # col
        col_ind = square % 3
        col = [self.state[col_ind+i*3] for i in range(3)]
        if all([s == letter for s in col]):
            return True
        # diag
        if square % 2 == 0:
            diagonal1 = [self.state[i] for i in [0, 4, 8]]
            if all([s == letter for s in diagonal1]):
                return True
            diagonal2 = [self.state[i] for i in [2, 4, 6]]
            if all([s == letter for s in diagonal2]):
                return True
        return False