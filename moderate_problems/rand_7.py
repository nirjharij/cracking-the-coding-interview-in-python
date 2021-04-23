# 1. Expanding a zero based random
# rand 10
# rand 100 from rand10
# rand_100 = 10*rand_10 + rand_10
# rand_1000 = 100*rand_10 + 10*rand_10 + rand_10
# rand_10 --- 1, 10
# rand_100 = 10*(rand_10-1) + (rand_10 - 1)
#
# 2. Discard and roll again
# 6 sided die and coin
# 1 - H, 2 - T anything else roll again
#
# 3. mapping Rule:
# 1,2,3: H 4,5,6 T


def rand_5():
    pass


def rand_7():
    while True:
        num = 5 * rand_5() + rand_5()
        if num < 21:
            return num % 7
