rope_list = [2, 3, 4, 6]
rope_cost = 0
for i in range(2, len(rope_list)+1):
    rope_sum = 0
    for j in range(0, i):
        rope_sum += rope_list[j]
    rope_cost += rope_sum


def maxSubArraySum(a, size):
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here

        if max_ending_here < 0:
            max_ending_here = 0
    return max_so_far

a = [-13, -3, -25, -20, -3, -16, -23, 12, -5, -22, -15, -4, -7]
max_sum = maxSubArraySum(a, len(a))
print(max_sum)
