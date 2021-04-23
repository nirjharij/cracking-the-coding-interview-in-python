import sys


def sequence(arr):
    max_so_far = -sys.maxsize
    max_ending_here = 0
    for item in arr:
        max_ending_here += item
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far


print(sequence([2, -8, 3, -2, 4, -10]))
