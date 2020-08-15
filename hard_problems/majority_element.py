def find_maj(arr):
    maj = 0
    count = 0
    for i in range(len(arr)):
        if count == 0:
            maj = arr[i]
        if arr[i] == maj:
            count += 1
        else:
            count -= 1
    return maj


def validate(arr, majority):
    count = 0
    for i in arr:
        if i == majority:
            count += 1

    if count > len(arr)//2:
        return majority
    else:
        return -1


arr = [1, 2, 5, 9, 5, 9, 5, 5, 5]
maj_element = find_maj(arr)
print(validate(arr, maj_element))
