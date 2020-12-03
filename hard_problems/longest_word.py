from collections import defaultdict


def find_longest(arr):
    arr = sorted(arr, key=len, reverse=True)
    map_dict = defaultdict(lambda: False)
    for i in arr:
        map_dict[i] = True

    for s in arr:
        if can_build(s, True, map_dict):
            print(s)
            return s


def can_build(s, is_original, map_dict):
    if s in map_dict and not is_original:
        return map_dict[s]

    for i in range(1, len(s)):
        left = s[0: i]
        right = s[i:]
        if map_dict[left] and can_build(right, False, map_dict):
            return True

    map_dict[s] = False
    return False

find_longest(['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker'])
