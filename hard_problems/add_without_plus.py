def add(a, b):
    if b == 0:
        return a
    sum_num = a ^ b
    carry = (a & b) << 1
    return add(sum_num, carry)


print(add(12, 14))
