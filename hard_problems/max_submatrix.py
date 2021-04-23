import sys


def find_max_submatrix(mat):
    max_sum = -sys.maxsize
    max_left = 0
    max_right = 0
    max_up = 0
    max_down = 0
    for i in range(len(mat)):
        partial_sum = [0 for n in range(len(mat[0]))]
        for j in range(i, len(mat)):
            for k in range(len(mat[0])):
                partial_sum[k] += mat[j][k]
            running_sum, start, end = max_sum_subarray(partial_sum)
            if max_sum < running_sum:
                max_sum = running_sum
                max_left = i
                max_right = j
                max_up = start
                max_down = end
    print(max_left, max_right, max_up, max_down)


def max_sum_subarray(arr):
    max_so_far = 0
    max_ending_here = 0
    start_index = 0
    end_index = 0
    for i in range(len(arr)):
        max_ending_here += arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
            start_index = i+1

        if max_so_far < max_ending_here:
            max_so_far = max_ending_here
            end_index = i
    return max_so_far, start_index, end_index


find_max_submatrix([[1, 2, 3], [-1, 2, 4], [-5, 7, 8]])
