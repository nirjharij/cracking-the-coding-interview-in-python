def check_str_permutation(str1, str2):
    sorted_str1 = ''.join(sorted(str1))
    sorted_str2 = ''.join(sorted(str2))
    if sorted_str1 == sorted_str2:
        return True
    else:
        return False

