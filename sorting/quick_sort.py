def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(arr, low, high):
    if low < high:
        partition_index = partition(arr, low, high)

        quick_sort(arr, low, partition_index-1)
        quick_sort(arr, partition_index+1, high)
    print(arr)

quick_sort([10, 7, 8, 9, 1, 5], 0, 5)

