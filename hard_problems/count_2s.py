def count_2s(num):
    count = 0
    for i in range(len(num)):
        count += count_2s_in_digits(num, i)
    return count


def count_2s_in_digits(num, d):
    power_of_10 = 10 ** d
    next_power_of_10 = 10 * power_of_10
    right = num % power_of_10

    round_down = num - (num % next_power_of_10)
    round_up = round_down + next_power_of_10

    digit = (num / power_of_10) % 10
    if digit < 2:
        return round_down / 10
    elif digit == 2:
        return round_up / 10 + right + 1
    else:
        return round_up / 10
