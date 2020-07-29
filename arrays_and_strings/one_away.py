def one_edit_away(str1, str2):
    if len(str1) == len(str2):
        return one_replace_away(str1, str2)
    elif len(str1) - 1 == len(str2):
        return one_insert_away(str2, str1)
    elif len(str1) + 1 == len(str2):
        return one_insert_away(str1, str2)
    else:
        return False


def one_insert_away(str1, str2):
    found_diff = False
    i = 0
    j = 0
    while i < len(str1) and j < len(str2):
        if str1[i] != str2[j]:
            if found_diff:
                return False
            found_diff = True
            j += 1
        else:
            i += 1
            j += 1
    return True


def one_replace_away(str1, str2):
    found_diff = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if found_diff:
                return False
            found_diff = True
    return True


if __name__ == "__main__":
    print(one_edit_away("apple", "appple"))

