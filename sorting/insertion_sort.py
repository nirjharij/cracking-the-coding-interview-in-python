# Insertion sort is a simple sorting algorithm that works the way we sort playing cards in our hands.


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]

        j = i-1
        while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
        data[j+1] = key
    print(data)


insertion_sort([20, 7, 10, 3, 8])
