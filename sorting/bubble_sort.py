# Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements
# if they are in wrong order.


def bubble_sort(data):
    for i in range(len(data)-1, 0, -1):
        for j in range(i):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
    print(data)


bubble_sort([10, 7, 4, 3])
