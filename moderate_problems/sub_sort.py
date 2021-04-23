import sys


class Pointer:
    def __init__(self, start=None, end=None):
        self.start = start
        self.end = end

    def print_index(self):
        print(self.start, self.end)


def find_sort_index(arr):
    L = Pointer()
    M = Pointer()
    R = Pointer()

    L.start = 0
    R.end = len(arr) - 1
    max_so_far = -sys.maxsize
    for i in range(len(arr)):
        if arr[i] > max_so_far:
            L.end = i
            max_so_far = arr[i]
        else:
            left_max_index = i
            break

    min_so_far = sys.maxsize
    for i in range(len(arr)-1, 0, -1):
        right_min_index = i
        if arr[i] < min_so_far:
            R.start = i
            min_so_far = arr[i]
        else:
            break

    M.start = left_max_index
    M.end = right_min_index

    min_val = min(min(arr[M.start:M.end+1]), min(arr[R.start:R.end+1]))
    max_val = max(max(arr[L.start:L.end+1]), max(arr[M.start:M.end+1]))

    # M.print_index()
    # L.print_index()
    # R.print_index()

    while arr[L.end] > min_val:
        L.end = L.end - 1

    while arr[R.start] < max_val:
        R.start = R.start + 1

    print(L.end+1, R.start)


find_sort_index([1, 2, 4, 7, 10, 11, 8, 6, 5, 12, 16, 18])
