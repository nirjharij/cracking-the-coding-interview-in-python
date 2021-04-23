# The good thing about selection sort is it never makes more than O(n) swaps and
# can be useful when memory write is a costly operation.


def sort(data):
    """

    :param data: list of data to be sorted
    :return: sorted list
    """
    length = len(data)
    for i in range(length):
        min_data = data[i]
        min_index = i
        for j in range(i+1, length):
            if min_data > data[j]:
                min_data = data[j]
                min_index = j
        # temp = data[i]
        data[i], data[min_index] = min_data, data[i]

    print(data)


sort([4, 7, 2, 1, 9, 0, 2])
