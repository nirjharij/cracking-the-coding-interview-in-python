def negate(a):
    num = 0
    neg = -1 if a > 0 else 1
    neg_num = 0 if a > 0 else 1
    while a != 0:
        if a + neg < 0 and not neg_num:
            neg = -1
        elif a + neg > 0 and neg_num:
            neg = 1
        a += neg
        num += neg
        neg += neg
    return num


def subtract(a, b):
    return a + negate(b)


def multiply(a, b):
    if a < b:
        return multiply(b, a)

    sum = 0
    for i in range(abs(b)):
        sum += abs(a)

    if b < 0:
        sum = negate(sum)

    return sum


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError

    count = 0
    sum = 0
    while sum != abs(a):
        if sum > abs(a):
            break
        sum += abs(b)
        count += 1

    if a < 0 and b > 0 or a > 0 and b < 0:
        count = negate(count)
    return count


print(divide(100, -2))
