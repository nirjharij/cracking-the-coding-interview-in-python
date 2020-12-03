# recursion with memoization
def max_minutes(minutes, memo, index):
    if index >= len(minutes):
        return 0
    if memo[index] == 0:
        best_with = minutes[index] + max_minutes(minutes, memo, index+2)
        best_without = max_minutes(minutes, memo, index+1)
        memo[index] = max(best_with, best_without)
    return memo[index]


# iterative solution
def max_min_iter(minutes):
    one_away = 0
    two_away = 0
    for i in range(len(minutes)-1, -1, -1):
        best_with = minutes[i] + two_away
        best_without = one_away
        best = max(best_with, best_without)
        two_away = one_away
        one_away = best
    return one_away


minutes = [30, 15, 60, 75, 45, 15, 15, 45]
memo = [0] * len(minutes)
print(max_minutes(minutes, memo, 0))
print(max_min_iter(minutes))
