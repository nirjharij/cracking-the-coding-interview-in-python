def get_all_length(k, shorter, longer):
    length_list = list()
    for i in range(k+1):
        length = shorter * i + (k - i) * longer
        length_list.append(length)
    print(length_list)


get_all_length(5, 2, 5)
