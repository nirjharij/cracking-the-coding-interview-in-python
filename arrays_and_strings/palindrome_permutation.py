from collections import Counter


def check_palindrome_permutation(input_str):
    input_str = input_str.lower()
    input_str = list(filter(lambda i: i.isalpha(), input_str))
    count_dict = Counter(input_str)
    even_count = 0
    odd_count = 0
    for item in count_dict.items():
        if item[1] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    if len(input_str) % 2 == 0:
        if odd_count == 0 and even_count == len(input_str)//2:
            return True
        else:
            return False
    else:
        if odd_count == 1 and even_count == len(input_str)//2:
            return True
        else:
            return False


def check_permutation_palindrome_bits(input_str):
    input_str = input_str.lower()
    input_str = list(filter(lambda i: i.isalpha(), input_str))


if __name__ == "__main__":
    out = check_palindrome_permutation("Tact Coa")
    if out:
        print("It is a palindrome permutation")
    else:
        print("It is not a palindrome permutation")
