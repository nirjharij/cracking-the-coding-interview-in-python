def urlify_string(str, true_length):
    str_array = list(str)
    index = len(str)
    for i in range(true_length-1, 0, -1):
        if str_array[i] == ' ':
            str_array[index - 1] = '0'
            str_array[index - 2] = '2'
            str_array[index - 3] = '%'
            index = index - 3
        else:
            str_array[index - 1] = str_array[i]
            index = index - 1

    return ''.join(str_array)


if __name__ == "__main__":
    s = "Mr John Smith    "
    length = 13
    out = urlify_string(s, length)
    print(out)
