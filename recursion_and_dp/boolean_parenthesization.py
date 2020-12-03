def get_number_of_ways(S, i, j, isTrue):
    if i > j:
        return 0
    if i == j:
        if isTrue:
            return 'T' == S[i]
        else:
            return 'F' == S[i]

    ans = 0
    for k in range(i+1, j):
        left_true = get_number_of_ways(S, i, k-1, True)
        left_false = get_number_of_ways(S, i, k-1, False)
        right_true = get_number_of_ways(S, k+1, j, True)
        right_false = get_number_of_ways(S, k+1, j, False)

        if S[k] == '^':
            if isTrue:
                ans += (left_true * right_false) + (left_false * right_true)
            else:
                ans += (left_true * right_true) + (left_false * right_false)
        elif S[k] == '|':
            if isTrue:
                ans += (left_true * right_false) + (left_false * right_true) + (right_true * left_true)
            else:
                ans += left_false * right_false
        elif S[k] == '&':
            if isTrue:
                ans += left_true * right_true
            else:
                ans += (left_true * right_false) + (left_false * right_false) + (left_false * right_true)
    return ans

