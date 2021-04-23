# Time complexity: nlogn


def merge_sort(arr):
    if len(arr) > 1:

        mid = len(arr) // 2
        left_array = arr[:mid]
        right_array = arr[mid:]
        print(mid)
        print("-------------")
        print(left_array)
        print("===================")
        print(right_array)
        merge_sort(left_array)
        merge_sort(right_array)

        i = j = k = 0
        print(f"length of left_array: {len(left_array)}")
        print(f"length of right_array: {len(right_array)}")
        while i < len(left_array) and j < len(right_array):
            print(i, j)
            if left_array[i] > right_array[j]:
                arr[k] = right_array[j]
                j += 1
            else:
                arr[k] = left_array[i]
                i += 1
            k += 1

        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1

    print(arr)


merge_sort([12, 11, 13, 5, 6, 7])
