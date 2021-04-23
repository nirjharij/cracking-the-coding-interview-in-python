class TicTacToe:
    def __init__(self, board_size):
        self.board_size = board_size
        self.row = [0] * board_size
        self.col = [0] * board_size
        self.diag = [0]
        self.anti_diag = [0]

    def has_won(self, row, col):
        self.row[row] += 1
        self.col[col] += 1
        if row == col:
            self.diag[0] += 1
        if row + col == self.board_size-1:
            self.anti_diag[0] += 1

        if self.row[row] == self.board_size or self.col[col] == self.board_size or \
                self.diag[0] == self.board_size or self.anti_diag[0] == self.board_size:
            return True
        else:
            return False


if __name__ == "__main__":
    player1 = TicTacToe(3)
    player2 = TicTacToe(3)
    player1.has_won(1, 1)
    player2.has_won(1, 2)
    player1.has_won(0, 0)
    player2.has_won(2, 2)
    player1.has_won(0, 2)
    player2.has_won(0, 1)
    resp = player1.has_won(2, 0)
    if resp:
        print("WON")
    else:
        print("Not won")
