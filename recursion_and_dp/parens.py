def generate_parens(input):
    output = []
    get_all_valid_parens(input, input, output, '')
    print(output)


def get_all_valid_parens(left_paren, right_paren, out, final_str):
    if left_paren < 0 or left_paren > right_paren:
        return
    if left_paren == 0 and right_paren == 0:
        out.append(final_str)
    else:
        if left_paren > 0:
            get_all_valid_parens(left_paren-1, right_paren, out, final_str + '(')
        if right_paren > left_paren:
            get_all_valid_parens(left_paren, right_paren-1, out, final_str + ')')


generate_parens(3)