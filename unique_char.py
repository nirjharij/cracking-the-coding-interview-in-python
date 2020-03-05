def unique_char_with_ds(s):
    char_flag = dict()

    if len(s) > 128:
        return False

    for c in s:
        if c in char_flag:
            return False
        else:
            char_flag[c] = True
    return True


def unique_char_without_ds(s):
    sorted_s = ''.join(sorted(s))
    for i in range(len(sorted_s) - 1):
        if sorted_s[i] == sorted_s[i+1]:
            return False
    return True


def unique_char_using_bits(s):
    pass

# TC1 assuming only alphabets
s1 = "ajabckajcaoichakcjakc"

# TC2 assuming we also have special chars
s2 = "alcacah9823yr2fhcck.cmalckjalcj"

s3 = "abcdefghijklmnopqrstuvwxyz"

s4 = "abcdefghijklmnopqrstuvwxyz ("

result = unique_char_with_ds(s4)
result2 = unique_char_without_ds(s4)
print("result with ds: {}".format(str(result)))
print("result without ds: {}".format(str(result2)))
