import heapq


def find_smallest(arr, k):
    heapq.heapify(arr)
    print(heapq.nsmallest(k, arr))

    # create max heap of k elements by iterating over array. For each element if element is less than largest
    # element remove that element and insert the smaller element by the end of the loop the heap will
    # have smallest k elements

# Approach 2


def find_k_smallest(arr, k):
    quick_sort(arr, 0, len(arr) - 1, k)


def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high, k):
    if low < high:
        partition_index = partition(arr, low, high)
        left_size = partition_index - low + 1
        if left_size == k:
            return max(arr[low:partition_index+1])
        elif k < left_size:
            return quick_sort(arr, low, partition_index - 1, k)
        else:
            return quick_sort(arr, partition_index + 1, high, k)
