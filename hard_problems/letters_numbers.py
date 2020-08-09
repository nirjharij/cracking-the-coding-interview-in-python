# brute for would be N^2
# The other approach is to create a table with with digit and char count as we move forward in the array
#       a 1  1 a  1  1  a a a a 1
#   a   1 1  1 2  2  2  3 4 5 6 6
#   1   0 1  2 2  3  4  4 4 4 4 5
#   d   1 0 -1 0 -1 -2 -1 0 1 2 1
# where a denotes a character and 1 denotes a number
# now one thing to notice is that where ever the diff is same means after the first index where diff was found same,
# same number of characters and digits have been added


def find_longest_subarray(arr):
    delats = find_delta(arr)
    # print(delats)
    match = find_longest_match(delats)
    print(match)
    return arr[match[0]+1:match[1]+1]


def find_delta(arr):
    deltas = []
    delta = 0
    for i in arr:
        if i.isdigit():
            delta -= 1
        else:
            delta += 1
        deltas.append(delta)
    return deltas


def find_longest_match(deltas):
    hash_table = dict()
    max_index = (0, 0)
    for i in range(len(deltas)):
        delta = deltas[i]
        if delta not in hash_table:
            hash_table[delta] = i
        else:
            match = hash_table.get(delta)
            current_distance = i - match
            max_distance = max_index[1] - max_index[0]
            if current_distance > max_distance:
                max_index = (match, i)
    return max_index


print(find_longest_subarray(['a', '1', '1', 'a', '1', '1', 'a', 'a', 'a', 'a', '1']))
