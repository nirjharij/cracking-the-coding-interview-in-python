from collections import defaultdict


def multiply(bigger, smaller, memo):
    if smaller == 0:
        return 0
    elif smaller == 1:
        return bigger

    if memo[smaller] > 0:
        return memo[smaller]

    s = smaller // 2

    out = multiply(bigger, s, memo)
    if smaller % 2 == 1:
        out_num = out + out + bigger
    else:
        out_num = out + out

    memo[smaller] = out_num
    return memo[smaller]


memo = defaultdict(lambda: 0)
print(multiply(9, 8, memo))
