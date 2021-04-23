# recursion
def count_ways(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_ways(n-1) + count_ways(n-2) + count_ways(n-3)


# DP
def count_ways_dp(n, memo):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif memo[n] > -1:
        return memo[n]
    else:
        memo[n] = count_ways_dp(n-1, memo) + count_ways_dp(n-2, memo) + count_ways_dp(n-3, memo)
        return memo[n]


n = 4
memo = [-1] * (n+1)
print(count_ways_dp(n, memo))
