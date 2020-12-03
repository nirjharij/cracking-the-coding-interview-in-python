import math


def find_missing(arr, n):
    sum_num = 0
    square_sum = 0
    for i in arr:
        sum_num += i
        square_sum += i*i

    total_sum = (n * (n+1)) // 2
    total_sum_squares = 0

    for i in range(1, n+1):
        total_sum_squares += i*i

    rem_squares = total_sum_squares - square_sum
    rem_sum = total_sum - sum_num

    x, y = solve_quadratic(rem_sum, rem_squares)
    print(x, y)


def solve_quadratic(rem_sum, rem_squares):
    a = 2
    b = -2 * rem_sum
    c = rem_sum * rem_sum - rem_squares

    part1 = -1 * b
    part2 = math.sqrt(b*b - 4 * a * c)
    part3 = 2 * a

    x = int((part1 + part2) // part3)
    y = rem_sum - x
    return x, y


find_missing([1, 2, 4, 6, 7], 7)