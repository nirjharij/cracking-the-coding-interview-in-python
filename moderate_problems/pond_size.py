def get_pond_size(mat):
    row = len(mat)
    col = len(mat[0])
    visited = [[0 for i in range(col)] for j in range(row)]
    final_sizes = list()
    for i in range(0, row):
        for j in range(0, col):
            if mat[i][j] == 0:
                if not visited[i][j]:
                    pond_size = compute_size(mat, i, j, visited)
                    final_sizes.append(pond_size)
    return final_sizes


def compute_size(mat, row, col, visited, size=1):
    if row < 0 or col < 0 or row >= len(mat) or col >= len(mat[0]):
        return 0
    if visited[row][col] or mat[row][col]:
        return 0
    visited[row][col] = 1
    for i in range(-1, 2):
        for j in range(-1, 2):
            size += compute_size(mat, row+i, col+j, visited, size=size)
    return size


print(get_pond_size([[0, 2, 1, 0], [0, 1, 0, 1], [1, 1, 0, 1], [0, 1, 0, 1]]))
