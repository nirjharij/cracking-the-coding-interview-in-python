def get_ways(n, denoms, index):
    if index >= len(denoms):
        return 1
    denom = denoms[index]
    i = 0
    ways = 0
    while i * denom <= n:
        amount_rem = n - i * denom
        ways += get_ways(amount_rem, denoms, index+1)
        i += 1
    return ways


print(get_ways(5, [25, 10, 5, 1], 0))
