# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements
# if they are in wrong order.
# Time complexity n^2


def bubble_sort(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    print(data)


def bubble_sort_new(data):
    for i in range(len(data)):
        for j in range(0, len(data)-i-1):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    print(data)


bubble_sort_new([10, 7, 4, 3, 11])

