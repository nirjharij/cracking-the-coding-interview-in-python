GRID_SIZE = 4


def place_queens(row, board):
    if row == GRID_SIZE:
        return True
    else:
        for col in range(GRID_SIZE):
            if check_valid(board, row, col):
                board[row][col] = 1
                if place_queens(row+1, board):
                    return True
                board[row][col] = 0
    return False


def check_valid(board, row, col):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, GRID_SIZE, 1),
                    range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
place_queens(0, board)
print(board)
