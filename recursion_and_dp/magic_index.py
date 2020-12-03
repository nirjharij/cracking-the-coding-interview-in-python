# sorted array with distinct values
def find_magic_index(arr, start, end):
    mid = (start + end) // 2

    if arr[mid] == mid:
        return mid
    elif arr[mid] < mid:
        index = find_magic_index(arr, mid + 1, end)
    else:
        index = find_magic_index(arr, start, mid - 1)

    return index


# sorted array with non distinct values
def magic_index(arr, start, end):
    if end < start:
        return -1
    mid = (start + end) // 2

    if arr[mid] == mid:
        return mid

    left_index = min(mid - 1, arr[mid])
    left = magic_index(arr, start, left_index)
    if left >= 0:
        return left

    right_index = max(arr[mid], mid+1)
    right = magic_index(arr, right_index, end)
    return right


# print(find_magic_index([-10, -5, 0, 3, 5, 6, 7, 8, 9], 0, 9))
print(magic_index([-1, 0, 1, 2, 6, 6, 6, 7, 8, 9], 0, 9))
