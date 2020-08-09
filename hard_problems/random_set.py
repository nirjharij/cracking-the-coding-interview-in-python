import random


def find_random_set(arr, m):
    subset = []
    for i in range(0, m):
        subset.append(arr[i])

    for i in range(m, len(arr)):
        rand = random.sample(range(i), 1)
        if rand[0] < m:
            subset[rand[0]] = arr[i]

    return subset


print(find_random_set([1,7,9,10, 2, 3,4], 2))
