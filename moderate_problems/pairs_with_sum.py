from collections import defaultdict

# Approach 1
def find_pairs(arr, target):
    hash_table = defaultdict(lambda: 0)
    for i in range(len(arr)):
        hash_table[arr[i]] += 1

    final_pairs = list()
    for i in range(len(arr)):
        comp = target - arr[i]
        if hash_table[comp]:
            final_pairs.append((arr[i], comp))
            hash_table[comp] = 0
            hash_table[arr[i]] = 0
    return final_pairs


# Approach 2:
def find_pairs_with_sum(arr, target):
    arr.sort()
    i = 0
    j = len(arr) - 1
    pairs = list()
    while i < j:
        if arr[i] + arr[j] < target:
            i += 1
        elif arr[i] + arr[j] > target:
            j -= 1
        else:
            pairs.append((arr[i], arr[j]))
            i += 1
            j -= 1
    return pairs


print(find_pairs_with_sum([-1, 2, 5, -10, 20, 8, 11, 15, 5], 10))
# print(find_pairs([-1, 2, 5, -10, 20, 8, 11, 15, 5], 10))
