def flip(bit):
    return 1 ^ bit


def sign(number):
    return flip((number >> 31) & 1)


def find_max(a, b):
    c = a - b

    sa = sign(a)
    sb = sign(b)
    sc = sign(c)

    # when a & b are of opposite signs there is a chance of overflow so use sign of a
    # else use sign of c
    use_sign_of_a = sa ^ sb

    use_sign_of_c = flip(sa ^ sb)

    k = use_sign_of_a * sa + use_sign_of_c * sc
    q = flip(k)
    return a*k + b*q


if __name__ == "__main__":
    max_num = find_max(2, 10097)
    print(max_num)
