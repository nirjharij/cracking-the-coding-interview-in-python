def find_max_black_sq(mat):
    processed = preprocess_mat(mat)
    for i in range(len(mat), 0, -1):
        size = find_square(processed, i)
        if size:
            return size
    return None


def find_square(processed, size):
    count = len(processed) - size + 1
    for r in range(0, count):
        for c in range(0, count):
            if square_exists(processed, r, c, size):
                return size


def square_exists(mat, row, col, size):
    top_left = mat[row][col]
    top_right = mat[row][col+size-1]
    bottom_left = mat[row+size-1][col]

    if top_left[0] < size or top_left[1] < size or top_right[1] < size or bottom_left[0] < size:
        return False
    return True


def preprocess_mat(mat):
    processed = [[0 for i in range(len(mat))] for j in range(len(mat))]
    for row in range(len(mat)-1, -1, -1):
        for col in range(len(mat)-1, -1, -1):
            right_zeros = 0
            below_zeros = 0
            if mat[row][col] == 0:
                right_zeros += 1
                below_zeros += 1
                if col + 1 < len(mat):
                    previous = processed[row][col+1]
                    right_zeros += previous[0]
                if row + 1 < len(mat):
                    below = processed[row+1][col]
                    below_zeros += below[1]
            processed[row][col] = (right_zeros, below_zeros)
    return processed


# print(find_max_black_sq([[1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0], [0, 0, 0, 0]]))
print(find_max_black_sq([[1, 0, 1], [0, 0, 1], [0, 0, 1]]))