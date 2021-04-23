import sys


def find_volume(arr):
    left_max = []
    right_max = []
    min_val = []
    delta = []

    for i in range(len(arr)):
        if not left_max:
            left_max.append(arr[i])
        else:
            if left_max[i-1] < arr[i]:
                left_max.append(arr[i])
            else:
                left_max.append(left_max[i-1])

    for i in range(len(arr)-1, -1, -1):
        if not right_max:
            right_max.append(arr[i])
        else:
            if right_max[0] < arr[i]:
                right_max.insert(0, arr[i])
            else:
                right_max.insert(0, right_max[0])

    for i in range(len(arr)):
        min_val.insert(i, min(left_max[i], right_max[i]))

    for i in range(len(arr)):
        delta.insert(i, min_val[i] - arr[i])

    return sum(delta)


print(find_volume([0, 0, 4, 0, 0, 6, 0, 0, 3, 0, 8, 0, 2, 0, 5, 2, 0, 3, 0, 0]))
