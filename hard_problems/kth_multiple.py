def find_kth_number(k):
    numbers = [1]
    queue_3 = [3]
    queue_5 = [5]
    queue_7 = [7]

    for i in range(1, k):
        q3 = queue_3[0]
        q5 = queue_5[0]
        q7 = queue_7[0]

        min_val = min(q3, q5, q7)
        if min_val == q3:
            val = queue_3.pop(0)
            numbers.append(min_val)
            queue_3.append(3*val)
            queue_5.append(5*val)
            queue_7.append(7*val)
        elif min_val == q5:
            val = queue_5.pop(0)
            numbers.append(min_val)
            queue_5.append(5 * val)
            queue_7.append(7 * val)
        elif min_val == q7:
            val = queue_7.pop(0)
            numbers.append(min_val)
            queue_7.append(7 * val)
    return numbers[-1]


print(find_kth_number(7))
