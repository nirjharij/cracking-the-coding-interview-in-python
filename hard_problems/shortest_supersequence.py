import sys
from collections import defaultdict


class Node:
    def __init__(self, key, index):
        self.key = key
        self.index = index
        # self.val = val


def find_shortest(s_arr, b_arr):
    dict = defaultdict(list)
    for i in range(len(b_arr)):
        if b_arr[i] in s_arr:
            dict[b_arr[i]].append(i)

    temp = []
    for item in dict:
        temp.append(Node(item, dict[item][0]))

    min_range = sys.maxsize
    while len(temp) == len(dict):
        min_val, min_key, min_index = get_val(temp, val='min')
        max_val, max_key, max_index = get_val(temp, val='max')
        cur_range = max_val - min_val
        if cur_range < min_range:
            min_range = cur_range

        dict[min_key].pop(0)
        temp.pop(min_index)
        if dict[min_key]:
            temp.append(Node(min_key, dict[min_key][0]))

    print(min_range)


def get_val(arr, val):
    if val == 'min':
        min_val = sys.maxsize
        for i in range(len(arr)):
            item = arr[i]
            if item.index < min_val:
                min_val = item.index
                min_key = item.key
                min_index = i
        return min_val, min_key, min_index
    elif val == 'max':
        max_val = -sys.maxsize
        for i in range(len(arr)):
            item = arr[i]
            if item.index > max_val:
                max_val = item.index
                max_key = item.key
                max_index = i
        return max_val, max_key, max_index


find_shortest([1, 5, 9], [7, 5, 9, 0, 2, 1, 3, 5, 7, 9, 1, 1, 5, 8, 8, 9, 7])
