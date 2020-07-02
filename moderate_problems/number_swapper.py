def swap_numbers(n1, n2):
    n1 = n2 - n1
    n2 = n2 - n1
    n1 = n1 + n2
    print(n1, n2)


def swap_numbers_with_xor(n1, n2):
    n1 = n1 ^ n2
    n2 = n1 ^ n2
    n1 = n1 ^ n2
    print(n1, n2)


if __name__ == "__main__":
    swap_numbers(1, 5)
    swap_numbers_with_xor(7, 10)
