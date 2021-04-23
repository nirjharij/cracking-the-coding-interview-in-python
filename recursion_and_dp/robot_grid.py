def find_path(mat, row, col, cache, path):
    if row < 0 or col < 0:
        return False

    if (row, col) in cache:
        return cache.get((row, col))

    is_origin = True if row == 0 and col == 0 else False
    flag = False
    if is_origin or find_path(mat, row - 1, col, cache, path) or find_path(mat, row, col - 1, cache, path):
        path.append((row, col))
        flag = True

    cache[(row, col)] = flag
    return flag


mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
path = []
cache = {}
if find_path(mat, 2, 2, cache, path):
    print(path)
