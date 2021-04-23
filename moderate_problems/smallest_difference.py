import sys


def smallest_difference(arr1, arr2):
    min_diff = sys.maxsize
    arr1.sort()
    arr2.sort()

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] == arr2[j]:
            min_diff = 0
            return min_diff
        if arr1[i] > arr2[j]:
            diff = arr1[i] - arr2[j]
            if diff < min_diff:
                min_diff = diff
            j += 1
        else:
            diff = arr2[j] - arr1[i]
            if diff < min_diff:
                min_diff = diff
            i += 1
    return min_diff


if __name__ == "__main__":
    diff = smallest_difference([1, 3, 15, 11, 2], [23, 127, 235, 19, 8])
    print(diff)
