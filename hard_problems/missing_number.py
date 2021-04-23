# we can find missing number by adding all the numbers of the list from 0 to n and
# computing n*(n+1)/2 then subtracting from this number to get the missing number
# TC: O(n * length(n)) = O(n log n)

# if n % 2 == 0 count(0s) = 1 + count(1s)
# if n % 2 == 1 count(0s) = count(1s)
# if missing number v is odd and LSB i (v) = 1: count(0s) > count(1s) for even n
# if missing number v is even and LSB i (v) = 0: count(0s) = count(1s) for even n
# if missing number v is odd and LSB i (v) = 1: count(0s) > count(1s) for odd n
# if missing number v is even and LSB i (v) = 0: count(0s) < count(1s) for odd n


def find_missing(arr, col):
    zero_bits = []
    one_bits = []
    if col >= INTEGER.SIZE:
        return 0
    for bit in arr:
        if bit.fetch(col) == 0:
            zero_bits.append(bit)
        else:
            one_bits.append(bit)

    if len(zero_bits) <= len(one_bits):
        v = find_missing(arr, col+1)
        return v << 1 | 0
    else:
        v = find_missing(arr, col + 1)
        return v << 1 | 1
