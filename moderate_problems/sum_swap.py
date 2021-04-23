# sum1 -a + b = sum2 -b + a
# sum1 - sum2 = 2a - 2b
# a - b = sum1 - sum2 /2


def equal_sum(arr1, arr2):
    s1 = sum(arr1)
    s2 = sum(arr2)
    diff = s1 - s2
    if diff % 2 != 0:
        print("No pair found")
        return None
    target = diff / 2
    return find_difference(arr1, arr2, target)


def find_difference(arr1, arr2, target):
    for one in arr1:
        two = int(one - target)
        if two in arr2:
            return one, two


print(equal_sum([4, 1, 2, 1, 1, 2], [3, 6, 3, 3]))
