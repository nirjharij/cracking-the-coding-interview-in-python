from collections import defaultdict

str_dict = defaultdict(lambda: 0)


def get_permutations(input_str):
    for item in input_str:
        str_dict[item] += 1
    permute(str_dict, '', len(input_str))


def permute(str_dict, prefix, remaining):
    if remaining == 0:
        print(prefix)
        return
    for c in str_dict:
        count = str_dict[c]
        if count != 0:
            str_dict[c] = count - 1
            permute(str_dict, prefix + c, remaining-1)
            str_dict[c] = count


get_permutations("ABA")
