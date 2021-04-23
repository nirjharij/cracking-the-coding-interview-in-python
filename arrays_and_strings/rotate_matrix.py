def matrix_rotate(mat):
    n = len(mat)

    for layer in range(0, n//2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first

            top = mat[first][i]
            mat[first][i] = mat[last - offset][first]
            mat[last - offset][first] = mat[last][last - offset]
            mat[last][last - offset] = mat[i][last]
            mat[i][last] = top
    print(mat)


if __name__ == "__main__":
    matrix_rotate([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
