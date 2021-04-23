def count_zeros(num):
    count = 0
    for i in range(2, num+1):
        count += factors_of_5(i)
    return count


def factors_of_5(num):
    count = 0
    while num % 5 == 0:
        count += 1
        num /= 5
    return count


def multiples_of_5(num):
    i = 5
    count = 0
    while num/i > 0:
        count += num / i
        i = i * 5
    return count
